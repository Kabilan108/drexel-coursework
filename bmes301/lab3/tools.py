"""
Functions for Data Analysis
"""

# Imports
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
from scipy import stats


def load_data(filepath, datastart=46):
    """
    Load data from csv files

    This function should work on data from Labs 1 and 2. For lab 3, 
    change the datastart parameter to 45.

    This assumes that the data is in the format of a csv file with numeric 
    data beginning on the `datastart` line. 
    This function only loads the 'Elapsed Time', 'Disp' and 'Load' columns.
    """

    ## Check assumptions about file structure
    head, units = datastart-3, datastart-2
    with open(filepath, 'r') as file:
        lines = file.readlines()
    assert 'Points,Elapsed Time,Scan Time,Disp,Load' in lines[head].replace('"', ''), \
        "Unexpected header format on line 44"
    assert 'Sec,Sec,mm,N' in lines[units].replace('"', ''), \
        "Unexpected header format on line 45"

    df = (pd.read_csv(filepath, header=None, skiprows=datastart-1)
        .iloc[:, [1, 3, 4]]
        .astype(float))
    df.columns = ["time", "disp", "load"]

    return df


def assign_cycles(data, ncycles=10, timecol='time', loadcol='load', 
                  dispcol='disp'):
    """
    Identify the preconditioning cycle start times from mechanical
    testing data.
    """

    # Check inputs
    data = data.copy()
    assert timecol in data.columns, "timecol not in data"
    assert loadcol in data.columns, "loadcol not in data"
    assert dispcol in data.columns, "dispcol not in data"

    # Identify the local minima
    minima = argrelextrema(data[dispcol].values, np.less)[0]

    # Compute the period between minima
    min_period = np.diff(data[timecol].iloc[minima])

    # Identify the start of the preconditioning cycles
    for i, diff in enumerate(min_period):
        if np.floor(diff) > 3:  break
        i = 0
    cycle_starts = minima[i:]

    # Preallocate the cycle and stage arrays
    cycle = np.array([0 for _ in range(len(data))])
    stage = np.array(['nan' for _ in range(len(data))], 
                     dtype=np.dtype('U9'))

    # Assign the cycle and stage
    for i, start in enumerate(cycle_starts, 1):
        # Create slice for the cycel
        cycle_slice = (slice(start, -1) if i == len(cycle_starts)
                                    else slice(start, cycle_starts[i]))

        # Assign the cycle
        cycle[cycle_slice] = i

        # Assign the stage
        ipeak = np.argmax(data[cycle_slice]['disp'])
        stage[start:start+ipeak] = 'loading'
        stage[start+ipeak:cycle_slice.stop] = 'unloading'

    # Add the cycle and stage to the dataframe
    data['cycle'] = cycle
    data['stage'] = stage

    # This process erronously assigns additional cycles to the plateau
    # region of the displacement-time curve. To correct this, we remove
    # the cycles that are not part of the preconditioning cycles
    data = data[data['cycle'] <= ncycles]

    # Get rid of pre and post cycles
    data = data[data['stage'] != 'nan']

    # Zero the time and displacement
    data['time'] = data['time'] - data['time'].iloc[0]
    data['disp'] = data['disp'] - data['disp'].iloc[0]

    return data


def plot_disp_cycles(data):

    # Plot Displacement-time curves
    fig, axes = plt.subplots(5, 2, figsize=(8, 8), sharex=True)
    axes = axes.flatten()

    ## Cycle colors
    colors = sns.color_palette("tab10", 10).as_hex()

    ## Create data for legend
    line = lambda c, ls, x: Line2D([], [], color=c, lw=2, linestyle=ls, label=x)
    legend_patches = (
        [line('black', ls, x) for ls, x in zip(['-', '--'], ['Loading', 'Unloading'])] +
        [line(None, '', '')] + 
        [line(c, '-', f"Cycle {x}") for c, x in zip(colors, range(1, 11))]
    )

    for i, team in enumerate(data['team'].unique()):
        ## Extract data for this team
        _df = data.query(f"team == '{team}'")

        ## Plot data
        for cycle, color in zip(_df['cycle'].unique(), colors):
            for stage, ls in zip(['loading', 'unloading'], ['-', '--']):
                sns.lineplot(
                    data=_df.query(f"cycle == {cycle} and stage == '{stage}'"),
                    x='time', y='disp', ax=axes[i], color=color, 
                    linestyle=ls, legend=False
                ).set(xlabel=None, ylabel=None)
                sns.despine()
                axes[i].set_title(f"Team {team}")
            
    ## Legend
    fig.legend(
        handles=legend_patches, 
        loc='upper left', 
        bbox_to_anchor=(1, 0.7),
        facecolor='#f2f2f2',
        edgecolor='#ffffff',
        fancybox=False,
        fontsize=11
    )

    ## Plot Labels
    fig.subplots_adjust(left=0.15, bottom=0.15)
    fig.supxlabel('Time (s)', size=14)
    fig.supylabel('Displacement (mm)', size=14)
    fig.tight_layout()

    return fig, axes


def plot_stress_strain_cycles(data):
    """
    Plot the cycles of stress-strain curves
    """
    
    fig = px.line(
        data,
        x='disp', 
        y='load',
        color='cycle',
        line_dash='stage',
        facet_col='team',
        facet_col_wrap=2
    )
    fig.update_yaxes(matches=None, title=None);
    fig.update_xaxes(matches=None, title=None);
    fig.update_layout(template='ggplot2', width=800, height=800);
    fig.add_annotation(
        x=0.5, y=-0.2, text='Displacement (mm)', 
        font_size=14,
        showarrow=False,
        xref='paper', yref='paper'
    );
    fig.add_annotation(
        x=-0.1, y=0.5, text='Load (N)', 
        font_size=14, textangle=-90,
        showarrow=False,
        xref='paper', yref='paper'
    );
    
    return fig


def find_linear_region(data, cutoff=0.4):
    """
    Identify the portion of a curve that is most 'linear' by iteratively
    removing points and computing the r2 values to check the 'goodness'
    of the fit
    """

    # Initialize
    r2 = []
    strain = data['strain'].values
    stress = data['stress'].values

    # Loop through points
    for i in range(len(strain)):
        # Fit line
        slope, intercept, r_value, p_value, std_err = stats.linregress(strain[i:], stress[i:])
        r2.append(r_value**2)

        if r2[-1] > 0.99:
            break

        if i > 0 and abs(r2[-1] - r2[-2]) < 1e-4:
            break

        if i == round(cutoff * len(strain)):
            break

    # Get valus for the final fit
    res = stats.linregress(strain[i:], stress[i:])
    lin_strain = strain[i:]
    lin_stress = res.intercept + res.slope * lin_strain

    return lin_strain, lin_stress, res.slope, res.rvalue**2


def plot_fit_stress_strain(data, lin_stress, lin_strain):
    """
    Plot the stress-strain curve overlayed with the fitted line
    """

    # Extract data
    strain = data['strain'].values
    stress = data['stress'].values

    # Create figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=strain, y=stress, mode='markers',
                             opacity=0.5))
    fig.add_trace(go.Scatter(x=lin_strain, y=lin_stress, mode='lines',
                             line=dict(color='red', width=2)))

    return fig
