import requests
from PIL import Image
from io import BytesIO

def download_and_open_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        dog_image_url = data.get("message")

        image_response = requests.get(dog_image_url)

        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))
            image.show()  
            print("Зображення собаки успішно відкрите.")
        else:
            print("Не вдалося завантажити зображення з посилання.")
    else:
        print("Не вдалося отримати посилання на зображення. Спробуйте ще раз.")

download_and_open_dog_image()
