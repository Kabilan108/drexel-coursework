# By Kelvin Koser and Michael Welsh.
#-----------------------------------------------------------------------------------------------------------------------

# Standard modules
import ctypes
from   datetime import datetime
import os
from   os.path import exists, join
import numpy as np
import pandas as pd
import pathlib
import platform
import PySimpleGUI as sg
import threading
import time

# Our modules
from backend import process
# def process(nuc_seq_str):
#     time.sleep(5)
#     return pd.DataFrame({
#         'symbol': [53, 23],
#         'nt_accession': ['QRZ', 'XYZ'],
#         'GO_ID': ['GO:1899081', 'GO:0560950590'],
#         'Description': ['Capsular export', 'Membrane structure'],
#         'class': ['Biological Process', 'Molecular Function'],
#         'evalue': [np.random.rand(), 1e-30]
#     })
# end process

#-----------------------------------------------------------------------------------------------------------------------
def thread_func(gui, nuc_seq):
    df = process(nuc_seq)
    col_map = {
        'nt_accession': 'Accession',
        'GO_ID': 'GO:Terms',
        'class': 'Class',
        'evalue': 'E-Value',
        'symbol': 'Symbol'
    }
    df.rename(columns=col_map, inplace=True)
    df = df[['E-Value', 'Accession', 'Symbol', 'GO:Terms', 'Description', 'Class']]
    gui.write_event_value('BACKEND_DONE', df)
# thread_func

#-----------------------------------------------------------------------------------------------------------------------
def main():
    # Make cache CSV path
    cache_csv_path = 'cache.csv'

    # Make GUI DPI-aware if Windows
    if platform.system() == 'Windows' and int(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    #

    # Set GUI theme
    sg.theme('DefaultNoMoreNagging')

    # Create GUI layout
    layout = [
        [
            [
                sg.Text('Enter nucleotide sequence:')
            ],
            [
                sg.Input(key='SEQ_INPUT_TEXTFIELD'),
                sg.Button('Submit', key='SEQ_SUBMIT_BUTTON')
            ],
            [
                sg.Table(
                    values=[],
                    headings=['E-Value', 'Accession', 'Symbol', 'GO:Terms', 'Description', 'Class'],
                    display_row_numbers=False,
                    auto_size_columns=False,
                    def_col_width=20,
                    num_rows=10,
                    key='TABLE'
                )
            ],
            [
                sg.Button('Download to CSV', key='DOWNLOAD_BUTTON'),
                sg.Text('', key='OUTPUT_TEXT')
            ]
        ]
    ]

    # Create GUI
    gui = sg.Window('Rapid Structural & Functional Annotation of a Gene', layout, grab_anywhere=False, icon='favicon.ico')

    # Keep track of last processed nucleotide sequence/DataFrame
    last_nuc_seq = None
    last_df      = None

    # Start GUI
    while True:
        # Read events
        event, values = gui.read()

        # Try to process events/values; catch any exceptions and print them on the GUI
        try:
            # If the user wants to close the GUI, then close the GUI
            if event == sg.WIN_CLOSED:
                gui.close()
                break
            #
            # Else if the user hit the submit button...
            elif event == 'SEQ_SUBMIT_BUTTON':
                # Reset error text
                gui['OUTPUT_TEXT'].update(text_color='black', value='Handling submit...')

                # Reset table
                gui['TABLE'].update(values=[])

                # Get nucleotide sequence from text field
                nuc_seq = values['SEQ_INPUT_TEXTFIELD']

                # Error check, make sure it is not an empty sequence
                if nuc_seq == '':
                    raise RuntimeError(f'Given an empty nucleotide sequence')
                #

                # Process nucleotide sequence by first seeing if results are cached, and if not cached, then obtain them
                cached = False
                if exists(cache_csv_path):
                    cache_df = pd.read_csv(cache_csv_path)
                    if nuc_seq in cache_df['nucleotide_sequence'].values:
                        df = cache_df[cache_df['nucleotide_sequence'] == nuc_seq]
                        df = df.iloc[:, 1:]
                        cached = True
                    #
                #
                if not cached:
                    threading.Thread(target=thread_func, args=(gui, nuc_seq), daemon=True).start()
                    close      = False
                    time_start = time.time()
                    while True:
                        t_event, t_values = gui.read(timeout=1000)
                        if t_event == sg.WIN_CLOSED:
                            close = True
                            gui.close()
                            break
                        #
                        elif t_event == 'BACKEND_DONE':
                            df = t_values[t_event]
                            break
                        #
                        time_elapsed_in_sec = int(time.time() - time_start)
                        gui['OUTPUT_TEXT'].update(
                            text_color='black',
                            value=f'Handling submit... {time_elapsed_in_sec:4d}s'
                        )
                    #
                    if close:
                        break
                    #
                #

                # Sort by e-value
                df = df.sort_values(by=['E-Value'], ascending=True)

                # Update table to display DataFrame
                gui['TABLE'].update(values=df.values.tolist())

                # Save values for later in case the user hits the download button
                df['nucleotide_sequence'] = [nuc_seq] * df.shape[0]
                cols         = df.columns.tolist()
                cols         = cols[-1:] + cols[:-1]
                df           = df[cols]
                last_nuc_seq = nuc_seq
                last_df      = df

                # Save this DataFrame in a permanent cache (which is just one big CSV) if it is not already cached
                if not cached:
                    if exists(cache_csv_path):
                        cache_df = pd.read_csv(cache_csv_path)
                        pd.concat([df, cache_df]).to_csv(cache_csv_path, index=False)
                    #
                    else:
                        df.to_csv(cache_csv_path, index=False)
                    #
                #

                # Print completion message on GUI
                gui['OUTPUT_TEXT'].update(text_color='black', value='Nucleotide sequence processing complete!')
            #
            # Else if the user hit the download-CSV button...
            elif event == 'DOWNLOAD_BUTTON':
                # Reset error text
                gui['OUTPUT_TEXT'].update(text_color='black', value='Handling download...')

                # Save the DataFrame if available, or raise error saying we have do
                if last_nuc_seq is not None:
                    downloads_dir_path = 'downloads'
                    pathlib.Path(downloads_dir_path).mkdir(parents=True, exist_ok=True)
                    sec   = int(datetime.now().second)
                    minu  = int(datetime.now().minute)
                    hour  = int(datetime.now().hour)
                    day   = int(datetime.now().day)
                    month = int(datetime.now().month)
                    year  = int(datetime.now().year)
                    nuc_seq_csv_path = join(
                        downloads_dir_path,
                        f'{year}_{month}_{day}_{hour}_{minu}_{sec}.csv'
                    )
                    last_df.to_csv(nuc_seq_csv_path, index=False)
                #
                else:
                    raise RuntimeError('Cannot download an empty table!')
                #

                # Print completion message on GUI
                gui['OUTPUT_TEXT'].update(text_color='black', value='CSV download complete!')
            #
        #
        except Exception as e:
            # Print error on GUI
            gui['OUTPUT_TEXT'].update(text_color='red', value=f'Error: {str(e)}')
        #
    #
# end main

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
# EOF