import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample data points
x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Plot the data points
plt.scatter(x, y)
plt.title('Scatter Plot of Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Combine x and y into a list of (x, y) pairs
data = list(zip(x, y))

# Find inertia for 1 to 10 clusters
inertias = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.plot(range(1, 11), inertias, marker='o')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

# Apply KMeans with 3 clusters
kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
plt.scatter(x, y, c=kmeans.labels_)
plt.show()