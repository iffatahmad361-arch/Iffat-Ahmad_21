import pandas as pd
import numpy as np
df = pd.read_csv("India_AQI_500_City_Filled_Readings_18_Nov_2026.csv")
print(df.head())

# Display all column names
print(df.columns)

# Check the number of rows and columns
print(df.shape)

# Check dataset information
print(df.info())

# Check statistical summary
print(df.describe())
# Check missing values
print(df.isnull().sum())

# Check duplicate rows
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Check missing values again
print(df.isnull().sum())# Check missing values
print(df.isnull().sum())

# Check duplicate rows
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Check missing values again
print(df.isnull().sum())
print(df.columns)
print(df.shape)
print(df.info())
print(df.head(10))
# Data Visualization

import matplotlib.pyplot as plt
import seaborn as sns

# Check column names
print(df.columns)
# DATA VISUALIZATION

import matplotlib.pyplot as plt
import seaborn as sns

# Convert US AQI into numeric values
df['US AQI'] = pd.to_numeric(df['US AQI'], errors='coerce')

# 1. Histogram of US AQI
plt.figure(figsize=(10, 5))
plt.hist(df['US AQI'].dropna(), bins=20, edgecolor='black')
plt.title('Distribution of US AQI')
plt.xlabel('US AQI Value')
plt.ylabel('Number of Cities')
plt.show()


# 2. Top 10 Cities by US AQI
top_cities = df.nlargest(10, 'US AQI')

plt.figure(figsize=(12, 6))
sns.barplot(data=top_cities, x='City', y='US AQI')
plt.title('Top 10 Cities with Highest US AQI')
plt.xlabel('City')
plt.ylabel('US AQI')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 3. AQI by Source Category
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Source category')
plt.title('Readings by Source Category')
plt.xlabel('Source Category')
plt.ylabel('Number of Readings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# EXPLORATORY DATA ANALYSIS (EDA)

# Convert AQI into numeric format
df['US AQI'] = pd.to_numeric(df['US AQI'], errors='coerce')

# 1. Average AQI
print("Average AQI:", df['US AQI'].mean())

# 2. Highest AQI
print("Highest AQI:", df['US AQI'].max())

# 3. Lowest AQI
print("Lowest AQI:", df['US AQI'].min())

# 4. Median AQI
print("Median AQI:", df['US AQI'].median())

# 5. City with highest AQI
highest_city = df.loc[df['US AQI'].idxmax()]
print("Most polluted city:", highest_city['City'])
print("Highest AQI value:", highest_city['US AQI'])

# 6. City with lowest AQI
lowest_city = df.loc[df['US AQI'].idxmin()]
print("Least polluted city:", lowest_city['City'])
print("Lowest AQI value:", lowest_city['US AQI'])

# 7. Top 10 polluted cities
print("\nTop 10 polluted cities:")
print(df.nlargest(10, 'US AQI')[['City', 'US AQI']])

# 8. Bottom 10 polluted cities
print("\nBottom 10 polluted cities:")
print(df.nsmallest(10, 'US AQI')[['City', 'US AQI']])
# GRAPH 2: TOP 10 POLLUTED CITIES

top_cities = df.nlargest(10, 'US AQI')

plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_cities,
    x='City',
    y='US AQI'
)

plt.title('Top 10 Cities with Highest AQI')
plt.xlabel('City')
plt.ylabel('US AQI')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('aqi_graph.png')
plt.show()
# GRAPH 3: LEAST POLLUTED CITIES

bottom_cities = df.nsmallest(10, 'US AQI')

plt.figure(figsize=(12, 6))

sns.barplot(
    data=bottom_cities,
    x='City',
    y='US AQI'
)

plt.title('Top 10 Cities with Lowest AQI')
plt.xlabel('City')
plt.ylabel('US AQI')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('aqi_graph.png')
plt.show()# GRAPH 3: LEAST POLLUTED CITIES

bottom_cities = df.nsmallest(10, 'US AQI')

plt.figure(figsize=(12, 6))

sns.barplot(
    data=bottom_cities,
    x='City',
    y='US AQI'
)

plt.title('Top 10 Cities with Lowest AQI')
plt.xlabel('City')
plt.ylabel('US AQI')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('aqi_graph.png')
plt.show()
# STATE-WISE AQI ANALYSIS

state_aqi = df.groupby(
    'State/UT (as reported)'
)['US AQI'].mean().sort_values(ascending=False)

print("\n===== STATE-WISE AVERAGE AQI =====")
print(state_aqi.round(2))
# GRAPH 4: STATE-WISE AQI

plt.figure(figsize=(14, 7))

state_aqi.head(10).plot(kind='bar')

plt.title('Top 10 States with Highest Average AQI')
plt.xlabel('State / UT')
plt.ylabel('Average US AQI')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('graph4_statewise_aqi.png')
plt.show()
print("State-wise analysis completed!")
print(state_aqi.head(10))
# GRAPH: LINE GRAPH - TOP 10 MOST POLLUTED CITIES

top_cities = df.nlargest(10, 'US AQI').sort_values('US AQI')

plt.figure(figsize=(12, 6))

plt.plot(
    top_cities['City'],
    top_cities['US AQI'],
    marker='o',
    linestyle='-',
    linewidth=2
)

plt.title('Top 10 Most Polluted Cities in India - AQI')
plt.xlabel('City')
plt.ylabel('US AQI')

plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('aqi_line_graph.png', dpi=300)
plt.show()