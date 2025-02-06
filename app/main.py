from fastapi import FastAPI
from .db import get_connection
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from your new ticketing backend!"}


@app.get("/testdb")
def test_db():
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT VERSION() AS version")
            row = cursor.fetchone()
        conn.close()
        return {"db_version": row["version"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
