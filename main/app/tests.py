from django.test import SimpleTestCase
from django.urls import reverse
from PIL import Image
from . import views
from django.core.files.uploadedfile import SimpleUploadedFile
import os


class ImageTests(SimpleTestCase):
    """Создаем тестовое изображение, загружаем на страницу и проверяем что количество найденных пикселей совпадает
    после чего удаляем тестовое изображение.
    """
    def test_image_upload_and_count_pixels(self):
        path = 'media\\test_image_100x100.png'
        img = Image.new('RGB', (100, 100), color=(255, 0, 0))
        img.save(path)
        file = SimpleUploadedFile(name='test_image_100x100_u.png', content=open(path, 'rb').read(), content_type='image/jpeg')
        color = 'ff0000'
        data = {'image': img, 'color': color}
        response = self.client.post('/', {'image': file, 'color': color})
        self.assertContains(response, 'Количество пикселей (255, 0, 0) цвета: 10000')
        self.assertContains(response, 'Белых (255, 255, 255) пикселей не найдено')
        self.assertContains(response, 'Черных (0, 0, 0) пикселей не найдено')
        os.remove(path)
        os.remove('media\\test_image_100x100_u.png')


class IndexPageTests(SimpleTestCase):

    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Выберите изображение:')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Этого сообщения не должно быть на странице')
