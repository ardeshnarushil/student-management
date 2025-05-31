import json
from students.db import get_db_connection

def get_student_by_id_handler(event, context):
    try:
        student_id = event['pathParameters']['student_id']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, name, age, grade FROM students WHERE id = %s", (student_id,))
        row = cur.fetchone()

        cur.close()
        conn.close()

        if row:
            student = {
                "id": row[0],
                "name": row[1],
                "age": row[2],
                "grade": row[3]
            }
            return {
                "statusCode": 200,
                "body": json.dumps(student)
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Student not found"})
            }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
