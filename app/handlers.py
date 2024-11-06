from fastapi import APIRouter, UploadFile, HTTPException, status
from utils import generate_random_string, get_file_by_id, remove_file
from config import images
router = APIRouter(prefix="/image")


@router.post("/")
async def save_image(image: UploadFile) -> str:
    """
    Функция которая будет получать изображение. Создавать ему ID и сохранять в файловой системе.
    Возвращает ID в виде строки с 20 символами.
    """
    id_lenght = 20
    image_id = generate_random_string(length=id_lenght)
    with open(f"{images}/{image_id}{image.filename}", "wb") as f:
        content = await image.read()
        f.write(content)
    return image_id

@router.post("/{id}")
async def update_image(new_image: UploadFile, id: str):
    filename = get_file_by_id(id=id)
    if filename is None:
        raise HTTPException(status_code=404, detail="Файл не найден")
    with open(f"{images}/{filename}", "wb") as f:
        content = await new_image.read()
        f.write(content)
    return id

@router.delete("/{id}")
async def delete_image(id: str):
    filename = get_file_by_id(id=id)
    if filename is None:
       raise HTTPException(status_code=404, detail="Файл не найден")
    remove_file(name=filename)
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)