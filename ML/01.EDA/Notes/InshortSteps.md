Yes. Here is a **short chart/roadmap** you can use for your ML notes.

### 📊 EDA → Data Cleaning → Data Preprocessing

| Step                            | Categorical Data                             | Continuous/Numerical Data                    |
| ------------------------------- | -------------------------------------------- | -------------------------------------------- |
| **1. Understand data**          | `df.info()`                                  | `df.info()`                                  |
| **2. Check unique values**      | `unique()`, `nunique()`                      | `describe()`                                 |
| **3. Missing values**           | `isna().sum()`                               | `isna().sum()`                               |
| **4. Duplicate values**         | `duplicated()`                               | `duplicated()`                               |
| **5. Distribution**             | `value_counts()`                             | `histplot()`, `boxplot()`                    |
| **6. Outliers**                 | Usually not applicable                       | `boxplot()`, IQR, Z-score                    |
| **7. Relationship with target** | `crosstab()`, `groupby()`                    | `corr()`, scatterplot                        |
| **8. Clean missing values**     | Mode / `"Unknown"`                           | Mean / Median                                |
| **9. Remove duplicates**        | `drop_duplicates()`                          | `drop_duplicates()`                          |
| **10. Handle outliers**         | Usually not needed                           | Remove / Cap / Transform                     |
| **11. Encoding**                | One-Hot / Label / Ordinal                    | ❌ Not needed                                 |
| **12. Scaling**                 | ❌ Usually after encoding, depending on model | StandardScaler / MinMaxScaler                |
| **13. Feature selection**       | Relevant encoded columns                     | Remove irrelevant/highly correlated features |
| **14. Train/Test split**        | `train_test_split()`                         | `train_test_split()`                         |

### 🔄 Simple flow

**Categorical:**

`EDA → Missing Values → Duplicates → Categories Check → Clean → Encoding → Feature Selection → Train/Test`

**Continuous:**

`EDA → Missing Values → Duplicates → Distribution → Outliers → Clean → Feature Engineering → Scaling → Feature Selection → Train/Test`

### ⭐ Remember

* **Categorical:** `Male/Female`, `Yes/No`, `City`, `Department`
* **Continuous:** `Age`, `Salary`, `Charges`, `Height`, `Weight`
* **Encoding:** converts categorical → numerical
* **Scaling:** brings numerical features to a comparable scale
* **Outlier handling:** mainly important for continuous numerical data
* **Target column:** analyze it separately because your preprocessing depends on whether the target is **classification or regression**.
