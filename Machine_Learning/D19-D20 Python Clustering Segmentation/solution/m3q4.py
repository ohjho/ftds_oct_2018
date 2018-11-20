
# Put PC_items into a dataframe
item_pca = pd.DataFrame(PC_items)
print(type(item_pca))

# Name the columns
item_pca.columns = ['PC{}'.format(i+1) for i in range(PC_items.shape[1])]

# Update its index
item_pca.index = item_data.index

# Display first 5 rows
item_pca.head()
