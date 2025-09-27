from app.domain.common.result import Result, success, failure
from app.domain.user.entities import User
from app.domain.user.errors import AuthError
from app.infrastructure.database.repositories import DatabaseRepository
from app.infrastructure.security.password_hasher import verify_password
from . import user_service


async def signup(
    repository: DatabaseRepository, email: str, username: str, password: str
) -> Result[User, AuthError]:
    if await user_service.get_user_by_email(repository, email) is not None:
        return failure(AuthError(400, "User with this email already exists"))

    if await user_service.get_user_by_username(repository, username) is not None:
        return failure(AuthError(400, "User with this username already exists"))

    user = User.create(email, username, password)
    await user_service.save_user(repository, user)

    return success(user)


async def signin(
    repository: DatabaseRepository, username: str, password: str
) -> Result[User, AuthError]:
    user = await user_service.get_user_by_username(repository, username)

    if user is None:
        return failure(AuthError(400, "User with this username does not exist"))

    if verify_password(password, user.password) is False:
        return failure(AuthError(400, "Invalid password"))

    return success(user)
