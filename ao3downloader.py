import urllib.request
import re
import sys

username = sys.argv[1] #your username
currentPage = 1 #the page of bookmarks to start with
end = False

while not end:
  # gets the current page from your bookmarks
  with urllib.request.urlopen('http://archiveofourown.org/users/'+username+'/bookmarks?page='+str(currentPage)) as response:
    #decodes the html
    responseBytesString = response.read()
    html = responseBytesString.decode('utf-8')
    # finds things that look like
    # <a href="/works/#"> where # is a number
    p = '<a href="\/works\/(\d+)">'
    matches = re.findall(p, html)
    #if there are no matches we've reached the end
    if len(matches) < 1:
       end = True
    for match in matches:
      print('http://archiveofourown.org/works/' + match)
    currentPage += 1

print("Finished!")
