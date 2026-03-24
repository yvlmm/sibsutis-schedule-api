import requests
import json
import private #Для хранения логина и пароля от платформы
import groups #Для хранения id групп

def get_html(group): # по идее сюда передаем str группу, дальше в функции находим её айди и поджставляем

    group_id = groups.find_group(group)
    if group_id is None:
        print("Группа не найдена")
        return None

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
    
    url = "https://sibsutis.ru/students/schedule/?type=student&group=" + str(group_id)
    response = session.get(url)

    html = response.text

    return extract_days(html)

def extract_days(html):
    results = []
    pos = 0

    while True:
        # ищем начало days[
        start = html.find("days[", pos)
        if start == -1:
            break

        # ищем первую кавычку после =
        start_quote = html.find("'", start)
        if start_quote == -1:
            break

        # ищем закрывающую кавычку
        end_quote = html.find("'", start_quote + 1)
        if end_quote == -1:
            break

        raw_json = html[start_quote + 1:end_quote]

        try:
            data = json.loads(raw_json)
            results.append(data)
        except Exception as e:
            print("Ошибка JSON:", e)

        pos = end_quote + 1

    return results

print(get_html("ИВ-422")[12])
