df = pd.DataFrame.from_dict( place_freqs,orient='index')
df.columns = ["Place"]
print(df)
df.plot.bar()