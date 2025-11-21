from bot.client.http import client
from bot.config import API_URL
from bot.utils import cache

async def get_verse(query: str):
    # intento leer de cache
    cached = cache.get(query)
    if cached:
        return cached

    r = await client.get(f"{API_URL}{query}")
    if r.status_code != 200:
        return None

    data = r.json()

    if "text" not in data:
        return None

    text = data["text"]
    ref = data.get("reference", query)

    full = f"{ref}:\n{text}"

    # guardo en cache
    cache.set(query, full)

    return full
