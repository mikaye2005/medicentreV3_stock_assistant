import psycopg

conn = psycopg.connect(
    host="127.0.0.1",
    port=5432,
    dbname="demo",
    user="postgres",
    password="Collowinsky2005.",
)

cur = conn.cursor()

cur.execute("SHOW search_path;")
print("search_path =", cur.fetchone())

cur.execute("""
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema = 'demo'
  AND table_name IN (
    'tblitems',
    'tblcompanybranchitems',
    'tblitemstoragelocations',
    'tblstockchanges',
    'tblstocktakes'
  )
ORDER BY table_name;
""")
print("visible tables =", cur.fetchall())

conn.close()