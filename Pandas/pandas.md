## What is Pandas?

**Pandas is a Python library used mainly for data analysis and data manipulation.**

Think of it as:

> **Python + Excel-like tables + powerful data operations**

```python
import pandas as pd
```

---

## Why do we need Pandas?

Python lists/dictionaries can store data, and NumPy is excellent for numerical calculations. But when you have **real-world tabular data**, Pandas makes it much easier to work with.

Example data:

| Name | Age | Salary | City   |
| ---- | --: | -----: | ------ |
| Amit |  25 |  40000 | Pune   |
| Ram  |  30 |  50000 | Mumbai |
| John |  28 |  45000 | Delhi  |

With Pandas, you can easily:

* Read this data
* Filter rows
* Select columns
* Sort data
* Handle missing values
* Remove duplicates
* Group data
* Calculate statistics
* Merge datasets
* Export results

---

## Main Pandas data structures

| Structure       | Meaning                                     |
| --------------- | ------------------------------------------- |
| **Series**      | One-dimensional labeled data                |
| **DataFrame** ⭐ | Two-dimensional table with rows and columns |

Example:

```python
import pandas as pd

data = {
    "name": ["Amit", "Ram", "John"],
    "age": [25, 30, 28]
}

df = pd.DataFrame(data)
```

`df` looks like:

```text
   name  age
0  Amit   25
1  Ram    30
2  John   28
```

---

# Where is Pandas used?

### 1. Data Analysis ⭐

Analyze large datasets:

```python
df["salary"].mean()
```

---

### 2. Data Cleaning ⭐

Real-world data often contains:

```text
Missing values
Duplicates
Wrong data
Inconsistent formats
```

Pandas provides functions to handle these.

```python
df.dropna()
df.fillna()
df.drop_duplicates()
```

---

### 3. Reading CSV/Excel files

Very common use case:

```python
df = pd.read_csv("employees.csv")
```

```python
df = pd.read_excel("employees.xlsx")
```

---

### 4. Filtering data

```python
df[df["age"] > 25]
```

Meaning:

> Give me employees whose age is greater than 25.

---

### 5. Sorting

```python
df.sort_values("salary")
```

---

### 6. Grouping

Very important for data analysis:

```python
df.groupby("city")["salary"].mean()
```

Meaning:

> Find the average salary for each city.

---

### 7. Combining datasets

You can combine tables using:

```python
pd.merge()
pd.concat()
```

Similar to SQL **JOIN** and combining datasets.

---

### 8. Machine Learning / AI ⭐

Pandas is commonly used **before machine learning**.

Typical workflow:

```text
CSV / Database
      ↓
   Pandas
      ↓
Clean data
      ↓
Analyze data
      ↓
Prepare features
      ↓
NumPy / Scikit-learn
      ↓
Machine Learning model
```

---

# Pandas vs NumPy

| NumPy                          | Pandas                      |
| ------------------------------ | --------------------------- |
| Numerical computing            | Data analysis               |
| Mainly arrays                  | Tables/DataFrames           |
| Fast mathematical operations   | Data manipulation           |
| Matrix/vector operations       | Filtering/grouping/merging  |
| `ndarray`                      | `DataFrame`, `Series`       |
| Foundation for many data tools | Built on/uses NumPy heavily |

### Simple example

**NumPy:**

```python
arr = np.array([10, 20, 30])
arr.mean()
```

Good for numerical calculations.

**Pandas:**

```python
df["salary"].mean()
```

Good for calculating/analyzing a column in a dataset.

---

# Real-world use cases

Pandas is used for:

* 📊 Data analysis
* 🧹 Data cleaning
* 📁 CSV/Excel processing
* 🤖 Machine Learning data preparation
* 📈 Business reports
* 🔍 Exploratory Data Analysis (EDA)
* 🗄️ Processing database/query results
* 🧪 Research and scientific data
* 💰 Financial data analysis
* 👥 Customer/employee data analysis

---

## What should you learn first?

For your **NumPy → Pandas → ML/AI** path, learn Pandas in this order:

```text
1. Series
2. DataFrame
3. Creating DataFrames
4. Reading CSV/Excel
5. head(), tail(), info(), describe()
6. Selecting rows and columns
7. loc / iloc
8. Filtering
9. Sorting
10. Adding/updating/deleting columns
11. Missing values
12. Duplicates
13. groupby()
14. Aggregation
15. merge()
16. concat()
17. apply()
18. Basic EDA
```

### One-line interview answer ⭐

> **Pandas is a Python library used for data manipulation, cleaning, analysis, and preparation of structured/tabular data, mainly using Series and DataFrame.**


