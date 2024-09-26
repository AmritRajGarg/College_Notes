import pandas as pd

url = 'https://github.com/AmritRajGarg/College_Notes/raw/main/AIML/data.csv'
data = pd.read_csv(url)

data.to_csv('exported_data.csv', index=False)

# Display details of the dataset
print("Number of Rows:", data.shape[0])
print("Number of Columns:", data.shape[1])
print("First Five Rows:\n", data.head())
print("Size of Dataset:", data.size)

# Missing values in each column
print("Missing Values:\n", data.isnull().sum())

# Sum, average, minimum, and maximum values of numerical columns
numerical_data = data.select_dtypes(include='number')
print("Sum of Numerical Columns:\n", numerical_data.sum())
print("Average of Numerical Columns:\n", numerical_data.mean())
print("Minimum Values in Numerical Columns:\n", numerical_data.min())
print("Maximum Values in Numerical Columns:\n", numerical_data.max())
