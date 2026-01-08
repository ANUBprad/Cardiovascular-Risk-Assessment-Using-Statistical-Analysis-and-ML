# Statistical Hypothesis Testing Results

To validate insights obtained during exploratory analysis, statistical hypothesis testing was performed to determine whether key features differ significantly between diseased and non-diseased populations.

---

## Test 1: Age

**Null Hypothesis (H₀):**  
Mean age is the same for individuals with and without cardiovascular disease.

**Test Used:**  
Two-sample t-test

**Result:**  
- p-value < 0.05

**Conclusion:**  
The null hypothesis is rejected. Age differs significantly between the two groups, confirming age as a statistically significant risk factor.

---

## Test 2: Total Cholesterol

**Null Hypothesis (H₀):**  
Cholesterol levels do not differ between diseased and non-diseased individuals.

**Test Used:**  
Mann–Whitney U test (non-parametric)

**Result:**  
- p-value < 0.05

**Conclusion:**  
Cholesterol levels are significantly different across groups, supporting its clinical relevance in cardiovascular risk assessment.

---

## Test 3: Heart Rate

**Null Hypothesis (H₀):**  
Mean heart rate is equal across diseased and non-diseased populations.

**Test Used:**  
Two-sample t-test

**Result:**  
- p-value < 0.05

**Conclusion:**  
Heart rate differs significantly between the two populations, indicating its role as a contributing physiological factor.

---

## Overall Interpretation
Statistical testing confirmed that age, cholesterol, and heart rate are not only correlated with cardiovascular disease but are also statistically significant predictors. These findings justify their inclusion in downstream feature engineering and modeling steps.
