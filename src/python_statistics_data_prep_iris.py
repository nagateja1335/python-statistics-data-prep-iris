"""
Minor Project
Python, Statistics & Data Preparation Walkthrough
Using Iris Dataset

This script demonstrates:

• Data Loading
• OOPS Implementation
• Decision Making
• Descriptive Statistics
• Visualization
• T-Test
• Chi-Square Test
"""

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy import stats

# Load Dataset
print("\nLoading Iris Dataset...\n")

iris = load_iris()

# Convert to DataFrame
df = pd.DataFrame(
    data=iris.data,
    columns=iris.feature_names
)

# Add species column
df['species'] = iris.target

# Map numeric labels to names
df['species'] = df['species'].map({
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
})

print("First 5 Rows:\n")
print(df.head())

# OOPS Implementation
class DataAnalyzer:
    
    def __init__(self, dataframe):
        self.data = dataframe
    
    # Method: Descriptive Statistics
    def get_descriptive_stats(self):
        print("\nDescriptive Statistics:\n")
        print(self.data.describe())


# Create object
analyzer = DataAnalyzer(df)
analyzer.get_descriptive_stats()

# Decision Making
print("\nCategorizing Petal Length...\n")

def categorize_petal_length(length):
    
    if length < 2:
        return "Small"
    
    elif 2 <= length < 5:
        return "Medium"
    
    else:
        return "Large"


# Apply categorization
df['petal_length_category'] = df['petal length (cm)'].apply(
    categorize_petal_length
)

print(df[['petal length (cm)', 'petal_length_category']].head())

# Manual Mean & Median
print("\nManual Statistical Calculations...\n")

mean_manual = sum(df['sepal length (cm)']) / len(df)
median_manual = np.median(df['sepal length (cm)'])

print("Manual Mean:", mean_manual)
print("Manual Median:", median_manual)

print("\nPandas Mean:", df['sepal length (cm)'].mean())
print("Pandas Median:", df['sepal length (cm)'].median())

# Visualization
print("\nDisplaying Histogram...\n")

plt.figure(figsize=(8,5))

plt.hist(df['petal width (cm)'], bins=20)

plt.title("Histogram of Petal Width")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")

plt.show()

# T-Test
print("\nT-Test Analysis...\n")

setosa = df[df['species'] == 'setosa']['sepal length (cm)']
versicolor = df[df['species'] == 'versicolor']['sepal length (cm)']

print("Setosa Mean:", setosa.mean())
print("Versicolor Mean:", versicolor.mean())

t_stat, p_value = stats.ttest_ind(setosa, versicolor)

print("\nT-Statistic:", t_stat)
print("P-Value:", p_value)

# Chi-Square Test
print("\nChi-Square Test Preparation...\n")

df['sepal_length_category'] = pd.cut(
    df['sepal length (cm)'],
    bins=[0, 5.5, 10],
    labels=['Short', 'Tall']
)

# Contingency Table
contingency_table = pd.crosstab(
    df['sepal_length_category'],
    df['species']
)

print("\nContingency Table:\n")
print(contingency_table)

# Chi-Square Test
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

print("\nChi-Square Value:", chi2)
print("P-Value:", p)
print("Degrees of Freedom:", dof)

# Coclusion
print("\nProject Completed Successfully!")