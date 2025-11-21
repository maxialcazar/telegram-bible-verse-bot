cache = {}

def get(key: str):
    return cache.get(key)

def set(key: str, value):
    cache[key] = value
