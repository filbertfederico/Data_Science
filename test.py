import pandas as pd

ExcelFilePath = "afterCleaning.xlsx"
df = pd.read_excel(ExcelFilePath)

print(df['Bullied'].isna().sum())

