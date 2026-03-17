import requests
import json
import private #Для хранения логина и пароля от платформы
import groups #Для хранения id групп


session = requests.Session()

session.post(
    "https://sibsutis.ru/auth/",
    data={
        "USER_LOGIN": private.login,
        "USER_PASSWORD": private.password,
        "AUTH_FORM": "Y",
        "TYPE": "AUTH",
        "Login": "Войти"
    }
)

url = "https://sibsutis.ru/students/schedule/?type=student&group=" + groups.group_id
response = session.get(url)

html = response.text

if "days[1]" in html:
    print("Авторизация успешна")
else:
    print("Авторизация не удалась")


