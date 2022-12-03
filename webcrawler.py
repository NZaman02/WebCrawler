import urllib.request
import re


#formats the locations so that it can be added to the array
def getJustHref(startPosit,theText):
    #getting just the https link
    midString = ""
    loop = True
    speechSeen = 0
    speech = '"'
    currentPos = startPosit
    while (loop == True):
      
        if(theText[currentPos] == speech):
            speechSeen += 1
        if(speechSeen == 2):
            loop = False 
        else:
            midString += theText[currentPos]
            currentPos += 1

    
   

    return(midString[8:len(midString)])



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


yourUrl = input("Input a URL to begin with")
hrefArray = []
x=0
addToArray(hrefArray,'https://news.ycombinator.com/')
while (len(hrefArray)<100):
    try:
        addToArray(hrefArray,hrefArray[x])
    except:
        #some links can be used by us but not by library 
        print(hrefArray[x])
        print("Not a fan of url")
    x+=1



for x in range(0, len(hrefArray)):
    print(hrefArray[x])

print(len(hrefArray))