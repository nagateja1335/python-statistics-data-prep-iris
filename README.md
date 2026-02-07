#  Python, Statistics & Data Preparation Walkthrough

### Minor Project — Iris Dataset Analysis

---

##  Project Description

This project demonstrates foundational skills in **Python programming, statistical analysis, and data preparation** using the well-known Iris dataset.

It provides a structured walkthrough of essential data analysis steps including data loading, preprocessing, descriptive statistics, visualization, and introductory inferential statistical techniques.

The objective is to build a strong base for advanced domains such as **Data Science, Machine Learning, and Artificial Intelligence**.

---

##  Project Objectives

* Load and structure dataset using Pandas
* Apply Object-Oriented Programming (OOPS) concepts
* Implement decision-making logic using conditional statements
* Perform descriptive statistical analysis
* Visualize feature distributions
* Prepare data for inferential statistics
* Conduct T-Test and Chi-Square analysis

---

##  Dataset Information

The **Iris dataset** is a classic dataset in statistics and machine learning containing flower measurements from three species:

* Setosa
* Versicolor
* Virginica

### Features Included:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Dataset Source: `sklearn.datasets`

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SciPy
* Scikit-learn
* Jupyter Notebook / VS Code

---

##  Project Structure

```
python-statistics-data-prep-iris/
│
├── notebook/
│   └── python_statistics_data_prep_iris.ipynb
│
├── src/
│   └── python_statistics_data_prep_iris.py
│
├── README.md
└── LICENSE
```

---

##  Key Implementations

###  Object-Oriented Programming

A custom class `DataAnalyzer` is implemented to:

* Load dataset
* Generate descriptive statistics

---

###  Decision Making Logic

Petal length values are categorized into:

* Small
* Medium
* Large

Using `if-elif-else` conditional statements.

---

###  Descriptive Statistics

Performed statistical summaries including:

* Mean
* Median
* Standard Deviation
* Minimum & Maximum values

Manual calculations were also verified using Pandas functions.

---

##  Data Visualization

Histogram plotted to analyze distribution of:

* Petal Width

Visualization helps in understanding spread and frequency of feature values.

---

##  Inferential Statistics

### T-Test

Compared mean Sepal Length between:

* Setosa
* Versicolor

**Hypothesis:**

* H₀: No significant difference in means
* H₁: Significant difference exists

---

### Chi-Square Test

Steps performed:

* Converted Sepal Length into categorical groups
* Created contingency table
* Applied Chi-Square test to study association with species


##  License

This project is licensed under the **MIT License**.

## If you found this project useful, consider giving it a star!
