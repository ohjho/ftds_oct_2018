plt.figure(figsize=(8,8))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='plasma')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')