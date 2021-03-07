import urllib.request

content=urllib.request.urlopen('http://www.google.com/').read()
print(content)