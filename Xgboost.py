import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
import numpy as np
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
# xg_reg = xgb.XGBClassifier(objective='reg:logistic')
#
# parameters = {"objective": ['reg:logistic'],
#               "colsample_bytree": [i for i in np.arange(0.5, 1.0, 0.1)],
#               "learning_rate": [i for i in np.arange(0.01, 0.3, 0.01)],
#               "max_depth": [1],
#               "alpha": [i for i in range(1, 10)],
#               "n_estimators": [10]}
#
# grid_GBC = GridSearchCV(estimator=xg_reg, param_grid=parameters, n_jobs=-1)
# grid_GBC.fit(train_X, train_y)
# print(" Results from Grid Search " )
# print("\n The best score across ALL searched params:\n",grid_GBC.best_score_)
# print("\n The best parameters across ALL searched params:\n",grid_GBC.best_params_)
# -----------------------------------------------------
# using the best possible parameters

xg_reg = xgb.XGBClassifier(objective='reg:logistic', colsample_bytree=0.9, learning_rate=0.01,
                           max_depth=50, alpha=2, n_estimators=2)

xg_reg.fit(train_X, train_y)

preds = xg_reg.predict(test_X)
print(f'accuracy for the xgboost model: {np.mean(preds == test_y)}')

print(classification_report(test_y, preds))