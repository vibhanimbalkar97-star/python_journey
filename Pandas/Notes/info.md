## Why do we need Jupyter Notebooks?

A notebook lets you write code in **small cells** and execute them one at a time. This makes it ideal for exploring data, testing ideas, and documenting your work.

For example, in a normal Python file (`main.py`):

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr)

arr = arr * 2

print(arr)
```

Every time you click **Run**, the **entire file** executes from top to bottom.

---

In a notebook (`.ipynb`), you can split the code into cells.

**Cell 1**

```python
import numpy as np

arr = np.array([10, 20, 30])
arr
```

Output:

```
array([10, 20, 30])
```

---

**Cell 2**

```python
arr * 2
```

Output:

```
array([20, 40, 60])
```

---

**Cell 3**

```python
arr.mean()
```

Output:

```
20.0
```

You can run only Cell 3 without rerunning the earlier cells (as long as `arr` already exists in memory).

---

# Why is this useful?

### 1. Experimenting

Suppose you're learning NumPy.

In a `.py` file:

```python
arr = np.array([10, 20, 30])

print(arr.shape)
print(arr.dtype)
print(arr.ndim)
print(arr.size)
```

If you want to test something new, you edit the file and run everything again.

In a notebook, you can create a new cell:

```python
arr.reshape(3, 1)
```

Run just that cell, see the result instantly, then try another idea in the next cell.

---

### 2. Data Analysis

Imagine you have a CSV with 1 million rows.

You load it once:

```python
import pandas as pd

df = pd.read_csv("employees.csv")
```

Now you can inspect it interactively:

```python
df.head()
```

```python
df.describe()
```

```python
df["Salary"].mean()
```

Without reloading the file each time.

---

### 3. Visualizations

Notebooks display charts directly below the code.

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 20, 15])
plt.show()
```

The graph appears immediately under that cell, making analysis much easier.

---

### 4. Notes + Code Together

You can mix explanations and code.

For example:

```
# NumPy Arrays

A NumPy array stores elements of the same type efficiently.

Example:
```

```python
arr = np.array([1, 2, 3])
```

This is useful for creating tutorials, reports, or sharing your analysis.

---

# Where are notebooks used in real companies?

They're widely used in:

* Data Analysis
* Data Science
* Machine Learning
* Artificial Intelligence
* Deep Learning
* Research and experimentation
* Business Intelligence

A data scientist might use a notebook to:

* Load data
* Clean it
* Analyze it
* Build a machine learning model
* Visualize results
* Document findings

All in one place.

---

# When should you use `.py` vs `.ipynb`?

| Use `.py`                  | Use `.ipynb`                    |
| -------------------------- | ------------------------------- |
| Build applications         | Learn NumPy                     |
| Build APIs (e.g., FastAPI) | Learn Pandas                    |
| Automation scripts         | Explore datasets                |
| Backend development        | Machine Learning experiments    |
| Production code            | Data analysis and visualization |

## For your learning path

Since you've already learned Python and you're planning to move on to **NumPy → Pandas → AI/ML**, here's a good workflow:

* **Learn and experiment** in a notebook (`.ipynb`) because it's interactive and lets you see results immediately.
* Once you understand a topic, **rewrite the examples in a `.py` file**. This reinforces your understanding and prepares you for writing production-quality code.

This approach combines the convenience of notebooks with the coding style you'll use in real software projects.
==================================================

What exactly is NumPy?

NumPy = Numerical Python

It is a Python library mainly used for:

Arrays
Mathematical calculations
Numerical operations
Matrix operations
Data manipulation

Example:

import numpy as np


arr = np.array([10, 20, 30, 40])


print(arr * 2)

Output:

[20 40 60 80]
What is Pandas?

Pandas is also a Python library, mainly used for data analysis and data manipulation.

For example:

import pandas as pd


data = {
    "name": ["Amit", "Ram", "John"],
    "age": [25, 30, 28]
}


df = pd.DataFrame(data)


print(df)

It gives you a table-like structure:

   name  age
0  Amit   25
1  Ram    30
2  John   28
So remember this
Python
  │
  ├── NumPy       → numerical calculations / arrays
  │
  ├── Pandas      → data analysis / tables
  │
  ├── Matplotlib  → graphs / visualization
  │
  └── Scikit-learn → Machine Learning

And on GitHub, numpy/ and pandas/ are simply folders you create to organize your practice. They are not the libraries themselves.
==================================================

