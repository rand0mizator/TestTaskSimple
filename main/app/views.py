import os.path
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from .utils import count_pixels
from PIL import ImageColor


def index(request):
    if request.method == "POST":
        color = '#' + request.POST["color"]  # получаем строку с цветом из формы в index.html, добавлем символ #
        try:
            color = ImageColor.getrgb(color)  # преобразуем строку с цветом в tuple вида (R, G, B)
        except ValueError:
            color = None
        file = request.FILES["image"]
        file_name = default_storage.save(file.name, file)  # сохраняем файл из request в default_storage = main/media/
        file_url = default_storage.url(file_name)  # получаем путь к файлу относительно файловой системы django
        absolute_file_path = os.path.join(settings.MEDIA_ROOT, file_name)  # собираем абсолютный полный путь к файлу
        white = count_pixels(absolute_file_path, (255, 255, 255))
        black = count_pixels(absolute_file_path, (0, 0, 0))
        color_px = count_pixels(absolute_file_path, color)
        return render(request, "index.html", {"image_url": file_url, 'white': white,
                                              'black': black, 'color': color,
                                              'color_px': color_px})
    return render(request, "index.html")
