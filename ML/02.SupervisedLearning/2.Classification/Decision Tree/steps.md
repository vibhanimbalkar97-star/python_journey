Bilkul. Decision Tree ko **actual ML workflow + behind-the-scenes mathematics** ke saath samjho. Main classification example use karunga, kyunki usme **Gini/Entropy** clearly samajh aata hai.

# 🌳 Decision Tree — Steps + Mathematical Explanation

Suppose business problem:

> **Customer loan lega ya nahi?**

Dataset:

| Age | Income | Loan |
| --: | -----: | ---- |
|  25 |    30K | No   |
|  28 |    35K | No   |
|  35 |    60K | Yes  |
|  40 |    70K | Yes  |
|  45 |    80K | Yes  |
|  30 |    40K | No   |

Here:

```text
X = Age, Income
y = Loan
```

Target categorical hai:

```text
Yes / No
```

---

# Step 1 — Dataset lo

```text
             Dataset
                ↓
        Age, Income, Loan
```

Sabse pehle:

```python
X = df.drop('Loan', axis=1)
y = df['Loan']
```

Mathematically:

$$
X = [Age, Income]
$$

$$
y = [Loan]
$$

---

# Step 2 — Train/Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
```

Example:

```text
80% → Training
20% → Testing
```

Training data se tree **rules/splits learn** karega.

---

# Step 3 — Decision Tree model create karo

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    criterion='gini',
    random_state=42
)
```

Yahan:

```text
criterion='gini'
```

ka matlab:

> Tree split choose karne ke liye **Gini Impurity** use karega.

Aap `entropy` bhi use kar sakte ho.

```python
criterion='entropy'
```

---

# Step 4 — `fit()` karo

```python
model.fit(X_train, y_train)
```

**Yahan actual mathematics start hoti hai.**

Tree ye nahi karta ki randomly `Age` choose kar liya.

It asks:

> **"Kaunsa feature aur kaunsi value data ko sabse achhe way mein split karegi?"**

For example:

```text
Age <= 30?
```

or

```text
Income <= 50K?
```

Tree different possible splits evaluate karta hai.

---

# Step 5 — Parent Node ki impurity calculate hoti hai

Suppose current node mein:

```text
10 customers

Yes = 6
No  = 4
```

Probabilities:

$$
P(Yes)=\frac{6}{10}=0.6
$$

$$
P(No)=\frac{4}{10}=0.4
$$

---

## Gini Impurity

Formula:

$$
Gini = 1-\sum p_i^2
$$

Do classes hain, therefore:

$$
Gini=1-[P(Yes)^2+P(No)^2]
$$

Values put karo:

$$
=1-(0.6^2+0.4^2)
$$

$$
=1-(0.36+0.16)
$$

$$
=1-0.52
$$

$$
\boxed{Gini=0.48}
$$

### Iska meaning?

`0.48` means node mixed hai.

Agar:

```text
Yes = 10
No = 0
```

Then:

$$
Gini=1-(1^2+0^2)
$$

$$
=0
$$

So:

> **Gini = 0 → completely pure node**

---

# Step 6 — Different splits try hote hain

Suppose tree check karta hai:

### Split 1:

```text
Age <= 30
```

After split:

```text
Left node:
Yes = 1
No = 4
Total = 5

Right node:
Yes = 5
No = 0
Total = 5
```

Ab dono child nodes ka Gini calculate karenge.

---

## Left node Gini

$$
P(Yes)=\frac15=0.2
$$

$$
P(No)=\frac45=0.8
$$

$$
Gini_{left}
=
1-(0.2^2+0.8^2)
$$

$$
=1-(0.04+0.64)
$$

$$
=0.32
$$

---

## Right node Gini

```text
5 Yes
0 No
```

$$
Gini_{right}
=
1-(1^2+0^2)
$$

$$
=0
$$

Perfectly pure.

---

# Step 7 — Weighted Gini calculate hota hai

Important point:

Child nodes ka simple average nahi lena.

Unke **sizes ko consider** karna hota hai.

Formula:

$$
Weighted\ Gini
=
\frac{N_{left}}{N_{total}}Gini_{left}
+
\frac{N_{right}}{N_{total}}Gini_{right}
$$

Here:

```text
Left = 5
Right = 5
Total = 10
```

Therefore:

$$
=\frac5{10}(0.32)+\frac5{10}(0)
$$

$$
=0.16
$$

So:

$$
\boxed{Weighted\ Gini=0.16}
$$

Parent Gini tha:

$$
0.48
$$

Split ke baad:

$$
0.16
$$

So impurity **decrease** hui.

---

# Step 8 — Tree different splits compare karta hai

Suppose:

| Split        | Weighted Gini |
| ------------ | ------------: |
| Age ≤ 30     |      **0.16** |
| Age ≤ 35     |          0.30 |
| Income ≤ 40K |          0.25 |
| Income ≤ 50K |          0.20 |

Tree generally **lowest weighted impurity** wali split choose karega when using Gini.

Therefore:

```text
Age <= 30
```

select ho sakta hai.

---

# Step 9 — Entropy use karoge toh calculation different hogi

Agar:

```python
criterion='entropy'
```

then tree Entropy calculate karega.

Formula:

$$
Entropy=-\sum p_i\log_2(p_i)
$$

For:

```text
6 Yes
4 No
```

$$
Entropy=
-[0.6\log_2(0.6)+0.4\log_2(0.4)]
$$

Approximately:

$$
\boxed{Entropy=0.971}
$$

Then different splits ke **Information Gain** compare kiye ja sakte hain.

$$
Information\ Gain
=
Entropy(parent)-WeightedEntropy(children)
$$

Higher Information Gain generally better split hoti hai.

---

# Step 10 — Split recursively repeat hota hai

Ab first split mil gaya:

```text
                 Age <= 30?
                /          \
              Yes           No
              /              \
          Node 1            Node 2
```

Ab Node 1 aur Node 2 ke andar bhi tree check karega:

```text
Kya aur split useful hai?
        ↓
Gini/Entropy calculate
        ↓
Best split
        ↓
Again split
```

Ye process **recursively** hota hai.

---

# Step 11 — Tree kab stop hota hai?

Agar tree unlimited grow kare:

```text
Data
 ↓
Split
 ↓
Split
 ↓
Split
 ↓
Split
 ↓
...
```

Tree training data ko bahut closely memorize kar sakta hai.

Result:

```text
Training accuracy → very high
Test performance → may decrease
```

This is **overfitting**.

Isliye stopping conditions use karte hain.

---

# Step 12 — `max_depth`

Example:

```python
model = DecisionTreeClassifier(
    max_depth=3
)
```

Meaning:

> Tree ko maximum depth 3 tak grow hone do.

---

# Step 13 — `min_samples_split`

```python
min_samples_split=10
```

Meaning:

> Node ko split karne ke liye minimum 10 samples hone chahiye.

Agar:

```text
samples = 5
```

toh split nahi hoga.

---

# Step 14 — `min_samples_leaf`

```python
min_samples_leaf=5
```

Meaning:

> Har final leaf mein minimum 5 samples hone chahiye.

Ye bhi tree ko unnecessarily complex hone se rokta hai.

---

# Step 15 — Final tree

Example:

```text
                    Age <= 30?
                   /          \
                 Yes           No
                 /              \
          Income <= 35K?      Loan = Yes
             /     \
           No       Yes
```

Leaf nodes final prediction dete hain.

---

# Step 16 — New data par prediction

Suppose new customer:

```text
Age = 28
Income = 40K
```

Tree follow karega:

```text
Age <= 30?
     ↓
    Yes
     ↓
Income <= 35K?
     ↓
    No
     ↓
Prediction
```

So final leaf ki class prediction milegi.

---

# Step 17 — `predict()`

```python
y_pred = model.predict(X_test)
```

Prediction ke time **Gini/Entropy calculate karke new tree nahi banaya jata**.

Tree already trained hai.

New data simply:

```text
Root
 ↓
Condition
 ↓
Branch
 ↓
Condition
 ↓
Leaf
 ↓
Prediction
```

---

# Complete Mathematical Flow

```text
                DATA
                  ↓
             X and y
                  ↓
           Train/Test Split
                  ↓
             Training Data
                  ↓
        Parent Node impurity
                  ↓
        ┌─────────────────┐
        │ Gini / Entropy  │
        └─────────────────┘
                  ↓
       Try different features
                  ↓
       Try different thresholds
                  ↓
      Calculate child impurity
                  ↓
        Weighted impurity
                  ↓
        Choose best split
                  ↓
             Split data
                  ↓
          Repeat recursively
                  ↓
        Stopping condition
                  ↓
            Final Tree
                  ↓
             New Data
                  ↓
          Follow tree path
                  ↓
              Leaf Node
                  ↓
             Prediction
```

# ⭐ Interview mein mathematical explanation

Agar interviewer bole:

**"Explain how Decision Tree selects a split mathematically."**

Aap simple English mein bol sakte ho:

> **"For classification, the Decision Tree calculates an impurity measure such as Gini impurity for the current node. It tries different features and split points, calculates the weighted impurity of the child nodes, and selects the split that gives the lowest impurity when using Gini. This process is repeated recursively until a stopping condition is reached."**

### Sabse important formulas

**Gini:**

$$
\boxed{Gini=1-\sum p_i^2}
$$

**Weighted Gini:**

$$
\boxed{
Gini_{split}
=
\frac{N_L}{N}Gini_L+
\frac{N_R}{N}Gini_R
}
$$

**Entropy:**

$$
\boxed{
Entropy=-\sum p_i\log_2p_i
}
$$

**Information Gain:**

$$
\boxed{
IG=Entropy_{parent}-WeightedEntropy_{children}
}
$$

### 🧠 Ek line mein yaad rakho

> **Decision Tree → different splits try karta hai → Gini/Entropy calculate karta hai → best split choose karta hai → recursively repeat karta hai → leaf node par prediction deta hai.**
============================================================================================================================================

Agar aap **Decision Tree me `criterion`** ki baat kar rahe ho, to mainly **Gini** aur **Entropy** choose karte hain.

### 1. Criterion ka matlab kya hai?

Criterion = **Decision Tree ko kaise decide karna hai ki best split kaunsa hai.**

```python
DecisionTreeClassifier(criterion="gini")
```

or

```python
DecisionTreeClassifier(criterion="entropy")
```

### 2. Gini kab choose kare?

**Gini = default criterion** in `DecisionTreeClassifier`.

```python
DecisionTreeClassifier(criterion="gini")
```

Gini impurity calculate karta hai:

$$
Gini = 1 - \sum p_i^2
$$

**Simple rule:**
Agar koi specific requirement nahi hai → **Gini use kar sakte ho.**

---

### 3. Entropy kab choose kare?

```python
DecisionTreeClassifier(criterion="entropy")
```

Entropy:

$$
Entropy = -\sum p_i\log_2(p_i)
$$

Ye **Information Gain** ke through best split choose karta hai:

$$
IG = Entropy(parent)-WeightedEntropy(children)
$$

**Simple rule:**
Agar aap specifically **Information Gain / Entropy** explain ya use karna chahte ho → Entropy.

---

### 4. Kya data dekhkar decide karte hain?

Usually **sirf dataset dekhkar ye nahi bolte ki Gini hi use karna hai**.

Dono try kar sakte ho:

```python
model1 = DecisionTreeClassifier(criterion="gini", random_state=42)
model2 = DecisionTreeClassifier(criterion="entropy", random_state=42)
```

Phir validation/test performance compare kar sakte ho.

But **sirf accuracy dekhkar blindly choose nahi karna**—problem ke appropriate evaluation metric ko use karo.

### Interview me kya bolna hai?

> **“For a Decision Tree classifier, Gini is commonly used and is the default criterion in scikit-learn. Entropy can also be used when we want to select splits based on Information Gain. In practice, I can compare both using validation performance and choose the suitable one.”**

### Easy memory 🧠

**Gini → impurity minimize**
**Entropy → Information Gain maximize**

Aur ek important point: **criterion ka choice usually model performance par bahut huge difference nahi karta**, so beginner projects me `gini` se start karna perfectly fine hai.
