import requests,re

raw_header = '''Host: my.5ka.ru
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: application/json, text/plain, */*
X-Authorization: Tokene4deed8f2b3b1679806f1194d6beeca90d75dda2
Connection: keep-alive'''
headers = {}
q = raw_header.split('\n')
rec = re.compile(r':\s')
for i in q:
    headers[rec.split(i)[0]] = rec.split(i)[1]
url = 'https://my.5ka.ru/api/v2/transactions/?card=07302bd9-c662-42f5-a10a-386fde0c8742&limit=100&offset=0&type='
cookies = headers
r = requests.get(url, headers=cookies)
print(r.content)
