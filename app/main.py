from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()


@app.get("/")
def root():
    return RedirectResponse(url="/api")


@app.get("/api")
def greet():
    return JSONResponse(
        status_code=200, content={"message": "Welcome to the Tracker API"}
    )
