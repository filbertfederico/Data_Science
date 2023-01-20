import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

FilePath = "csv_files/mental_illness_stats.csv"
df = pd.read_csv(FilePath)

pearsoncorr = df.corr(method='pearson')
print(pearsoncorr)

sb.heatmap(pearsoncorr,
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5,
           fmt= '.2f',
           cbar_kws={'orientation': 'horizontal'})
plt.show()