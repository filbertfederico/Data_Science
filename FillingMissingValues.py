import pandas as pd


FilePath = "csv_files/CategorisedData.csv"
df = pd.read_csv(FilePath)

df = df.apply(lambda x:x.fillna(x.value_counts().index[0]))

# getting rid of columns with the same value in every row
nunique = df.nunique()
cols_to_drop = nunique[nunique == 1].index
print(cols_to_drop)
df.drop(cols_to_drop, axis=1, inplace=True)

df.to_csv("csv_files/filledData.csv", index=False)
df.to_excel("excel_files/filledData.xlsx", index=False)

