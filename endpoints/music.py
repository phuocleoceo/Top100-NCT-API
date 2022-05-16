from models.driver import database, API_URL
from fastapi import APIRouter
import requests

router = APIRouter(
    prefix="/music",
    tags=["Music"],
    responses={404: {"description": "Not found"}},
)


@router.get("/get_from_api")
async def get_music_from_api():
    # Gọi API
    response = requests.get(API_URL)
    # Parse sang JSON
    songs = response.json()["songs"]
    # Duyệt qua mỗi top_name (top100_VN,...)
    # Mỗi top có 1 mảng danh sách các thể loại
    for top_name, top_songs in songs.items():
        # Truy cập DB và Collection tương ứng
        db = await database()
        collection = db[top_name]
        # Xóa toàn bộ Document cũ
        await collection.delete_many({})
        # Thêm vào Document hiện tại các thể loại bài hát
        # Mỗi thể loại có 1 mảng songs chứa các bài hát
        await collection.insert_many(top_songs)
    # Trả về status_code của response
    return response.status_code
