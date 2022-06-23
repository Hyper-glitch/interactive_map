# Interactive map

## Basic information

***interactive_map*** allows you to add and describe interesting places via Django admin and show them on the World map.

## Starting

| Environmental           | Description                                              |
|-------------------------|----------------------------------------------------------|
| `SECRET_KEY`            | A secret key for a particular Django installation.       |
| `SESSION_COOKIE_SECURE` | Whether to use a secure cookie for the session cookie    |
| `DEBUG`                 | It provides a detailed traceback with the local variables|
| `ALLOWED_HOSTS`         | A list of strings representing the host/domain names     |

1. clone the repository:
```bash
git clone https://github.com/Hyper-glitch/interactive_map.git
```
2. Create **.env** file and set the <ins>environmental variables</ins> as described above.
3. Create venv
```bash
python3 -m venv venv
```
4. Activate venv
```bash
. venv/bin/activate
```
5. Install dependencies:
```bash
pip install -r requirements.txt
```
6. Run django server
```bash
python3 manage.py runserver
```
JSON example with place's information
```
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```
## There are urls
for the main page: https://hyperglitch.pythonanywhere.com   
for django admin: https://hyperglitch.pythonanywhere.com/admin   
<details><summary>Admin creds</summary>
<p>
Username: admin<br>
Password: admin
</p>
</details>
