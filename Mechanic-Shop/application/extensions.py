# Import
from flask_marshmallow import Marshmallow
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache

ma = Marshmallow()

# Create a Limiter instance with memory storage (configured properly for development)
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="memory://",
    default_limits=["1000 per hour"]
)

# Create a Cache instance
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
