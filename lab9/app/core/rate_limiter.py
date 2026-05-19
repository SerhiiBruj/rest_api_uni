import time
from fastapi import Request, HTTPException
from app.db.redis import redis
from app.core.config import RATE_LIMITS

async def rate_limit(request: Request, user_id: str | None):
    identity = user_id or request.client.host
    limit_type = "authenticated" if user_id else "anonymous"

    limit, period = RATE_LIMITS[limit_type]

    key = f"rate_limit:{identity}"

    now = int(time.time())
    window_start = now - period

    await redis.zremrangebyscore(key, 0, window_start)

    await redis.zadd(key, {str(now): now})

    request_count = await redis.zcard(key)

    print("==== RATE LIMIT DEBUG ====")
    print("identity:", identity)
    print("key:", key)
    print("count:", request_count)

    # 4. перевірка
    if request_count > limit:
        raise HTTPException(
            status_code=429,
            detail="Too many requests"
        )

    # 5. TTL
    await redis.expire(key, period)