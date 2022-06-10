# Interactive map

## Basic information

***interactive_map*** allows you to add and describe interesting places via Django admin and show them on front side.

## Starting

| Environmental           | Description                                             |
|-------------------------|---------------------------------------------------------|
| `SECRET_KEY`            | A secret key for a particular Django installation.      |
| `SESSION_COOKIE_SECURE` | Whether to use a secure cookie for the session cookie   |
| `DEBUG`                 | Never deploy a site into production with DEBUG turned on|
| `ALLOWED_HOSTS`         | A list of strings representing the host/domain names    |

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
source venv/bin/activate
```
5. Install dependencies:
```bash
pip install -r requirements.txt
```
6. Run django server
```bash
python3 manage.py runserver
```
## There are urls
for main page: http://127.0.0.1:8000/   
for django admin: http://127.0.0.1:8000/admin
