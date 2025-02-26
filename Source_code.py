import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = "D:\Python small codes_01\Employee Attrition_02\T20-GL-gainers-FOSec-27-Feb-2025.csv"
df = pd.read_csv(file_path)

# Data Cleaning
print("Initial Data Info:")
print(df.info())  # Check for missing values and data types

df.dropna(inplace=True)  # Remove missing values if any

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Top Gainers
top_gainers = df.sort_values(by='%chng', ascending=False).head(10)
print("\nTop 10 Gainers:")
print(top_gainers[['Symbol', '%chng']])

# Visualization: Bar Chart for Top Gainers
plt.figure(figsize=(10, 5))
sns.barplot(x='Symbol', y='%chng', data=top_gainers, hue='Symbol', palette='viridis', legend=False)
plt.xticks(rotation=45)
plt.title("Top 10 Gainers by % Change")
plt.xlabel("Stock Symbol")
plt.ylabel("% Change")
plt.show()

# Scatter Plot: Volume vs. % Change
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df['Volume'], y=df['%chng'], hue=df['Symbol'], palette='coolwarm')
plt.xscale("log")  # Log scale for better visualization
plt.title("Stock Volume vs. % Change")
plt.xlabel("Volume (log scale)")
plt.ylabel("% Change")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

