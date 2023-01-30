"""
Function for plotting PCA and Silhouette scores
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plotpca2d(Y, V, samples):
    """
    Plot the 2D PCA data in Y.

    @param Y: PCA data with >= 2 dimensions
    @param V: Explained variance ratio
    @param samples: Sample labels
    """
    
    # Plotting
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    g = sns.scatterplot(
        x=Y[:, 0], y=Y[:, 1], hue=samples, s=150, alpha=0.5, legend='full',
        palette='Dark2', ax=ax
    )

    # Legend
    g.legend(loc='upper right', fontsize=12, frameon=False)

    # Labels
    ax.set_xlabel(f'PC1 ({V[0]:.2%})', fontsize=14)
    ax.set_ylabel(f'PC2 ({V[1]:.2%})', fontsize=14)
    ax.set_title('PCA', fontsize=16)

    # Figure appearance
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_linewidth(1.2)
    ax.tick_params(axis='both', labelsize=12)
    ax.minorticks_on()
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black', 
            alpha=0.4)
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black', 
            alpha=0.7)
    ax.axis('square')

    return fig, ax


def silhouetteplot(si, samples, mean_scores):
    """
    Plot Silhouette scores for each disease and compute mean scores
    @param si: Silhouette scores
    """

    

    # Plotting
    fig, ax = plt.subplots(1, 1, figsize=(6, 4))
    g = sns.boxplot(
        x=si, 
        y=[x.replace(' ', '\n') for x in samples], 
        ax=ax, 
        palette='Dark2',
        saturation=0.6, 
        width=0.8, 
        linewidth=1.2
    )

    # Labels
    ax.set_xlabel('Silhouette Score', fontsize=14)
    ax.set_title('Silhouette Scores', fontsize=16)

    # Show mean silhouette scores
    labels = [x.get_text().replace('\n', ' ') for x in g.get_yticklabels()]
    colors = sns.color_palette('Dark2', n_colors=len(labels))
    for i, (label, color) in enumerate(zip(labels, colors)):
        ax.text(
            x=0.55, y=i, s=f'$\mu=${mean_scores[label]:.2f}',
            fontsize=12, ha='left', va='center', color='black',
            bbox=dict(
                facecolor=color, edgecolor='white', boxstyle='round,pad=0.2',
                alpha=0.4,
            )
        )

    # Figure appearance
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_linewidth(1.2)
    ax.tick_params(axis='both', labelsize=12)
    ax.minorticks_on()
    ax.grid(which='minor', axis='x', linestyle=':', linewidth='0.5', 
            color='black', alpha=0.3)
    ax.grid(which='major', axis='x', linestyle='-', linewidth='0.5', 
            color='black', alpha=0.5)

    return fig, ax