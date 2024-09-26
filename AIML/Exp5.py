import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the URL
url = 'https://github.com/AmritRajGarg/College_Notes/raw/main/AIML/data.csv'
data = pd.read_csv(url)

# Basic statistical summary
print("Summary Statistics:\n", data.describe())

# Visualizing missing data
plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Data Heatmap")
plt.show()

# Correlation heatmap for numerical columns
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# Pairplot for numerical variables (optional)
sns.pairplot(data.select_dtypes(include='number'))
plt.show()

# Value counts of a categorical column (replace 'gender' with your actual categorical column name)
print("Value Counts of Gender:\n", data['gender'].value_counts())
