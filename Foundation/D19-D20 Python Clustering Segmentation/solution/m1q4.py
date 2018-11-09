# Only keep transactions with customerID, using pandas .notnull method

data_updated=data[data.CustomerID.notnull()]
print(data_updated.shape)
print(data_updated.head())
