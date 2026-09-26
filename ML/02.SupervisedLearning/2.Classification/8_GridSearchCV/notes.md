Yes. Since you have understood **Cross-Validation**, `GridSearchCV` is the next important concept.

## 1. What is GridSearchCV?

**GridSearchCV = Hyperparameter tuning + Cross-Validation**

Simple meaning:

> We give multiple possible hyperparameter values to the model, and GridSearchCV tries all combinations using cross-validation and tells us which combination gives the best CV score.

---

# 2. First understand: What is a hyperparameter?

A **hyperparameter** is a setting that we choose **before training** the model.

For SVM:

```python
SVC(
    kernel='rbf',
    C=1,
    gamma='scale'
)
```

Here:

```text
C       → hyperparameter
kernel  → hyperparameter
gamma   → hyperparameter
```

The model doesn't automatically learn these values from the training data in the same way it learns model parameters.

We choose/tune them.

---

# 3. Why do we need GridSearchCV?

Suppose you create SVM:

```python
SVC(kernel='rbf')
```

But you don't know what value of `C` is best.

You could try:

```text
C = 0.1
C = 1
C = 10
C = 100
```

Instead of manually doing:

```python
model = SVC(C=0.1)
model.fit(...)

model = SVC(C=1)
model.fit(...)

model = SVC(C=10)
model.fit(...)
```

GridSearchCV does this automatically.

---

# 4. Simple example

Suppose we give:

```python
param_grid = {
    'C': [0.1, 1, 10],
    'gamma': [0.01, 0.1]
}
```

We have:

```text
C values     → 0.1, 1, 10       = 3
gamma values → 0.01, 0.1        = 2
```

Total combinations:

$$
3 \times 2 = 6
$$

So GridSearchCV will test:

```text
Combination 1 → C=0.1, gamma=0.01
Combination 2 → C=0.1, gamma=0.1

Combination 3 → C=1,   gamma=0.01
Combination 4 → C=1,   gamma=0.1

Combination 5 → C=10,  gamma=0.01
Combination 6 → C=10,  gamma=0.1
```

---

# 5. Where does Cross-Validation come in?

Suppose:

```python
cv=5
```

That means **5-fold cross-validation for every combination**.

For:

```text
C=0.1, gamma=0.01
```

GridSearchCV does:

```text
Fold 1 → 82%
Fold 2 → 85%
Fold 3 → 80%
Fold 4 → 87%
Fold 5 → 84%
```

Average:

$$
(82+85+80+87+84)/5
$$

$$
=83.6\%
$$

So:

```text
C=0.1, gamma=0.01
CV score = 83.6%
```

Then it moves to the next combination.

---

# 6. Behind-the-scenes complete example

Suppose the results are:

|   C | Gamma | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 |      Mean |
| --: | ----: | -----: | -----: | -----: | -----: | -----: | --------: |
| 0.1 |  0.01 |     82 |     85 |     80 |     87 |     84 | **83.6%** |
| 0.1 |   0.1 |     84 |     86 |     83 |     88 |     85 | **85.2%** |
|   1 |  0.01 |     87 |     89 |     88 |     90 |     86 | **88.0%** |
|   1 |   0.1 |     90 |     91 |     89 |     92 |     90 | **90.4%** |
|  10 |  0.01 |     88 |     87 |     89 |     90 |     88 | **88.4%** |
|  10 |   0.1 |     89 |     90 |     91 |     90 |     89 | **89.8%** |

GridSearchCV compares the **mean CV score**.

It identifies:

```text
C = 1
gamma = 0.1

Mean CV Accuracy = 90.4%
```

So it selects that combination as the best based on the specified scoring metric.

---

# 7. Code implementation

For your SVM:

```python
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
```

Create model:

```python
model_svc = SVC(kernel='rbf')
```

Create parameter grid:

```python
param_grid = {
    'C': [0.1, 1, 10],
    'gamma': [0.01, 0.1]
}
```

Create GridSearchCV:

```python
grid = GridSearchCV(
    model_svc,
    param_grid,
    cv=5,
    scoring='accuracy'
)
```

Fit:

```python
grid.fit(X_train, y_train)
```

Now check best parameters:

```python
print(grid.best_params_)
```

Example:

```text
{'C': 1, 'gamma': 0.1}
```

Best CV score:

```python
print(grid.best_score_)
```

Example:

```text
0.904
```

Meaning:

```text
Best CV Accuracy = 90.4%
```

---

# 8. What is `best_estimator_`?

Very useful:

```python
print(grid.best_estimator_)
```

You might get:

```text
SVC(C=1, gamma=0.1)
```

This is the **model configured with the best hyperparameters found by GridSearchCV**.

You can use it directly:

```python
best_model = grid.best_estimator_

y_pred = best_model.predict(X_test)
```

Then evaluate on your untouched test set:

```python
from sklearn.metrics import accuracy_score

test_accuracy = accuracy_score(y_test, y_pred)

print(test_accuracy)
```

---

# 9. Important: GridSearchCV + Pipeline

Since you just learned Pipeline, this is where they come together.

For SVM, scaling is usually important.

So instead of:

```python
GridSearchCV(SVC(), ...)
```

you can do:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', SVC(kernel='rbf'))
])
```

Now parameter names need the **Pipeline step name**:

```python
param_grid = {
    'model__C': [0.1, 1, 10],
    'model__gamma': [0.01, 0.1]
}
```

Notice:

```text
model__C
      ↑
  double underscore
```

Because `C` belongs to the `model` step.

Then:

```python
grid = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring='accuracy'
)

grid.fit(X_train, y_train)
```

Then:

```python
print(grid.best_params_)
print(grid.best_score_)
```

---

# 10. Why `model__C` instead of just `C`?

Your Pipeline is:

```text
Pipeline
   |
   ├── scaler
   |
   └── model
         |
         ├── C
         ├── gamma
         └── kernel
```

So we tell GridSearchCV:

```python
'model__C'
```

Meaning:

> Go to the Pipeline step called `model` and tune its `C` parameter.

Similarly:

```python
'model__gamma'
```

means:

> Go to the `model` step and tune `gamma`.

---

# 11. How many times does the model actually train?

This is a very good interview question.

Suppose:

```text
C values = 3
gamma values = 2
cv = 5
```

Combinations:

$$
3 \times 2 = 6
$$

Each combination uses 5 folds:

$$
6 \times 5 = 30
$$

So the model is trained **30 times during CV**.

Then GridSearchCV generally **refits the best configuration on the full training dataset** when `refit=True` (the default).

So you can think:

```text
6 parameter combinations
        ↓
5-fold CV each
        ↓
6 × 5 = 30 fits
        ↓
Compare mean CV scores
        ↓
Best parameters
        ↓
Refit best model on complete X_train
```

---

# 12. GridSearchCV vs Cross-Validation

This distinction is important:

### `cross_val_score`

Answers:

> **"How well does this particular model/configuration perform?"**

```python
cross_val_score(model, X_train, y_train, cv=5)
```

### `GridSearchCV`

Answers:

> **"Among these hyperparameter combinations, which configuration performs best according to CV?"**

```python
GridSearchCV(
    model,
    param_grid,
    cv=5
)
```

So:

```text
Cross Validation
       ↓
Evaluate a configuration

GridSearchCV
       ↓
Try many configurations
       ↓
Cross-validation for each
       ↓
Choose best configuration
```

---

# 🎯 Interview-ready answer

If interviewer asks **"What is GridSearchCV?"**, say:

> **GridSearchCV is a hyperparameter tuning technique provided by Scikit-learn. We provide a grid of possible hyperparameter values, and GridSearchCV tries every possible combination. For each combination, it performs cross-validation, calculates the mean validation score, and selects the combination with the best score according to the selected scoring metric.**

If they ask **"How does it work behind the scenes?"**:

> **For example, if I have 3 values of C, 2 values of gamma, and 5-fold cross-validation, GridSearchCV tests 3 × 2 = 6 parameter combinations. Each combination is evaluated across 5 folds, resulting in 30 model fits. It calculates the mean score for each combination, selects the best parameters, and by default refits the best model on the complete training data.**

### Remember this formula:

```text
Number of combinations
= number of values of parameter 1
× number of values of parameter 2
× ...

Total CV fits
= combinations × number of folds
```

That's the core of **GridSearchCV**.
