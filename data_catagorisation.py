import pandas as pd

FilePath = "csv_files/afterPreProcess.csv"
df = pd.read_csv(FilePath)


# Part 1 Crime Separation


def categorise_crimes1(row, number):
    if number in row["Part I Crimes"]:
        return 1
    else:
        return 0


def categorise_crimes1_with_multiple_variables(row, numbers):
    if any(x in row["Part I Crimes"] for x in numbers):
        return 1
    else:
        return 0


df['Homicide'] = df.apply(lambda row: categorise_crimes1(row, '1'), axis=1)
df['Forcible Rape'] = df.apply(lambda row: categorise_crimes1(row, '2'), axis=1)
df['Robbery'] = df.apply(lambda row: categorise_crimes1(row, '3'), axis=1)
df['Aggravated Assault'] = df.apply(lambda row: categorise_crimes1(row, '4'), axis=1)
df['Burglary'] = df.apply(lambda row: categorise_crimes1(row, '5'), axis=1)
df['Theft'] = df.apply(lambda row: categorise_crimes1_with_multiple_variables(row, ['6', '7']), axis=1)
df['Arson'] = df.apply(lambda row: categorise_crimes1(row, '8'), axis=1)

# Changing the data in crime 1
df['Part I Crimes'] = df.apply(lambda row: categorise_crimes1_with_multiple_variables(row, ["1", "2", "3", "4", "5",
                                                                                            "6", "7", "8"]), axis=1)


# Part 2 Crime Separation


def categorise_crimes2(row, number):
    if number in row["Part II Crimes"]:
        return 1
    else:
        return 0


def categorise_crimes2_with_multiple_variables(row, numbers):
    if any(x in row["Part II Crimes"] for x in numbers):
        return 1
    else:
        return 0


df['Simple Assault'] = df.apply(lambda row: categorise_crimes2(row, '1'), axis=1)
df['Embezzlement'] = df.apply(lambda row: categorise_crimes2(row, '2'), axis=1)
df['Stolen Property'] = df.apply(lambda row: categorise_crimes2(row, '3'), axis=1)
df['Vandalism'] = df.apply(lambda row: categorise_crimes2(row, '4'), axis=1)
df['Weapons offenses'] = df.apply(lambda row: categorise_crimes2(row, '5'), axis=1)
df['Prostitution and other non-rape sex offenses'] = df.apply(lambda row: categorise_crimes2(row, '6'), axis=1)
df['Drugs'] = df.apply(lambda row: categorise_crimes2(row, '7'), axis=1)
df['DUI'] = df.apply(lambda row: categorise_crimes2(row, '8'), axis=1)
df['Other crimes'] = df.apply(lambda row: categorise_crimes2(row, '9'), axis=1)

# Changing the data in crime 2
df['Part II Crimes'] = df.apply(lambda row: categorise_crimes2_with_multiple_variables(row, ["1", "2", "3", "4", "5",
                                                                                             "6", "7", "8", "9"]),
                                axis=1)


# Domestic abuse specified Separation


def categorise_domestic_abuse_specified(row, number):
    if number in str(row["Domestic Abuse Specified"]):
        return 1
    else:
        return 0


def categorise_domestic_abuse_specified_with_multiple_variables(row, numbers):
    if any(x in str(row["Domestic Abuse Specified"]) for x in numbers):
        return 1
    else:
        return 0


df['Domestic Abuse Specified: Violence'] = df.apply(lambda row: categorise_domestic_abuse_specified(row, '1'), axis=1)
df['Domestic Abuse Specified: Sexual Violence'] = df.apply(lambda row: categorise_domestic_abuse_specified(row, '2'),
                                                           axis=1)
df['Domestic Abuse Specified: Control'] = df.apply(lambda row: categorise_domestic_abuse_specified(row, '3'), axis=1)
df['Domestic Abuse Specified: Weapon'] = df.apply(lambda row: categorise_domestic_abuse_specified(row, '4'), axis=1)

# Changing the data Domestic Abuse Specified
df = df.drop("Domestic Abuse Specified", axis=1)


# Ongoing stressors Separation


def categorise_recent_stressor(row, number):
    if number in str(row["Recent or Ongoing Stressor"]):
        return 1
    else:
        return 0


def categorise_recent_stressor_with_multiple_variables(row, numbers):
    if any(x in str(row["Recent or Ongoing Stressor"]) for x in numbers):
        return 1
    else:
        return 0


df['Recent Break-up'] = df.apply(lambda row: categorise_recent_stressor(row, '1'), axis=1)
df['Employment Stressor'] = df.apply(lambda row: categorise_recent_stressor(row, '2'), axis=1)
df['Economic Stressor'] = df.apply(lambda row: categorise_recent_stressor(row, '3'), axis=1)
df['Family Issue'] = df.apply(lambda row: categorise_recent_stressor(row, '4'), axis=1)
df['Legal Issue'] = df.apply(lambda row: categorise_recent_stressor(row, '5'), axis=1)
df['Other stressor'] = df.apply(lambda row: categorise_recent_stressor(row, '6'), axis=1)

# Changing the data in crime 2
df['Recent or Ongoing Stressor'] = df.apply(lambda row: categorise_recent_stressor_with_multiple_variables(row,
                                                                                                           ["1", "2",
                                                                                                            "3",
                                                                                                            "4", "5",
                                                                                                            "6"]),
                                            axis=1)


# Voluntary or involuntary counselling Separation


def categorise_counselling(row, number):
    if number in str(row["Voluntary or Mandatory Counseling"]):
        return 1
    else:
        return 0


def categorise_counselling_with_multiple_variables(row, numbers):
    if any(x in str(row["Voluntary or Mandatory Counseling"]) for x in numbers):
        return 1
    else:
        return 0


df['Voluntary Counseling'] = df.apply(lambda row: categorise_recent_stressor(row, '1'), axis=1)
df['Involuntary Counseling'] = df.apply(lambda row: categorise_recent_stressor(row, '2'), axis=1)

# Changing the data in hospitalization
df['Voluntary or Mandatory Counseling'] = df.apply(lambda row: categorise_recent_stressor_with_multiple_variables(row,
                                                                                                                  ["1",
                                                                                                                   "2"]),
                                                   axis=1)
df.rename(columns={'Voluntary or Mandatory Counseling': 'Counseling'})


# Mental illness separation


def categorise_mental_illness(row, number):
    if number in str(row["Mental Illness"]):
        return 1
    else:
        return 0


def categorise_mental_illness_with_multiple_variables(row, numbers):
    if any(x in str(row["Mental Illness"]) for x in numbers):
        return 1
    else:
        return 0


df['Mood Disorder'] = df.apply(lambda row: categorise_recent_stressor(row, '1'), axis=1)
df['Thought Disorder'] = df.apply(lambda row: categorise_recent_stressor(row, '2'), axis=1)
df['Other Psychiatric Disorder'] = df.apply(lambda row: categorise_recent_stressor(row, '3'), axis=1)
df['Indication of psychiatric disorder but no diagnosis'] = df.apply(lambda row: categorise_recent_stressor(row, '4'),
                                                                     axis=1)
# Changing the data in mental illness
df['Mental Illness'] = df.apply(
    lambda row: categorise_recent_stressor_with_multiple_variables(row, ["1", "2", "3", "4"]),
    axis=1)


# Mental illness separation


def categorise_substance_use(row, number):
    if number in str(row["Substance Use"]):
        return 1
    else:
        return 0


def categorise_substance_use_with_multiple_variables(row, numbers):
    if any(x in str(row["Substance Use"]) for x in numbers):
        return 1
    else:
        return 0


df['Problem with alcohol'] = df.apply(lambda row: categorise_substance_use(row, '1'), axis=1)
df['Marijuana'] = df.apply(lambda row: categorise_substance_use(row, '2'), axis=1)
df['Other Drugs'] = df.apply(lambda row: categorise_substance_use(row, '3'), axis=1)

# Changing the data in mental illness
df['Substance Use'] = df.apply(
    lambda row: categorise_substance_use_with_multiple_variables(row, ["1", "2", "3"]),
    axis=1)

#fixing adult trauma


def categorise_adult_trauma(row, number):
    if number in str(row["Adult Trauma"]):
        return 3


df['Adult Trauma'] = df.apply(
    lambda row: categorise_substance_use_with_multiple_variables(row, ["1, 3"]),
    axis=1)

#cahnge known family mental health history


def categorise_fam_health(row, number):
    if number in str(row["Known Family Mental Health History"]):
        return 1
    else:
        return 0


df['Family member with health issues'] = df.apply(lambda row: categorise_fam_health(row, "1"), axis=1)
df['Family member with mental health issues'] = df.apply(lambda row: categorise_fam_health(row, "2"), axis=1)

df = df.drop("Known Family Mental Health History", axis=1)

df.to_csv("csv_files/CategorisedData.csv", index=False)
df.to_excel("excel_files/CategorisedData.xlsx", index=False)
