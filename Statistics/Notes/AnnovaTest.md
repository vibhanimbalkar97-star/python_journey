### ANOVA — Simple Explanation

**ANOVA (Analysis of Variance)** is used to check whether the **means of 3 or more groups are significantly different**.

### Example

Suppose we have exam scores from 3 teaching methods:

```text
Method A → 70, 72, 68, 71
Method B → 80, 82, 78, 81
Method C → 75, 77, 74, 76
```

Question:

> **Are the average scores of these groups significantly different?**

ANOVA helps answer this.

### Hypotheses

```text
H₀: All group means are equal
H₁: At least one group mean is different
```

### How to decide?

ANOVA gives an **F-statistic** and **p-value**.

```text
p-value < 0.05
      ↓
Reject H₀
      ↓
At least one group mean is different
```

```text
p-value > 0.05
      ↓
Fail to reject H₀
      ↓
Not enough evidence that the means differ
```

### When to use ANOVA?

| Situation                     | Test       |
| ----------------------------- | ---------- |
| Compare **2 means**           | t-test     |
| Compare **3+ means**          | ⭐ ANOVA    |
| Compare categorical variables | Chi-square |

### 🧠 Easy identification

> **"I have 3 or more groups and want to compare their means." → ANOVA**

One important point: if ANOVA says there **is** a difference, it doesn't directly tell you **which groups differ**. You would typically use a **post-hoc test** such as Tukey's test.


Yes. In a **real dataset/table**, you identify ANOVA based on the **type of columns**.

### Simple rule ⭐

ANOVA needs:

> **1 categorical column = groups**
> **1 numerical column = values whose means you want to compare**

For example, a student dataset:

| Method | Gender | Score | Age |
| ------ | ------ | ----: | --: |
| A      | Female |    72 |  20 |
| A      | Male   |    75 |  21 |
| B      | Female |    85 |  20 |
| B      | Male   |    82 |  22 |
| C      | Female |    78 |  21 |
| C      | Male   |    80 |  20 |

If the question is:

> **Does teaching Method affect Score?**

Then:

```text
Categorical → Method
Numerical   → Score
```

So you do **ANOVA on `Score` grouped by `Method`**.

```text
Method A → scores
Method B → scores
Method C → scores
       ↓
Compare their means
       ↓
ANOVA
```

### How to identify from any table

| Question                                             | Group column | Numerical column | Test       |
| ---------------------------------------------------- | ------------ | ---------------- | ---------- |
| Do 3 teaching methods have different average scores? | Method       | Score            | ⭐ ANOVA    |
| Do 4 cities have different average salaries?         | City         | Salary           | ⭐ ANOVA    |
| Do 3 departments have different average ages?        | Department   | Age              | ⭐ ANOVA    |
| Do 2 methods have different average scores?          | Method       | Score            | t-test     |
| Is Gender related to Pclass?                         | Gender       | Pclass           | Chi-square |

### In real data

You **don't automatically apply ANOVA to every numerical column**.

You first ask:

> **"Which categorical column represents my groups, and which numerical column's mean am I comparing?"**

For example, with a Titanic dataset:

```text
Pclass → categorical/group variable
Fare   → numerical variable
```

Question:

> **Does average Fare differ across Pclass 1, 2, and 3?**

Then ANOVA is appropriate:

```text
Pclass 1 → Fare values
Pclass 2 → Fare values
Pclass 3 → Fare values
              ↓
            ANOVA
```

If you have a real CSV/table, you can upload it and I can show you **exactly which columns are candidates for t-test, ANOVA, chi-square, and correlation**.


Sure. Let's use the **Seaborn Titanic dataset** as a real-data example and identify **exactly when ANOVA is used**.

### Titanic dataset — relevant columns

Some important columns are:

| Column     | Type                | Example      |
| ---------- | ------------------- | ------------ |
| `survived` | Categorical/Binary  | 0, 1         |
| `sex`      | Categorical         | male, female |
| `pclass`   | Categorical/Ordinal | 1, 2, 3      |
| `age`      | Numerical           | 22.0         |
| `fare`     | Numerical           | 7.25         |
| `embarked` | Categorical         | S, C, Q      |

---

### Example: `pclass` vs `fare`

Question:

> **Does the average fare differ between the 3 passenger classes?**

Here:

```text
pclass → Group/Categorical
fare   → Numerical
```

We have **3 groups**:

```text
Pclass 1 → Fare values
Pclass 2 → Fare values
Pclass 3 → Fare values
```

Therefore:

### ⭐ ANOVA

```python
import seaborn as sns
import scipy.stats as stats

df = sns.load_dataset("titanic")

group1 = df[df["pclass"] == 1]["fare"].dropna()
group2 = df[df["pclass"] == 2]["fare"].dropna()
group3 = df[df["pclass"] == 3]["fare"].dropna()

f_stat, p_value = stats.f_oneway(group1, group2, group3)

print(f_stat)
print(p_value)
```

### Hypotheses

```text
H₀: Mean Fare₁ = Mean Fare₂ = Mean Fare₃

H₁: At least one mean is different
```

Then:

```text
p-value < 0.05 → Reject H₀
p-value > 0.05 → Fail to reject H₀
```

### 🧠 How to identify ANOVA in Titanic

| Question                                  | Columns            | Test        |
| ----------------------------------------- | ------------------ | ----------- |
| Does `fare` differ across `pclass` 1,2,3? | `pclass` + `fare`  | ⭐ ANOVA     |
| Does `age` differ across `pclass` 1,2,3?  | `pclass` + `age`   | ⭐ ANOVA     |
| Does `fare` differ between male/female?   | `sex` + `fare`     | t-test      |
| Is `sex` related to `survived`?           | `sex` + `survived` | Chi-square  |
| Is `age` related to `fare`?               | `age` + `fare`     | Correlation |

**Main identification rule:**

> **Categorical column with 3+ groups + Numerical column → ANOVA (when comparing the group means).**
