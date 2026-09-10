Outliers **kyu check karte hain** aur **kiske check karte hain**, dono simple way mein samjho.

### 1. Outliers kyu check karte hain?

**Outlier = aisi value jo baaki values se bahut zyada ya bahut kam ho.**

Example:

```text
Salary: 25k, 30k, 28k, 32k, 35k, 500k
```

Yahan `500k` baaki values se bahut different hai → **outlier**.

Outlier check karte hain because:

* 📊 **Mean ko affect kar sakta hai**
* 🤖 **ML model ki performance affect kar sakta hai**
* 📈 Distribution/skewness ko change kar sakta hai
* ❌ Kabhi-kabhi data-entry mistake hoti hai
* ✅ Kabhi-kabhi outlier actually genuine value hoti hai

**Important:** Outlier milne ka matlab automatically usko delete karna nahi hai. Pehle reason samajhna hai.

---

### 2. Outliers kiske check karte hain?

EDA mein generally **continuous/numerical columns** ke outliers check karte hain.

For example:

| Column      | Type        | Outlier check? |
| ----------- | ----------- | -------------- |
| Age         | Continuous  | ✅ Yes          |
| Salary      | Continuous  | ✅ Yes          |
| Height      | Continuous  | ✅ Yes          |
| Weight      | Continuous  | ✅ Yes          |
| Study_Hours | Continuous  | ✅ Yes          |
| Gender      | Categorical | ❌ Not normally |
| City        | Categorical | ❌ No           |
| Department  | Categorical | ❌ No           |

So simple rule:

> **Outlier checking → mainly numerical/continuous data ke liye.**

### 3. Kaise check karte hain?

Most common:

**Boxplot**

```python
sns.boxplot(x=df['Salary'])
```

Or mathematically using **IQR**:

```text
Q1 = 25th percentile
Q3 = 75th percentile

IQR = Q3 - Q1

Lower = Q1 - 1.5 × IQR
Upper = Q3 + 1.5 × IQR
```

Jo values `Lower` se neeche ya `Upper` se upar hain → **potential outliers**.

### Interview mein simple answer

> **“We check outliers mainly in numerical/continuous features because extreme values can affect statistical analysis and ML model performance.”**
================================================================================================================================================

| Step   | What to check            | Example                              |
| ------ | ------------------------ | ------------------------------------ |
| 1️⃣    | Understand data          | `df.head()`, `df.shape`              |
| 2️⃣    | Select numerical columns | `df.select_dtypes(include='number')` |
| 3️⃣    | Check data types         | `df.info()`                          |
| 4️⃣    | Check missing values     | `df[num_cols].isna().sum()`          |
| 5️⃣    | Check duplicates         | `df.duplicated().sum()`              |
| 6️⃣    | Statistical summary      | `df[num_cols].describe()`            |
| 7️⃣    | Check distribution       | Histogram                            |
| 8️⃣    | Check skewness           | `df[num_cols].skew()`                |
| 9️⃣    | Detect outliers          | Boxplot                              |
| 🔟     | Check relationships      | Scatterplot                          |
| 1️⃣1️⃣ | Check correlation        | Correlation matrix / heatmap         |
| 1️⃣2️⃣ | Compare with target      | Depends on target type               

================================================================================================================================================

Yes. For **continuous/numerical data**, keep the data cleaning + preprocessing flow like this:

### Data Cleaning & Preprocessing — Continuous Data

| Step | What we do                      | Common method                              |
| ---- | ------------------------------- | ------------------------------------------ |
| 1️⃣  | Check data type                 | `df.info()`                                |
| 2️⃣  | Handle missing values           | Mean / Median                              |
| 3️⃣  | Check duplicates                | `duplicated()`                             |
| 4️⃣  | Check invalid values            | Domain/business rules                      |
| 5️⃣  | Check outliers                  | IQR / Boxplot                              |
| 6️⃣  | Handle outliers if needed       | Remove / Cap / Transform                   |
| 7️⃣  | Check skewness                  | `skew()`                                   |
| 8️⃣  | Transform skewed data if needed | Log / Power transformation                 |
| 9️⃣  | Feature scaling                 | StandardScaler / MinMaxScaler              |
| 🔟   | Final check                     | `describe()`, missing values, distribution |

### Example

Suppose your dataset has:

```text
Age
Salary
Experience
Study_Hours
```

#### Step 1 — Missing values

```python
df[['Age', 'Salary', 'Experience', 'Study_Hours']].isna().sum()
```

For continuous data:

```python
df['Age'] = df['Age'].fillna(df['Age'].median())
```

**Mean vs Median:**

* Normally distributed → Mean can be used
* Skewed / outliers present → Median is usually safer

---

#### Step 2 — Check invalid values

Example:

```text
Age = -5
Study_Hours = 50
```

If `Age` cannot logically be negative, investigate/fix it.

---

#### Step 3 — Handle outliers

First **detect** them.

```python
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

Then decide whether to:

* Keep → if genuine
* Remove → if error/extreme and inappropriate
* Cap → if genuine but too influential
* Transform → if highly skewed

---

#### Step 4 — Handle skewness

Check:

```python
df['Salary'].skew()
```

If highly right-skewed, you may use a transformation such as log transformation.

---

#### Step 5 — Scaling

If your ML algorithm needs features on a similar scale:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df[['Age', 'Salary', 'Experience']] = scaler.fit_transform(
    df[['Age', 'Salary', 'Experience']]
)
```

Common scalers:

| Scaler           | When commonly used                            |
| ---------------- | --------------------------------------------- |
| `StandardScaler` | Data centered around mean, many ML algorithms |
| `MinMaxScaler`   | Want values generally between 0 and 1         |
| `RobustScaler`   | Data contains significant outliers            |

### Easy flow to remember

**Missing → Duplicates → Invalid values → Outliers → Skewness → Transformation → Scaling → Final check**

One important distinction:

**EDA:** *“Problem hai kya?”*
**Cleaning:** *“Problem ko fix karein.”*
**Preprocessing:** *“Data ko ML model ke liye ready karein.”*
