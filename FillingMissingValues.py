import pandas as pd


FilePath = "CategorisedData.csv"
df = pd.read_csv(FilePath)

df = df.apply(lambda x:x.fillna(x.value_counts().index[0]))

df.to_excel("filledData.xlsx", index=False)
df.to_csv("filledData.csv", index=False)
