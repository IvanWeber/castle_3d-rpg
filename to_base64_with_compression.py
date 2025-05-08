from PIL import Image
import base64
from io import BytesIO

def compress_and_encode_image(input_path, output_txt_path, scale_factor=0.33, quality=25):
    # Открываем изображение
    with Image.open(input_path) as img:
        # Убираем альфа-канал, если есть
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        # Уменьшаем размер
        new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
        img_resized = img.resize(new_size, Image.Resampling.LANCZOS)

        # Сохраняем в память как JPEG с высоким сжатием
        buffer = BytesIO()
        img_resized.save(buffer, format="JPEG", quality=quality)
        buffer.seek(0)

        # Кодируем в base64
        encoded = base64.b64encode(buffer.read()).decode("utf-8")

        # Записываем в файл с нужным префиксом
        with open(output_txt_path, "w", encoding="utf-8") as out_file:
            out_file.write("data:image/jpeg;base64," + encoded)

# Пример использования
compress_and_encode_image("grass.png", "grass.txt")
