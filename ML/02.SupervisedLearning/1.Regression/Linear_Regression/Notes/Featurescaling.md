**No, StandardScaler is not mandatory for Linear Regression.** But it can be important in some situations.

### Simple rule to remember

| Situation                                          | Standard Scaling? |
| -------------------------------------------------- | ----------------- |
| Linear Regression using OLS (`LinearRegression()`) | ❌ Not required    |
| Linear Regression using Gradient Descent           | ✅ Recommended     |
| Features have very different scales                | ✅ Helpful         |
| Ridge Regression                                   | ✅ Recommended     |
| Lasso Regression                                   | ✅ Recommended     |
| Polynomial Regression                              | ✅ Often helpful   |

### Why?

Suppose your features are:

```text
age          → 20–70
salary       → 20,000–2,00,000
experience   → 1–20
```

Their scales are very different.

With **Gradient Descent**, scaling helps the algorithm move toward the minimum more efficiently.

After StandardScaler:

```text
age          → around -2 to +2
salary       → around -2 to +2
experience   → around -2 to +2
```

### Interview-ready answer 🎯

> **"Standard scaling is not mandatory for ordinary Linear Regression because the OLS solution does not depend on feature scale. However, scaling is recommended when using optimization methods like Gradient Descent or regularized models such as Ridge and Lasso."**

### One important clarification

Don't say:

> ❌ "Linear Regression always needs StandardScaler."

Say:

> ✅ **"Linear Regression itself doesn't require scaling, but scaling can be useful depending on the optimization method and model."**

For your ML workflow, if you're using:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
```

you **can train without StandardScaler**.

If you're using:

```python
from sklearn.linear_model import Ridge, Lasso
```

then **scaling becomes much more important** because regularization depends on the magnitude of the coefficients.
