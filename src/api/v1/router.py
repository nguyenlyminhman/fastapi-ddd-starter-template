from fastapi import APIRouter, Depends
from core.security import has_access

api_router = APIRouter()
PROTECTED = [Depends(has_access)]

from modules.mock.presentation import mock_controller as mock_endpoint


api_router.include_router(mock_endpoint.router, tags=["Mock"] );

