# 18. Stacking

Now the third technique.

### Stacking = different models + another model

Suppose we have:

```text
                 Dataset
                    ↓
       ┌────────────┼────────────┐
       ↓            ↓            ↓
 Logistic       Random        KNN
Regression      Forest
       ↓            ↓            ↓
      prediction outputs
             ↓
       Meta Model
             ↓
      Final prediction
```

The final model is called:

**Meta-model / Meta-learner**

---

# 19. Stacking example

Suppose we want to predict whether a customer will churn.

We train:

```text
Model 1 → Logistic Regression
Model 2 → Random Forest
Model 3 → KNN
```

For one customer:

```text
Logistic Regression → 0.70 probability
Random Forest       → 0.85 probability
KNN                 → 0.60 probability
```

These outputs become inputs to another model:

```text
X_meta = [
    0.70,
    0.85,
    0.60
]
```

Meta-model might predict:

```text
Churn probability = 0.80
```

Final:

```text
Churn = Yes
```

---

# 20. Why stacking?

Different models learn different patterns.

For example:

```text
Logistic Regression
→ good at linear relationships

Random Forest
→ good at nonlinear relationships

KNN
→ good based on nearby observations
```

Instead of choosing only one, stacking can combine their information.

---

# 21. Stacking code

```python
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

estimators = [
    ("lr", LogisticRegression()),
    ("rf", RandomForestClassifier(n_estimators=100, random_state=42)),
    ("knn", KNeighborsClassifier())
]

stacking_model = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression()
)

stacking_model.fit(X_train, y_train)

y_pred = stacking_model.predict(X_test)
```

Here:

```text
lr
rf
knn
```

are **base estimators**.

And:

```python
final_estimator=LogisticRegression()
```

is the **meta-model**.

---

# 22. Very important: Stacking calculation

Suppose training data has:

```text
X1 X2 X3
```

Three base models generate:

| Row | Logistic |  RF | KNN | Actual |
| --- | -------: | --: | --: | -----: |
| 1   |      0.8 | 0.7 | 0.9 |      1 |
| 2   |      0.2 | 0.3 | 0.1 |      0 |
| 3   |      0.6 | 0.8 | 0.7 |      1 |

Meta-model gets:

```text
        LR    RF    KNN
Row1   0.8   0.7   0.9
Row2   0.2   0.3   0.1
Row3   0.6   0.8   0.7
```

It learns:

```text
LR prediction
RF prediction
KNN prediction
        ↓
Meta-model
        ↓
Final prediction
```

In proper stacking, these training predictions are generally generated using **cross-validation/out-of-fold predictions** so the meta-model doesn't simply learn from predictions made on data the base model already saw.

That point is important for interviews.

---

# 23. Bagging vs Boosting vs Stacking

| Feature    | Bagging              | Boosting                         | Stacking                    |
| ---------- | -------------------- | -------------------------------- | --------------------------- |
| Models     | Usually same type    | Usually sequential weak learners | Usually different models    |
| Training   | Parallel/independent | Sequential                       | Base models + meta-model    |
| Main idea  | Reduce variance      | Reduce errors/bias               | Combine different models    |
| Example    | Random Forest        | XGBoost                          | RF + KNN + Logistic         |
| Focus      | Stability            | Correct previous errors          | Learn how to combine models |
| Common use | Tabular data         | High-performance tabular ML      | Combining diverse models    |

---

# 24. Easy way to remember

### Bagging

> **Many models independently → vote/average**

```text
Model 1 ──┐
Model 2 ──┤
Model 3 ──┼──→ Final
Model 4 ──┤
Model 5 ──┘
```

### Boosting

> **One model after another → fix previous errors**

```text
Model 1
   ↓
errors
   ↓
Model 2
   ↓
remaining errors
   ↓
Model 3
   ↓
Final
```

### Stacking

> **Different models → meta-model**

```text
LR ───────┐
RF ───────┼──→ Meta Model → Final
KNN ──────┘
```

---

# 25. When to choose which?

For a new tabular dataset, don't blindly choose one.

A practical workflow is:

```text
Dataset
   ↓
EDA
   ↓
Preprocessing
   ↓
Train/Test Split
   ↓
Baseline models
   ↓
Compare
   ↓
Try Ensemble models
   ↓
Cross Validation
   ↓
Hyperparameter tuning
   ↓
Final evaluation
```

You can try:

```text
Logistic Regression / Linear Regression
        ↓
Decision Tree
        ↓
Random Forest
        ↓
Gradient Boosting
        ↓
XGBoost / CatBoost / LightGBM
        ↓
Stacking if useful
```

Then compare appropriate metrics.

For classification:

```text
Accuracy
Precision
Recall
F1
ROC-AUC
```

For regression:

```text
MAE
MSE
RMSE
R²
```

---

## 26. Interview answer — very short

If interviewer asks:

**"What is ensemble learning?"**

You can say:

> "Ensemble learning combines multiple machine learning models to produce a stronger and more robust prediction than an individual model."

**"What is bagging?"**

> "Bagging trains multiple models independently on different bootstrap samples and combines their predictions. Random Forest is a common example."

**"What is boosting?"**

> "Boosting trains models sequentially, where each new model focuses on reducing the errors made by previous models. Examples include AdaBoost, Gradient Boosting and XGBoost."

**"What is stacking?"**

> "Stacking combines predictions from multiple different base models and uses another model called a meta-learner to make the final prediction."

### One-line memory trick

```text
Bagging  → Independent models → Combine
Boosting → Sequential models  → Correct errors
Stacking → Different models   → Meta-model
```

============================================================================================================================================

For the **Iris dataset**, you usually **do not need `LabelEncoder` for `y` when using `StackingClassifier`**, because the target is already represented as class labels and scikit-learn classifiers can handle them.

### Iris example

```python
import seaborn as sns

df = sns.load_dataset("iris")

X = df.drop("species", axis=1)
y = df["species"]

print(y.head())
```

`y` looks like:

```text
0        setosa
1        setosa
2        setosa
...
50     versicolor
...
100     virginica
```

So `y` contains:

```text
setosa
versicolor
virginica
```

### Do we need LabelEncoder?

**No, not necessarily.**

You can directly do:

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

estimators = [
    ("lr", LogisticRegression(max_iter=1000)),
    ("dt", DecisionTreeClassifier(random_state=42)),
    ("knn", KNeighborsClassifier())
]

stacking_model = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression()
)

stacking_model.fit(X_train, y_train)
```

This works with:

```text
setosa
versicolor
virginica
```

directly.

---

## If you DO LabelEncode Iris `y`

You can also do:

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

y_encoded = le.fit_transform(y)
```

Then:

```text
setosa      → 0
versicolor  → 1
virginica   → 2
```

Then train:

```python
stacking_model.fit(X_train, y_train_encoded)
```

And after prediction:

```python
y_pred = stacking_model.predict(X_test)

y_pred_original = le.inverse_transform(y_pred)
```

So both approaches are possible.

### Important

Don't think:

> "Stacking requires LabelEncoder."

Instead think:

> **"My target is categorical. Do my estimator/workflow require numeric target labels?"**

For normal **scikit-learn classification**, string labels such as Iris `species` are generally accepted directly.

### Iris workflow

```text
Iris dataset
     ↓
X = sepal/petal features
y = species
     ↓
Train-test split
     ↓
StackingClassifier
     ↓
Logistic + Decision Tree + KNN
     ↓
Meta-model
     ↓
Prediction
```

**LabelEncoder is optional here**, not a requirement of stacking.
=============================================================================================================================================

Yes, but **only when `y` (target) is categorical text** and the models need numeric target labels.

### Example

Suppose your target is:

```python
y = ["Yes", "No", "Yes", "No", "Yes"]
```

Most scikit-learn classifiers can actually handle string labels directly, so **you don't necessarily need to manually use `LabelEncoder`**.

If you do encode:

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

y_encoded = le.fit_transform(y)
```

You get something like:

```text
No  → 0
Yes → 1
```

Then:

```python
stacking_model.fit(X_train, y_train_encoded)
```

### Why encode `y`?

Because internally classification algorithms work with **class labels**, and numeric representation is convenient/required for some algorithms or workflows.

But remember:

### `LabelEncoder` for `y` ≠ `OneHotEncoder` for `X`

For a binary target:

```text
y:
Yes → 1
No  → 0
```

is perfectly fine.

For example:

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

stacking_model.fit(X_train, y_train)
```

After prediction, if you want the original labels back:

```python
y_pred = stacking_model.predict(X_test)

y_pred_original = le.inverse_transform(y_pred)
```

So:

```text
Original y
   ↓
LabelEncoder
   ↓
0 / 1
   ↓
Stacking model
   ↓
prediction 0 / 1
   ↓
inverse_transform()
   ↓
No / Yes
```

### One important point for your stacking learning

**Stacking itself does NOT require LabelEncoder.**

The reason for encoding is the **target/model requirements**, not because it is stacking.

For example, this can work directly:

```python
y = ["Yes", "No", "Yes", "No"]

stacking_model.fit(X, y)
```

Scikit-learn classifiers generally handle string class labels.

**Interview answer:**

> "Label encoding can be applied to a categorical target to represent class labels numerically, such as Yes/No → 1/0. However, stacking itself does not require LabelEncoder; it's dependent on the target format and estimator requirements."



