import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("filledData.csv")
df2 = df.iloc[:, :25]
df3 = df.iloc[:, 25:50]
df4 = df.iloc[:, 50:73]
df5 = df.iloc[:, 73:96]
df6 = df.iloc[:, 96:-1]

print("The correlation between number of killed and all others:")

corr_dfNK = df[df.columns[1:]].corr()['Number Killed'][:]
print(corr_dfNK[1].columns)

# for i in corr_dfNK:
#     if i > 0.15:
#         print(corr_dfNK.)

corr_matrix = df6.corr()
sns.heatmap(corr_matrix, annot=True)
plt.show()
