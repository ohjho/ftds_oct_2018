df = pd.DataFrame()
df["Chapter"] = list(range(1,len(chapters) + 1))
for key,value in chapter_counts.items():
    df[key] = value