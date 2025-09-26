from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse

from app.core.database import connect_to_database, disconnect_from_database

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await connect_to_database()


@app.on_event("shutdown")
async def shutdown_event():
    await disconnect_from_database()


@app.get("/")
def root():
    return RedirectResponse(url="/api")


@app.get("/api")
def greet():
    return JSONResponse(
        status_code=200, content={"message": "Welcome to the Tracker API"}
    )
