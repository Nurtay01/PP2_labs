import psycopg2
from lab11.config import host,user,password,db_name


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    
    #cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"SERVER version: {cursor.fetchone()}")
    
except Exception as ex:
    print("[INFO] Error while working with PostgreSQL",ex)
finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")