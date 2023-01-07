import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

df = pd.read_csv("csv_files/labeledData.csv")
workable_dataset = df.loc[:, ~df.columns.isin(['Shooter Last Name', 'Shooter First Name', 'Full Date', 'City'])]

train, test = train_test_split(workable_dataset, test_size=0.2)

train_X = train.iloc[:, 6:95]
train_y = train.iloc[:, -1]
test_X = test.iloc[:, 6:95]
test_y = test.iloc[:, -1]

# the next lines were used to determine the best possible parameters, only run it once
# -----------------------------------------------------
# model_poly = SVC(kernel="rbf")
#
# parameters = {"kernel": ["rbf"],
#               'C': [i for i in (1.0, 5.0, 0.1)],
#               'gamma': [i for i in np.arange(0.1, 10.0, 0.1)],
#               }
#
# grid_GBC = GridSearchCV(estimator=model_poly, param_grid=parameters, n_jobs=-1)
# grid_GBC.fit(train_X, train_y)
# print(" Results from Grid Search " )
# print("\n The best score across ALL searched params:\n",grid_GBC.best_score_)
# print("\n The best parameters across ALL searched params:\n",grid_GBC.best_params_)
# -----------------------------------------------------
# using the best possible parameters

model_rbf = SVC(kernel='rbf', C=5.0, gamma=0.1)
model_rbf.fit(train_X, train_y)
pred_test_rbf = model_rbf.predict(test_X)

print(f'accuracy for SVC kernel model rbf: {np.mean(pred_test_rbf == test_y)}')

print(classification_report(test_y, pred_test_rbf))