from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse

from app.infrastructure.database.repositories import (
    DatabaseConnection,
    close_database_connection,
)
from app.core.dependencies import get_database_connection
from app.routes.auth_routes import auth_router

_db_connection: DatabaseConnection | None = None

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    global _db_connection
    _db_connection = await get_database_connection()


@app.on_event("shutdown")
async def shutdown_event():
    if _db_connection:
        await close_database_connection(_db_connection)


@app.get("/")
def root():
    return RedirectResponse(url="/api")


@app.get("/api")
def greet():
    return JSONResponse(
        status_code=200, content={"message": "Welcome to the Tracker API"}
    )


app.include_router(auth_router, prefix="/api/auth")


@app.exception_handler(HTTPException)
async def custom_exception_handler(_request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})
