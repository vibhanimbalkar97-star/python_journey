Yes. Let's see **Cross-Validation implementation from basic → practical ML project**.

Assume you already have:

```python
X_train, X_test, y_train, y_test
```

from `train_test_split()`.

---

## Step 1: Import

For basic K-Fold CV:

```python
from sklearn.model_selection import cross_val_score
```

---

## Step 2: Create your model

Example: Logistic Regression

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
```

---

## Step 3: Apply Cross-Validation

```python
scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)
```

Here:

| Parameter            | Meaning                          |
| -------------------- | -------------------------------- |
| `model`              | ML model                         |
| `X_train`            | Training features                |
| `y_train`            | Training target                  |
| `cv=5`               | 5 folds                          |
| `scoring="accuracy"` | Calculate accuracy for each fold |

---

## Step 4: See individual scores

```python
print(scores)
```

Example output:

```text
[0.82 0.85 0.80 0.87 0.84]
```

These are the 5 validation scores:

```text
Fold 1 → 82%
Fold 2 → 85%
Fold 3 → 80%
Fold 4 → 87%
Fold 5 → 84%
```

---

## Step 5: Calculate average CV score

```python
print(scores.mean())
```

Behind the scenes:

```text
(0.82 + 0.85 + 0.80 + 0.87 + 0.84) / 5
= 0.836
```

So:

```text
CV Score = 83.6%
```

You can also write:

```python
print("Mean CV Score:", scores.mean())
```

---

# Complete code

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)

print("Fold Scores:", scores)
print("Mean CV Score:", scores.mean())
```

---

# For Classification → Stratified K-Fold

Since you are learning classification, this is important.

Instead of manually creating `StratifiedKFold`, you can use:

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

model = LogisticRegression()

scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=cv,
    scoring="accuracy"
)

print("Fold Scores:", scores)
print("Mean CV Score:", scores.mean())
```

### Flow:

```text
X_train + y_train
       ↓
StratifiedKFold
       ↓
 ┌─────┼─────┬─────┬─────┐
 ↓     ↓     ↓     ↓     ↓
F1    F2    F3    F4    F5
 ↓     ↓     ↓     ↓     ↓
82%   85%   80%   87%   84%
       ↓
    Average
       ↓
    83.6%
```

---

# Step 6: After CV, train final model

This is another important point.

After you've evaluated/selected your model using CV, you can train the model on **all training data**:

```python
model.fit(X_train, y_train)
```

Then evaluate once on your untouched test data:

```python
y_pred = model.predict(X_test)
```

For classification:

```python
from sklearn.metrics import accuracy_score

test_accuracy = accuracy_score(y_test, y_pred)

print("Test Accuracy:", test_accuracy)
```

So the complete real-world flow is:

```text
                 Dataset
                    ↓
            train_test_split
             ↙            ↘
        X_train            X_test
           ↓                 ↓
   Cross Validation       KEEP ASIDE
           ↓
   Model / Hyperparameter
       Selection
           ↓
    model.fit(X_train)
           ↓
     X_test prediction
           ↓
     Final evaluation
```

### One thing to remember

**Cross-validation is normally performed on the training data, not on the final test data.**

The test set should remain untouched until the final evaluation.

---

## If your model requires scaling

For KNN, Logistic Regression, SVM, etc., don't scale the entire dataset before CV. Use a **Pipeline** so scaling is fitted separately inside each fold:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

scores = cross_val_score(
    pipeline,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)

print("Fold Scores:", scores)
print("Mean CV Score:", scores.mean())
```

This avoids **data leakage** during cross-validation.

**For your ML learning sequence, I'd learn next:** `Cross-Validation → GridSearchCV → RandomizedSearchCV → Pipeline → complete model tuning project`.
