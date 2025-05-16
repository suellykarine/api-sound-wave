import psycopg2

try:
    conn = psycopg2.connect(
        dbname="banco_teste",
        user="postgres",
        password="Sk151181",
        host="localhost",
        port="5432",
    )
    print("Conexão OK!")
    conn.close()
except Exception as e:
    print("Erro na conexão:", e)
