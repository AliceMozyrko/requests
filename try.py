import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def get_posts():
    """Отримати список всіх постів."""
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            posts = response.json()
            print("Пости отримані успішно:")
            for post in posts: 
                print(f"\nID: {post['id']}, Title: {post['title']}, Body: {post['body']}")
        else:
            print("Не вдалося отримати пости", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Сталася помилка під час отримання постів:", e)

def get_specified_post():
    """Отримати один пост за його ID."""
    try:
        post_id = int(input("Введіть ID поста: "))
    except ValueError:
        print("Помилка: ID поста повинен бути числом.")
        return

    try:
        response = requests.get(f"{BASE_URL}/{post_id}")
        if response.status_code == 200:
            post = response.json()  # Отримуємо словник з даними поста
            print("Пост отримано успішно:")
            print(f"\nID: {post['id']}, Title: {post['title']}, Body: {post['body']}")
        else:
            print("Не вдалося отримати пост", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Сталася помилка під час отримання поста:", e)

last_user_id = 100  

next_id = 101

def create_post():
    """Створити новий пост."""
    global next_id  
    
    title = input("Введіть заголовок для поста: ")
    body = input("Введіть текст для поста: ")
    
    new_post = {
        "title": title,
        "body": body,
        "userId": 1,
        "id": next_id 
    }
    
    try:
        response = requests.post(BASE_URL, json=new_post)
        if response.status_code == 201:
            created_post = response.json()
            print("Пост створений успішно:", created_post)
            next_id += 1 
        else:
            print("Не вдалося створити пост", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Сталася помилка під час створення поста:", e)


def update_post():
    """Оновити існуючий пост."""

    try:
        post_id = int(input("Введіть ID поста, який ви хочете оновити: "))
    except ValueError:
        print("Помилка: ID поста повинен бути числом.")
        return
    
    title = input("Введіть заголовок для поста: ")
    body = input("Введіть текст для поста: ")

    updated_data = {
        "title": title,
        "body": body,
    }
    
    try:
        response = requests.patch(f"{BASE_URL}/{post_id}", json=updated_data)
        if response.status_code == 200:
            updated_post = response.json()
            print("Пост оновлено успішно:", updated_post)
        else:
            print("Не вдалося оновити пост. Статус-код:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Сталася помилка під час оновлення поста:", e)

def delete_post():
    """Видалити пост."""
    try:
        post_id = int(input("Введіть ID поста, який потрібно видалити: "))
    except ValueError:
        print("Помилка: ID поста повинен бути числом.")
        return
    
    try:
        response = requests.delete(f"{BASE_URL}/{post_id}")
        if response.status_code == 200:
            print(f"Пост з ID {post_id} видалено успішно.")
        else:
            print("Не вдалося видалити пост", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Сталася помилка під час видалення поста:", e)

if __name__ == "__main__":
    # print("GET метод:")
    # get_posts()
    # print("\nPOST метод:")
    # create_post()
    # print("\nPATCH метод:")
    # update_post()
    # get_specified_post()
    print("\nDELETE метод:")
    delete_post()  