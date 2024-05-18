# Streaming file ..............................

import requests

url = ("https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-624.exe")
r = requests.get(url , stream=True)
totalExpectedBytes = int(r.headers["Content-Length"])
# print(totalExpectedBytes)
bytesReceived = 0

with open("winrar.wav", "wb") as f:
    for chunk in r.iter_content(chunk_size=128):
        print(f"{bytesReceived} received out of total {totalExpectedBytes}")
        f.write(chunk)
        bytesReceived += 128


# Get Request....................................

r = requests.get("https://www.codewithharry.com")
print(r.text)
with open("index.html",'w') as f:
    f.write(r.text)

#Basic Example..................................

r = requests.get('https://api.github.com/events')

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())

# Request With Querty...........................


payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get('https://httpbin.org/get', params=payload)
# print(r.text)

print(r.json(), "\n", type(r.json()))

# "https://httpbin.org/get?key1=value1&key2=value2"


# Pose Request.....................................

r = requests.post('https://httpbin.org/post?a=b', data={'key': 'value'})
print(r.text)

# Put Request.......................................

r = requests.put("https://httpbin.org/put", data={"a":1, "b":3})
print(r.text)

