from fastapi import APIRouter, UploadFile, HTTPException, status
from utils import generate_random_string, remove_file
from config import images

router = APIRouter(prefix="/image")


@router.post("/")
async def save_image(image: UploadFile) -> str:
    """
    Функция которая будет получать изображение. Создавать ему ID и сохранять в файловой системе.
    Возвращает ID в виде строки с 20 символами + название + формат изображения.
    """
    id_lenght = 20
    image_id = generate_random_string(length=id_lenght)
    with open(f"{images}/{image_id}{image.filename}", "wb") as f:
        content = await image.read()
        f.write(content)
    return f"{image_id}{image.filename}"


@router.delete("/{filename}")
async def delete_image(filename: str):
    if filename is None:
        raise HTTPException(status_code=404, detail="Файл не найден")
    remove_file(name=filename)
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
