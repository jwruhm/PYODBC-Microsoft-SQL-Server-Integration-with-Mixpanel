📩 SQL to Mixpanel Profile Sync

This Python script connects to a Microsoft SQL Server database using the pyodbc driver, retrieves user data from a Users table, and pushes selected user profile properties to Mixpanel in batch format via the /engage#profile-batch-update endpoint.

📦 Features

Connects to SQL Server securely with SQL authentication

Fetches and logs data from the Users table

Transforms SQL rows into Mixpanel profile update payloads

Sends user property updates in a single batch to Mixpanel

Supports fields like:

MS_SQL_customer_lifetime_value

MS_SQL_last_order_amount

MS_SQL_last_purchase_date

💠 Requirements

Python 3.7+

ODBC Driver 18 for SQL Server (or compatible)

Mixpanel project with a valid token

Python Packages

Install required packages:

pip install pyodbc requests

⚙️ Configuration

Update the following values in the script before running:

SERVER = '<Server>'             # e.g., 'myserver.database.windows.net'
DATABASE = '<Database>'         # e.g., 'MyDatabase'
USERNAME = '<Uid>'              # e.g., 'myusername'
PASSWORD = '<Pwd>'              # e.g., 'mypassword'

MIXPANEL_PROJECT_TOKEN = '<Mixpanel Token>'

Ensure the Users table includes the following columns (or update the script accordingly):

distinct_id

MS_SQL_customer_lifetime_value

MS_SQL_last_order_amount

MS_SQL_last_purchase_date

▶️ Running the Script

python sync_sql_to_mixpanel.py

You should see output like:

distinct_id   MS_SQL_customer_lifetime_value   ...
--------------------------------------------------
abc123        350.75                            ...
xyz789        120.10                            ...
Mixpanel Response: 200 {'status': 1, 'error': None}

📤 Example Mixpanel Payload

{
  "$token": "your-mixpanel-token",
  "$distinct_id": "abc123",
  "$set": {
    "MS_SQL_customer_lifetime_value": 350.75,
    "MS_SQL_last_order_amount": 89.99,
    "MS_SQL_last_purchase_date": "2024-03-01"
  }
}

❓Troubleshooting

Ensure your IP address is whitelisted on the SQL Server.

If you get ODBC errors, verify that ODBC Driver 18 is installed and properly configured.

Check Mixpanel’s API status codes if the response is not 200.

📄 License

MIT License. Feel free to use, modify, and share.

