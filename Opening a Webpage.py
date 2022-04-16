import urllib.request
data = urllib.request.urlopen('https://pythonschoolkvs.wordpress.com/')
print(data.read())
