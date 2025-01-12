import psycopg2
import csv
from datetime import datetime

conn = psycopg2.connect(dbname="dummy_database", user="postgres", password="changeme", host="localhost")
cursor = conn.cursor()

# Replace 'your_table' with the actual table name
table_name = "project_user_table"

# Define the data types for each column in the new CSV file
column_types = [
    "INTEGER",   # ID
    "TEXT",      # Tiltle
    "TEXT",      # Position
    "TEXT",      # Skill
    "INTEGER",   # Salary
    "DATE",      # Jobstart_date
    "DATE",      # Job_end_date
    "TEXT",      # Technology_Level
    "TEXT",      # Role
    "TEXT",      # Cycle
    "REAL",      # Service_Score
    "INTEGER",   # Total_number_of_profiles
    "TEXT",      # Provider_Name
    "INTEGER",   # Discount
    "INTEGER"    # Duration(days)
]

# Check if the table already exists
cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
table_exists = cursor.fetchone()[0]

if not table_exists:
    # Create the table with the specified data types
    create_table_query = f"""
        CREATE TABLE {table_name} (
            "ID" {column_types[0]},
            "Tiltle" {column_types[1]},
            "Position" {column_types[2]},
            "Skill" {column_types[3]},
            "Salary" {column_types[4]},
            "Jobstart_date" {column_types[5]},
            "Job_end_date" {column_types[6]},
            "Technology_Level" {column_types[7]},
            "Role" {column_types[8]},
            "Cycle" {column_types[9]},
            "Service_Score" {column_types[10]},
            "Total_number_of_profiles" {column_types[11]},
            "Provider_Name" {column_types[12]},
            "Discount" {column_types[13]},
            "Duration(days)" {column_types[14]}
        )
    """
    cursor.execute(create_table_query)
    conn.commit()
    print(f"Table '{table_name}' created successfully.")
else:
    print(f"Table '{table_name}' already exists.")

with open('/home/jennadar/Downloads/Final_Data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        # Convert 'NA' in the "Cycle" column to NULL
        row = [value.strip() if value.lower() != 'na' else None for value in row]

        # Convert date strings to datetime objects
        row[5] = datetime.strptime(row[5], '%d-%m-%Y') if row[5] else None
        row[6] = datetime.strptime(row[6], '%d-%m-%Y') if row[6] and row[6].lower() != 'na' else None

        cursor.execute(f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)

conn.commit()
cursor.close()
conn.close()
