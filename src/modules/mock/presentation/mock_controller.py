from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get("/mock")
async def create_megaboom() -> dict:
    """
    Get boombee.
    """
    return {"message": "MegaBoom created successfully."}


    