import urllib
import webbrowser
weburl=urllib.request.urlopen('http://www.facebook.com/')
html=weburl.read()
data=weburl.getcode()
url=weburl.geturl()
hd=weburl.headers
inf=weburl.info()
print("The url is",url)
print("HTTP status code is :",data)
print("headers returned \n",hd)
print("the info returned :\n",inf)
print("Now opening the url",url)
webbrowser.open_new(url)
