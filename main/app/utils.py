from PIL import Image


def count_pixels(file_path, color: tuple):
    """Принимает путь к файлу и искомый цвет в виде (R, G, B),
    преобразует файл в RGB, собирает словарь цветов вида {цвет: количество пикселей} с помощью PIL.getcolors.
    Возвращает количество пикселей соответствующего цвета.
    """
    img = Image.open(file_path)
    img.convert('RGB')
    color_dict = {color: count for count, color in img.getcolors(img.size[0]*img.size[1])}  # img.size[0]*img.size[1] -
    try:                                                                                    # - макс количество цветов
        pixel_count = color_dict[color]                                                     # на изображении
        return pixel_count
    except KeyError:
        pixel_count = -1
    return pixel_count
