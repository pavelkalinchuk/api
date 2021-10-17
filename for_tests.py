import requests
import json

# Получаем данные по rest api в переменную response в виде json-файла
response = requests.get('https://reqres.in/api/users?page=2').json()
# Открываем на запись файл result.json в текущем каталоге
f = open("result.json", 'w')
# Записываем полученные данные в открытый файл result.json отформатировав данные в читабельный вид
f.write(json.dumps(response, indent=4))
# Закрываем файл result.json
f.close()
# print(json.dumps(response, indent=4)


print("\ntest")
