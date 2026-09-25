## Cross-Validation — simple explanation

**Cross-validation** is a technique used to check whether our ML model performs consistently on different parts of the dataset.

Normally, we do:

```text
Train data → Model → Test data → Accuracy
```

But there is a problem: **what if our particular test data is easy or difficult?**

Cross-validation solves this by **splitting the training data into multiple parts and training/testing multiple times.**

The most common type is **K-Fold Cross-Validation**.

---

## 1. Example: K-Fold Cross-Validation

Suppose we have **10 records**:

```text
Data = [1,2,3,4,5,6,7,8,9,10]
```

We choose:

```python
K = 5
```

So data is divided into **5 folds**:

```text
Fold 1 → [1, 2]
Fold 2 → [3, 4]
Fold 3 → [5, 6]
Fold 4 → [7, 8]
Fold 5 → [9, 10]
```

Now model will be trained **5 times**.

### Round 1

```text
Training → Fold 2 + 3 + 4 + 5
Validation → Fold 1

Accuracy = 80%
```

### Round 2

```text
Training → Fold 1 + 3 + 4 + 5
Validation → Fold 2

Accuracy = 90%
```

### Round 3

```text
Training → Fold 1 + 2 + 4 + 5
Validation → Fold 3

Accuracy = 85%
```

### Round 4

```text
Training → Fold 1 + 2 + 3 + 5
Validation → Fold 4

Accuracy = 95%
```

### Round 5

```text
Training → Fold 1 + 2 + 3 + 4
Validation → Fold 5

Accuracy = 90%
```

---

# 2. Behind-the-scenes calculation

Now we have:

```text
Accuracy 1 = 80%
Accuracy 2 = 90%
Accuracy 3 = 85%
Accuracy 4 = 95%
Accuracy 5 = 90%
```

Cross-validation score is basically the **average**:

$$
CV\ Score =
\frac{80 + 90 + 85 + 95 + 90}{5}
$$

```text
= 440 / 5

= 88%
```

So we say:

> **5-Fold Cross-Validation Score = 88%**

This tells us the model's performance is around **88% on average across different validation sets**.

---

# 3. Why not just calculate accuracy once?

Suppose we only did:

```text
Train → 8 records
Test → 2 records

Accuracy = 100%
```

It looks excellent.

But maybe those 2 test records were very easy.

With cross-validation:

```text
Fold 1 → 80%
Fold 2 → 90%
Fold 3 → 85%
Fold 4 → 95%
Fold 5 → 90%

Average → 88%
```

Now we have a better idea of the model's **general performance**.

---

# 4. Important: Cross-validation doesn't mean final test set

This is very important for interviews.

Usually the process is:

```text
                 Dataset
                    |
             Train/Test Split
                    |
          ┌─────────┴─────────┐
          ↓                   ↓
      Training             Test
          |
    Cross Validation
          |
    ┌─────┼─────┐
    ↓     ↓     ↓
  Fold1  Fold2  Fold3 ... Fold5
    |
    ↓
Model selection / tuning
    |
    ↓
Final model
    |
    ↓
     Test data
    |
    ↓
Final evaluation
```

So **test data should generally be kept separate** and not repeatedly used during cross-validation.

---

# 5. Example with an actual ML model

Suppose you're building a **car price prediction** model.

You have:

```text
1000 rows
```

First:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
```

Now:

```text
800 rows → Training
200 rows → Test
```

We perform 5-fold CV on the **800 training rows**.

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()

scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="r2"
)

print(scores)
print(scores.mean())
```

For example:

```text
scores =
[0.81, 0.85, 0.83, 0.79, 0.84]
```

Average:

```text
(0.81 + 0.85 + 0.83 + 0.79 + 0.84) / 5

= 0.824
```

So:

```text
CV R² = 0.824
```

Then after choosing/tuning the model, we finally evaluate on the untouched test set.

---

# 6. What exactly happens inside each fold?

This is the key **behind-the-scenes interview answer**.

Suppose:

```text
K = 5
```

Then:

```text
Iteration 1:
80% → Train
20% → Validation

Iteration 2:
80% → Train
20% → Validation

Iteration 3:
80% → Train
20% → Validation

Iteration 4:
80% → Train
20% → Validation

Iteration 5:
80% → Train
20% → Validation
```

Every record gets a chance to become validation data.

```text
Record       Used for validation
1            Fold 1
2            Fold 1
3            Fold 2
4            Fold 2
5            Fold 3
...
```

The model is trained separately in each iteration.

Then:

```text
Score1
Score2
Score3
Score4
Score5
   ↓
Average
   ↓
CV Score
```

---

# 7. Why do we use cross-validation?

Main purposes:

### 1. Check model consistency

If:

```text
[88%, 87%, 89%, 90%, 88%]
```

Model is performing fairly consistently.

But:

```text
[98%, 60%, 91%, 55%, 95%]
```

Performance varies a lot.

That tells us something about the model/data may need investigation.

### 2. Model comparison

Suppose:

```text
Logistic Regression → CV = 84%
Random Forest       → CV = 89%
KNN                 → CV = 86%
```

CV gives us a more reliable basis for comparing their average validation performance than relying on one split.

### 3. Hyperparameter tuning

For example:

```text
Random Forest

n_estimators = 50   → CV = 86%
n_estimators = 100  → CV = 89%
n_estimators = 200  → CV = 90%
n_estimators = 300  → CV = 89%
```

We can use CV while selecting/tuning the hyperparameters.

---

# 8. One important interview point: K-Fold vs Stratified K-Fold

For **classification**, we often use **StratifiedKFold**.

Why?

Suppose:

```text
100 patients

90 → No Disease
10 → Disease
```

We want each fold to have approximately the same class distribution.

For example:

```text
Fold 1 → 18 No + 2 Disease
Fold 2 → 18 No + 2 Disease
Fold 3 → 18 No + 2 Disease
...
```

This prevents a fold from accidentally having very few or no positive examples.

Example:

```python
from sklearn.model_selection import StratifiedKFold

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
```

---

## Interview-ready answer 🎯

If interviewer asks:

**"What is cross-validation?"**

You can say:

> **Cross-validation is a model evaluation technique used to check how well a model generalizes to unseen data. In K-Fold Cross-Validation, we divide the training data into K folds. We train the model on K-1 folds and validate it on the remaining fold. We repeat this process K times, so every fold is used once for validation. Finally, we calculate the average of all validation scores as the cross-validation score. It helps us get a more reliable estimate of model performance and is commonly used for model comparison and hyperparameter tuning.**

### Behind-the-scenes one-liner:

> **For 5-fold CV, the model is trained and validated 5 times; each time a different 20% is used for validation, and the five scores are averaged.**

That's the main concept you should remember.
