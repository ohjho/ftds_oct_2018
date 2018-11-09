pd.get_dummies(exp_df['CustomerID'])
exp_item_dummies = pd.get_dummies(exp_df['CustomerID'])
exp_item_dummies['CustomerID'] = exp_df['CustomerID']
exp_item_dummies
