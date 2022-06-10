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
git clone https://github.com/Hyper-glitch/Comics_publicist.git
```
2. Create **.env** file and set the <ins>environmental variables</ins> as described above.
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run python script
```bash
python3 main.py
```
5. Run with docker
```bash
docker build -t comics_publicist . && docker run -d --env-file .env comics_publicist
```
