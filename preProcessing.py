import pandas as pd

from datetime import datetime

ExcelFilePath = "afterCleaning.xlsx"
df = pd.read_excel(ExcelFilePath)

# deleting everything except the important columns
df.drop(df.columns.difference(['Shooter Last Name', 'Shooter First Name', 'Full Date', 'City', 'Number Killed', 'Age',
                               'Gender', 'Education', 'School Performance', 'School Performance Specified',
                               'Community Involvement', 'Community Involvement Specified', 'Criminal Record',
                               'Part I Crimes', 'Part II Crimes', 'Highest Level of Criminal Justice Involvement',
                               'History of Physical Altercations', 'History of Animal Abuse',
                               'History of Domestic Abuse', 'Domestic Abuse Specified', 'History of Sexual Offenses',
                               'Violent Video Games', 'Bully', 'Bullied', 'Raised by Single Parent',
                               'Parental Divorce / Separation', 'Parental Death in Childhood', 'Parental Suicide ',
                               'Childhood Trauma', 'Physically Abused', 'Sexually Abused', 'Emotionally Abused',
                               'Neglected', 'Childhood SES', 'Mother Violent Treatment', 'Parental Substance Abuse',
                               'Parent Criminal Record', 'Family Member Incarcerated', 'Adult Trauma',
                               'Recent or Ongoing Stressor', 'Signs of Being in Crisis', 'Timeline of Signs of Crisis',
                               'Signs of Crisis Expanded', 'Inability to Perform Daily Tasks', 'Notably Depressed Mood',
                               'Unusually Calm or Happy', 'Rapid Mood Swings', 'Increased Agitation', 'Abusive Behavior',
                               'Isolation', 'Losing Touch with Reality', 'Paranoia', 'Suicidality',
                               'Prior Hospitalization', 'Voluntary or Involuntary Hospitalization', 'Prior Counseling',
                               'Voluntary or Mandatory Counseling', 'Psychiatric Medication',
                               'Psychiatric Medication Specified', 'Treatment 6 Months Prior to Shooting',
                               'Mental Illness', 'Known Family Mental Health History', 'Autism Spectrum',
                               'Substance Use', 'Health Issues', 'Health Issues - Specify', 'Head Injury / Possible TBI',
                               'Known Prejudices', 'Motive: Racism/Xenophobia', 'Motive: Religious Hate',
                               'Motive: Misogyny', 'Motive: Homophobia', 'Motive: Employment Issue',
                               'Motive: Economic Issue', 'Motive: Legal Issue', 'Motive: Relationship Issue',
                               'Motive: Interpersonal Conflict', 'Motive: Fame-Seeking', 'Motive: Other',
                               'Motive: Unknown', 'Role of Psychosis in the Shooting', 'Social Media Use ']), 1,
        inplace=True)


df.to_excel("afterPreProcess.xlsx", index=False)