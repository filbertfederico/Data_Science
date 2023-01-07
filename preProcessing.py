import pandas as pd

from datetime import datetime

FilePath = "csv_files/afterCleaning.csv"
df = pd.read_csv(FilePath)

# deleting everything except the important columns
df.drop(df.columns.difference(['Shooter Last Name', 'Shooter First Name', 'Full Date', 'City', 'Number Killed', 'Age',
                               'Gender', 'Education', 'School Performance',
                               'Community Involvement', 'Criminal Record',
                               'Part I Crimes', 'Part II Crimes',
                               'History of Physical Altercations', 'History of Animal Abuse',
                               'History of Domestic Abuse', 'Domestic Abuse Specified', 'History of Sexual Offenses',
                               'Violent Video Games', 'Bully', 'Bullied', 'Raised by Single Parent',
                               'Parental Divorce / Separation', 'Parental Death in Childhood', 'Parental Suicide ',
                               'Childhood Trauma', 'Physically Abused', 'Sexually Abused', 'Emotionally Abused',
                               'Neglected', 'Childhood SES', 'Mother Violent Treatment', 'Parental Substance Abuse',
                               'Parent Criminal Record', 'Family Member Incarcerated', 'Adult Trauma',
                               'Recent or Ongoing Stressor', 'Signs of Being in Crisis',
                               'Inability to Perform Daily Tasks', 'Notably Depressed Mood',
                               'Unusually Calm or Happy', 'Rapid Mood Swings', 'Increased Agitation', 'Abusive Behavior',
                               'Isolation', 'Losing Touch with Reality', 'Paranoia', 'Suicidality',
                               'Prior Hospitalization', 'Voluntary or Involuntary Hospitalization', 'Prior Counseling',
                               'Voluntary or Mandatory Counseling', 'Psychiatric Medication', 'Treatment 6 Months Prior to Shooting',
                               'Mental Illness', 'Known Family Mental Health History', 'Autism Spectrum',
                               'Substance Use', 'Health Issues', 'Head Injury / Possible TBI',
                               'Known Prejudices', 'Motive: Racism/Xenophobia', 'Motive: Religious Hate',
                               'Motive: Misogyny', 'Motive: Homophobia', 'Motive: Employment Issue',
                               'Motive: Economic Issue', 'Motive: Legal Issue', 'Motive: Relationship Issue',
                               'Motive: Interpersonal Conflict', 'Motive: Fame-Seeking', 'Motive: Other',
                               'Motive: Unknown', 'Social Media Use ']), 1,
        inplace=True)

# df = df.fillna("NULL")
df = df.drop(144) # empty row

print("column with more than 1 null: ")
for i in df.columns:
    if df[i].isnull().sum() > 1:
        print(i)
print("----------------------------------------------------------------------------")

print("column with more than 10 null: ")
for i in df.columns:
    if df[i].isnull().sum() > 1:
        print(i)
print("----------------------------------------------------------------------------")

print("column with more than 50 null: ")
for i in df.columns:
    if df[i].isnull().sum() > 1:
        print(i)
print("----------------------------------------------------------------------------")


df.to_csv("csv_files/afterPreProcess.csv", index=False)
df.to_excel("excel_files/afterPreProcess.xlsx")