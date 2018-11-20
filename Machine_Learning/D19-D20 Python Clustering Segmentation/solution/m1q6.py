product_data = data.groupby('CustomerID')['StockCode'].agg({'total_product':'count', 'total_unique_product':'nunique'})
