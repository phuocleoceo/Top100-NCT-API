from fastapi import APIRouter


router = APIRouter(
    prefix="/music",
    tags=["Music"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_music():
    return {"abc": "abc"}
