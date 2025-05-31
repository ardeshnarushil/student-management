import psycopg2

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="host.docker.internal",
            database="school",
            user="postgres",
            password="rushil",
            port=5432
        )
        return conn
    except Exception as e:
        print(f"DB connection error: {e}")
        return None
