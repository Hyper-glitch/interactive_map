# Interactive map

## Basic information

***interactive_map*** allows you to add and describe interesting places via Django admin and show them on front side.

## Starting

| Environmental          | Description                                           |
|------------------------|-------------------------------------------------------|
| `VK_CLIENT_ID`         | your application ID, needed for getting access token  |
| `VK_ACCESS_TOKEN`      | personal token to interact with VK API methods        |
| `PUBLICATION_FREQUENCY`| posting frequency into VK public                      |

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
