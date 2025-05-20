#  Task 1: Load and Explore the Dataset
# Step 1: Load the dataset
import pandas as pd
import seaborn as sns

# Load the Iris dataset from seaborn
df = sns.load_dataset('iris')

# Display the first few rows
print(df.head())

# Step 2: Check Data Types and Missing Values
# Data types and non-null counts
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Step 3: Clean the Dataset
# In the Iris dataset, there are no missing values, but here's how you'd handle them
df_cleaned = df.dropna() 

# Confirm cleaning
print(df_cleaned.isnull().sum())

# Task 2: Basic Data Analysis
# Step 1: Basic Statistics
# Descriptive statistics
print(df_cleaned.describe())

# Step 2: Group by Species and Compute Mean
# Mean values grouped by species
grouped_means = df_cleaned.groupby('species').mean()
print(grouped_means)

# Task 3: Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')

# Bar Chart – Average petal length per species
# Bar chart
plt.figure(figsize=(8, 5))
sns.barplot(data=df_cleaned, x='species', y='petal_length')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()
