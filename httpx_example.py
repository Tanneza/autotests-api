import httpx

# httpx.get()
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
# response = httpx.get("https://jsonplaceholder.typicode.com/todos")

print(response.status_code)
print(response.json())


data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

# httpx.post()
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)
# print(response.request.headers) # 'content-type': 'application/json'
print(response.json())

# application/x-www-form-urlencoded
data = {"username": "test_user", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
# print(response.request.headers) # 'Content-Type': 'application/x-www-form-urlencoded'
print(response.json())


# Передача заголовков
headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.request.headers)
print(response.json())

# параметры params
# response = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1")
params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)
print(response.json())

#Отправка файлов
files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)

print(response.json()) #Content-Type': 'multipart/form-data'


# Работа с сессиями (httpx.Client)
with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())
print(response2.json())


client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")

print(response.json())

client.close()