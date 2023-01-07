import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn import tree


df = pd.read_csv("csv_files/labeledData.csv")
workable_dataset = df.loc[:, ~df.columns.isin(['Shooter Last Name', 'Shooter First Name', 'Full Date', 'City'])]

train, test = train_test_split(workable_dataset, test_size=0.2)

train_X = train.iloc[:, 6:95]
train_y = train.iloc[:, -1]
test_X = test.iloc[:, 6:95]
test_y = test.iloc[:, -1]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_X, train_y)
y_pred_CLF = clf.predict(test_X)

print(f'accuracy for decision tree model: {np.mean(y_pred_CLF == test_y)}')

print(classification_report(test_y, y_pred_CLF))
