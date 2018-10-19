df = pd.DataFrame.from_dict(person_freqs,orient='index')
df.columns = ["Person"]
print(df)
df.plot.bar()