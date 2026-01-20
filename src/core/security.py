import time
from jose import jwt, JWTError
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from config.setting import JWT_SECRET

security = HTTPBearer()


async def has_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
        Function that is used to validate the token in the case that it requires it
    """
    # to-do: fix bug decode
    # try:
    token = credentials.credentials
    print('token', token)
    print('JWT_SECRET', JWT_SECRET)
    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
    print("decoded_token", decoded_token)
    print('decoded token to check valid time')
    return decoded_token if decoded_token["expriration"] >= time.time() else None
    # except:
    #     print('<=.=> Bug in here ')
    #     return None