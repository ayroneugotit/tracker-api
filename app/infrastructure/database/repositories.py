import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException
from dataclasses import dataclass
from typing import Protocol

from app.core.config import settings
from app.core.logger import logger


@dataclass(frozen=True)
class DatabaseConnection:
    client: AsyncIOMotorClient
    db_name: str

    @property
    def db(self):
        return self.client[self.db_name]


class DatabaseRepository(Protocol):
    async def find_one(self, collection: str, query: dict) -> dict | None: ...
    async def find_many(self, collection: str, query: dict) -> list[dict]: ...
    async def insert_one(self, collection: str, document: dict) -> None: ...


class MongoRepository:
    def __init__(self, connection: DatabaseConnection):
        self._connection = connection

    async def find_one(self, collection: str, query: dict) -> dict | None:
        try:
            return await self._connection.db[collection].find_one(query)
        except Exception as e:
            logger.critical(f"Something went wrong while trying to find one: {e}")
            raise HTTPException(status_code=500, detail="Database operation failed")

    async def find_many(self, collection: str, query: dict) -> list[dict]:
        try:
            return (
                await self._connection.db[collection].find(query).to_list(length=None)
            )
        except Exception as e:
            logger.critical(f"Something went wrong while trying to find many: {e}")
            raise HTTPException(status_code=500, detail="Database operation failed")

    async def insert_one(self, collection: str, document: dict) -> None:
        try:
            await self._connection.db[collection].insert_one(document)
        except Exception as e:
            logger.critical(f"Something went wrong while trying to insert one: {e}")
            raise HTTPException(status_code=500, detail="Database operation failed")


async def create_database_connection() -> DatabaseConnection:
    for attempt in range(1, settings.DB_RECONNECT_ATTEMPTS + 1):
        logger.info(
            f"Connecting to the database (attempt {attempt} of {settings.DB_RECONNECT_ATTEMPTS})"
        )
        try:
            client = AsyncIOMotorClient(settings.MONGODB_URI)
            connection = DatabaseConnection(client, settings.MONGODB_DBNAME)
            await connection.client.admin.command("ping")
            logger.info("Server successfully connected to the database")
            return connection
        except Exception as e:
            if attempt < settings.DB_RECONNECT_ATTEMPTS:
                logger.warning("Failed to connect to the database")
                await asyncio.sleep(2 * attempt)
            else:
                logger.critical(
                    f"Something went wrong while trying to connect to the database: {e}"
                )
                raise


async def close_database_connection(connection: DatabaseConnection) -> None:
    try:
        connection.client.close()
        logger.info("Server successfully disconnected from the database")
    except Exception as e:
        logger.critical(
            f"Something went wrong while trying to disconnect from the database: {e}"
        )
        raise
