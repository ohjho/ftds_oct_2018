sales_data = data.groupby('CustomerID')['Sales'].agg({'total_sales':'sum','avg_product_value':'mean'})
