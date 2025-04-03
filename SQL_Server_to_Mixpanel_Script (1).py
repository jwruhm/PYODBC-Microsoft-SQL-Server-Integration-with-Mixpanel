import pyodbc
import requests

#SQL Auth to database
SERVER = '<Server>'
DATABASE = '<Database>'
USERNAME = '<Uid>'
PASSWORD = '<Pwd>'

#Mixpanel credentials & endpoint (profile batch update method)
MIXPANEL_PROJECT_TOKEN = "<Mixpanel Token>"
MIXPANEL_API_URL = "https://api.mixpanel.com/engage#profile-batch-update"

#Connect to database via pyodbc
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)


#Retrieve data from Users table via pyodbc (print column names as header & retrieve each row of data)
SQL_QUERY = "SELECT * FROM Users;"

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

columns = [column[0] for column in cursor.description]
print("\t".join(columns))
print("-" * 80)

records = cursor.fetchall()
for r in records:
    print("\t".join(str(value) for value in r))


# Convert records to JSON format
mixpanel_data = [
    {
        "$token": MIXPANEL_PROJECT_TOKEN,
        "$distinct_id": str(r.distinct_id),
        "$set": {
            "MS_SQL_customer_lifetime_value": float(r.MS_SQL_customer_lifetime_value),
            "MS_SQL_last_order_amount": float(r.MS_SQL_last_order_amount),
            "MS_SQL_last_purchase_date": str(r.MS_SQL_last_purchase_date)
        }
    }
    for r in records
]

# Send batch request to Mixpanel
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
response = requests.post(MIXPANEL_API_URL, headers=headers, json=mixpanel_data)

# Print response from Mixpanel
print("Mixpanel Response:", response.status_code, response.json())

# Close database connection
cursor.close()
conn.close()
