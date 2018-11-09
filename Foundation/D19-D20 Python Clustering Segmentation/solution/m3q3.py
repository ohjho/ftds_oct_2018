
# Initialize PCA transformation, only keeping 125 components
pca = PCA(n_components = 125)

# Fit and transform item_data_scaled
PC_items = pca.fit_transform(item_data_scaled)

# Display shape of PC_items
PC_items.shape
