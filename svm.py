import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import tree

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

model_linear = SVC(kernel="linear")
model_linear.fit(train_X, train_y)
pred_test_linear = model_linear.predict(test_X)

print(f'accuracy for linear model: {np.mean(pred_test_linear == test_y)}')

model_poly = SVC(kernel="poly", degree=4, C=1.0)
model_poly.fit(train_X, train_y)
pred_test_poly = model_poly.predict(test_X)

print(f'accuracy for SVC kernel model poly: {np.mean(pred_test_poly == test_y)}')

model_rbf = SVC(kernel = 'rbf', C = 0.1, gamma = 0.1)
model_rbf.fit(train_X, train_y)
pred_test_rbf = model_rbf.predict(test_X)

print(f'accuracy for SVC kernel model rbf: {np.mean(pred_test_rbf == test_y)}')


clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_X, train_y)
y_pred_CLF = clf.predict(test_X)

print(f'accuracy for decidsion tree model: {np.mean(y_pred_CLF == test_y)}')


print(classification_report(test_y, pred_test_rbf))
print(classification_report(test_y, y_pred_CLF))
