import urllib.request
import urllib.parse
import re
import sys

username = sys.argv[1] #your username
password = ""
if len(sys.argv) > 2:
  password = sys.argv[2]
currentPage = 1 #the page of bookmarks to start with
end = False

#login stuff
if (password != ''):
  url = 'http://archiveofourown.org/user_sessions/'
  values = {
    'user_session[login]': username,
    'user_session[password]': password,
    'user_session[remember_me]': 0,
    'commit': 'Log in',
    'utf8': u'✓',
   }
  data = urllib.parse.urlencode(values)
  data = data.encode('ascii') # data should be bytes
  req = urllib.request.Request(url, data)
  with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page)

# url = 'http://archiveofourown.org/user_sessions/'
# data = urllib.urlencode({username: username, password:password})
# with urllib2.urlopen(url=url, data=data).read() as content:
#   print(content)



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
