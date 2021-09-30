<h3>Описание задачи</h3>
<p>Напишите WEB-сервис на Python, у которого будет HTML страничка с возможностью
загрузить картинку.<p>
Сервис должен:
<li>уметь сообщать каких пикселей больше на картинке, белых или чёрных;</li>
<li>по HEX коду цвета считать количество пикселей этого цвета на картинке.</li>

<h3>Реализация</h3>
<p>Используется фреймворк Django и библиотека pillow.<br>
Django выступает в качестве сервера для получения и хранения файлов,<br>
pillow с помощью PIL.Image.getcolors() создает словарь вида {цвет: количество пикселей цвета}.
<br>
После чего происходит поиск соответствующего введенному цвету ключа и количества пикселей.
<br>
<h3>Недостатки</h3>
<li>Для больших изображений, создание словаря цветов занимает продолжительное время и большое количество памяти.</li>
<li>Поиск ведется по конкретному коду RGB, что подходит не для всех изображений. Возможна ложная фильтрация. Например: 
на изображении из пикселей цвета (254, 254, 254) не будет найдено белых (255, 255, 255) пикселей. Хотя для человека оба
изображения абсолютно белые.</li>
<li>Для такой простой задачи, использование Django избыточно.</li>

<h3>Возможные улучшения</h3>
<li>Рассмотреть flask в качестве движка</li>
<li>Ипользовать numpy для поиска совпадений в массиве пикселей</li>
<li>Использовать opencv для поиска пикселей в диапазоне значений около указанного цвета. Например: считать черными
все пиксели до цвета (10, 10, 10). Белыми, соответственно выше (250, 250, 250).</li>
<li>Удалять файл после обработкой (или не сохранять перед, а читать из stream)</li>