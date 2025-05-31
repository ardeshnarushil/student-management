import json
from students.db import get_db_connection

def get_students_handler(event, context):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, name, age, grade FROM students")
        rows = cur.fetchall()

        students = []
        for row in rows:
            students.append({
                "id": row[0],
                "name": row[1],
                "age": row[2],
                "grade": row[3]
            })

        cur.close()
        conn.close()

        return {
            "statusCode": 200,
            "body": json.dumps(students)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
