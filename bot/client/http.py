import httpx
from bot.config import HTTP_TIMEOUT

client = httpx.AsyncClient(timeout=HTTP_TIMEOUT)
