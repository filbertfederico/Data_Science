from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
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
# rf = RandomForestClassifier(random_state=42)
#
# parameters = {"n_estimators": [i for i in range(1, 500)]}
#
# grid_GBC = GridSearchCV(estimator=rf, param_grid=parameters, n_jobs=-1)
# grid_GBC.fit(train_X, train_y)
# print(" Results from Grid Search " )
# print("\n The best score across ALL searched params:\n",grid_GBC.best_score_)
# print("\n The best parameters across ALL searched params:\n",grid_GBC.best_params_)
# -----------------------------------------------------
# using the best possible parameters

# Instantiate model with 1000 decision trees
rf = RandomForestClassifier(n_estimators=327, random_state=42)
# Train the model on training data
rf.fit(train_X, train_y)
predictions = rf.predict(test_X)
print(rf.feature_importances_)

print(f'accuracy for SVC kernel model poly: {np.mean(predictions == test_y)}')

print(classification_report(test_y, predictions))

