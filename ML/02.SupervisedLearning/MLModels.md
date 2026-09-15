| ML Type                    | Main problem                  | Important models/algorithms                                                              |
| -------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------- |
| **Supervised Learning**    | Have target/output            |                                                                                          |
| → Regression               | Predict a number              | Linear Regression, Polynomial Regression, Ridge, Lasso, Random Forest, Gradient Boosting |
| → Classification           | Predict a category            | Logistic Regression, KNN, Decision Tree, Random Forest, SVM, Naive Bayes                 |
| **Unsupervised Learning**  | No target/output              |                                                                                          |
| → Clustering               | Find groups                   | K-Means, Hierarchical, DBSCAN                                                            |
| → Dimensionality Reduction | Reduce features               | PCA                                                                                      |
| → Association              | Find relationships            | Apriori                                                                                  |
| **Reinforcement Learning** | Learn using rewards/penalties | Q-Learning, Policy Gradient                                                              |


1. Supervised Learning

Regression
Classification

2. Unsupervised Learning

Clustering
PCA / dimensionality reduction

3. Then advanced topics

Ensemble learning
Gradient Boosting
XGBoost/LightGBM
Neural Networks → Deep Learning

===============================================================================================================================

## Classification in Machine Learning

**Classification** is a **Supervised Machine Learning** technique used to predict a **category/class (label)** as the output.

### Simple example

Suppose we want to predict whether a person has heart disease:

**Input (X):**

* Age
* Blood pressure
* Cholesterol
* Heart rate

**Output (y):**

* `0 → No heart disease`
* `1 → Heart disease`

So, because the output is a **category**, this is a **classification problem**.

---

### Types of Classification

| Type                          | Meaning                             | Example                        |
| ----------------------------- | ----------------------------------- | ------------------------------ |
| **Binary Classification**     | Only 2 classes                      | Spam / Not Spam                |
| **Multiclass Classification** | More than 2 classes                 | Cat / Dog / Horse              |
| **Multilabel Classification** | One record can have multiple labels | Image → Cat + Animal + Outdoor |

### Common Classification Algorithms

| Algorithm                     | Common Use Case                                  |
| ----------------------------- | ------------------------------------------------ |
| **Logistic Regression**       | Simple binary classification, medical prediction |
| **K-Nearest Neighbors (KNN)** | Small datasets, similarity-based classification  |
| **Decision Tree**             | Easy-to-understand rule-based predictions        |
| **Random Forest**             | Strong general-purpose classification            |
| **SVM**                       | Small/medium datasets, clear class boundaries    |
| **Naive Bayes**               | Text classification, spam detection              |
| **Gradient Boosting**         | High-performance tabular data                    |
| **XGBoost**                   | Very popular for structured/tabular datasets     |
| **Neural Networks**           | Complex patterns, images, text, large datasets   |

### Classification vs Regression

| Classification        | Regression            |
| --------------------- | --------------------- |
| Predicts **category** | Predicts **number**   |
| Output is discrete    | Output is continuous  |
| Heart disease: Yes/No | House price: ₹50 lakh |
| Spam/Not Spam         | Salary prediction     |
| Logistic Regression   | Linear Regression     |

**Important:** Even though **Logistic Regression** has "Regression" in its name, it is primarily a **classification algorithm**.

### Typical Classification Workflow

```text
Business Problem
      ↓
Identify Target (y)
      ↓
EDA
      ↓
Data Cleaning
      ↓
Encoding categorical features
      ↓
Feature Scaling (when required)
      ↓
Train-Test Split
      ↓
Choose Classification Algorithm
      ↓
Train Model
      ↓
Prediction
      ↓
Evaluate Model
```

For classification, common evaluation metrics are **Accuracy, Precision, Recall, F1-score, Confusion Matrix, and ROC-AUC**.
=========================================================================================================================================