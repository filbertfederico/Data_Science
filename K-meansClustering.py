import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# read csv input file
FilePath = "filledData.csv"
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
kmeans = KMeans(init="random", n_clusters=4, n_init=10, random_state=1)

# fit k-means algorithm to data
kmeans.fit(scaled_df)

# view cluster assignments for each observation
print(kmeans.labels_)
y_kmeans = kmeans.predict(scaled_df)
df['cluster'] = kmeans.labels_

print(workable_dataset.iloc[:, 6])
# plt.scatter(workable_dataset.iloc[:, 1], workable_dataset.iloc[:, 20], c=y_kmeans, s=20, cmap='viridis')
#
# centers = kmeans.cluster_centers_
# plt.scatter(centers[:, 0], centers[:, 1], c='black', s=20, alpha=0.5)
# plt.show()

print(df)
