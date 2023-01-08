from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("csv_files/labeledData.csv")
workable_dataset = df.loc[:, ~df.columns.isin(['Shooter Last Name', 'Shooter First Name', 'Full Date', 'City', "Age",
                                               "Gender", "Education", "School Performance", "Community Involvement",
                                               "History of Domestic Abuse", "Violent Video Games",
                                               "Voluntary or Involuntary Hospitalization", "Motive: Racism/Xenophobia"])]

train, test = train_test_split(workable_dataset, test_size=0.2)

train_X = train.iloc[:, 1:81]
train_y = train.iloc[:, -1]
test_X = test.iloc[:, 1:81]
test_y = test.iloc[:, -1]

classifier = LogisticRegression(solver="lbfgs", random_state=0)
classifier.fit(train_X, train_y)
predicted_y = classifier.predict(test_X)
print(classifier.score(test_X, test_y))