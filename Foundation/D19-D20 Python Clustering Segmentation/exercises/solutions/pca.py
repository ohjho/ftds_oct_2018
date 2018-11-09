from sklearn.decomposition import PCA

pca = PCA(n_components=2)

principalComponent = pca.fit_transform(x)
