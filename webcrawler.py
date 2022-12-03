import urllib.request
import re


#formats the locations so that it can be added to the array
def getJustHref(startPosit,theText):
    endString = ""
    loop = True
    speechSeen = False
    currentPos = startPosit
    while (loop == True):
        if(theText[currentPos] == '>'):
            loop = False
        else:
            endString += theText[currentPos]
            currentPos += 1
    return(endString[8:len(endString)-1])



def addToArray(theArray,theLink):
    #reads the website into array
    response = urllib.request.urlopen(theLink) 
    html = str(response.read())
    strToFind = 'a href="http'
    
    #finds all locations of all href links
    res = [i.start() for i in re.finditer(strToFind, html)]
    
    #adds all unique links to an array
    for x in range(0, len(res)):
        if getJustHref(res[x],html) in theArray:
            continue
        else:
            theArray.append(getJustHref(res[x],html))

    return(theArray)



hrefArray = []
addToArray(hrefArray,'https://news.ycombinator.com/')
for x in range(0, len(hrefArray)):
    print(hrefArray[x])


