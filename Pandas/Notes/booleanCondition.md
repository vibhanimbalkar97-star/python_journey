Haan 👍 Pandas mein **Boolean condition** tab use karte hain jab humein DataFrame mein se **specific rows filter/select** karni hoti hain.

### 🧠 Basic idea

Boolean condition ka result hota hai:

```text
True / False
```

Aur Pandas mein:

```python
df[condition]
```

ka matlab hota hai:

> **Jahan condition True hai, sirf woh rows do.**

### Common examples

Maan lo:

| Title | Score | Episodes |
| ----- | ----: | -------: |
| A     |   8.5 |       12 |
| B     |   9.2 |       24 |
| C     |   7.8 |       12 |
| D     |   9.5 |       50 |

#### 1. Score > 9

```python
df[df["Score"] > 9]
```

👉 Sirf Score 9 se greater wali rows.

---

#### 2. Score == 9.5

```python
df[df["Score"] == 9.5]
```

👉 Jiska score exactly 9.5 hai.

---

#### 3. Episodes < 20

```python
df[df["Episodes"] < 20]
```

👉 20 se kam episodes wali rows.

---

#### 4. Multiple conditions — `AND`

```python
df[(df["Score"] > 8) & (df["Episodes"] > 20)]
```

👉 Score > 8 **AND** Episodes > 20.

---

#### 5. Multiple conditions — `OR`

```python
df[(df["Score"] > 9) | (df["Episodes"] > 40)]
```

👉 Score > 9 **OR** Episodes > 40.

---

#### 6. Specific text

```python
df[df["Title"] == "Naruto"]
```

👉 Title exactly `"Naruto"` wali row.

---

#### 7. Maximum value wali row

Jo tumne abhi poocha tha:

```python
df[df["Score"] == df["Score"].max()]
```

👉 Pehle maximum Score find karo, phir **usi score wali row filter** karo.

---

### 🔥 Kab Boolean condition use karni hai?

| Requirement                        | Boolean condition? |
| ---------------------------------- | ------------------ |
| Score > 8 wale anime               | ✅                  |
| Episodes < 20                      | ✅                  |
| Title == Naruto                    | ✅                  |
| Maximum Score wali row             | ✅                  |
| Score aur Episodes dono conditions | ✅                  |
| Sirf maximum score calculate karna | ❌                  |
| Sirf average calculate karna       | ❌                  |
| Sirf column ka sum                 | ❌                  |

### 🧠 Simple rule

Question mein agar words aaye:

**"which rows", "where", "whose", "only those", "filter", "greater than", "less than", "equal to"**

➡️ Boolean filtering ke baare mein socho.

```python
df[condition]
```

Yahi Pandas mein **filtering** ka core concept hai.
============================================================================================================================

Both are used to **select/filter rows**, but they work differently.

Suppose:

```python
df
```

| index | Name | Age |
| ----: | ---- | --: |
|     0 | A    |  18 |
|     1 | B    |  22 |
|     2 | C    |  25 |
|     3 | D    |  19 |
|     4 | E    |  30 |
|     5 | F    |  24 |

---

### 1. `df.iloc[0:5]`

`iloc` = **integer position**

```python
df.iloc[0:5]
```

Means:

> Give me rows from **position 0 up to 5 (5 excluded)**.

So you get:

| index | Name | Age |
| ----: | ---- | --: |
|     0 | A    |  18 |
|     1 | B    |  22 |
|     2 | C    |  25 |
|     3 | D    |  19 |
|     4 | E    |  30 |

🧠 Same slicing concept as Python lists:

```python
arr[0:5]
```

---

### 2. `df.loc[df["Age"] > 20]`

Here `loc` is being used with a **condition**.

First:

```python
df["Age"] > 20
```

creates:

```text
0    False
1    True
2    True
3    False
4    True
5    True
```

Then:

```python
df.loc[df["Age"] > 20]
```

means:

> Give me rows where `Age` is greater than 20.

Result:

| index | Name | Age |
| ----: | ---- | --: |
|     1 | B    |  22 |
|     2 | C    |  25 |
|     4 | E    |  30 |
|     5 | F    |  24 |

---

### 🧠 Main difference

| Code                     | Meaning            | Selection based on  |
| ------------------------ | ------------------ | ------------------- |
| `df.iloc[0:5]`           | First 5 rows       | **Position**        |
| `df.loc[df["Age"] > 20]` | Age > 20 rows      | **Condition/label** |
| `df.iloc[2]`             | 3rd row            | Position            |
| `df.loc[2]`              | Row with index `2` | Index label         |

### Easy way to remember

```text
iloc → integer POSITION
loc  → LABEL / CONDITION
```

For example, if you want **rows 0–4** → `iloc`.

If you want **people whose Age > 20** → `loc`.
