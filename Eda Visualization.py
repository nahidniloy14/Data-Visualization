# 🧠 Topics:
# Exploratory Data Analysis (EDA)

# Time Series Data Visualization

# Geospatial Data Visualization

# [Scene: A classroom setting. The teacher walks in holding a box of colorful balloons and a map.]

# Teacher:
# Good morning, data detectives! 👀 Today, we’re going on a journey — not just into data,
#  but into the heart of SunnyVille, a town full of secrets, weather changes, and even... pigeons with GPS trackers. 🕵️‍♂️📈🌍



# 🧩 Part 1: Exploratory Data Analysis (EDA)
# Teacher (narrating):
# Once upon a time, in SunnyVille, the mayor was worried. People were complaining about power cuts, traffic,
#  and even too many ice cream carts in some areas. So, she collected tons of data from surveys,
#   temperature logs, electricity usage, and more.

# Now, imagine you're her data scientist.

# You open the Excel file. What do you see?

# Some rows have missing values.

# Some columns like “complaint_type” have strange typos like "Trafic" and "Traffick."

# There are 10 types of ice cream carts in just one street. 🍦

# Welcome to Exploratory Data Analysis (EDA) — the art of understanding your data before doing anything else.

# We ask:

# What’s the shape of the data?

# Are there missing or duplicate values?

# What are the data types?

# What's the average number of complaints per district?

# You use:

# Histograms

# Box plots

# Correlation heatmaps

# Bar charts

# And slowly, the messy jungle of numbers becomes a clear story.


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------
# 📊 Step 1: Mock Data Creation
# ------------------------

np.random.seed(42)  # reproducibility

districts = ['Downtown', 'East Side', 'West End', 'Northville', 'Southtown']
complaint_types = ['Power Cut', 'Trafic', 'Traffick', 'Noise', 'Garbage', 'Water Leak', 'Power Cut', 'Ice Cream Cart']
ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Mango', 'Lemon', 'Pistachio', 'Cookie Dough', 'Coffee', 'Blueberry']

n_rows = 500

data = {
    'district': np.random.choice(districts, size=n_rows),
    'complaint_type': np.random.choice(complaint_types, size=n_rows),
    'temperature': np.random.normal(loc=32, scale=5, size=n_rows),
    'electricity_usage': np.random.normal(loc=250, scale=50, size=n_rows),
    'num_ice_cream_carts': np.random.choice([0, 1, 2, 5, 10, 10, 10], size=n_rows),
    'survey_rating': np.random.choice([1, 2, 3, 4, 5, np.nan], size=n_rows),
}

df = pd.DataFrame(data)

# Introduce some missing and duplicate values
df.loc[5:10, 'complaint_type'] = np.nan
df = pd.concat([df, df.iloc[0:5]])  # duplicate rows

# Save to Excel (optional)
# df.to_excel("sunnyville_data.xlsx", index=False)

# ------------------------
# 🔍 Step 2: EDA Begins
# ------------------------

print("\n📦 Data Snapshot:")
print(df.head())

print("\n🔢 Data Shape:", df.shape)

print("\n🧼 Missing Values:")
print(df.isnull().sum())

print("\n📁 Duplicate Rows:", df.duplicated().sum())

print("\n📐 Data Types:")
print(df.dtypes)

print("\n📊 Complaints per District:")
print(df['district'].value_counts())

print("\n🧮 Average Number of Complaints per District:")
complaints_per_district = df.groupby('district')['complaint_type'].count()
print(complaints_per_district)

# ------------------------
# 📈 Step 3: Visualization
# ------------------------

sns.set(style='whitegrid')

# Histogram: Temperature
plt.figure(figsize=(8, 4))
sns.histplot(df['temperature'], kde=True, bins=20)
plt.title("Temperature Distribution in SunnyVille")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Boxplot: Electricity Usage by District
plt.figure(figsize=(10, 6))
sns.boxplot(x='district', y='electricity_usage', data=df)
plt.title("Electricity Usage by District")
plt.xlabel("District")
plt.ylabel("Electricity Usage (kWh)")
plt.tight_layout()
plt.show()

# Heatmap: Correlation
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Bar Chart: Complaint Types (fixed typos)
df['complaint_type_clean'] = df['complaint_type'].replace({
    'Trafic': 'Traffic',
    'Traffick': 'Traffic'
})
plt.figure(figsize=(10, 4))
df['complaint_type_clean'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Frequency of Complaint Types")
plt.xlabel("Complaint Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
