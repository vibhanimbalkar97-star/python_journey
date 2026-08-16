Yes. If you're learning **NumPy for interviews**, you don't need every NumPy feature. Focus on the basics that are commonly asked and useful for data/AI work.

## NumPy — Interview Basics

### 1. What is NumPy?

**NumPy (Numerical Python)** is a Python library used for **numerical and scientific computing**.

Mainly used for:

* Arrays
* Mathematical operations
* Matrix operations
* Numerical calculations
* Data manipulation

```python
import numpy as np
```

---

### 2. Why use NumPy instead of Python lists?

This is a very common interview question.

**Python list:**

```python
a = [1, 2, 3, 4]
```

**NumPy array:**

```python
a = np.array([1, 2, 3, 4])
```

NumPy arrays are generally better for numerical computation because they support **vectorized operations** and are more memory-efficient for homogeneous numerical data.

Example:

```python
arr = np.array([1, 2, 3])

arr * 2
```

Output:

```text
[2 4 6]
```

With a Python list, `list * 2` repeats the list instead of multiplying each element.

---

### 3. What is an ndarray?

The main data structure of NumPy is called **`ndarray`** — N-dimensional array.

```python
arr = np.array([1, 2, 3])
```

This is a 1-dimensional NumPy array.

2D:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

3D and higher dimensions are also possible.

---

### 4. Important array properties

Know these:

```python
arr.ndim
arr.shape
arr.size
arr.dtype
```

Example:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

```python
arr.ndim
```

```text
2
```

```python
arr.shape
```

```text
(2, 3)
```

```python
arr.size
```

```text
6
```

```python
arr.dtype
```

Something like:

```text
int64
```

depending on your environment.

**Interview shortcut:**

* `ndim` → number of dimensions
* `shape` → dimensions/size of each axis
* `size` → total number of elements
* `dtype` → data type

---

### 5. Creating arrays

Know these methods:

```python
np.array()
np.zeros()
np.ones()
np.arange()
np.linspace()
```

Examples:

```python
np.zeros(5)
```

```text
[0. 0. 0. 0. 0.]
```

```python
np.ones(5)
```

```text
[1. 1. 1. 1. 1.]
```

```python
np.arange(1, 10, 2)
```

```text
[1 3 5 7 9]
```

---

### 6. Indexing and slicing

Very important.

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]
```

```text
10
```

```python
arr[1:4]
```

```text
[20 30 40]
```

For 2D arrays:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr[0, 1]
```

Output:

```text
2
```

---

### 7. Vectorization

Another important interview concept.

Instead of:

```python
result = []

for x in arr:
    result.append(x * 2)
```

NumPy allows:

```python
result = arr * 2
```

This is called **vectorized operation**.

---

### 8. Broadcasting ⭐

Very commonly discussed.

```python
arr = np.array([1, 2, 3])

arr + 10
```

Output:

```text
[11 12 13]
```

NumPy automatically applies `10` to every element.

This behavior is called **broadcasting**.

---

### 9. Reshaping

```python
arr = np.array([1, 2, 3, 4, 5, 6])

arr.reshape(2, 3)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

Important:

```python
arr.reshape(2, 3)
```

means:

**2 rows × 3 columns**

The total number of elements must remain the same.

---

### 10. `reshape()` vs `resize()`

Interviewers can ask this.

`reshape()` changes the shape and normally returns a reshaped array without changing the original array.

```python
new_arr = arr.reshape(2, 3)
```

`resize()` changes the array itself and can change its total size.

For beginner interviews, remember:

> `reshape()` → change shape
> `resize()` → modify/resize the array

---

### 11. `flatten()` vs `ravel()`

Both convert multidimensional arrays into 1D.

```python
arr.flatten()
```

and

```python
arr.ravel()
```

Basic difference:

* `flatten()` generally returns a **copy**
* `ravel()` generally returns a **view when possible**

This is a slightly more advanced interview question.

---

### 12. Aggregation functions

Very useful:

```python
arr.sum()
arr.mean()
arr.min()
arr.max()
arr.std()
```

Example:

```python
arr = np.array([10, 20, 30, 40])

arr.mean()
```

```text
25.0
```

---

### 13. Axis ⭐

This is one topic you should definitely understand.

For:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

```python
arr.sum(axis=0)
```

Output:

```text
[5 7 9]
```

It calculates down the **rows**, giving column-wise results.

```python
arr.sum(axis=1)
```

Output:

```text
[6 15]
```

It calculates across the **columns**, giving row-wise results.

A simple way to remember:

```text
axis=0 → work down rows → column result

axis=1 → work across columns → row result
```

---

### 14. Boolean filtering

Very useful for data analysis.

```python
arr = np.array([10, 25, 30, 15, 40])

arr[arr > 20]
```

Output:

```text
[25 30 40]
```

This is called **boolean indexing/masking**.

---

### 15. `where()`

```python
arr = np.array([10, 20, 30, 40])

np.where(arr > 20)
```

It gives the indices where the condition is true.

You can also use it for conditional values:

```python
np.where(arr > 20, "High", "Low")
```

---

## Most important interview questions to practice

I'd prioritize these:

1. What is NumPy?
2. Why use NumPy instead of Python lists?
3. What is an `ndarray`?
4. Difference between list and NumPy array?
5. What are `ndim`, `shape`, `size`, and `dtype`?
6. How do you create a NumPy array?
7. What is vectorization?
8. What is broadcasting?
9. What is indexing and slicing?
10. How do you reshape an array?
11. Difference between `reshape()` and `resize()`?
12. What is `axis`?
13. Difference between `axis=0` and `axis=1`?
14. What is boolean indexing?
15. Difference between `flatten()` and `ravel()`?
16. What are `zeros()`, `ones()`, `arange()`, and `linspace()`?
17. How do you find mean, max, min, and standard deviation?
18. How do you combine two NumPy arrays?
19. How do you find unique values?
20. How do you handle missing values (`NaN`)?

