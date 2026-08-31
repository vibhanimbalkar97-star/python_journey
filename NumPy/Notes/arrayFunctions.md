Yes. **NumPy array generation functions** are functions used to create arrays quickly without manually writing every element.

### Important ones

| Function        | What it does                               | Example               |
| --------------- | ------------------------------------------ | --------------------- |
| `np.array()`    | Creates array from existing data           | `np.array([1,2,3])`   |
| `np.zeros()`    | Creates array filled with `0`              | `np.zeros(5)`         |
| `np.ones()`     | Creates array filled with `1`              | `np.ones(5)`          |
| `np.full()`     | Creates array filled with a specific value | `np.full(5, 7)`       |
| `np.arange()`   | Creates numbers with a step                | `np.arange(1,10,2)`   |
| `np.linspace()` | Creates evenly spaced numbers              | `np.linspace(0,10,5)` |
| `np.eye()`      | Creates identity matrix                    | `np.eye(3)`           |
| `np.empty()`    | Creates an uninitialized array             | `np.empty(5)`         |

### Most important for interviews ⭐

Focus first on:

```python
np.array()
np.zeros()
np.ones()
np.arange()
np.linspace()
```

Examples:

```python
np.zeros(3)
# [0. 0. 0.]
```

```python
np.ones(3)
# [1. 1. 1.]
```

```python
np.arange(1, 6)
# [1 2 3 4 5]
```

```python
np.linspace(0, 10, 5)
# [ 0.   2.5  5.   7.5 10. ]
```

**Easy difference:**

`arange()` → you specify the **step**

```python
np.arange(0, 10, 2)
```

`linspace()` → you specify the **number of values**

```python
np.linspace(0, 10, 5)
```

This `arange()` vs `linspace()` difference is worth remembering for interviews.
