import pandas as pd
import numpy as np

# Load the dataset
url = "https://github.com/AmritRajGarg/College_Notes/raw/main/AIML/data.csv"
data = pd.read_csv(url)

# Explore the data
print("Data head:")
print(data.head())  # Display the first few rows
print("Data info:")
print(data.info())  # Get information about data types and missing values

# Handle missing values
# For numeric columns, impute with the median due to potential outliers
numeric_cols = data.select_dtypes(include=np.number).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())

# For categorical columns, impute with the mode
categorical_cols = data.select_dtypes(include=object).columns
data[categorical_cols] = data[categorical_cols].fillna(data[categorical_cols].mode().iloc[0])

# Handle outliers using IQR (Interquartile Range)
def handle_outliers(column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)
    data.loc[(data[column] < lower_bound) | (data[column] > upper_bound), column] = np.nan
    data[column] = data[column].fillna(data[column].median())

# Apply outlier handling to numeric columns
for col in numeric_cols:
    handle_outliers(col)

# Explore the data after preprocessing
print("Data head after preprocessing:")
print(data.head())
print("Data info after preprocessing:")
print(data.info())
