## Chi-Square Test — Simple Explanation

**Chi-square test** is mainly used when your data is **categorical** (categories, not continuous numbers).

### Why use it?

To check whether there is a **relationship/association between categorical variables**.

For example:

> Is **gender** related to **product preference**?

|        | Product A | Product B |
| ------ | --------: | --------: |
| Male   |        40 |        20 |
| Female |        25 |        35 |

Chi-square can tell us whether the difference is likely **real** or could have happened by chance.

---

### How to identify when to use Chi-square? ⭐

Ask yourself:

> **"Are my variables categorical?"**

If yes → Chi-square may be appropriate.

Examples:

| Variable 1           | Variable 2     | Chi-square? |
| -------------------- | -------------- | ----------- |
| Gender               | Product choice | ✅           |
| Education            | Job type       | ✅           |
| Device type          | Purchased?     | ✅           |
| Age                  | Salary         | ❌           |
| Height               | Weight         | ❌           |
| Average score A vs B | ❌ → t-test     |             |

---

### Main Chi-square tests

There are two important ones:

**1. Chi-square Test of Independence**

> Are **two categorical variables related?**

Example:

```text
Gender ↔ Product choice
```

**2. Chi-square Goodness of Fit**

> Does the observed distribution match an **expected distribution**?

Example:

> A dice should give each number equally often. Does our observed data match that expectation?

---

### Hypothesis

For **independence test**:

```text
H₀: Variables are independent (no relationship)
H₁: Variables are related
```

Then use the p-value:

```text
p-value < 0.05 → Reject H₀
p-value > 0.05 → Fail to reject H₀
```

genui{"learning_viz":{"type_id":"CHI_SQUARE_GOODNESS_OF_FIT"}}

### 🧠 Easy identification

```text
Categorical + Categorical
        ↓
   Chi-square
```

```text
Numerical mean + Numerical mean
        ↓
      t-test
```

```text
Numerical mean + known population mean
        ↓
      Z-test / t-test
```
===================================================================================================

Yes. This line:

```python
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
```

returns **4 important values**.

| Variable   | Simple meaning                                                                                 |
| ---------- | ---------------------------------------------------------------------------------------------- |
| `chi2`     | **Chi-square statistic** — measures how different the observed counts are from expected counts |
| `p_value`  | Tells whether the difference/relationship is **statistically significant**                     |
| `dof`      | **Degrees of freedom** — determines how much independent information is available              |
| `expected` | The counts we would **expect if H₀ were true**                                                 |

### Example

Suppose:

```python
contingency_table = [
    [94, 122],
    [76, 108],
    [144, 347]
]

chi2, p_value, dof, expected = chi2_contingency(contingency_table)
```

You might get something like:

```text
chi2     →  ...
p_value  →  ...
dof      →  2
expected →  [[..., ...],
             [..., ...],
             [..., ...]]
```

### Most important: `chi2` vs `p_value`

Think of it like this:

```text
Observed counts
      ↓
Compare with expected counts
      ↓
   chi2 statistic
      ↓
   p-value
      ↓
Compare p-value with 0.05
```

If:

```text
p_value < 0.05
```

➡️ **Reject H₀** → there is evidence of a relationship between the categorical variables.

If:

```text
p_value > 0.05
```

➡️ **Fail to reject H₀** → not enough evidence of a relationship.

### What is `expected`?

This is especially important for Chi-square.

**Observed:** what you actually have.

**Expected:** what you would expect **if the two variables were independent**.

So Chi-square basically asks:

> **"Are my observed counts sufficiently different from what I would expect if there were no relationship?"**

=================================================================================================================


