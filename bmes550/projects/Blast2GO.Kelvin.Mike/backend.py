# By Kelvin Koser and Michael Welsh.
#-----------------------------------------------------------------------------------------------------------------------

#Standard Modules
import flit_core.config
import pandas as pd
import sqlite3
from sqlite3 import Error
import numpy as np
from Bio.Blast import NCBIWWW

#Our modules
##None needed?

#-----------------------------------------------------------------------------------------------------------------------
#function to accept nucleotide sequence and perform blast_practice test
def get_BLAST_results(nuc_seq):
    seq_data = nuc_seq.upper()

    # perform blast_practice
    result_handle = NCBIWWW.qblast(program="blastn", database="nt", sequence=seq_data, format_type="Tabular",
                                   entrez_query='txid9606[ORGN]')

    # read results
    with open('results.tsv', 'w') as save_file:
        blast_results = result_handle.read()
        save_file.write(blast_results)

    raw_res = pd.read_csv("results.tsv", sep="\t", skiprows=13)
    raw_res.columns = ['query_accession', 'nt_accession', 'percent_identity', 'alignment_length', 'mismatches',
                       'gap_opens', 'query_start', 'query_end', 'subject_start', 'subject_end', 'evalue', 'bit_score']
    E_VALUE_THRESH = 1e-20  # threshold to ID only best hits
    top_hits = raw_res.loc[raw_res['evalue'] <= E_VALUE_THRESH]
    final_blast_res = top_hits[['nt_accession', 'evalue']]
    blast_res_sorted = final_blast_res.sort_values(by=['evalue'], ascending=False).drop_duplicates(
        subset='nt_accession', keep='first')

    return blast_res_sorted

#def function to quickly connect to database
def connect_to_db(db_file):
    sqlite3_conn = None

    try:
        sqlite3_conn = sqlite3.connect(db_file)
        return sqlite3_conn

    except Error as err:
#       print(err)

        if sqlite3_conn is not None:
            sqlite3_conn.close()
        raise err

#end conn to database


def blast_query(blast_res_sorted):

    conn = connect_to_db('gene_db')
    cur = conn.cursor()

    blast_arr = blast_res_sorted['nt_accession'].drop_duplicates().to_numpy()

    data=[]
    for val in blast_arr:
        t = (val,)
        #print(t)
        cur.execute("""SELECT ge.nt_accession, ge.symbol, go_practice.GO_ID, go_practice.Description, go_practice.class FROM annotation_table ge, gene_ontology_table go_practice \
                                WHERE ge.nt_accession =? AND ge.GO_ID = go_practice.GO_ID""", t)

        rows = cur.fetchall()

        if len(rows) == 0:
            cur.execute("""SELECT ge.symbol FROM annotation_table ge \
                            WHERE ge.nt_accession =?""", t)
            sym_vals = cur.fetchall()
            if len(sym_vals) ==0:
                sym = 'none'
            else:
                sym = sym_vals[0]
            #sym = blast_res_sorted.loc[blast_res_sorted['nt_accession'] == f'{val}', 'symbol'].iloc[0]#.item()
            row_fill = [[f'{val}', f'{sym}', 'none', 'none', 'none']]
            df = pd.DataFrame(row_fill, columns=['nt_accession', 'symbol', 'GO_ID', 'Description', 'class'])
        else:
            df = pd.DataFrame(rows)
            df.columns = [x[0] for x in cur.description]
            df = df.drop_duplicates()
        data.append(df)

    data_df = pd.concat(data)
    conn.close()

    go_res_comp = pd.merge(data_df, blast_res_sorted, how = 'left', on='nt_accession')
    go_res_comp = go_res_comp[['nt_accession', 'symbol', 'evalue', 'GO_ID', 'Description', 'class']]
    go_res_comp = go_res_comp.sort_values(by='evalue')
    return go_res_comp


def process(nuc_seq):
    return blast_query(get_BLAST_results(nuc_seq))



#-----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    blast_results = get_BLAST_results(nucleo_str)

    query_results = blast_query(blast_results)

    query_results.to_csv("query_results.csv")
# EOF
