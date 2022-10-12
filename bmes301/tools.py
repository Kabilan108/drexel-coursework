"""
Functions for Data Analysis
"""

import statsmodels.formula.api as smf
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def load_data(filepath, datastart=46):
    """
    Load data from csv files

    This function should work on data from Labs 1 and 2. 

    This assumes that the data is in the format of a csv file with numeric 
    data beginning on line 46. 
    This function only loads the 'Elapsed Time', 'Disp' and 'Load' columns.
    """

    ## Check assumptions about file structure
    with open(filepath, 'r') as file:
        lines = file.readlines()
    assert lines[43] == '"Points","Elapsed Time","Scan Time","Disp","Load",\n', \
        "Unexpected header format on line 44"
    assert lines[44] == '"","Sec","Sec","mm","N",\n', \
        "Unexpected header format on line 45"

    df = (pd.read_csv(filepath, header=None, skiprows=45)
        .drop([0, 2, 5], axis=1)
        .astype(float))
    df.columns = ["time", "disp", "load"]

    return df


def plot_data(data, xvar, yvar, xlab, ylab, title, team='05',
              highlight_ramp=False, ramp_time=None):
    """
    Compare LCL and MCL data
    """

    fig, axes = plt.subplots(1, 2, figsize=(8, 4), sharey=True)

    for tissue, color, ax in zip (['LCL', 'MCL'], ['#377eb8', '#e41a1c'], axes):
        I = (data['team'] == team) & (data['tissue'] == tissue)
        
        # Plot data
        sns.lineplot(
            data=data.loc[I],
            x=xvar,
            y=yvar,
            color=color,
            ax=ax
        )

        # Highlight ramp region
        if highlight_ramp:
            sns.lineplot(
                data=data.loc[I & (data['time'] > ramp_time)],
                x=xvar,
                y=yvar,
                color='#e39e44',
                ax=ax,
                linewidth=10,
                alpha=.2
            )

        ax.set_title(tissue, fontsize=14)
        ax.set_xlabel(xlab, fontsize=12)
        ax.set_ylabel(ylab, fontsize=12)
        sns.despine()

    if highlight_ramp:
        lcl = mpatches.Patch(color='#377eb8', label='LCL')
        mcl = mpatches.Patch(color='#e41a1c', label='MCL')
        ramp = mpatches.Patch(color='#e39e44', alpha=.4, label='Ramp')
        fig.legend(
            handles=[lcl, mcl, ramp], 
            loc='upper center', 
            bbox_to_anchor=(0.5, 0.05), 
            ncol=3,
            fancybox=False,
            shadow=False,
            fontsize=12,
            frameon=False
        )

    fig.subplots_adjust(top=0.9)
    fig.suptitle(title, fontsize=16)
    plt.tight_layout()

    return fig, axes


def get_linear_region(data):
    """
    Determing the linear region of the stress-strain curve

    The linear region is defined as the region where the slope of the stress-strain 
    curve is constant. This is determined by removing one data point, fitting 
    the model and checking the R^2 value. This process is repeated, removing 
    one data point at a time, until the R^2 values converge. 
    The loop is terminated if more than 30% of the data is removed
    """

    i, r2, flag = 0, [], True
    n = data.shape[0]

    while flag:
        if i > 0.4 * n:
            print("R^2 didn't converge after 40% of the data was removed")
            i = 1
            break

        # Fit model
        model = smf.ols('stress ~ strain', data=data[i:])
        model = model.fit()

        # Compute R^2
        r2.append(model.rsquared)

        # Check for convergence
        if i > 0:
            if abs(r2[-1] - r2[-2]) < 1e-4:
                flag = False

        i += 1

    return i-1, r2


def plot_regression(data, model, i, title):

    # Compute predictions
    pred = model.get_prediction().summary_frame(alpha=0.05)
    pred['strain'] = data['strain'][i:].values

    # Equation label
    eqn = r"$\sigma = (%.2f MPa) \cdot \varepsilon$" % model.params['strain']
    r2 = r"$R^2 = %.4f$" % model.rsquared

    # Plot figure
    fig, ax = plt.subplots(figsize=(6,4))
    sns.scatterplot(
        data=data, x='strain', y='stress',  label='Data', 
        s=40, color='lightblue', edgecolor='darkblue', linewidth=0.3, 
        alpha=.4, ax=ax,
    )
    sns.lineplot(
        data=pred, x='strain', y='mean', label='Regression Line',
        color='red', linewidth=2, ax=ax
    )

    # Annotations
    plt.annotate(
        eqn, xy=(0.01, 0.6), xycoords='data', fontsize=12, color='crimson'
    )
    plt.annotate(
        r2, xy=(0.01, 0.5), xycoords='data', fontsize=12, color='crimson'
    )
    plt.legend(frameon=False, fontsize=11)
    ax.set_title(title, fontsize=14)
    ax.set_xlabel('Strain', fontsize=12)
    ax.set_ylabel('Stress (MPa)', fontsize=12)
    sns.despine()

    return fig, ax
