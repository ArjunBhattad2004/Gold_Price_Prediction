import pandas as pd
import numpy as np
from scipy.stats import zscore
from datetime import datetime

# Load the datasets
gold_price_data = pd.read_csv('datasets/gold_price_data.csv')
macrotrends_data = pd.read_csv('datasets/macrotrends_gold_price.csv')
final_uso_data = pd.read_csv('datasets/FINAL_USO.csv')

# --- 1. Data Wrangling for gold_price_data.csv ---

# Convert Date column to datetime and handle errors
gold_price_data['Date'] = pd.to_datetime(gold_price_data['Date'], errors='coerce')
gold_price_data.dropna(subset=['Date'], inplace=True)  # Remove rows where Date conversion failed
gold_price_data = gold_price_data.drop_duplicates()  # Remove duplicate rows

# Interpolate missing values for numeric columns
gold_price_data.interpolate(method='linear', inplace=True)

# Outlier detection and handling for GLD column using Z-score
gold_price_data['Gold_Price_Z'] = zscore(gold_price_data['GLD'].fillna(gold_price_data['GLD'].mean()))
gold_price_data = gold_price_data[abs(gold_price_data['Gold_Price_Z']) < 3]  # Filter out outliers

# Drop the helper Z-score column after filtering
gold_price_data.drop(columns=['Gold_Price_Z'], inplace=True)

# Save cleaned gold_price_data
gold_price_data.to_csv('datasets/cleaned_gold_price_data.csv', index=False)


# --- 2. Data Wrangling for macrotrends_gold_price.csv ---

# Convert Year column to datetime, extracting only the year if other characters are present
macrotrends_data['Year'] = macrotrends_data['Year'].str.replace(r'[^\d]', '', regex=True)
macrotrends_data['Year'] = pd.to_datetime(macrotrends_data['Year'], format='%Y', errors='coerce')
macrotrends_data.dropna(subset=['Year'], inplace=True)  # Remove rows where Year conversion failed
macrotrends_data.rename(columns={'Year': 'Date'}, inplace=True)

# Remove any non-numeric symbols (like $) from price columns and convert to float
price_cols = ['Average_Closing_Price', 'Year_Open', 'Year_High', 'Year_Low', 'Year_Close']
for col in price_cols:
    macrotrends_data[col] = macrotrends_data[col].replace('[\$,]', '', regex=True).astype(float)

# Fill any missing values by forward fill
macrotrends_data.fillna(method='ffill', inplace=True)

# Save cleaned macrotrends data
macrotrends_data.to_csv('datasets/cleaned_macrotrends_gold_price.csv', index=False)


# --- 3. Data Wrangling for FINAL_USO.csv ---

# Convert Date column to datetime and handle errors
final_uso_data['Date'] = pd.to_datetime(final_uso_data['Date'], errors='coerce')
final_uso_data.dropna(subset=['Date'], inplace=True)  # Remove rows where Date conversion failed
final_uso_data = final_uso_data.drop_duplicates()  # Remove duplicate rows

# Forward fill missing values in the financial data columns to maintain continuity
final_uso_data.fillna(method='ffill', inplace=True)

# Save cleaned final_uso data
final_uso_data.to_csv('datasets/cleaned_final_uso.csv', index=False)

print("Data wrangling complete. Cleaned files saved as 'cleaned_gold_price_data.csv', 'cleaned_macrotrends_gold_price.csv', and 'cleaned_final_uso.csv'")

