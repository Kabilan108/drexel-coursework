"""
Preprocessing for Lab 4 data

This module performs the following preprocessing steps:

- Load data from MTS exported txt files
    - Convert to pandas dataframe and combine into one dataframe
- Calculate the second moment of area, I for each specimen
- Identify the yield point for each force-deflection curve
- Calculate the flexural stress and strain for each specimen
- Plot the force-deflection curves for each specimen
- Plot the stress-strain curves for each specimen
"""

# Set working directory
import os, sys
os.chdir("/home/kabil/sietch/courses/bmes301/lab4")
sys.path.append(os.getcwd())

# Import modules
from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import pickle
import tools
import re


def main():

    datapath = Path("data")

    ## Regular expression to pull team information from file name
    meta = re.compile(r'G(?P<team>\d{2})_(?P<strain_group>[AB])')

    raw_data = []

    for file in sorted(datapath.glob('*.txt')):
        ## Extract metadata
        m = meta.search(file.name)

        ## Load data
        try:
            _df = tools.load_data(file)
            _df['team'] = int(m.group('team'))
            _df['strain_group'] = m.group('strain_group')
            raw_data.append(_df)
        except AssertionError as e:
            print(f"Error loading {file.name}: {e}")

    ## Concatenate data
    raw_data = (pd.concat(raw_data)
        .sort_values(['team', 'strain_group', 'time'])
        .reset_index(drop=True))

    ## Load specimen dimensions
    specimen = (pd.read_excel(datapath / 'lab4_specimen_dimensions.xlsx')
        .rename(columns={
            'Group #': 'team',
            'Sample ID': 'strain_group',
            'Strain Rate (s^-1)': 'strain_rate',
            'Outer height (mm)': 'h0',
            'Outer base (mm)': 'b0',
            'Inner height (mm)': 'hi',
            'Inner base (mm)': 'bi',
        })
        .drop(columns=['Notes']))

    ## Compute second moment of area
    specimen['I'] = np.pi / 64 * (specimen['b0']*specimen['h0']**4 - specimen['bi']*specimen['hi']**4)

    ## Fixed Span Length
    L = 40  # mm

    ## Create figures
    ### Force-Deflection Curves
    FD_fig = plt.figure(constrained_layout=True, figsize=(6, 25))
    FD_fig.suptitle("Force-Deflection Curves", fontsize=16)
    FD_subfigs = FD_fig.subfigures(10, 1, wspace=0.1, hspace=0.1)

    ### Flexural Stress-Flexural Strain Curves
    SS_fig = plt.figure(constrained_layout=True, figsize=(6, 25))
    SS_fig.suptitle("Flexural Stress-Flexural Strain Curves", fontsize=16)
    SS_subfigs = SS_fig.subfigures(10, 1, wspace=0.1, hspace=0.1)

    ## Define strain rates for each group
    strain_rates = {'A': 0.0016, 'B': 0.40, 'C': 0.0016, 'D': 0.40}

    ## Create list to store processed data
    data = []

    for team, FD, SS in zip(raw_data['team'].unique(), FD_subfigs, SS_subfigs):
        ### FD: Create axes
        FD.suptitle(f"Team {team}")
        FD_ax = FD.add_subplot(111)
        FD_ax.set_xlabel("Deflection (mm)", fontsize=11)
        FD_ax.set_ylabel("Force (N)", fontsize=11)

        ### SS: Create axes
        SS.suptitle(f"Team {team}")
        SS_ax = SS.add_subplot(111)
        SS_ax.set_xlabel("Flexural Strain", fontsize=11)
        SS_ax.set_ylabel("Flexural Stress (MPa)", fontsize=11)

        for strain_group, color in zip(raw_data['strain_group'].unique(), ['#f24444', '#4185f2']):

            ### Subset data for this team and strain group
            _raw = (raw_data.query("team == @team & strain_group == @strain_group")
                .reset_index(drop=True))

            ### Locate yield point
            force = _raw['force'].values
            if strain_group == 'A':
                J = np.where(abs(np.diff(force)) > 100)[0] - 1
                J = J[0]
            else:
                J = np.argmax(np.diff(force) < 0)

            ### Compute flexural stress and flexural strain
            h0 = specimen.query("team == @team & strain_group == @strain_group")['h0'].values[0]
            I = specimen.query("team == @team & strain_group == @strain_group")['I'].values[0]
            _raw['flex_stress'] = (L * h0) / (8 * I) * _raw['force']
            _raw['flex_strain'] = (6 * h0) / (L**2) * _raw['deflect']

            ### Split the data
            _df = _raw.iloc[:J].copy()
            _raw = _raw.iloc[J:].copy()
            yield_point = _raw.iloc[0]
            
            ### Plot the Force-Deflection Curve
            sns.lineplot(data=_df, x='deflect', y='force', ax=FD_ax, 
                         label=f"{strain_group}", linewidth=2, 
                         linestyle='-', color=color)
            sns.lineplot(data=_raw, x='deflect', y='force', ax=FD_ax,
                         legend=False, linewidth=2, linestyle='--', 
                         color=color)
            FD_ax.plot(yield_point['deflect'], yield_point['force'], 'ok',
                       markersize=7)

            ### Plot Flexural Stress-Flexural Strain Curve
            sns.lineplot(data=_df, x='flex_strain', y='flex_stress', ax=SS_ax, 
                         label=f"{strain_group}", linewidth=2, linestyle='-', 
                         color=color)
            sns.lineplot(data=_raw, x='flex_strain', y='flex_stress', ax=SS_ax,
                         legend=False, linewidth=2, linestyle='--', color=color)
            SS_ax.plot(yield_point['flex_strain'], yield_point['flex_stress'], 
                       'ok', markersize=7)

            ### Store data
            _df['strain_rate'] = strain_rates[strain_group]
            data.append(_df)

            print(f"Team {team} (Sample {strain_group}) processed.")

    ## Save figures
    with PdfPages('results/force-deflection.pdf') as pdf:
        pdf.savefig(FD_fig)
    with PdfPages('results/flexural-stress-strain.pdf') as pdf:
        pdf.savefig(SS_fig)

    ## Close figures
    plt.close('all')

    ## Save data
    data = pd.concat(data)
    with open('results/data.pkl', 'wb') as f:
        pickle.dump([specimen, data], f)

    return specimen, data


if __name__ == '__main__':
    main();
