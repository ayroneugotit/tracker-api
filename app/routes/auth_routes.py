from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from dataclasses import asdict

from app.services import auth_service
from app.infrastructure.database.repositories import DatabaseRepository
from app.core.dependencies import get_repository
from app.domain.common.result import Success, Failure


auth_router = APIRouter()


@auth_router.post("/signup")
async def signup(
    email: str,
    username: str,
    password: str,
    repository: DatabaseRepository = Depends(get_repository),
) -> JSONResponse:
    result = await auth_service.signup(repository, email, username, password)

    match result:
        case Success(user):
            return JSONResponse(
                status_code=201,
                content={
                    "message": "User signed up successfully",
                    "data": asdict(user),
                },
            )
        case Failure(error):
            raise HTTPException(status_code=error.status_code, detail=error.detail)


@auth_router.post("/signin")
async def signin(
    username: str,
    password: str,
    repository: DatabaseRepository = Depends(get_repository),
) -> JSONResponse:
    result = await auth_service.signin(repository, username, password)

    match result:
        case Success(user):
            return JSONResponse(
                status_code=200,
                content={
                    "message": "User signed in successfully",
                    "data": asdict(user),
                },
            )
        case Failure(error):
            raise HTTPException(status_code=error.status_code, detail=error.detail)
