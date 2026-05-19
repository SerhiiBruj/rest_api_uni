from fastapi import Request, Depends
from app.core.security import get_current_user
from app.core.rate_limiter import rate_limit


async def rate_limited(
    request: Request,
    user: str | None = Depends(get_current_user)
):
    await rate_limit(request, user)