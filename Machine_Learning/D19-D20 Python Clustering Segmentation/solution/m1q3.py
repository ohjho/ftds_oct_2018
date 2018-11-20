# Make figsize
plt.figure(figsize = (10,10))

# Bar plot by country
sns.countplot(y='Country',data = data)
