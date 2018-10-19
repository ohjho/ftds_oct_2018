df = pd.read_html("https://en.wikipedia.org/wiki/List_of_human_genes")[0]
df = df.rename(columns=df.iloc[0]).drop(df.index[0])
df.head()