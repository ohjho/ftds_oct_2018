principalDf = pd.DataFrame(data=principalComponent, columns=['principal component 1','principal component2'])
principalDf = pd.concat([principalDf, df['target']], axis = 1)

principalDf.head()