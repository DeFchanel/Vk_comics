import requests
import os
from dotenv import load_dotenv
import random


def download_img(file_path, url):
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def download_comic():
    filename = 'comics.png'
    dir_name = 'images'
    url = 'https://xkcd.com/info.0.json'
    os.makedirs(dir_name, exist_ok=True)
    file_path = os.path.join(dir_name, filename)
    response = requests.get(url)
    response.raise_for_status()
    number_of_comics = response.json()['num']
    random_number = random.randint(1, number_of_comics)
    comic_url = f'https://xkcd.com/{random_number}/info.0.json'
    comic_response = requests.get(comic_url)
    comic_response.raise_for_status()
    url_of_comic = comic_response.json()['img']
    download_img(file_path, url_of_comic)
    return comic_response.json()['alt']
    



def get_upload_url(access_token, group_id):
    payload = {
        'group_id': group_id,
        'access_token': access_token,
        'v': 5.131
    }
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()['response']['upload_url']


def upload_photo(upload_url):
    with open('images/comics.png', 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(upload_url, files=files)
        response.raise_for_status()
        return response.json()


def upload_photo_albom(server, photo, hash):
        payload = {
            'server': server,
            'photo': photo,
            'hash': hash,
            'group_id': group_id,
            'access_token': access_token,
            'v': 5.131
        }
        url = 'https://api.vk.com/method/photos.saveWallPhoto'
        response = requests.post(url, params=payload)
        response.raise_for_status()
        return response.json()


def publick_photo(from_group, attachments, message, access_token):
    payload = {
        'owner_id': f'-{group_id}',
        'from_group': from_group,
        'attachments': attachments,
        'message': message,
        'access_token': access_token,
        'v': 5.131
        }
    url = 'https://api.vk.com/method/wall.post'
    response = requests.post(url, params=payload)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    message = download_comic()
    load_dotenv()
    access_token = os.getenv('ACCESS_TOKEN')
    group_id = os.getenv('GROUP_ID')
    upload_url = get_upload_url(access_token, group_id)
    response = upload_photo(upload_url)
    server = response['server']
    photo = response['photo']
    hash = response['hash']
    albom_response = upload_photo_albom(server, photo, hash)
    owner_id = albom_response['response'][0]['owner_id']
    media_id = albom_response['response'][0]['id']
    attachments = f'photo{owner_id}_{media_id}'
    from_group = 1
    publick_photo(from_group, attachments, message, access_token)
    os.remove('images/comics.png')