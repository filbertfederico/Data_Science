import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("filledData.csv")
workable_dataset = df.loc[:, ~df.columns.isin(['Shooter Last Name', 'Shooter First Name', 'Full Date', 'City'])]

conditions = [(workable_dataset["Number Killed"] <= 5),
              workable_dataset["Number Killed"] > 5]
choices = [0, 1]

workable_dataset['label'] = np.select(conditions, choices, default=np.nan)

train, test = train_test_split(workable_dataset, test_size=0.3)

train_X = train.iloc[:, 5:70]
train_y = train.iloc[:, -1]
test_X = test.iloc[:, 5:70]
test_y = test.iloc[:, -1]

classifier = LogisticRegression(solver="lbfgs", random_state=0)
classifier.fit(train_X, train_y)
predicted_y = classifier.predict(test_X)
print(classifier.score(test_X, test_y))