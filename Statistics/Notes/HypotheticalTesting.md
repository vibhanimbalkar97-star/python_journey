### Hypothesis Testing — Simple Explanation

**Hypothesis testing** is used to decide whether a claim about data is **likely true or just happened by chance**.

### Why do we use it?

Suppose a company says:

> "Our new website feature increases the average purchase amount."

We collect data before and after the feature.

Hypothesis testing helps us answer:

> **Is the increase actually significant, or could it simply be random variation?**

---

### Basic idea

We create two hypotheses:

| Hypothesis                      | Meaning                                |
| ------------------------------- | -------------------------------------- |
| **H₀ (Null Hypothesis)**        | Nothing changed / no effect            |
| **H₁ (Alternative Hypothesis)** | Something changed / there is an effect |

Example:

**Claim:** New website design increases sales.

```text
H₀: New design does NOT increase sales
H₁: New design DOES increase sales
```

Then we use the data to decide whether there is enough evidence to **reject H₀**.

---

### Where is it used?

| Use case            | Question                               |
| ------------------- | -------------------------------------- |
| 🛒 A/B Testing      | Does new UI increase purchases?        |
| 💊 Medicine         | Does a new medicine work better?       |
| 🤖 Machine Learning | Is a model improvement significant?    |
| 🏭 Manufacturing    | Did the new process reduce defects?    |
| 📊 Business         | Did a new strategy increase revenue?   |
| 🌐 Website          | Does a new feature improve conversion? |

### Simple real-world example

You have two buttons:

**A:** "Buy Now"
**B:** "Get Started"

You show A to 5,000 users and B to 5,000 users.

```text
A → 400 purchases
B → 450 purchases
```

B looks better.

But the question is:

> **Is B genuinely better, or did B just get lucky with this sample?**

That's where **hypothesis testing** is used.

You will commonly encounter:

**Hypothesis → Test statistic → p-value → Decision**

The most important thing to understand next is **p-value**, because it tells us whether the observed result provides enough evidence against H₀.
==============================================================================================================================================

Sure. After understanding the basic idea, these are the **remaining important parts of hypothesis testing**, explained simply.

### 1. Null Hypothesis (H₀)

It represents **no change, no difference, or no effect**.

Example:

> New website design does not increase sales.

```text
H₀: New design = Old design
```

---

### 2. Alternative Hypothesis (H₁ / Ha)

It represents **a change, difference, or effect**.

```text
H₁: New design ≠ Old design
```

It can also be directional:

```text
H₁: New design > Old design
```

or

```text
H₁: New design < Old design
```

---

### 3. Significance Level (α)

This is the **threshold we choose before testing**.

Most commonly:

```text
α = 0.05
```

Meaning:

> We accept a **5% risk of rejecting H₀ when H₀ is actually true**.

Think of `0.05` as our **decision boundary**.

---

### 4. p-value ⭐⭐⭐

This is one of the most important concepts.

The p-value tells us:

> **If H₀ were true, how surprising is our observed result?**

Decision rule:

| p-value      | Decision            |
| ------------ | ------------------- |
| **p ≤ 0.05** | Reject H₀ ❌         |
| **p > 0.05** | Fail to reject H₀ ✅ |

Example:

```text
p-value = 0.02
α = 0.05
```

Since:

```text
0.02 < 0.05
```

➡️ **Reject H₀**

There is statistically significant evidence of an effect.

---

### 5. Test Statistic

We calculate a value from our sample data to measure **how far our result is from what H₀ expects**.

Examples:

* **Z-score** → Z-test
* **t-score** → t-test
* **χ²** → Chi-square test
* **F-statistic** → ANOVA

You don't need to memorize formulas initially. Understand **what they measure**.

---

### 6. Critical Value

Another way to make the decision is using a **critical value**.

For example:

```text
Calculated value > Critical value
        ↓
Reject H₀
```

So there are two common approaches:

**p-value approach:**

```text
p-value ≤ α → Reject H₀
```

**Critical-value approach:**

```text
Test statistic falls in rejection region → Reject H₀
```

---

### 7. One-tailed vs Two-tailed Test

#### One-tailed

You care about a **specific direction**.

Example:

> Does the new design increase sales?

```text
H₁: New design > Old design
```

#### Two-tailed

You only care whether there is **any difference**.

```text
H₁: New design ≠ Old design
```

Example:

> Does the new design change sales?

It could increase **or** decrease sales.

---

### 8. Type I Error

You reject H₀ even though H₀ is actually true.

```text
H₀ is TRUE
     ↓
You reject H₀
     ↓
Type I Error ❌
```

Simple example:

> You conclude the new medicine works, but actually it doesn't.

Also called a **false positive**.

---

### 9. Type II Error

You fail to reject H₀ even though H₀ is actually false.

```text
H₀ is FALSE
     ↓
You fail to reject H₀
     ↓
Type II Error ❌
```

Example:

> You conclude the new medicine has no effect, but actually it works.

Also called a **false negative**.

---

### 10. Statistical Significance

If:

```text
p-value ≤ 0.05
```

we generally say the result is **statistically significant**.

But remember:

> **Statistically significant ≠ practically important**

Example:

A new website increases conversion from:

```text
10.00% → 10.01%
```

It might be statistically significant with a huge dataset, but the actual business improvement is tiny.

---

## 11. Confidence Interval

A confidence interval gives us a **range of plausible values** for a population parameter.

Example:

```text
Average improvement = 5%
95% CI = [3%, 7%]
```

Meaning roughly:

> Based on the sample and method, the plausible population improvement is around **3%–7%**.

---

## 12. Common Hypothesis Tests

| Test                  | Common use                                              |
| --------------------- | ------------------------------------------------------- |
| **Z-test**            | Compare mean when conditions for z-test are appropriate |
| **t-test** ⭐          | Compare means, especially with smaller samples          |
| **Chi-square test** ⭐ | Test relationship between categorical variables         |
| **ANOVA** ⭐           | Compare means of 3+ groups                              |
| **Correlation test**  | Test whether variables are associated                   |
| **Proportion test**   | Compare proportions/conversion rates                    |

---

## Complete flow ⭐⭐⭐

This is the most important thing to remember:

```text
1. Define problem
       ↓
2. Set H₀ and H₁
       ↓
3. Choose significance level α
       ↓
4. Collect sample data
       ↓
5. Choose appropriate statistical test
       ↓
6. Calculate test statistic
       ↓
7. Calculate p-value
       ↓
8. Compare p-value with α
       ↓
9. Reject H₀ OR Fail to reject H₀
       ↓
10. Give conclusion in real-world terms
```

### One complete example

**Question:** Does a new UI increase conversion?

```text
H₀: New UI does not increase conversion
H₁: New UI increases conversion

α = 0.05

p-value = 0.01
```

Compare:

```text
0.01 < 0.05
```

Therefore:

```text
Reject H₀
```

Conclusion:

> There is statistically significant evidence that the new UI increases conversion.

### 🎯 For your ML/Data Science preparation

Focus strongly on:

**H₀/H₁ → α → p-value → test statistic → one/two-tailed → Type I/II errors → confidence interval → t-test → chi-square → ANOVA**

You don't need to go deeply into the mathematical proofs initially.
