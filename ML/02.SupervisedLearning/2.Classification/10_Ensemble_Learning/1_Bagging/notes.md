# 3. Bagging

### Main idea

**Bagging = train many models independently and combine their predictions.**

Bagging means:

> **Bootstrap Aggregating**

Think:

```text
Original Dataset
       ↓
 ┌─────┼─────┐
 ↓     ↓     ↓
Data1 Data2 Data3
 ↓     ↓     ↓
Model1 Model2 Model3
 ↓     ↓     ↓
Pred1 Pred2 Pred3
   \    |    /
    Final Prediction
```

The important point:

### Models are trained independently.

They don't wait for each other.

---

# 4. Bagging behind the scenes

Suppose we have 10 records:

```text
1 2 3 4 5 6 7 8 9 10
```

Bagging creates different datasets using **random sampling with replacement**.

For example:

### Dataset 1

```text
1 2 2 5 7 8 8 9 10 10
```

### Dataset 2

```text
1 3 4 4 5 6 7 7 9 10
```

### Dataset 3

```text
2 2 3 5 6 8 9 9 10 10
```

Notice:

* Some records appear multiple times.
* Some records aren't selected.

Each dataset trains a separate model.

---

# 5. Bagging calculation — classification

Suppose 5 decision trees give:

```text
Tree 1 → Yes
Tree 2 → Yes
Tree 3 → No
Tree 4 → Yes
Tree 5 → No
```

Count:

```text
Yes = 3
No  = 2
```

Majority voting:

```text
Final = Yes
```

So:

**Bagging classification → majority voting**

---

# 6. Bagging calculation — regression

Suppose 5 models predict house price:

```text
Model 1 → ₹50 lakh
Model 2 → ₹55 lakh
Model 3 → ₹52 lakh
Model 4 → ₹48 lakh
Model 5 → ₹50 lakh
```

Average:

```text
(50 + 55 + 52 + 48 + 50) / 5

= 255 / 5

= ₹51 lakh
```

Final prediction:

**₹51 lakh**

So:

```text
Classification → Voting
Regression     → Average
```

---

# 7. Random Forest = Bagging

This is very important for interviews.

**Random Forest is an ensemble of Decision Trees.**

It uses two important kinds of randomness:

### 1. Random rows

Each tree gets a bootstrap sample.

### 2. Random features

At each split, only a random subset of features is considered.

Example:

```text
Dataset
   ↓
Random rows + Random features
   ↓
Tree 1
Tree 2
Tree 3
Tree 4
Tree 5
   ↓
Voting / Average
   ↓
Final prediction
```

---

# 8. Bagging code

### Classification

```python
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

bagging_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,
    random_state=42
)

bagging_model.fit(X_train, y_train)

y_pred = bagging_model.predict(X_test)
```

Important parameters:

```python
n_estimators=100
```

means:

> Create 100 models/trees.

---

### Random Forest

Usually, instead of manually creating bagging with trees, we use:

```python
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)
```

---

# 9. When should we use Bagging?

Bagging is especially useful when the base model has **high variance**.

For example:

```text
Decision Tree
     ↓
Can overfit easily
     ↓
Bagging
     ↓
Many trees
     ↓
More stable prediction
```

Typical use:

* Classification
* Regression
* Tabular datasets
* When Decision Trees are performing well but overfitting
* When you want a strong baseline

Examples:

```text
Random Forest
BaggingClassifier
BaggingRegressor
```

---

Yes. The most important thing is to separate **Bagging**, **Random Forest**, and **variance**. They are related, but they are not exactly the same thing.

## 1. What does Bootstrap Aggregating mean?

**Bootstrap Aggregating = Bagging**

Break the words:

* **Bootstrap** → create multiple datasets by **random sampling with replacement**
* **Aggregating** → combine predictions from all models

Suppose original dataset has:

```text
A B C D E F
```

We create bootstrap samples:

```text
Sample 1 → A B B D E F
Sample 2 → A C C D F F
Sample 3 → B B C E E F
```

Notice that:

* Some rows are repeated.
* Some rows are missing.
* Every sample can be different.

Then train a model on each:

```text
Sample 1 → Decision Tree 1
Sample 2 → Decision Tree 2
Sample 3 → Decision Tree 3
```

Then combine their predictions.

For classification:

```text
Tree 1 → Yes
Tree 2 → No
Tree 3 → Yes

Final → Yes
```

That's **Bagging**.

---

# 2. Then why do we say Random Forest = Bagging?

This is a very important distinction.

### Basic Bagging with Decision Trees

```text
Dataset
   ↓
Bootstrap sample
   ↓
Decision Tree 1

Dataset
   ↓
Bootstrap sample
   ↓
Decision Tree 2

Dataset
   ↓
Bootstrap sample
   ↓
Decision Tree 3
```

The trees are trained independently.

### Random Forest adds another layer of randomness

Random Forest does:

```text
Random rows
+
Random features
+
Many Decision Trees
+
Voting/Average
```

So:

> **Random Forest is a specialized ensemble method based on bagging Decision Trees, with additional random feature selection.**

For example, suppose you have:

```text
age
salary
experience
city
education
```

At a particular tree split, Random Forest might randomly consider only:

```text
age
salary
```

instead of all 5 features.

Another split might consider:

```text
experience
education
```

This makes the trees **less similar to each other**.

And that's useful because combining diverse trees works better.

---

# 3. Why do we want trees to be different?

Imagine 5 trees all make almost exactly the same mistake:

```text
Tree 1 → Wrong
Tree 2 → Wrong
Tree 3 → Wrong
Tree 4 → Wrong
Tree 5 → Wrong
```

Voting doesn't help much.

But suppose:

```text
Tree 1 → Yes
Tree 2 → Yes
Tree 3 → No
Tree 4 → Yes
Tree 5 → No
```

Now majority voting can correct some individual mistakes.

That's one of the main ideas behind Random Forest.

---

# 4. Now what is HIGH VARIANCE?

This is extremely important for understanding why Bagging works.

**Variance = how much a model's prediction changes when the training data changes.**

Imagine we train a Decision Tree on Dataset A:

```text
Dataset A → Tree → prediction = 80
```

Now we slightly change the training data:

```text
Dataset B → Tree → prediction = 50
```

Another small change:

```text
Dataset C → Tree → prediction = 90
```

The predictions changed a lot.

That means:

> **High variance**

A Decision Tree can be a high-variance model because small changes in training data can create a very different tree.

---

# 5. Simple example of high variance

Suppose:

```text
Training data:
100 rows
```

You train Tree 1.

```text
Tree 1 → 90% accuracy
```

Change/remove a few rows:

```text
Tree 2 → 75%
```

Change some rows again:

```text
Tree 3 → 94%
```

Large variation.

So:

```text
Training data changes slightly
             ↓
Model changes significantly
             ↓
High Variance
```

genui{"learning_viz":{"type_id":"VARIANCE","locale_override":"en-IN"}}

---

# 6. What is LOW VARIANCE?

Now imagine:

```text
Dataset A → Model → 82%
Dataset B → Model → 83%
Dataset C → Model → 82%
Dataset D → Model → 84%
```

Small changes in training data produce similar models/predictions.

That's:

> **Low variance**

So remember:

```text
High variance
→ Model changes a lot with training data

Low variance
→ Model changes little with training data
```

---

# 7. How do I know whether a model has high variance?

You can often identify it by looking at **training vs validation/test performance**.

### Example 1

```text
Training accuracy = 99%
Validation accuracy = 75%
```

Large gap.

This is a strong sign of **overfitting**, which is commonly associated with high variance.

```text
Train = 99%
Test  = 75%

       ↓

Model learned training data too specifically
       ↓
High variance / overfitting
```

### Example 2

```text
Training accuracy = 78%
Validation accuracy = 76%
```

Small gap.

This is not showing the typical high-variance pattern.

---

# 8. But be careful: high variance ≠ simply "train-test gap"

This is an important interview point.

You don't directly calculate:

```text
variance = train accuracy - test accuracy
```

That's **not** the mathematical definition of variance.

The train/test gap is a **diagnostic clue** for overfitting.

Variance mathematically describes how much predictions/model estimates vary across different training samples.

In practical ML, we often diagnose high variance through:

* Train vs validation performance
* Cross-validation scores
* Model stability across different samples
* Learning curves

---

# 9. Why does Bagging help high variance?

This is the main reason Bagging is powerful.

Suppose:

```text
Tree 1 → 70
Tree 2 → 80
Tree 3 → 75
Tree 4 → 90
Tree 5 → 85
```

Individual trees vary significantly.

Bagging combines them:

```text
(70 + 80 + 75 + 90 + 85) / 5

= 80
```

Instead of relying on one unstable tree, we average many trees.

This tends to make the final prediction **more stable**.

So:

```text
High-variance trees
       ↓
Many different trees
       ↓
Average / voting
       ↓
More stable ensemble
```

That's the intuition behind why Random Forest often performs better than one Decision Tree.

---

# 10. Is Ensemble Learning only for Decision Trees?

**No. Definitely not.**

Ensemble learning is a **general technique**.

You can build ensembles using different algorithms.

For example:

### Bagging

Can use:

```text
Decision Trees
KNN
Other estimators
```

Scikit-learn's `BaggingClassifier` allows you to specify the base estimator.

Example:

```python
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier

model = BaggingClassifier(
    estimator=KNeighborsClassifier(),
    n_estimators=50,
    random_state=42
)
```

So Bagging isn't restricted to Decision Trees.

---

# 11. Why are Decision Trees so common in ensembles?

Because Decision Trees have several properties that work very well with ensemble methods.

A single tree can:

* Capture nonlinear relationships
* Handle feature interactions
* Work with different feature scales
* Be relatively unstable/high variance
* Overfit when grown deeply

Therefore:

```text
Single Decision Tree
        ↓
Can have high variance
        ↓
Bagging many trees
        ↓
Random Forest
        ↓
More stable model
```

That's why you see trees everywhere in ensemble learning.

---

# 12. What about Boosting?

Boosting also commonly uses Decision Trees.

For example:

```text
AdaBoost
Gradient Boosting
XGBoost
LightGBM
CatBoost
```

often use **small/shallow Decision Trees** as their base learners.

But the purpose is different.

### Bagging

```text
Tree 1 ─────┐
Tree 2 ─────┤
Tree 3 ─────┼──→ Combine
Tree 4 ─────┤
Tree 5 ─────┘

Independent
```

### Boosting

```text
Tree 1
  ↓
Find errors
  ↓
Tree 2
  ↓
Find errors
  ↓
Tree 3
  ↓
Final model

Sequential
```

---

# 13. The easiest way to remember everything

### Decision Tree

```text
One tree
↓
Can overfit
↓
High variance
```

### Bagging

```text
Many independent models
↓
Combine predictions
↓
Reduce variance
```

### Random Forest

```text
Many Decision Trees
+
Bootstrap samples
+
Random feature selection
↓
Voting / averaging
```

### Boosting

```text
Tree 1
↓
Fix errors
↓
Tree 2
↓
Fix errors
↓
Tree 3
↓
Final
```

### Stacking

```text
Model 1 ──┐
Model 2 ──┼──→ Meta-model → Final
Model 3 ──┘
```

---

## 14. One interview question you should be ready for

**Q: Why does Random Forest reduce overfitting compared with a single Decision Tree?**

Good beginner answer:

> "A single Decision Tree can have high variance and may overfit the training data. Random Forest trains many trees on different bootstrap samples and considers random subsets of features. Their predictions are then combined, which makes the final prediction more stable and generally reduces variance."

And one correction to remember:

> **Random Forest is not simply "many Decision Trees."** It combines **bootstrap sampling + random feature selection + many trees + aggregation**.

