import psycopg2


database = 'postgres'
username = 'postgres'
# password = '123'
hostname = 'localhost'
port = '5432'
# Connect with psycopg2
conn = psycopg2.connect(database=database,
                        user=username,
                        # password=password,
                        host=hostname,
                        port=port)
# Connection cursor
cur = conn.cursor()
# Select table and display
cur.execute("""SELECT * FROM information_schema.tables;""")
rows = cur.fetchall()
for row in rows:
    print(row)
