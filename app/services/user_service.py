from dataclasses import asdict

from app.infrastructure.database.repositories import DatabaseRepository
from app.domain.user.entities import User


async def get_user_by_email(repository: DatabaseRepository, email: str) -> User | None:
    user_data = await repository.find_one("users", {"email": email})
    return User.create_from_dict(user_data) if user_data else None


async def get_user_by_username(
    repository: DatabaseRepository, username: str
) -> User | None:
    user_data = await repository.find_one("users", {"username": username})
    return User.create_from_dict(user_data) if user_data else None


async def save_user(repository: DatabaseRepository, user: User) -> None:
    user_dict = asdict(user)
    await repository.insert_one("users", user_dict)
