import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv("csv_files/labeledData.csv")
workable_dataset = df.drop(df.columns.difference(["Inability to Perform Daily Tasks",
                                                  "Unusually Calm or Happy", "Rapid Mood Swings", "Increased Agitation",
                                                  "Abusive Behavior", "Isolation", "Losing Touch with Reality",
                                                  "Paranoia", "Suicidality", "Psychiatric Medication",
                                                  "Mental Illness", "Autism Spectrum", "Mood Disorder",
                                                  "Other Psychiatric Disorder"]), 1)
workable_dataset1 = df.drop(df.columns.difference(["Bullied", "Parental Divorce / Separation",
                                                   "Parental Death in Childhood", "Childhood Trauma", "Physically Abused",
                                                   "Sexually Abused", "Emotionally Abused", "Neglected", "Childhood SES",
                                                   "Mother Violent Treatment", "Parental Substance Abuse",
                                                   "Parent Criminal Record", "Family Incarcerated", "Adult Trauma",
                                                   "Recent or Ongoing Stressor", "Signs of Being in Crisis",
                                                   "Other stressor", "Family Issue", "Legal Issue"]), 1)


def compute_mental_illness_count(df, df1):
    for i in range(df.shape[0]):
        total = 0
        for j in df.columns:
            if df.at[i, j] == 1:
                total += 1
        df1.at[i, "Mental Illness Count"] = total


def compute_trauma_count(df, df1):
    for i in range(df.shape[0]):
        total = 0
        for j in df.columns:
            if df.at[i, j] == 1:
                total += 1
        df1.at[i, "Trauma Count"] = total


compute_mental_illness_count(workable_dataset, df)
compute_trauma_count(workable_dataset1, df)


newdf = df.filter(['Number Killed', 'Mental Illness Count', 'Trauma Count'], axis=1)
print(newdf)
