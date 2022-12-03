import urllib.request
import re

response = urllib.request.urlopen('https://news.ycombinator.com/') 

html = str(response.read())

test_sub = "href"
 
# using re.finditer()
# All occurrences of substring in string
res = [i.start() for i in re.finditer(test_sub, html)]
 
# printing result
print("The start indices of the hrefs are : " + str(res))