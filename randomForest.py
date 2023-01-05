from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("filledData.csv")
workable_dataset = df.loc[:, ~df.columns.isin(['Shooter Last Name', 'Shooter First Name', 'Full Date', 'City'])]

conditions = [(workable_dataset["Number Killed"] <= 6),
              workable_dataset["Number Killed"] > 6]
choices = [0, 1]

workable_dataset['label'] = np.select(conditions, choices, default=np.nan)

# X = workable_dataset.drop(["label"], axis=1)
# y = workable_dataset["label"]
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

train, test = train_test_split(workable_dataset, test_size=0.3)
X_train = train.iloc[:, 20:70]
y_train = train.iloc[:, -1]
X_test = test.iloc[:, 20:70]
y_test = test.iloc[:, -1]

# Instantiate model with 1000 decision trees
rf = RandomForestClassifier(n_estimators=500, max_features="auto", random_state=42)
# Train the model on training data
rf.fit(X_train, y_train)
predictions = rf.predict(X_test)
print(predictions)
print(rf.predict_proba(X_test))
print(rf.feature_importances_)

print(np.mean(predictions == y_test))