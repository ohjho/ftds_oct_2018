
# Initialize and fit a PCA transformation
pca = PCA()
pca.fit(item_data_scaled)

# Generate new features
PC_items = pca.transform(item_data_scaled)

# Display first 5 rows
PC_items[:5]
