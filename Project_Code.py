# Import necessary libraries for the project:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the A&E dataset:
dataframe = pd.read_csv("AandE-Admissions_Dataset.csv", skiprows=3)

# Appropriately name columns
dataframe.columns.values[0] = "Weekday"
dataframe.columns.values[1] = "Hour"
for i in range(2, 7):
    dataframe.columns.values[i] = "Reason: " + dataframe.columns[i]  # Replace '_suffix' with your desired suffix or prefix

print(dataframe.head())
print(dataframe.describe())

# Create a new DataFrame tracking sports injuries by Weekday and hour
dataframe_sports = dataframe["Weekday", "Hour", "Reason: Sports injury "]  # Replace with the actual column indices you want to select
print(dataframe_sports)
print(dataframe_sports.dtypes)

# Convert the sports injuries column to numeric
dataframe_sports.iloc[:, -1] = pd.to_numeric(dataframe_sports.iloc[:, -1], errors='coerce')

# Ensure the 'Weekday' column contains valid string values
print(dataframe_sports['Weekday'].unique())

# Data processing: drop the N/A values to enable analysis.
dataframe_sports = dataframe_sports.dropna()

print(dataframe_sports.head())


# Calculate the average value for sports injuries by day
avg_sports_injuries_by_day = dataframe_sports.groupby("Weekday").mean().iloc[:, -1]
print(avg_sports_injuries_by_day)
