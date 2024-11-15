import mysql.connector
import pandas as pd

# Database connection parameters
host = 'localhost'       # Change this to your MySQL server host
user = 'root'   # Replace with your MySQL username
password = 'password'  # Replace with your MySQL password

# File paths for the CSV files
gold_price_file = 'Final_Datasets/gold_price_data.csv'
uso_file = 'Final_Datasets/FINAL_USO.csv'

# Load the datasets
gold_data = pd.read_csv(gold_price_file)
uso_data = pd.read_csv(uso_file)

# Connect to MySQL server
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)
cursor = conn.cursor()

# Create the database
db_name = 'Gold_Price_Prediction'
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
print(f"Database '{db_name}' created or already exists.")

# Connect to the newly created database
conn.database = db_name

# Create Kaggle_Dataset table
try:
    # Drop tables if they already exist (optional, for a clean start)
    cursor.execute("DROP TABLE IF EXISTS Kaggle_Dataset")
    cursor.execute("DROP TABLE IF EXISTS Final_USO_Dataset")
    
    # Create Kaggle_Dataset table dynamically based on CSV columns
    gold_columns = ", ".join([f"`{col}` TEXT" for col in gold_data.columns])
    cursor.execute(f"CREATE TABLE Kaggle_Dataset ({gold_columns})")
    print("Table 'Kaggle_Dataset' created.")
    
    # Create Final_USO_Dataset table dynamically based on CSV columns
    uso_columns = ", ".join([f"`{col}` TEXT" for col in uso_data.columns])
    cursor.execute(f"CREATE TABLE Final_USO_Dataset ({uso_columns})")
    print("Table 'Final_USO_Dataset' created.")
    
    # Insert data into Kaggle_Dataset table
    for _, row in gold_data.iterrows():
        cursor.execute(f"INSERT INTO Kaggle_Dataset VALUES ({', '.join(['%s'] * len(row))})", tuple(row))
    print(f"Inserted {len(gold_data)} rows into 'Kaggle_Dataset'.")
    
    # Insert data into Final_USO_Dataset table
    for _, row in uso_data.iterrows():
        cursor.execute(f"INSERT INTO Final_USO_Dataset VALUES ({', '.join(['%s'] * len(row))})", tuple(row))
    print(f"Inserted {len(uso_data)} rows into 'Final_USO_Dataset'.")
    
    # Commit the changes
    conn.commit()
    
finally:
    # Close the connection
    cursor.close()
    conn.close()
    print("Connection to MySQL closed.")
