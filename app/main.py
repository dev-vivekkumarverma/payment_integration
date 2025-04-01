from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import razorpay

import os
from dotenv import load_dotenv
from pydantic import BaseModel
from datetime import datetime
from fastapi import status

from database import (get_db_connection, init_db)
# Load environment variables
load_dotenv()


# Database Setup
DB_PATH = os.getenv("DB_PATH", None)
if not DB_PATH:
    raise Exception("DB_PATH missing in .env")

db_conn=init_db(dbPath=DB_PATH)
if db_conn:
    print("DB setup done !")
else:
    print("DB setup failed !")

# FastAPI app instance
app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific domains for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get(path="/")
def healthCheck():
    return {
        "health": "OK"
    }, status.HTTP_200_OK

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

