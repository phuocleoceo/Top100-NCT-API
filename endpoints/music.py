from models.ResponseModel import ResponseModel
from models.driver import database, API_URL
from models.Song import Category, Song
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
    # Trả về các top
    return ResponseModel(list(songs.keys()), 200, "Get Music Successfully", False)


@router.get("/get_top_category")
async def get_top_category():
    # Danh sách các Collection chính là danh sách Top
    db = await database()
    tops = await db.list_collection_names()
    # Tạo object/dict lưu trữ các Top
    d = {}
    for top in tops:
        # Mỗi Top sẽ chứa 1 mảng các Category
        d[top] = []
        collection = db[top]
        cursor = collection.find({})
        if cursor:
            async for user in cursor:
                d[top].append(Category(**user).name)
    return ResponseModel(d, 200, "Get Top Category Successfully", False)


@router.get("/filter_by_top_category")
async def filter_by_top_category(top: str, category: str):
    # Lấy collection với Top tương ứng
    db = await database()
    collection = db[top]
    # Filter theo category
    cursor = await collection.find_one({"name": category})
    category_cursor = Category(**cursor)
    # Trả về danh sách bài hát
    return ResponseModel(category_cursor.songs, 200, "Filter Successfully", False)
