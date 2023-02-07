"""
Function for plotting PCA and Silhouette scores
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib

palette = 'Dark2'

def plotpca(Xpca, V, y):
    """
    Plot the 2D PCA data in Y.

    @param Xpca: PCA data with >= 2 dimensions
    @param    V: Explained variance ratio
    @param    y: Sample IDs
    """
    
    # Plotting
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    sns.scatterplot(
        x=Xpca[:, 0], y=Xpca[:, 1], hue=y, s=150, alpha=.8,
        palette=palette, ax=ax, linewidth=1, edgecolor='black'
    )

    # Legend
    ax.legend(
        fontsize=12, fancybox=False, facecolor='white',
        edgecolor='white', framealpha=0.7
    )

    # Labels
    ax.set_xlabel(f'PC1 ({V[0]:.2%})', fontsize=14)
    ax.set_ylabel(f'PC2 ({V[1]:.2%})', fontsize=14)

    # Figure appearance
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_linewidth(1.2)
    ax.tick_params(axis='both', labelsize=12)
    ax.minorticks_on()
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black', 
            alpha=0.2)
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black', 
            alpha=0.3)
    ax.axis('square')

    return fig, ax

def plotdecisionbound(lda, Xpca, y, y_pred, ax, shade=True, show_pf=True):
    """
    Plot the Decision Boundary for Discriminant Analysis
    
    @param    lda: Fitted LDA model
    @param   Xpca: PCA data with >= 2 dimensions
    @param      y: Sample IDs
    @param y_pred: Predicted labels
    @param     ax: Axes object
    @param   shade: Shade the decision boundary
    @param  show_pf: Show true and false positives
    """

    # Define true and false positives (tp & fp)
    tp = y == y_pred                     # tp
    tp0, tp1 = tp[y == 'thalamus'], tp[y == 'gloubus']    # tp for class 0 and 1
    X0, X1 = Xpca[y == 'thalamus'], Xpca[y == 'gloubus']  # samples for class 0 and 1
    X0_tp, X0_fp = X0[tp0], X0[~tp0]     # tp and fp for class 0
    X1_tp, X1_fp = X1[tp1], X1[~tp1]     # tp and fp for class 1

    # Get colors
    colors = sns.color_palette(palette, 2).as_hex()

    if show_pf:
        # class 0: dots,
        ax.scatter(X0_tp[:, 0], X0_tp[:, 1], marker=".", s=20, color='k', label='True Positive')
        ax.scatter(X0_fp[:, 0], X0_fp[:, 1], marker="x", s=20, color='k', label='False Positive')

        # class 1: dots
        ax.scatter(X1_tp[:, 0], X1_tp[:, 1], marker=".", s=20, color="k")
        ax.scatter(X1_fp[:, 0], X1_fp[:, 1], marker="x", s=20, color="k")

    # Create meshgrid to highlight decision boundary
    nx, ny = 500, 500
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, nx), np.linspace(y_min, y_max, ny))
    Xmesh = np.c_[xx.ravel(), yy.ravel()]  # Flatten and concatenate arrays
    Z = lda.predict(Xmesh)
    Z = Z.reshape(xx.shape)

    # Enclode meshgrid labels numerically
    Z = np.where(Z == 'thalamus', 0, 1)

    # Plot decision boundary
    cmap = matplotlib.colors.ListedColormap(colors)
    if shade:
        ax.contourf(xx, yy, Z,  alpha=0.2, cmap=cmap)
    ax.contour(xx, yy, Z, colors='k', linewidths=0.8)

    # Add legend
    ax.legend(
        loc='upper left', bbox_to_anchor=(1.0, 0.7), frameon=False,
        fontsize=12, markerscale=1.5, labelspacing=0.5
    )

    return ax
