import pandas as pd
import numpy as np

# File path apne PC ke hisaab se daalo
file_path = r"C:\Users\webexert\Desktop\zomato.csv"

# CSV file load karo
df = pd.read_csv(file_path)

# Top 5 rows dekho
print("\nTop 5 Rows:")
print(df.head())

# Shape dekho
print("\nShape of dataset:", df.shape)

# Columns dekho
print("\nColumns:")
print(df.columns)

# Data types dekho
print("\nData types:")
print(df.dtypes)

#missing values
print(df.isnull().sum())

#Null remove
df = df[~df['rate'].isnull()]
print("New shape after removing null rates:", df.shape)

import pandas as pd
import numpy as np

# File path
file_path = r"C:\Users\webexert\Desktop\zomato.csv"

# Load CSV
df = pd.read_csv(file_path)

# Remove rows where rate is missing
df = df[~df['rate'].isnull()]
print("New shape after removing null rates:", df.shape)

# Clean rate column
df['rate'] = df['rate'].astype(str)
df['rate'] = df['rate'].apply(lambda x: x.split('/')[0])
df['rate'] = df['rate'].replace(['NEW', '-'], None)
df['rate'] = df['rate'].astype(float)

# Clean approx_cost(for two people)
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].str.replace(',', '')
df['approx_cost(for two people)'] = pd.to_numeric(df['approx_cost(for two people)'], errors='coerce')

# Fill missing approx_cost with median
median_cost = df['approx_cost(for two people)'].median()
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].fillna(median_cost)

# Fill missing values for categorical columns
df['cuisines'] = df['cuisines'].fillna('Unknown')
df['rest_type'] = df['rest_type'].fillna('Unknown')
df['location'] = df['location'].fillna('Unknown')
df['phone'] = df['phone'].fillna('Not Available')
df['dish_liked'] = df['dish_liked'].fillna('Not mentioned')

# Check missing values again
print("\nMissing values after cleaning:\n", df.isnull().sum())

# Show first few rows
print("\nSample data:\n", df.head())

# Drop rows where rate is still null
df = df[~df['rate'].isnull()]
print("\nMissing values after dropping null rate rows:\n", df.isnull().sum())
print("\nNew shape:", df.shape)


import matplotlib.pyplot as plt
import seaborn as sns
# Plot 1 – Ratings Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['rate'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Restaurant Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Restaurants')
plt.savefig("ratings_distribution.png")

plt.show()
# INSIGHT:
# Most restaurants have ratings between 3.5 and 4.5.
# Very few restaurants are rated below 3.
# This suggests majority of restaurants maintain average to good quality.

# Plot 2 – Online Order vs No Online Order
online_order_counts = df['online_order'].value_counts()

plt.figure(figsize=(6,4))
sns.barplot(x=online_order_counts.index, y=online_order_counts.values, palette='viridis')
plt.title('Restaurants Offering Online Order')
plt.xlabel('Online Order')
plt.ylabel('Count')
plt.savefig("online_order_distribution.png")

plt.show()
# INSIGHT:
# About 60-65% restaurants provide online ordering facilities.
# This shows how digital platforms have become essential in the food industry.

# Plot 3 – Cost for Two Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['approx_cost(for two people)'], bins=30, kde=True, color='orange')
plt.title('Distribution of Approx Cost for Two People')
plt.xlabel('Approx Cost (INR)')
plt.ylabel('Number of Restaurants')
plt.savefig("approx_cost_distribution.png")
plt.show()
# INSIGHT:
# Majority of restaurants have meals for two costing between Rs. 200 and Rs. 800.
# Very few high-end restaurants charge above Rs. 2000.
# This indicates that mid-range pricing dominates Bangalore's food scene.

# Plot 4 – Top 10 Locations
top_locations = df['location'].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_locations.values, y=top_locations.index, palette='coolwarm')
plt.title('Top 10 Restaurant Locations')
plt.xlabel('Number of Restaurants')
plt.ylabel('Location')
plt.savefig("top_10_locations.png")
plt.show()
# INSIGHT:
# Koramangala, BTM Layout, and Indiranagar are the top hotspots for restaurants.
# These areas likely have high footfall and food demand.

# Plot 5 – Top 10 Cuisines
# Flatten cuisines column (because multiple cuisines are comma-separated)
from collections import Counter

cuisine_series = df['cuisines'].dropna().apply(lambda x: [i.strip() for i in str(x).split(',')])
cuisine_list = [cuisine for sublist in cuisine_series for cuisine in sublist]
cuisine_counts = Counter(cuisine_list)

top_cuisines = cuisine_counts.most_common(10)

# Plot
labels, values = zip(*top_cuisines)

plt.figure(figsize=(10,5))
sns.barplot(x=list(values), y=list(labels), palette='magma')
plt.title('Top 10 Cuisines in Bangalore Restaurants')
plt.xlabel('Count')
plt.ylabel('Cuisine')
plt.savefig("top_10_cuisines.png")
plt.show()
# INSIGHT:
# North Indian and Chinese cuisines dominate Bangalore’s restaurant scene.
# South Indian and Fast Food also feature prominently.
# This reflects diverse food preferences in Bangalore.