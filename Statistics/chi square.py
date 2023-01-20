import pandas as pd
from scipy import stats

FilePath = "csv_files/mental_illness_stats.csv"
df = pd.read_csv(FilePath)
subset = df.sample(70)

crosstab1 = pd.crosstab(df['Number Killed'], df['Mental Illness Count'])
crosstab2 = pd.crosstab(df['Number Killed'], df['Trauma Count'])
crosstab3 = pd.crosstab(df['Number Killed'], df['mental_state_stats'])
# print(crosstab1)

print(f'the p value between Number Killed and mental state stats is {stats.chi2_contingency(crosstab1)[1]}')
print(f'the p value between Number Killed and mental state stats is {stats.chi2_contingency(crosstab2)[1]}')
print(f'the p value between Number Killed and mental state stats is {stats.chi2_contingency(crosstab3)[1]}')
