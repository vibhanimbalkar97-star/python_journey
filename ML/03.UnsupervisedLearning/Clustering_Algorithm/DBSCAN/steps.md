Bilkul. DBSCAN ka **practical coding flow** K-Means jaisa hi hai, but yahan **K choose nahi karna hota**. Instead, hum `eps` aur `min_samples` tune karte hain.

# DBSCAN implementation steps

```text
1. Load dataset
      ↓
2. EDA
      ↓
3. Select features X
      ↓
4. Handle missing values
      ↓
5. Encode categorical features if needed
      ↓
6. Scale features ⭐
      ↓
7. Choose eps + min_samples
      ↓
8. Create DBSCAN model
      ↓
9. Fit model
      ↓
10. Get cluster labels
      ↓
11. Identify noise (-1)
      ↓
12. Analyze clusters
      ↓
13. Visualize
```

---

## Step 1 — Import libraries

```python
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
```

---

## Step 2 — Load dataset

```python
df = pd.read_csv("customers.csv")
```

Basic EDA:

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

# Step 3 — Select features

Suppose customer dataset hai:

```text
Age
AnnualIncome
SpendingScore
```

```python
X = df[['Age', 'AnnualIncome', 'SpendingScore']]
```

DBSCAN mein bhi **target `y` nahi hota**.

---

# Step 4 — Handle missing values

```python
X = X.fillna(X.mean())
```

Real project mein missing values ke according appropriate imputation strategy choose kar sakte ho.

---

# Step 5 — Encoding

Agar categorical column hai:

```text
Gender
Male
Female
```

toh encode karna padega.

For example:

```python
X = pd.get_dummies(
    X,
    columns=['Gender'],
    drop_first=True
)
```

Agar sirf numerical columns hain, ye step skip.

---

# Step 6 — Scaling ⭐

DBSCAN **distance-based** hai, isliye scaling important hai.

```python
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

Ab:

```text
Age
Income
SpendingScore
```

comparable scale par aa jayenge.

---

# Step 7 — DBSCAN model create karo

```python
dbscan = DBSCAN(
    eps=0.5,
    min_samples=5
)
```

Yahan:

```text
eps = neighbourhood radius
min_samples = minimum points required for dense region
```

---

# Step 8 — Fit model

```python
dbscan.fit(X_scaled)
```

Behind the scenes:

```text
Point
 ↓
eps ke andar neighbours find
 ↓
Enough neighbours?
 ↓
Core / Border / Noise
 ↓
Cluster expand
```

---

# Step 9 — Cluster labels nikalo

```python
labels = dbscan.labels_
```

Example:

```text
[0, 0, 0, 1, 1, 1, -1, 0]
```

Meaning:

```text
0  → Cluster 0
1  → Cluster 1
-1 → Noise
```

---

# Step 10 — DataFrame mein cluster add karo

```python
df['Cluster'] = labels
```

Now:

| Age | Income | SpendingScore | Cluster |
| --: | -----: | ------------: | ------: |
|  22 |    25K |            20 |       0 |
|  24 |    28K |            25 |       0 |
|  45 |    80K |            85 |       1 |
|  48 |    85K |            90 |       1 |
|  70 |    10K |             5 |      -1 |

`-1` means DBSCAN ne us point ko **noise** classify kiya.

---

# Step 11 — Number of clusters check karo

```python
set(labels)
```

Suppose output:

```python
{0, 1, 2, -1}
```

Matlab:

```text
3 actual clusters
+
noise points
```

Number of clusters calculate karne ke liye:

```python
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

print(n_clusters)
```

---

# Step 12 — Noise points count karo

```python
noise_count = list(labels).count(-1)

print(noise_count)
```

Example:

```text
Noise points = 8
```

---

# Step 13 — Clusters analyze karo

```python
df.groupby('Cluster')[['Age', 'AnnualIncome', 'SpendingScore']].mean()
```

Isse pata chalega ki har cluster mein average customer characteristics kya hain.

---

# Step 14 — Visualization

Agar sirf 2 features hain:

```python
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=labels
)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("DBSCAN Clustering")

plt.show()
```

---

# Complete beginner code

```python
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN


# 1. Load data
df = pd.read_csv("customers.csv")


# 2. Select features
X = df[['Age', 'AnnualIncome', 'SpendingScore']]


# 3. Handle missing values
X = X.fillna(X.mean())


# 4. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# 5. Create DBSCAN model
dbscan = DBSCAN(
    eps=0.5,
    min_samples=5
)


# 6. Fit model
dbscan.fit(X_scaled)


# 7. Get labels
labels = dbscan.labels_


# 8. Add labels to dataframe
df['Cluster'] = labels


# 9. Check clusters
print(df['Cluster'].value_counts())


# 10. Count noise
noise_count = list(labels).count(-1)
print("Noise:", noise_count)


# 11. Analyze clusters
print(
    df.groupby('Cluster')[[
        'Age',
        'AnnualIncome',
        'SpendingScore'
    ]].mean()
)


# 12. Visualize
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=labels
)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("DBSCAN Clustering")

plt.show()
```

## K-Means vs DBSCAN code mein main difference

### K-Means

```python
# First choose K
kmeans = KMeans(n_clusters=3)

kmeans.fit(X_scaled)
```

### DBSCAN

```python
# No K
dbscan = DBSCAN(
    eps=0.5,
    min_samples=5
)

dbscan.fit(X_scaled)
```

So remember:

```text
K-Means
→ Choose K
→ Elbow Method
→ Centroids
→ Clusters


DBSCAN
→ Choose eps
→ Choose min_samples
→ Density
→ Core / Border / Noise
→ Clusters
```

**Next important DBSCAN practical topic:** `eps` ko **kaise choose kare using k-distance graph**, kyunki real project mein `eps=0.5` blindly nahi lena chahiye.
