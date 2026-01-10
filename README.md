# ❤️ Cardiovascular Risk Assessment Using Statistical Analysis & Machine Learning

🚑 **An end-to-end Data Science project focused on early cardiovascular disease risk identification using statistical validation and supervised machine learning.**

---

## 📌 Overview
Cardiovascular disease is a leading cause of global mortality.  
This project applies **data science principles** to structured healthcare data to identify key risk factors and deliver **probability-based risk stratification** for decision support.

Key highlights:
- 📊 Statistical validation of risk factors  
- 🧠 Interpretable machine learning models  
- 🎯 Recall-focused evaluation for medical screening  
- 🌐 Deployment via Streamlit web application  

---

## ❓ Problem Statement
Early detection of cardiovascular risk enables preventive intervention and improved outcomes.  
The objective of this project is to:
- Analyze clinical and lifestyle data
- Validate predictors using statistical hypothesis testing
- Build predictive models with medical-context evaluation
- Translate predictions into actionable risk categories

---

## 🗂️ Dataset
- 📁 Structured healthcare dataset with **4,000+ patient records**
- 🎯 Target variable: `TenYearCHD` (10-year cardiovascular disease risk)
- 🧬 Features include demographics, medical history, and physiological measurements

Raw data is preserved and all preprocessing steps are fully reproducible.

---

## 📊 Exploratory Data Analysis (EDA)
Key insights from EDA:
- 📈 Age and systolic blood pressure strongly correlate with disease risk
- 🧪 Cholesterol shows higher variability among high-risk individuals
- 🚬 Lifestyle factors such as smoking contribute meaningfully
- 🔗 Multiple features exhibit moderate to strong correlation with the target

Detailed insights are available in:

1. reports/eda_insights.md

```
## 📐 Statistical Hypothesis Testing
To validate EDA findings, formal statistical tests were conducted:

- ✔ Two-sample **t-tests** for normally distributed variables
- ✔ **Mann–Whitney U tests** for non-parametric comparisons

Results confirm statistically significant differences in:
- Age
- Cholesterol
- Heart rate

```

2. reports/statistical_test_result.md

```
## 🧪 Feature Engineering
Feature engineering steps included:
- Handling missing values using median imputation
- Creating age-based buckets for non-linear risk capture
- Engineering interaction terms (e.g., age × cholesterol)
- Encoding categorical variables for modeling consistency
```

## 🤖 Modeling Approach

Supervised learning models trained and evaluated:
- Logistic Regression (interpretable baseline)
- Random Forest
- Gradient Boosting

### 📏 Evaluation Metrics
Given the medical screening context:
- 🔁 **Recall** was prioritized to minimize false negatives
- 📊 Precision, ROC-AUC, and confusion matrix were also used


## 🔍 Model Interpretability

- 📉 Logistic Regression coefficients analyzed for feature influence
- 🌳 Tree-based feature importance used to identify dominant predictors

Consistently strong indicators included age, blood pressure, cholesterol, and smoking-related features.


## 🧭 Risk Stratification

Predicted probabilities were converted into:
- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

This enables actionable decision support beyond raw probability scores.


## 🌐 Deployment

A Streamlit-based web application enables:
- User-friendly health input collection
- Real-time risk prediction
- Probability-based risk categorization

This bridges the gap between modeling and real-world usability.


## ⚠️ Limitations

- Dataset represents a specific population and may not generalize universally
- Intended for **educational and screening purposes only**
- Not a substitute for professional medical diagnosis


## 🚀 Future Enhancements

- Integrate SHAP for instance-level explainability
- Hyperparameter tuning with cross-validation
- Expand dataset diversity
- Add longitudinal risk tracking


## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn, SciPy**
- **Streamlit**


## 👤 Author

**Anubhab Pradhan**  
🔗 GitHub: https://github.com/ANUBprad

---

## ⚖️ Disclaimer
This project is for educational and analytical purposes only and does not constitute medical advice.

```
