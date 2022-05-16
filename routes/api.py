from fastapi import APIRouter
from endpoints import music

router = APIRouter()
router.include_router(music.router)
