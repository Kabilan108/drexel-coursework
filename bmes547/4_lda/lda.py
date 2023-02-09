import numpy as np


class LDA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.linear_discriminants = None

    def fit(self, X, y):
        n_features = X.shape[1]
        class_labels = np.unique(y)

        # Within class scatter matrix:
        # SW = sum((X_c - mean_X_c)^2 )

        # Between class scatter:
        # SB = sum( n_c * (mean_X_c - mean_overall)^2 )

        mean_overall = np.mean(X, axis=0)
        SW = np.zeros((n_features, n_features))
        SB = np.zeros((n_features, n_features))
        for c in class_labels:
            X_c = X[y == c]
            mean_c = np.mean(X_c, axis=0)
            # (4, n_c) * (n_c, 4) = (4,4) -> transpose
            SW += (X_c - mean_c).T.dot((X_c - mean_c))

            # (4, 1) * (1, 4) = (4,4) -> reshape
            n_c = X_c.shape[0]
            mean_diff = (mean_c - mean_overall).reshape(n_features, 1)
            SB += n_c * (mean_diff).dot(mean_diff.T)

        self.SB = SB
        self.SW = SW

        # Determine SW^-1 * SB
        A = np.linalg.inv(SW).dot(SB)
        # Get eigenvalues and eigenvectors of SW^-1 * SB
        eigenvalues, eigenvectors = np.linalg.eig(A)
        # -> eigenvector v = [:,i] column vector, transpose for easier calculations
        # sort eigenvalues high to low
        eigenvectors = eigenvectors.T
        idxs = np.argsort(abs(eigenvalues))[::-1]
        eigenvalues = eigenvalues[idxs]
        eigenvectors = eigenvectors[idxs]
        # store first n eigenvectors
        self.linear_discriminants = eigenvectors[0 : self.n_components]

    def predict(self, X):
        # project data
        X_projected = np.dot(X, self.linear_discriminants.T)
        return X_projected

    def transform(self, X):
        # project data
        return np.dot(X, self.linear_discriminants.T)


# Testing
if __name__ == "__main__":
    # Imports
    import matplotlib.pyplot as plt
    from sklearn import datasets

    data = datasets.load_iris()
    X, y = data.data, data.target

    # Project the data onto the 2 primary linear discriminants
    lda = LDA(2)
    lda.fit(X, y)
    X_projected = lda.transform(X)

    print("Shape of X:", X.shape)
    print("Shape of transformed X:", X_projected.shape)

    x1, x2 = X_projected[:, 0], X_projected[:, 1]

    # Compare with LDA from sklearn
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA_sklearn

    lda_sklearn = LDA_sklearn(n_components=2)
    X_projected_sklearn = lda_sklearn.fit_transform(X, y)

    x1_sklearn, x2_sklearn = X_projected_sklearn[:, 0], X_projected_sklearn[:, 1]

    # Plot both
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].scatter(
        x1, x2, c=y, edgecolor="none", alpha=0.8, cmap=plt.cm.get_cmap("viridis", 3)
    )
    ax[0].set_xlabel("Linear Discriminant 1")
    ax[0].set_ylabel("Linear Discriminant 2")
    ax[0].set_title("My LDA")

    ax[1].scatter(
        -x1_sklearn, -x2_sklearn, c=y, edgecolor="none", alpha=0.8, cmap=plt.cm.get_cmap("viridis", 3)
    )
    ax[1].set_xlabel("Linear Discriminant 1")
    ax[1].set_ylabel("Linear Discriminant 2")
    ax[1].set_title("Sklearn LDA")

    # plt.colorbar()
    plt.show()