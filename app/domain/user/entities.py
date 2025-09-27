from dataclasses import dataclass
from uuid import uuid4

from app.infrastructure.security.password_hasher import hash_password


@dataclass(frozen=True)
class User:
    id: str
    project_ids: tuple[str, ...]

    email: str
    username: str
    password: str

    @staticmethod
    def create(email: str, username: str, password: str) -> "User":
        return User(
            id=str(uuid4()),
            project_ids=(),
            email=email,
            username=username,
            password=hash_password(password),
        )

    @staticmethod
    def create_from_dict(user_data: dict) -> "User":
        return User(
            id=user_data["id"],
            project_ids=tuple(user_data.get("project_ids", [])),
            email=user_data["email"],
            username=user_data["username"],
            password=user_data["password"],
        )

    def add_project_id(self, project_id: str) -> "User":
        return User(
            id=self.id,
            project_ids=self.project_ids + (project_id,),
            email=self.email,
            username=self.username,
            password=self.password,
        )
