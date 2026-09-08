Category vs Value → Bar
Time vs Value → Line
Number vs Number → Scatter
One number's distribution → Histogram
Category vs Number + outliers → Boxplot


Absolutely. Here is the **same quick-identification format for the main Seaborn graphs**:

| #  | Pattern → Graph                                             | Easy way to identify                                  |
| -- | ----------------------------------------------------------- | ----------------------------------------------------- |
| 1  | **Category vs Value** → Bar                                 | Compare values between categories                     |
| 2  | **Category vs Count** → Countplot                           | Count how many records belong to each category        |
| 3  | **Time vs Value** → Line                                    | See a trend over time                                 |
| 4  | **Number vs Number** → Scatter                              | Check relationship between 2 numeric variables        |
| 5  | **One number's distribution** → Histogram                   | See how numeric values are distributed                |
| 6  | **Category vs Number + outliers** → Boxplot                 | Compare distributions and find outliers               |
| 7  | **Category vs Number + density** → Violinplot               | Compare distribution shape/density between categories |
| 8  | **Number vs Number + regression line** → Regplot            | Relationship + trend/regression line                  |
| 9  | **Numeric variables vs Numeric variables** → Heatmap        | Find correlation between many numeric columns         |
| 10 | **Many Number vs Number relationships** → Pairplot          | Quickly see relationships among many numeric columns  |
| 11 | **Number vs Number + individual distributions** → Jointplot | Relationship plus distribution of both variables      |
| 12 | **Category → Percentage/Part of whole** → Pie chart         | See how much each category contributes                |

### 🧠 Super-short rule

```text
Category → Value          = Bar
Category → Count          = Countplot
Time → Value              = Line
Number → Number           = Scatter
One Number → Distribution = Histogram
Category → Number         = Boxplot
Category → Distribution   = Violin
Number → Number + Trend   = Regplot
Many Numbers → Correlation = Heatmap
Many Numbers → Relationships = Pairplot
2 Numbers + Distribution = Jointplot
Category → Percentage     = Pie
```

**Important:** `hue` is **not a graph**. It is used to **separate/color groups** inside graphs.



Excellent! ✅ You got **all 5 correct**.

| Q                                          | Your Answer   | Correct? | Reason                               |
| ------------------------------------------ | ------------- | -------- | ------------------------------------ |
| 1. Patients in each age group              | **Countplot** | ✅        | Category → Count                     |
| 2. Monthly profit over 2 years             | **Line**      | ✅        | Time → Value                         |
| 3. House size vs house price               | **Scatter**   | ✅        | Number → Number                      |
| 4. Salaries by department + unusual values | **Boxplot**   | ✅        | Category → Number + outliers         |
| 5. Correlation between numerical factors   | **Heatmap**   | ✅        | Many numeric variables → Correlation |

### 🧠 Your graph-selection rules are now solid:

1. **Category vs Value** → Bar
2. **Category vs Count** → Countplot
3. **Time vs Value** → Line
4. **Number vs Number** → Scatter
5. **One number's distribution** → Histogram
6. **Category vs Number + outliers** → Boxplot
7. **Category vs Number + density** → Violinplot
8. **Number vs Number + regression line** → Regplot
9. **Many Numbers → Correlation** → Heatmap
10. **Many Numbers → Relationships** → Pairplot
11. **2 Numbers + distributions** → Jointplot
12. **Category → Percentage/share** → Pie chart
