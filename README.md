# Публикация комиксов

С помощью этого проекта вы сможете легко опубликовать рандомный комикс xkcd в вашей группе в VK.

### Как установить

Для начала зарегистрируйте приложение в VK и получите его client id. Затем получите ключ доступа, положите его в файл .env и назовите его VK_ACCESS_TOKEN.
Затем положите id своей группы и положите его в файл .env под названием VK_GROUP_ID
```
VK_ACCESS_TOKEN=ваш ключ доступа вк
VK_GROUP_ID=ваш id группы
```

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как запустить
Затем запустите программу командой
```
python3 main.py
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).