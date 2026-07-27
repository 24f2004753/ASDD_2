import sqlite3

# Connect to your database
conn = sqlite3.connect('urls.db')
cursor = conn.cursor()

# Check if 'urls' table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='urls'")
result = cursor.fetchone()

if result:
    print("✓ Table 'urls' exists")
    
    # Also show what's in it
    cursor.execute("SELECT COUNT(*) FROM urls")
    count = cursor.fetchone()[0]
    print(f"  Contains {count} rows")
else:
    print("✗ Table 'urls' does NOT exist")

conn.close()
