Yes. This is an important NumPy distinction for interviews.

## 1. Array Attributes

**Attributes = information/properties about the array.**

You don't use `()` with attributes.

```python
import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])
```

| Attribute  | Meaning                    | Example        | Result   |
| ---------- | -------------------------- | -------------- | -------- |
| `ndim`     | Number of dimensions       | `arr.ndim`     | `2`      |
| `shape`    | Rows and columns           | `arr.shape`    | `(2, 3)` |
| `size`     | Total elements             | `arr.size`     | `6`      |
| `dtype`    | Data type                  | `arr.dtype`    | `int64`  |
| `itemsize` | Bytes used by each element | `arr.itemsize` | `8`*     |
| `nbytes`   | Total bytes used           | `arr.nbytes`   | `48`*    |

*Depends on the dtype/platform.

### Easy way to remember:

```text
arr.ndim   → How many dimensions?
arr.shape  → What is the structure?
arr.size   → How many elements?
arr.dtype  → What type?
```

---

# 2. Array Methods

**Methods = actions/operations you perform on the array.**

Methods use `()`.

Examples:

```python
arr.reshape()
arr.flatten()
arr.ravel()
arr.sum()
arr.mean()
arr.max()
arr.min()
arr.astype()
```

For example:

```python
arr.sum()
```

returns the sum.

```python
arr.mean()
```

returns the average.

```python
arr.reshape(3, 2)
```

changes the shape.

---

## Attribute vs Method

This is the easiest way to understand:

### Attribute

```python
arr.shape
```

You're **asking for information**.

> "What is the shape of this array?"

### Method

```python
arr.reshape(3, 2)
```

You're **asking NumPy to perform an operation**.

> "Change this array's shape."

---

## Important interview examples

```python
arr.ndim        # attribute
arr.shape       # attribute
arr.size        # attribute
arr.dtype       # attribute

arr.sum()       # method
arr.mean()      # method
arr.max()       # method
arr.min()       # method
arr.reshape()   # method
arr.flatten()   # method
```

### ⭐ Interview question

**How do you differentiate an attribute from a method in NumPy?**

Answer:

> An attribute provides information about the array and is accessed without parentheses, such as `shape`, `size`, `ndim`, and `dtype`. A method performs an operation on the array and is called with parentheses, such as `sum()`, `mean()`, and `reshape()`.
