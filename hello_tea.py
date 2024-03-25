import requests

def hello_tea_func():
    response = requests.get('https://app.tea.xyz/')
    print("Hello teaxyzzz7!")
    print("Status teaxyzzz7:", response.url, response.ok)
