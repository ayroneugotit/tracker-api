from fastapi import Depends

from app.infrastructure.database.repositories import (
    DatabaseConnection,
    DatabaseRepository,
    MongoRepository,
    create_database_connection,
)

_connection: DatabaseConnection | None = None


async def get_database_connection() -> DatabaseConnection:
    global _connection
    if _connection is None:
        _connection = await create_database_connection()
    return _connection


async def get_repository(
    connection: DatabaseConnection = Depends(get_database_connection),
) -> DatabaseRepository:
    return MongoRepository(connection)
