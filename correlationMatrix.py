import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("filledData.csv")
print(df.iloc[:, 20:108])
df2 = df.iloc[:, :25]
df3 = df.iloc[:, 25:50]
df4 = df.iloc[:, 50:73]
df5 = df.iloc[:, 73:96]
df6 = df.iloc[:, 96:-1]

print("The correlation between number of killed and all others:")

print(df.corrwith(df['Number Killed']))
for i in df.corrwith(df['Number Killed']):
    if i > 0.15:
        print(i[0])

# print(df3)

corr_matrix = df6.corr()
# print(corr_matrix)


sns.heatmap(corr_matrix, annot=True)
plt.show()
