# 10. Boosting

Now the concept changes.

### Bagging:

Models work **independently**.

### Boosting:

Models work **sequentially**.

The basic idea:

> **Each new model tries to improve the mistakes made by previous models.**

Think:

```text
Dataset
   ↓
Model 1
   ↓
Find mistakes
   ↓
Model 2 focuses on mistakes
   ↓
Find remaining mistakes
   ↓
Model 3 focuses on them
   ↓
...
   ↓
Final prediction
```

This is the key difference.

---

# 11. Boosting simple example

Suppose we have 5 students and we're predicting whether they will pass.

First model:

```text
Student 1 → Correct
Student 2 → Correct
Student 3 → Wrong ❌
Student 4 → Correct
Student 5 → Wrong ❌
```

Boosting says:

> Pay more attention to Student 3 and Student 5.

Second model:

```text
Student 3 → Correct
Student 5 → Correct
```

Then another model tries to fix whatever errors remain.

So models are built **one after another**.

---

# 12. AdaBoost — behind the scenes

AdaBoost is one of the easiest boosting algorithms to understand conceptually.

Initially, every training observation gets equal weight.

Suppose:

```text
5 observations

Weight:
A = 0.2
B = 0.2
C = 0.2
D = 0.2
E = 0.2
```

First weak learner predicts:

```text
A → correct
B → correct
C → wrong ❌
D → correct
E → wrong ❌
```

The incorrect observations get **higher importance**.

Conceptually:

```text
Correct:
0.2 → lower weight

Wrong:
0.2 → higher weight
```

Next model pays more attention to C and E.

This continues.

Finally, models are combined using their model weights.

---

# 13. AdaBoost final calculation

Suppose 3 weak models have weights:

```text
Model 1 → 0.5
Model 2 → 0.3
Model 3 → 0.2
```

For a new observation:

```text
Model 1 → Yes
Model 2 → No
Model 3 → Yes
```

Weighted voting:

```text
Yes = 0.5 + 0.2
    = 0.7

No  = 0.3
```

Therefore:

```text
Final = Yes
```

That's the basic idea of AdaBoost's weighted voting.

---

# 14. Gradient Boosting

Gradient Boosting works differently from AdaBoost.

Instead of simply increasing weights on incorrectly classified rows, it builds models to reduce the **loss/error** left by previous models.

Simple regression example:

Actual:

```text
100
```

First model:

```text
Prediction = 70
```

Residual/error:

```text
100 - 70 = 30
```

Second model tries to predict this residual:

```text
30
```

Suppose second model predicts:

```text
25
```

New prediction:

```text
70 + 25 = 95
```

Remaining error:

```text
100 - 95 = 5
```

Third model tries to fix the remaining error:

```text
5
```

Suppose it predicts 4:

```text
95 + 4 = 99
```

So prediction gradually improves:

```text
Model 1 → 70
Model 2 → +25 → 95
Model 3 → +4  → 99
```

This is the intuition behind Gradient Boosting.

---

# 15. Gradient Boosting formula

Conceptually:

```text
Final Model
=
Model 1
+
Learning Rate × Model 2
+
Learning Rate × Model 3
+
...
```

For example:

```text
Prediction 1 = 70

Learning rate = 0.1

Model 2 predicts residual = 30

Contribution = 0.1 × 30
             = 3

New prediction = 70 + 3
               = 73
```

Then another tree improves it further.

So the **learning rate controls how much each new model contributes**.

---

# 16. Gradient Boosting code

```python
from sklearn.ensemble import GradientBoostingClassifier

gb_model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

gb_model.fit(X_train, y_train)

y_pred = gb_model.predict(X_test)
```

For regression:

```python
from sklearn.ensemble import GradientBoostingRegressor

gb_model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

gb_model.fit(X_train, y_train)

y_pred = gb_model.predict(X_test)
```

---

# 17. XGBoost / LightGBM / CatBoost

These are advanced boosting algorithms.

Very common in real-world tabular ML.

```text
Boosting
│
├── AdaBoost
│
├── Gradient Boosting
│
├── XGBoost
│
├── LightGBM
│
└── CatBoost
```

They are particularly popular for:

* Structured/tabular data
* Classification
* Regression
* Ranking
* Kaggle competitions
* Business prediction problems

Example:

```python
from xgboost import XGBClassifier

xgb_model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

xgb_model.fit(X_train, y_train)

y_pred = xgb_model.predict(X_test)
```

---

