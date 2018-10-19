df = pd.read_csv("data/2017-12-city-of-london-street.csv")
print("Rows:{}\nCols:{}".format(*df.shape))
df.head()