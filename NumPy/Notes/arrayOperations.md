Here are the **important NumPy matrix operations** you should know for interviews:

| Operation                   | NumPy                      | Short meaning                      |
| --------------------------- | -------------------------- | ---------------------------------- |
| Create matrix               | `np.array([[1,2],[3,4]])`  | Create 2D matrix                   |
| Addition                    | `A + B`                    | Add corresponding elements         |
| Subtraction                 | `A - B`                    | Subtract corresponding elements    |
| Element-wise multiplication | `A * B`                    | Multiply corresponding elements    |
| Element-wise division       | `A / B`                    | Divide corresponding elements      |
| Matrix multiplication ⭐     | `A @ B`                    | Mathematical matrix multiplication |
| Matrix multiplication       | `np.matmul(A, B)`          | Same purpose as `@`                |
| Transpose                   | `A.T`                      | Rows ↔ columns                     |
| Determinant                 | `np.linalg.det(A)`         | Calculate determinant              |
| Inverse                     | `np.linalg.inv(A)`         | Find inverse matrix                |
| Rank                        | `np.linalg.matrix_rank(A)` | Find matrix rank                   |
| Trace                       | `np.trace(A)`              | Sum of diagonal elements           |
| Diagonal                    | `np.diag(A)`               | Get diagonal elements              |
| Sum                         | `A.sum()`                  | Sum all elements                   |
| Row-wise sum                | `A.sum(axis=1)`            | Sum each row                       |
| Column-wise sum             | `A.sum(axis=0)`            | Sum each column                    |
| Maximum                     | `A.max()`                  | Largest element                    |
| Minimum                     | `A.min()`                  | Smallest element                   |
| Mean                        | `A.mean()`                 | Average                            |
| Reshape                     | `A.reshape()`              | Change matrix dimensions           |
| Flatten                     | `A.flatten()`              | Convert to 1D                      |
| Horizontal stack            | `np.hstack((A,B))`         | Join columns                       |
| Vertical stack              | `np.vstack((A,B))`         | Join rows                          |
| Identity matrix             | `np.eye(3)`                | Create identity matrix             |
| Zeros matrix                | `np.zeros((2,3))`          | Matrix filled with 0               |
| Ones matrix                 | `np.ones((2,3))`           | Matrix filled with 1               |

### ⭐ Most important for interviews

Focus especially on these:

```python
A + B          # Addition
A - B          # Subtraction
A * B          # Element-wise multiplication
A @ B          # Matrix multiplication
A.T            # Transpose
np.linalg.det(A)  # Determinant
np.linalg.inv(A)  # Inverse
np.trace(A)       # Trace
A.sum(axis=0)     # Column-wise
A.sum(axis=1)     # Row-wise
```

### Most important difference

```python
A * B
```

➡️ **Element-by-element multiplication**

```python
A @ B
```

➡️ **Actual matrix multiplication**

This `*` vs `@` difference is one of the most important NumPy matrix concepts to remember.




Sure. Here are the **important NumPy vector operations** in the same format.

Assume:

```python
import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
```

| Operation                   | NumPy                     | Short meaning                   |
| --------------------------- | ------------------------- | ------------------------------- |
| Create vector               | `np.array([1,2,3])`       | Create 1D vector                |
| Addition                    | `v1 + v2`                 | Add corresponding elements      |
| Subtraction                 | `v1 - v2`                 | Subtract corresponding elements |
| Element-wise multiplication | `v1 * v2`                 | Multiply corresponding elements |
| Element-wise division       | `v1 / v2`                 | Divide corresponding elements   |
| Scalar multiplication       | `v1 * 5`                  | Multiply every element by 5     |
| Dot product ⭐               | `np.dot(v1, v2)`          | Sum of element-wise products    |
| Dot product                 | `v1 @ v2`                 | Dot product for 1D vectors      |
| Magnitude / norm ⭐          | `np.linalg.norm(v1)`      | Length of vector                |
| Sum                         | `v1.sum()`                | Sum all elements                |
| Mean                        | `v1.mean()`               | Average                         |
| Maximum                     | `v1.max()`                | Largest value                   |
| Minimum                     | `v1.min()`                | Smallest value                  |
| Absolute                    | `np.abs(v1)`              | Absolute values                 |
| Sort                        | `np.sort(v1)`             | Sort vector                     |
| Maximum index               | `np.argmax(v1)`           | Index of largest value          |
| Minimum index               | `np.argmin(v1)`           | Index of smallest value         |
| Unique                      | `np.unique(v1)`           | Remove duplicate values         |
| Reshape                     | `v1.reshape()`            | Change vector shape             |
| Normalize                   | `v1 / np.linalg.norm(v1)` | Convert to unit vector          |

### ⭐ Most important for interviews

Focus on:

```python
v1 + v2                  # Addition
v1 - v2                  # Subtraction
v1 * v2                  # Element-wise multiplication
np.dot(v1, v2)           # Dot product
v1 @ v2                  # Dot product
np.linalg.norm(v1)       # Magnitude
v1.sum()                 # Sum
v1.mean()                # Average
np.argmax(v1)            # Index of maximum
np.argmin(v1)            # Index of minimum
```

### Important: `*` vs `@`

For vectors:

```python
v1 * v2
```

➡️ Element-wise multiplication:

```text
[1,2,3] * [4,5,6]
= [4,10,18]
```

Whereas:

```python
v1 @ v2
```

➡️ Dot product:

```text
1×4 + 2×5 + 3×6
= 32
```

**Interview shortcut:** For NumPy, remember **vector = usually 1D array**, and know **element-wise operations, dot product, norm, indexing/slicing, and aggregation functions**.
