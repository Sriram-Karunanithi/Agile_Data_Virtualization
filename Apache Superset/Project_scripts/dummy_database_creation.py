import psycopg2
import csv
from datetime import datetime  # Import the datetime module

conn = psycopg2.connect(dbname="dummy_database", user="postgres", password="changeme", host="localhost")
cursor = conn.cursor()

# Replace 'your_table' with the actual table name
table_name = "dummy_table"

# Define the data types for each column
column_types = [
    "INTEGER",  # Service Request ID
    "TEXT",     # Providername
    "TEXT",     # Username
    "TEXT",     # Password
    "TEXT",     # Role
    "TEXT",     # Service type
    "TEXT",     # Description
    "TEXT",     # Status
    "DATE",     # Created on
    "DATE",     # Completed on
    "INTEGER",  # Expenses ($)
    "REAL",     # Service score
    "TEXT",     # Negotiation
    "INTEGER"   # Discount %
]

# Check if the table already exists
cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
table_exists = cursor.fetchone()[0]

if not table_exists:
    # Create the table with the specified data types
    create_table_query = f"""
        CREATE TABLE {table_name} (
            "Service_Request_ID" {column_types[0]},
            "Providername" {column_types[1]},
            "Username" {column_types[2]},
            "Password" {column_types[3]},
            "Role" {column_types[4]},
            "Service_Type" {column_types[5]},
            "Description" {column_types[6]},
            "Status" {column_types[7]},
            "Created_On" {column_types[8]},
            "Completed_On" {column_types[9]},
            "Expenses" {column_types[10]},
            "Service_Score" {column_types[11]},
            "Negotiation" {column_types[12]},
            "Discount" {column_types[13]}
        )
    """
    cursor.execute(create_table_query)
    conn.commit()
    print(f"Table '{table_name}' created successfully.")
else:
    print(f"Table '{table_name}' already exists.")

with open('/home/jennadar/Downloads/Dummydatasets_user_table.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        # Convert 'NA' in the "Completed on" column to NULL
        row = [value.strip() if value.lower() != 'na' else None for value in row]

        # Convert date strings to datetime objects
        row[8] = datetime.strptime(row[8], '%Y-%m-%d') if row[8] else None
        row[9] = datetime.strptime(row[9], '%Y-%m-%d') if row[9] and row[9].lower() != 'na' else None

        cursor.execute(f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)

conn.commit()
cursor.close()
conn.close()
