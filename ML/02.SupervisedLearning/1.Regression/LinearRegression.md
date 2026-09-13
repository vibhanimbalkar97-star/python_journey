बिल्कुल। **Linear Regression के steps** beginner के लिए Hindi में इस तरह याद रखो:

# Linear Regression के Steps

### 1️⃣ Problem समझो

सबसे पहले तय करो कि **क्या predict करना है**।

Example:

> हमें `Salary` predict करनी है।

तो:

```text
Target (Y) = Salary
```

---

### 2️⃣ Target और Features अलग करो

```python
X = df.drop("Salary", axis=1)
y = df["Salary"]
```

* `X` → input/features
* `y` → target/output

---

### 3️⃣ EDA करो

Data को समझो:

```python
df.head()
df.info()
df.describe()
df.isna().sum()
df.duplicated().sum()
```

Check करो:

* Missing values हैं?
* Duplicate rows हैं?
* Data types सही हैं?
* Outliers हैं?
* X और Y के बीच relationship है?

---

### 4️⃣ Data Cleaning

अगर missing values हैं:

```python
df.dropna()
```

या appropriate value से fill करो:

```python
df["Age"].fillna(df["Age"].mean())
```

Duplicate rows:

```python
df.drop_duplicates()
```

---

### 5️⃣ Categorical Features को Encode करो

अगर X में categorical columns हैं:

```text
Gender → Male / Female
```

तो उन्हें numerical form में convert करना होगा।

आमतौर पर:

```python
pd.get_dummies()
```

या `OneHotEncoder` इस्तेमाल कर सकते हो।

⚠️ **Target numerical होना चाहिए** Linear Regression के लिए।

---

### 6️⃣ Train-Test Split

Data को training और testing में divide करो:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

आमतौर पर:

```text
80% → Training
20% → Testing
```

---

### 7️⃣ Linear Regression Model बनाओ

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
```

---

### 8️⃣ Model को Train करो

```python
model.fit(X_train, y_train)
```

`fit()` का मतलब:

> Model training data से **X और Y का relationship सीखता है।**

यहीं model अपने:

* **Coefficient**
* **Intercept**

सीखता है।

---

### 9️⃣ Prediction करो

```python
y_pred = model.predict(X_test)
```

मतलब:

> Test data के X values देखकर model ने Y की prediction की।

Example:

```text
Actual Salary    Predicted Salary
₹50,000          ₹48,500
₹60,000          ₹62,000
₹70,000          ₹68,000
```

---

### 🔟 Model को Evaluate करो

Regression में important metrics:

```python
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
```

#### MAE

Average error कितना है।

#### MSE

Errors का squared average।

#### RMSE

Error को target की same unit में बताता है।

#### R² Score

Model data को कितनी अच्छी तरह explain कर रहा है।

---

# पूरा Flow एक बार में 🧠

```text
Dataset
   ↓
Problem Understanding
   ↓
Target (Y) Identify
   ↓
Features (X) Identify
   ↓
EDA
   ↓
Data Cleaning
   ↓
Categorical X → Encoding
   ↓
Train-Test Split
   ↓
LinearRegression()
   ↓
fit()
   ↓
predict()
   ↓
MAE / MSE / RMSE / R²
   ↓
Model Evaluation
```

### सबसे important rule:

> **Linear Regression में Target (Y) numerical/continuous होना चाहिए।**

उदाहरण:

```text
Age + BMI + Smoking → Insurance Charges
                         ↑
                    Numerical Y
                         ↓
                Linear Regression ✅
```

तुम्हारे **HeartDisease dataset** में `HeartDisease` 0/1 categorical target है, इसलिए वहाँ **Logistic Regression / Classification** इस्तेमाल होगा, Linear Regression नहीं।
