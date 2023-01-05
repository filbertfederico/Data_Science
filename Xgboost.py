import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
import numpy as np

df = pd.read_csv("filledData.csv")
workable_dataset = df.loc[:, ~df.columns.isin(['Shooter Last Name', 'Shooter First Name', 'Full Date', 'City'])]
conditions = [(workable_dataset["Number Killed"] <= 5),
              workable_dataset["Number Killed"] > 5]
choices = [0, 1]

workable_dataset['label'] = np.select(conditions, choices, default=np.nan)
train, test = train_test_split(workable_dataset, test_size=0.3)
print(len(df.columns))

n_row=160
chosen_features = ["School Performance", "History of Animal Abuse", "Bullied", "Childhood Trauma"]
train_X = train.iloc[:, 2:-1]
train_y = train.iloc[:n_row, -1]
test_X = test.iloc[:, 2:-1]
test_y = test.iloc[:n_row, -1]
print(train_X.info())
print(test_y.info())


xg_reg = xgb.XGBClassifier(objective='reg:logistic', colsample_bytree=0.2, learning_rate=0.01,
                           max_depth=10, alpha=10, n_estimators=10)

xg_reg.fit(train_X, train_y)

preds = xg_reg.predict(test_X)
print(np.mean(preds == test_y))
