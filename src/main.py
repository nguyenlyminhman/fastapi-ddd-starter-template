from fastapi import FastAPI, Depends
from api.v1.router import api_router

# from config.settings import DB_URL
# from fastapi.middleware.cors import CORSMiddleware

# from api.v1.api import api_router
# from api.auth import auth
# from tortoise.contrib.fastapi import register_tortoise
# from db import schemas




def get_app() -> FastAPI:
    mock_mint_app = FastAPI(title="FastApi DDD", version="0.0.1")

    # persona_app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=["*"],
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )

    mock_mint_app.include_router(api_router, prefix="/api/v1")

    return mock_mint_app


app = get_app()

# register_tortoise(
#     app,
#     db_url=DB_URL,
#     modules={"models": [schemas]},
#     generate_schemas=True,
#     add_exception_handlers=True
# )