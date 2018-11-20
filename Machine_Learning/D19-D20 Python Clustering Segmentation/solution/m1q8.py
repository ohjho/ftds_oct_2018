agg_cart_data = cart_data.groupby('CustomerID')['cart_value'].agg({'avg_cart_value':'mean','min_cart_value':'min','max_cart_value':'max'})
