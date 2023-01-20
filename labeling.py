import pandas as pd
import numpy as np

df = pd.read_csv("csv_files/filledData.csv")

conditions = [(df["Number Killed"] <= 5),
              df["Number Killed"] > 5]
choices = [0, 1]
df['label'] = np.select(conditions, choices, default=np.nan)

df.to_csv("csv_files/labeledData.csv", index=False)
df.to_excel("excel_files/labeledData.xlsx", index=False)
