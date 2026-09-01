Super-short cheat sheet

When solving Bayes questions:

1. What am I asked to FIND?
        ↓
   P(A | B)

2. What is A?
   → Thing I want to know

3. What is B?
   → Evidence I already know

4. Find:
   P(A)
   P(B | A)
   P(B)

5. Apply:
   P(A | B) = P(B | A) × P(A) / P(B)

   ============================================================================
   Sure. Let's use a **simple shopping/product example** instead of a health example.

# Bayes' Theorem — Beginner Example

Imagine an online store has **two warehouses**:

* Warehouse A
* Warehouse B

A package is selected randomly, and we find that the package is **damaged**.

We want to know:

> **What is the probability that the damaged package came from Warehouse A?**

This is a perfect Bayes example.

---

## 1. First understand what we're trying to FIND

Question:

> Package is damaged. What is the probability it came from Warehouse A?

So:

* **A = Package came from Warehouse A**
* **B = Package is damaged**

We want:

$$
P(A|B)
$$

In words:

> Probability of **Warehouse A**, given that the package is **damaged**.

---

## 2. Suppose we are given these values

Let's say:

* 60% of packages come from Warehouse A.
* 40% of packages come from Warehouse B.
* 5% of A's packages are damaged.
* 10% of B's packages are damaged.

Convert them into probability notation.

### Given 1

> 60% packages come from A.

$$
P(A)=0.60
$$

### Given 2

> 40% packages come from B.

$$
P(B\text{ warehouse})=0.40
$$

Since there are only two warehouses:

$$
P(\text{Not A})=0.40
$$

### Given 3

> 5% of A's packages are damaged.

$$
P(D|A)=0.05
$$

Meaning:

> Probability of **damaged**, given package came from A.

### Given 4

> 10% of B's packages are damaged.

$$
P(D|\text{Not A})=0.10
$$

---

# 3. What exactly do we want?

The question says:

> Package is **damaged**. What is the probability it came from **A**?

So:

$$
\boxed{P(A|D)}
$$

This is what we need to find.

Notice:

### Given:

$$
P(D|A)=0.05
$$

### Want:

$$
P(A|D)
$$

The direction has changed!

That's where **Bayes' theorem** comes in.

---

# 4. Bayes formula

$$
P(A|D)=\frac{P(D|A)\times P(A)}{P(D)}
$$

We already know:

$$
P(D|A)=0.05
$$

and

$$
P(A)=0.60
$$

But we don't know:

$$
P(D)
$$

So first we need to calculate it.

---

# 5. How do we find P(D)?

A package can be damaged in **two ways**:

### Case 1: It came from A and is damaged

$$
P(D|A)\times P(A)
$$

$$
=0.05\times0.60
$$

$$
=0.03
$$

---

### Case 2: It came from B and is damaged

$$
P(D|\text{Not A})\times P(\text{Not A})
$$

$$
=0.10\times0.40
$$

$$
=0.04
$$

Therefore:

$$
P(D)=0.03+0.04
$$

$$
P(D)=0.07
$$

---

# 6. Now use Bayes

We want:

$$
P(A|D)
$$

So:

$$
P(A|D)=
\frac{P(D|A)\times P(A)}
{P(D)}
$$

Put the values:

$$
P(A|D)=
\frac{0.05\times0.60}{0.07}
$$

$$
=\frac{0.03}{0.07}
$$

$$
=0.4286
$$

Convert to percentage:

$$
\boxed{42.86\%}
$$

So:

> If we know a package is damaged, there is about a **42.86% chance that it came from Warehouse A**.

---

# 7. Now understand the important part

Don't just memorize the formula. Understand **where each value comes from**.

| Symbol    | In our example | Meaning                         |
| --------- | -------------- | ------------------------------- |
| `A`       | Warehouse A    | Thing we're interested in       |
| `D`       | Damaged        | Evidence we know                |
| `P(A)`    | 0.60           | Probability package came from A |
| `P(D\|A)` | 0.05           | Damage probability if from A    |
| `P(A\|D)` | **?**          | What we're trying to find       |
| `P(D)`    | 0.07           | Overall probability of damage   |

---

# 8. The easiest way to identify A and B

Whenever you see a Bayes question, **don't immediately look at the formula.**

First ask:

### Question 1:

> **What am I being asked to find?**

Whatever comes **before the `given`** is A.

Whatever comes **after the `given`** is B.

For example:

> What is the probability that the package came from **A given that it is damaged**?

Break it:

```text
A given B

A = package came from A
B = package is damaged
```

Therefore:

$$
\boxed{P(A|B)}
$$

---

# 9. Another example

Suppose a college has:

* 70% students studying Computer Science
* 30% students studying Commerce
* 20% CS students play cricket
* 40% Commerce students play cricket

Question:

> A student is selected and we know that the student plays cricket. What is the probability that the student is from CS?

### Step 1 — What are we finding?

We want:

> CS given Cricket

Therefore:

$$
P(CS|Cricket)
$$

### Step 2 — Given values

$$
P(CS)=0.70
$$

$$
P(Cricket|CS)=0.20
$$

$$
P(Not\ CS)=0.30
$$

$$
P(Cricket|Not\ CS)=0.40
$$

### Step 3 — Find overall cricket probability

$$
P(Cricket)
=
(0.20)(0.70)+(0.40)(0.30)
$$

$$
=0.14+0.12
$$

$$
=0.26
$$

### Step 4 — Bayes

$$
P(CS|Cricket)
=
\frac{(0.20)(0.70)}{0.26}
$$

$$
=\frac{0.14}{0.26}
$$

$$
=\boxed{53.85\%}
$$

---

# 10. Remember this pattern

Most beginner Bayes questions follow this pattern:

```text
There are groups/categories
        ↓
You know the probability of each group
        ↓
You get some evidence
        ↓
Question asks:
"Given this evidence, which group is likely?"
        ↓
Use Bayes
```

### Formula to remember:

$$
\boxed{
P(A|B)=\frac{P(B|A)\times P(A)}{P(B)}
}
$$

And the most important distinction:

```text
P(A | B) → WHAT WE WANT TO FIND

P(B | A) → Usually GIVEN in the question
```

### Simple memory trick:

> **Want = A given B**
> **Given = B given A**

Once you can identify **"what I want"** and **"what evidence I have"**, Bayes questions become much easier.
===============================================================================================================
Yes — **this is the most important part of Bayes' theorem**. Let's forget the formula for a moment and understand only:

$$
P(A|B)
$$

using the **warehouse example**.

---

# 1. Our warehouse example

We have:

* **A = Package came from Warehouse A**
* **B = Package is damaged**

Now imagine I give you this information:

> 📦 "I know that this package is damaged."

And then I ask:

> **What is the probability that it came from Warehouse A?**

Think about the direction of the question:

```text
We KNOW → Package is damaged
             ↓
We WANT → Where did it come from?
             ↓
          Warehouse A?
```

So we write:

$$
\boxed{P(A|B)}
$$

---

# 2. What does `P(A|B)` literally mean?

The `|` symbol means:

> **given that**

Therefore:

$$
P(A|B)
$$

means:

> **Probability of A, given B**

In our example:

$$
P(A|B)
$$

means:

> **Probability that the package came from Warehouse A, given that we know it is damaged.**

That's exactly what the question asks.

---

# 3. Then what is `P(B|A)`?

Now reverse it:

$$
P(B|A)
$$

means:

> **Probability of B, given A**

In our example:

> Probability that the package is damaged, **given that we know it came from Warehouse A**.

That's a completely different question.

---

# 4. Compare them directly

| Probability | Meaning                                               |
| ----------- | ----------------------------------------------------- |
| `P(A \| B)` | Package came from **A**, given that it is **damaged** |
| `P(B \| A)` | Package is **damaged**, given that it came from **A** |

Notice the difference:

### `P(A|B)`

```text
KNOW → Damaged
ASK  → Warehouse A?
```

### `P(B|A)`

```text
KNOW → Warehouse A
ASK  → Damaged?
```

They are asking **opposite questions**.

---

# 5. Let's use actual numbers

Our example:

* 60% packages come from A
* 5% of A's packages are damaged

So:

$$
P(A)=60\%
$$

and

$$
P(B|A)=5\%
$$

What does this 5% mean?

### `P(B|A) = 5%`

> **If I already know a package came from A, there is a 5% chance that it is damaged.**

Imagine 1000 packages from A:

```text
1000 packages from A
        ↓
    5% damaged
        ↓
50 damaged packages
```

So:

$$
P(B|A)=\frac{50}{1000}=5\%
$$

---

# 6. But the question is different

The question says:

> "I found a **damaged package**. What is the probability it came from A?"

Now our starting point is different.

We already know:

```text
Package → DAMAGED
```

And we want to figure out:

```text
Where did it come from?
       ↓
   Warehouse A?
```

Therefore:

$$
\boxed{P(A|B)}
$$

---

# 7. Very simple real-life analogy

Imagine two boxes:

```text
Box A → 60% of products
Box B → 40% of products
```

You randomly pick one product.

You look at it and discover:

> 🔴 "This product is damaged."

Now you ask:

> "What is the probability that this product came from Box A?"

You're starting with:

**Damaged**

and trying to find:

**A**

Therefore:

$$
\boxed{P(A|B)}
$$

---

# 8. Why can't we use `P(B|A)`?

Because `P(B|A)` answers:

> "If I know it came from A, what's the chance it's damaged?"

But our question is:

> "I know it's damaged. What's the chance it came from A?"

These are different.

Think of it like:

### Question 1

> "If someone is a **student**, what is the probability they have a **laptop**?"

$$
P(Laptop|Student)
$$

### Question 2

> "If someone has a **laptop**, what is the probability they are a **student**?"

$$
P(Student|Laptop)
$$

Obviously, these don't necessarily have the same answer.

---

# 9. The easiest trick to identify it

Whenever you see:

> **"What is the probability of X given Y?"**

write:

$$
\boxed{P(X|Y)}
$$

The thing **after "given" goes on the right side**.

### Example:

> Probability package came from A **given that** it is damaged.

```text
Probability of A
        ↓
P(A | B)
     ↑
 "given damaged"
```

So:

$$
\boxed{P(A|B)}
$$

---

# 10. Why Bayes is needed

Here's the interesting part.

In our example, we **know**:

$$
P(B|A)=5\%
$$

But we **want**:

$$
P(A|B)
$$

So:

```text
We KNOW                         We WANT

P(B | A)  ─────── Bayes ───────→  P(A | B)
Damage given A                   A given Damage
```

**Bayes' theorem is basically a way to reverse conditional probability.**

That's why the formula contains:

$$
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
$$

### Remember just this:

> **`P(A|B)` = What I WANT to know, after knowing B.**

> **`P(B|A)` = What I know about B when A is already known.**

Once this distinction is clear, the rest of Bayes becomes much easier.
