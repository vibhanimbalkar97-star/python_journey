Bilkul. K-Means ko **real ML project mein code karne ka standard flow** simple steps mein dekhte hain.

## K-Means implementation flow

```text
1. Load dataset
      ↓
2. Understand data / EDA
      ↓
3. Select features (X)
      ↓
4. Handle missing values
      ↓
5. Encode categorical features if needed
      ↓
6. Scale features
      ↓
7. Find suitable K → Elbow Method
      ↓
8. Create KMeans model
      ↓
9. Fit model
      ↓
10. Get cluster labels
      ↓
11. Analyze clusters
      ↓
12. Visualize clusters
```

---

## Step 1 — Import libraries

```python
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
```

---

## Step 2 — Load dataset

For example, customer data:

```python
df = pd.read_csv("customers.csv")
```

Check data:

```python
df.head()
```

```python
df.shape
```

```python
df.info()
```

```python
df.isnull().sum()
```

---

## Step 3 — Select features

Suppose our dataset has:

```text
CustomerID
Age
AnnualIncome
SpendingScore
```

For clustering, we don't need `CustomerID`.

```python
X = df[['Age', 'AnnualIncome', 'SpendingScore']]
```

There is **no `y`** in K-Means.

---

## Step 4 — Handle missing values

Check:

```python
X.isnull().sum()
```

If missing values exist, handle them before K-Means.

For example:

```python
X = X.fillna(X.mean())
```

---

## Step 5 — Encode categorical columns if required

If your data contains:

```text
Gender
Male
Female
```

you need to convert it into numerical form.

For example:

```python
X = pd.get_dummies(X, columns=['Gender'], drop_first=True)
```

But if you're using only numerical columns like:

```text
Age
Income
SpendingScore
```

you don't need encoding.

---

# Step 6 — Feature Scaling ⭐

This is **very important for K-Means**.

Why?

Because K-Means uses **distance**.

Suppose:

```text
Age = 25
Income = 500000
```

Income has a much larger numerical range.

It can dominate the distance calculation.

So we scale:

```python
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

Now features are on a comparable scale.

---

# Step 7 — Find K using Elbow Method

Try different values of K:

```python
inertia = []

for k in range(1, 11):

    model = KMeans(n_clusters=k, random_state=42)

    model.fit(X_scaled)

    inertia.append(model.inertia_)
```

Now plot:

```python
plt.plot(range(1, 11), inertia, marker='o')

plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")

plt.show()
```

You inspect the graph and choose the approximate elbow.

Suppose you find:

```text
K = 3
```

---

# Step 8 — Create final K-Means model

```python
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)
```

---

# Step 9 — Fit the model

```python
kmeans.fit(X_scaled)
```

Behind the scenes:

```text
Initial centroids
       ↓
Calculate distances
       ↓
Assign points
       ↓
Calculate new centroids
       ↓
Repeat
       ↓
Final clusters
```

---

# Step 10 — Get cluster labels

```python
labels = kmeans.labels_
```

You might get:

```text
[0, 0, 1, 2, 2, 1, 0, ...]
```

These numbers represent the cluster assigned to each row.

---

# Step 11 — Add clusters to original DataFrame

This is useful for analysis:

```python
df['Cluster'] = labels
```

Now:

```text
Age   Income   SpendingScore   Cluster
22    25000    20              0
25    30000    25              0
45    80000    80              2
48    85000    90              2
35    50000    50              1
```

---

# Step 12 — Analyze each cluster

This is where **business meaning** comes in.

```python
df.groupby('Cluster')[['Age', 'AnnualIncome', 'SpendingScore']].mean()
```

You might get something like:

```text
Cluster  Age   Income   SpendingScore
0        24    28000    25
1        35    50000    50
2        47    82000    85
```

Then we can interpret:

```text
Cluster 0 → Lower income / lower spending
Cluster 1 → Medium income / medium spending
Cluster 2 → Higher income / higher spending
```

Remember: **K-Means only creates the clusters. We interpret what those clusters mean.**

---

# Step 13 — Visualize

If you have two features:

```python
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=labels
)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clusters")

plt.show()
```

If you have exactly two features, visualization is easy.

If you have many features, you can use **PCA** later to visualize them in 2D.

---

# Complete beginner code

This is the version I'd recommend you practice:

```python
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# 1. Load data
df = pd.read_csv("customers.csv")


# 2. Select features
X = df[['Age', 'AnnualIncome', 'SpendingScore']]


# 3. Handle missing values
X = X.fillna(X.mean())


# 4. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# 5. Elbow Method
inertia = []

for k in range(1, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42
    )

    model.fit(X_scaled)

    inertia.append(model.inertia_)


# 6. Plot Elbow
plt.plot(range(1, 11), inertia, marker='o')

plt.xlabel("K")
plt.ylabel("Inertia")
plt.title("Elbow Method")

plt.show()


# 7. Create final model
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)


# 8. Train model
kmeans.fit(X_scaled)


# 9. Get cluster labels
df['Cluster'] = kmeans.labels_


# 10. Check result
print(df.head())


# 11. Analyze clusters
print(
    df.groupby('Cluster')[[
        'Age',
        'AnnualIncome',
        'SpendingScore'
    ]].mean()
)
```

## Interview mein pura process ek line mein

> **"First I perform EDA and select relevant features, handle missing and categorical data, scale the features because K-Means is distance-based, use the Elbow Method to select a suitable K, train K-Means, get cluster labels, and finally analyze and interpret the clusters."**

### Important for your ML learning

K-Means practice karte waqt ye 4 concepts **properly samajhna**:

**1. Why scaling?** → Distance-based algorithm
**2. Why Elbow Method?** → Suitable K choose karne ke liye
**3. How centroid changes?** → Mean of points in cluster
**4. How to evaluate clustering?** → **Silhouette Score** is the next important topic.
