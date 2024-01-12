from urllib.request import urlopen, Request

url = input("Insert your URL: ")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
data = urlopen(req).read().decode('utf-8')
print(data)
while True:
    url = True
    if len(data) < 3000:
        break
    print(data.decode(), end='')
    