import requests

url = 'https://challenger.ai'

res = requests.get(url)

res = res.content()

print(res)

