# 📩 SQL to Mixpanel Profile Sync

This Python script connects to a Microsoft SQL Server database using the `pyodbc` driver, retrieves user data from a `Users` table, and pushes selected user profile properties to Mixpanel in batch format via the `/engage#profile-batch-update` endpoint.

## 📦 Features

- Connects to SQL Server securely with SQL authentication
- Fetches and logs data from the `Users` table
- Transforms SQL rows into Mixpanel profile update payloads
- Sends user property updates in a single batch to Mixpanel
- Supports fields like:
  - `Customer_Tier`
  - `Customer_Lifetime_Value`
  - `Last_Purchase_Date`

---

## 💠 Requirements

- Python 3.7+
- ODBC Driver 18 for SQL Server (or compatible)
- Mixpanel project with a valid token
- Distinct ID(s) (`$distinct_id`) of the user profiles being updated in Mixpanel

### Python Packages

Install required packages:

```bash
pip install pyodbc requests
```

---

## ⚙️ Configuration

Update the following values in the script before running:

```python
SERVER = '<Server>'             # e.g., 'myserver.database.windows.net'
DATABASE = '<Database>'         # e.g., 'MyDatabase'
USERNAME = '<Uid>'              # e.g., 'myusername'
PASSWORD = '<Pwd>'              # e.g., 'mypassword'

MIXPANEL_PROJECT_TOKEN = '<Mixpanel Token>'
```

Update the script to support the relevant fields in the `Users` table. The script includes support for the following fields as-is:

- `distinct_id` (required)
- `Customer_Tier`
- `Customer_Lifetime_Value`
- `Last_Purchase_Date`

---

## ▶️ Running the Script

```bash
python sync_sql_to_mixpanel.py
```

You should see output like:

```bash
distinct_id   Customer_Lifetime_Value   ...
--------------------------------------------------
abc123        350.75                            ...
xyz789        120.10                            ...
Mixpanel Response: 200 {'status': 1, 'error': None}
```

---

## 📤 Example Mixpanel Payload

```json
{
  "$token": "your-mixpanel-token",
  "$distinct_id": "abc123",
  "$set": {
    "Customer_Tier": "Gold",
    "Customer_Lifetime_Value": 189.32,
    "Last_Purchase_Date": "2024-03-01"
  }
}
```

---

## ❓Troubleshooting

- Ensure your IP address is whitelisted on the SQL Server.
- If you get ODBC errors, verify that **ODBC Driver 18** is installed and properly configured.
- Check Mixpanel’s [API status codes](https://developer.mixpanel.com/docs/http#response-format) if the response is not `200`.
- Check Mixpanel's API documentation for the [Update Multiple Profiles](https://developer.mixpanel.com/reference/profile-batch-update) method, which references the [Set Property](https://developer.mixpanel.com/reference/profile-set) method as an update command in this example
- Check Microsoft's [Python SQL Driver - pyodbc](https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver16) for troubleshooting authentication with the SQL Server

---

## 📄 License

MIT License. Feel free to use, modify, and share.

