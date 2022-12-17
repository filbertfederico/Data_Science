import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import tree

df = pd.read_csv("filledData.csv")
workable_dataset = df.loc[:, ~df.columns.isin(['Shooter Last Name', 'Shooter First Name', 'Full Date', 'City'])]



# print(df.info())
# print(workable_dataset.iloc[:, -1])
#
# print(len(workable_dataset[workable_dataset["Number Killed"] == 4]))  # low
# print(len(workable_dataset[workable_dataset["Number Killed"] == 5]))  # medium
# print(len(workable_dataset[workable_dataset["Number Killed"] == 6]))
# print(len(workable_dataset[workable_dataset["Number Killed"] > 6]))  # high

conditions = [workable_dataset["Number Killed"] == 4,
              (workable_dataset["Number Killed"] >= 5) & (workable_dataset["Number Killed"] <= 6),
              workable_dataset["Number Killed"] > 6]
choices = ['low', 'medium', 'high']
workable_dataset['label'] = np.select(conditions, choices, default=np.nan)

# print(workable_dataset[["label", "Number Killed"]].head())

train, test = train_test_split(workable_dataset, test_size=0.3)

train_X = train.iloc[:, 50:102]
train_y = train.iloc[:, -1]
test_X = test.iloc[:, 50:102]
test_y = test.iloc[:, -1]

# print(test.iloc[:, 50])

model_linear = SVC(kernel="linear")
model_linear.fit(train_X, train_y)
pred_test_linear = model_linear.predict(test_X)

print(np.mean(pred_test_linear == test_y))

model_poly = SVC(kernel="poly", degree=4, C=1.0)
model_poly.fit(train_X, train_y)
pred_test_poly = model_poly.predict(test_X)

print(np.mean(pred_test_poly == test_y))

model_rbf = SVC()
model_rbf.fit(train_X, train_y)
pred_test_rbf = model_rbf.predict(test_X)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_X, train_y)
y_pred_CLF = clf.predict(test_X)

print(np.mean(y_pred_CLF == test_y))

print(np.mean(pred_test_rbf == test_y))

print(classification_report(test_y, pred_test_rbf))
print(classification_report(test_y, y_pred_CLF))
