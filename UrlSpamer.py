import requests

loophandler = bool(True)
url = str(input("url: "))
count = int(0)

while loophandler == True:
    count += 1
    results = requests.get(url)
    print(f"Result {count}: {results}")
