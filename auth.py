
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
import os

api_key_header = APIKeyHeader(name="API_KEY", auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    print(os.getenv("API_KEY"))
    if api_key_header == os.getenv("API_KEY"):
        return api_key_header   
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )
