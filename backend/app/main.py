from fastapi import FastAPI
from fastapi.responses import JSONResponse
import psycopg2
from dotenv import load_dotenv
import os
from app.api import api_router

# Load environment variables
load_dotenv()

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# FastAPI app
app = FastAPI(title="Lol Muse API")
app.include_router(api_router, prefix="/api/v1")

# ✅ Define connection helper
def get_db_connection():
    return psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )

# ✅ Todos endpoint
@app.get("/todos")
def get_todos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, created_at, description FROM todos;")
        rows = cursor.fetchall()

        todos = [
            {"id": row[0], "created_at": row[1].isoformat(), "description": row[2]}
            for row in rows
        ]

        cursor.close()
        conn.close()

        return JSONResponse(content=todos)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
