Yes. Think of `isna()` as **finding missing values**, and `.any()` as **checking whether at least one exists**.

### 1. Why use `isna().any()`?

```python
df.isna().any()
```

It tells you **which columns have at least one missing value**.

Example:

```text
Name      False
Age       True
City      False
Salary    True
```

Meaning:

* `Age` → has missing value
* `Salary` → has missing value

### 2. Column-wise missing values

**Count missing values in each column:**

```python
df.isna().sum()
```

Example:

```text
Name      0
Age       2
City      1
Salary    3
```

**Find columns having any missing value:**

```python
df.isna().any()
```

**Get only those column names:**

```python
df.columns[df.isna().any()]
```

---

### 3. Row-wise missing values

**Count missing values in each row:**

```python
df.isna().sum(axis=1)
```

Example:

```text
0    0
1    2
2    0
3    1
```

👉 Row `1` has 2 missing values.

**Find rows having at least one missing value:**

```python
df[df.isna().any(axis=1)]
```

---

### 🧠 Column-wise vs Row-wise

| Task                          | Code                        |
| ----------------------------- | --------------------------- |
| Missing count **column-wise** | `df.isna().sum()`           |
| Missing count **row-wise**    | `df.isna().sum(axis=1)`     |
| Any missing **column-wise**   | `df.isna().any()`           |
| Any missing **row-wise**      | `df.isna().any(axis=1)`     |
| Show rows with missing values | `df[df.isna().any(axis=1)]` |

`axis=1` → **go across columns → work row-wise**

---

## 4. How to drop a column?

```python
df = df.drop(columns=['title'])
```

Multiple columns:

```python
df = df.drop(columns=['title', 'press'])
```

Alternative:

```python
df.drop('title', axis=1)
```

---

## 5. How to drop a row?

By **index**:

```python
df = df.drop(index=5)
```

👉 Removes row with index `5`.

Multiple rows:

```python
df = df.drop(index=[2, 5, 8])
```

### Drop rows based on condition

For example, remove countries where population is missing:

```python
df = df.dropna(subset=['population'])
```

### Quick memory

| Want to remove                  | Use                                 |
| ------------------------------- | ----------------------------------- |
| Column                          | `df.drop(columns=['column'])`       |
| Multiple columns                | `df.drop(columns=['col1', 'col2'])` |
| Row by index                    | `df.drop(index=5)`                  |
| Multiple rows                   | `df.drop(index=[2,5,8])`            |
| Rows with missing value         | `df.dropna()`                       |
| Rows missing in specific column | `df.dropna(subset=['population'])`  |





### Drop duplicates — short

| Task                                           | Code                                       |
| ---------------------------------------------- | ------------------------------------------ |
| Remove duplicate **rows**                      | `df = df.drop_duplicates()`                |
| Remove duplicate rows based on specific column | `df = df.drop_duplicates(subset=['name'])` |
| Remove **column**                              | `df = df.drop(columns=['name'])`           |
| Remove multiple columns                        | `df = df.drop(columns=['name', 'age'])`    |
| Remove row by index                            | `df = df.drop(index=5)`                    |
| Remove multiple rows                           | `df = df.drop(index=[2, 5, 8])`            |

**Remember:**

* `drop_duplicates()` → duplicate **rows**
* `drop(columns=...)` → **columns**
* `drop(index=...)` → **rows**
