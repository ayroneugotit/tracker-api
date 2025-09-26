from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

from app.core.config import settings
from app.core.logger import logger

client = None
db = None


async def connect_to_database():
    global client, db

    for attempt in range(1, settings.DB_RECONNECT_ATTEMPTS + 1):
        logger.info(
            f"Connecting to the database (attempt {attempt} of {settings.DB_RECONNECT_ATTEMPTS})"
        )
        try:
            client = AsyncIOMotorClient(settings.MONGODB_URI)
            db = client[settings.MONGODB_DBNAME]
            await client.admin.command("ping")
            logger.info("Server successfully connected to the database")
            break
        except Exception as e:
            if attempt < settings.DB_RECONNECT_ATTEMPTS:
                logger.warning(f"Failed to connect to the database: {e}")
                await asyncio.sleep(2 * attempt)
            else:
                logger.critical(
                    f"Something went wrong while connecting to database: {e}"
                )


async def disconnect_from_database():
    global client

    if not client:
        return

    try:
        client.close()
        logger.info("Server successfully disconnected from the database")
    except Exception as e:
        logger.critical(f"Something went wrong while disconnecting from database: {e}")
