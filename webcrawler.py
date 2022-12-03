import urllib.request

response = urllib.request.urlopen('https://news.ycombinator.com/') 

html = str(response.read())
print(type(html))

