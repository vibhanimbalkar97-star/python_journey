Sure — these are important NumPy concepts. Let's keep them simple.

## 1. Broadcasting

**Broadcasting means NumPy automatically adjusts smaller arrays/values so that an operation can happen between arrays of different shapes.**

### Example

```python
import numpy as np

arr = np.array([10, 20, 30])

arr + 5
```

Output:

```text
[15 25 35]
```

You gave one value `5`, but NumPy effectively applies it to every element:

```text
10 + 5
20 + 5
30 + 5
```

### Another example

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b
```

```text
[11 22 33]
```

### 2D example

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

a + 10
```

Output:

```text
[[11 12 13]
 [14 15 16]]
```

**Interview definition:**

> Broadcasting allows NumPy to perform operations on arrays with different but compatible shapes without manually reshaping or repeating the data.

---

# 2. Shallow Copy

A **shallow copy** creates a new outer object, but nested objects can still be shared.

For NumPy, a useful concept is **view vs copy**.

### NumPy view

```python
a = np.array([10, 20, 30])

b = a.view()

b[0] = 100

print(a)
```

Output:

```text
[100  20  30]
```

Why?

Because `a` and `b` share the **same underlying data**.

```text
a ─────┐
       ↓
    [10,20,30]
       ↑
b ─────┘
```

Changing `b` also changes `a`.

### Real copy

```python
a = np.array([10, 20, 30])

b = a.copy()

b[0] = 100

print(a)
```

Output:

```text
[10 20 30]
```

Now they have separate data:

```text
a → [10,20,30]

b → [100,20,30]
```

### Easy difference

| Concept        | Meaning                       |
| -------------- | ----------------------------- |
| **View**       | Shares underlying data        |
| **Copy**       | Creates independent data      |
| `b = a`        | Same array/reference          |
| `b = a.view()` | New array object, shared data |
| `b = a.copy()` | Completely independent copy   |

### ⭐ Interview shortcut

Remember:

```python
b = a
```

➡️ Same object/reference.

```python
b = a.view()
```

➡️ Different array object, **same underlying data**.

```python
b = a.copy()
```

➡️ Different array object, **different data**.

And:

**Broadcasting = different shapes → NumPy automatically makes the operation possible (when shapes are compatible).**




Sure, in **very simple words**:

| Copy             | Meaning                                                | Change in copy affects original? |
| ---------------- | ------------------------------------------------------ | -------------------------------- |
| **Shallow copy** | Copies the outer object, but nested objects are shared | ✅ Yes, for shared nested data    |
| **Deep copy**    | Copies everything, including nested objects            | ❌ No                             |

### Example

```python
import copy

a = [[1, 2], [3, 4]]

shallow = copy.copy(a)
deep = copy.deepcopy(a)
```

If we do:

```python
shallow[0][0] = 100
```

Then:

```python
a
# [[100, 2], [3, 4]]
```

Because the nested list is shared.

But:

```python
deep[0][0] = 200
```

does **not** change `a`:

```python
a
# [[100, 2], [3, 4]]
```

### Easy memory trick

```text
Shallow → nested data shared
Deep    → completely independent
```

For **NumPy**, remember that `view()` is similar to sharing the underlying data, while `copy()` creates independent data.
