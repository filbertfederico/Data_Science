import pandas as pd

from datetime import datetime

ExcelFilePath = "ViolenceProjectDataBase.xlsx"
df = pd.read_excel(ExcelFilePath)

new_header = df.iloc[0]
df = df[1:]
df.columns = new_header

d = df['Full Date']
newDate = []
for x in d:
    d = datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S')
    fd = d.strftime("%d/%m/%Y")
    newDate.append(fd)

df['Full Date'] = newDate

df.to_csv("csv_files/afterCleaning.csv", index=False)
df.to_excel("excel_files/afterCleaning.xlsx", index=False)



