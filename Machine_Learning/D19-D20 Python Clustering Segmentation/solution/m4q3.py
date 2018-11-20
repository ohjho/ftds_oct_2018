k_means = make_pipeline(StandardScaler(), KMeans(n_clusters=3, random_state=123))

k_means.fit(threshold_df)

threshold_df['cluster'] = k_means.predict(threshold_df)

threshold_df.head()
