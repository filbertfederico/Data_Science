import statistics

import pandas as pd

FilePath = "csv_files/mental_illness_stats.csv"
df = pd.read_csv(FilePath)

condition1 = df["Number Killed"] <= 5
condition2 = df["Number Killed"] > 5
subset1 = df[condition1].sample(70)
subset2 = df[condition2].sample(70)

MeanMentalIllness1 = statistics.mean(subset1['Mental Illness Count'])
MeanTrauma1 = statistics.mean(subset1['Trauma Count'])
MeanTotal1 = statistics.mean(subset1['mental_state_stats'])

MeanMentalIllness2 = statistics.mean(subset2['Mental Illness Count'])
MeanTrauma2 = statistics.mean(subset2['Trauma Count'])
MeanTotal2 = statistics.mean(subset2['mental_state_stats'])

print(f'The mean of the mental illness count for the first sample is {MeanMentalIllness1}')
print(f'The mean of the mental illness count for the second sample is {MeanMentalIllness2}')
print(f'The mean of the trauma count for the first sample is {MeanTrauma1}')
print(f'The mean of the trauma count for the second sample is {MeanTrauma2}')
print(f'The mean of the total of both counts for the first sample is {MeanTotal1}')
print(f'The mean of the total of both counts for the second sample is {MeanTotal2}')

sdMentalIllness1 = statistics.stdev(subset1['Mental Illness Count'])
sdTrauma1 = statistics.stdev(subset1['Trauma Count'])
sdTotal1 = statistics.stdev(subset1['mental_state_stats'])

sdMentalIllness2 = statistics.stdev(subset2['Mental Illness Count'])
sdTrauma2 = statistics.stdev(subset2['Trauma Count'])
sdTotal2 = statistics.stdev(subset2['mental_state_stats'])

print("\n")
print(f'The standard deviation of the mental illness count for the first sample is {sdMentalIllness1}')
print(f'The standard deviation of the mental illness count for the second sample is {sdMentalIllness2}')
print(f'The standard deviation of the trauma count for the first sample is {sdTrauma1}')
print(f'The standard deviation of the trauma count for the second sample is {sdTrauma2}')
print(f'The standard deviation of the total of both counts for the first sample is {sdTotal1}')
print(f'The standard deviation of the total of both counts for the second sample is {sdTotal2}')

