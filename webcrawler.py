import urllib.request
import re

def getJustHref(startPosit,theText):
    endString = ""
    loop = True
    currentPos = startPosit
    while (loop == True):
        if(theText[currentPos] == '>'):
            loop = False
        else:
            endString += theText[currentPos]
            currentPos += 1
    return(endString[7:len(endString)])

response = urllib.request.urlopen('https://news.ycombinator.com/') 

html = str(response.read())

strToFind = 'a href="http'
 
# using re.finditer()
# All occurrences of substring in string
res = [i.start() for i in re.finditer(strToFind, html)]
 

hrefArray = []
for x in range(0, len(res)):
    hrefArray.append(getJustHref(res[x],html))

print(hrefArray)