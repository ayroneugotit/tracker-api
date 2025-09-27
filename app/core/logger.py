import logging
import sys

from uvicorn.logging import DefaultFormatter

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    DefaultFormatter(fmt="%(levelprefix)s %(message)s", use_colors=True)
)

if not logger.hasHandlers():
    logger.addHandler(handler)
