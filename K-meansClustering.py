import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# read csv input file
FilePath = "csv_files/labeledData.csv"
df = pd.read_csv(FilePath)

workable_dataset = df.loc[:, ~df.columns.isin(['Shooter Last Name', 'Shooter First Name', 'Full Date', 'City'])]
# initialize kmeans parameters
kmeans_kwargs = {"init": "random", "n_init": 10, "random_state": 1}
scaled_df = StandardScaler().fit_transform(workable_dataset)
# create list to hold SSE values for each k
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(workable_dataset)
    sse.append(kmeans.inertia_)

# visualize results
plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()

# the elbow is situated at 4, therefore the value of k=4
kmeans = KMeans(init="random", n_clusters=2, n_init=10, random_state=1)

# fit k-means algorithm to data
kmeans.fit(scaled_df)

# view cluster assignments for each observation
print(kmeans.labels_)
y_kmeans = kmeans.predict(scaled_df)
df['cluster'] = kmeans.labels_

print(f'accuracy for k-means clustering: {np.mean(df["label"] == df["cluster"])}')

print(df)
