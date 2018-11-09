k_means = make_pipeline(StandardScaler(), KMeans(n_clusters=3, random_state=123))

k_means.fit(pca_df)

pca_df['cluster'] = k_means.predict(pca_df)

pca_df.head()
