# Get item_dummies
item_dummies = pd.get_dummies(data['StockCode'])

# Add CustomerID to item_dummies
item_dummies['CustomerID'] = data['CustomerID']

# Display first 5 rows of item_dummies
item_dummies.head()
