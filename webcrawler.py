import urllib.request
import re


#formats the ahrefs so that it can be added to the array
def getJustHref(startPosit,theText):
    #getting just the https link
    midString = ""
    loop = True
    speechSeen = 0
    speech = '"'
    currentPos = startPosit
    #formats based on idea the https link will be imbetween "" everything else must be removed
    #once both speech marks have been found dont need to look further 
    #seems to work for most different formats of links on websites
    while (loop == True):  
        #checks character by character
        if(theText[currentPos] == speech):
            speechSeen += 1
        if(speechSeen == 2):
            loop = False 
        else:
            #concatenate the letters we need so far
            midString += theText[currentPos]
            currentPos += 1
    return(midString[8:len(midString)])



def addToArray(theArray,theLink):
    #reads the website into varialbe
    response = urllib.request.urlopen(theLink) 
    html = str(response.read())
    strToFind = 'a href="http'
    
    #finds all locations of all href links in a string
    res = [i.start() for i in re.finditer(strToFind, html)]
    
    #adds all unique links to an array
    for x in range(0, len(res)):
        if getJustHref(res[x],html) in theArray:
            #ignore if seen
            continue
        else:
            theArray.append(getJustHref(res[x],html))

    return(theArray)

print("Warning: Library struggles with certain websites")
print("Example Format =  https://news.ycombinator.com")
print("Example Format =  https://www.bbc.co.uk/news")
yourUrl = input("Input a URL to begin: ")
hrefArray = []
x=0
webPages = 0
#to get started
addToArray(hrefArray,yourUrl)
#keeps going until 100 done 
while (len(hrefArray)<100):
    try:
        #loops through urls we've already found and looks in them for more links
        addToArray(hrefArray,hrefArray[x])
        webPages += 1
    except:
        #some links can be used by us when copy into google but not by library 
        #rare problem
        print(hrefArray[x])
        print("Not a fan of url")
    x+=1


#prints result
for x in range(0, len(hrefArray)):
    print(hrefArray[x])

print(len(hrefArray))
print(str(webPages) + " pages looked at")