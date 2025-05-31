import json
from students.db import get_db_connection

def create_student_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        name = body.get("name")
        age = body.get("age")
        grade = body.get("grade")

        if not name or not age or not grade:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Name, age, and grade are required."})
            }

        conn = get_db_connection()
        if conn is None:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Database connection failed"})
            }

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s) RETURNING id",
            (name, age, grade)
        )
        student_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return {
            "statusCode": 201,
            "body": json.dumps({"message": "Student added successfully", "id": student_id})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
