import re
import sys
import json
import requests

session = requests.Session()

username = sys.argv[1] #your username
password = ""
if len(sys.argv) > 2:
  password = sys.argv[2]
currentPage = 1 #the page of bookmarks to start with
end = False

#login stuff
if (password != ''):
  # get an "authenticity token", which is an annoying thing that took me 100 years to figure out
  authenticity_token = {}
  url_token = 'http://archiveofourown.org/token_dispenser.json'
  jsonThing = session.get(url_token)
  # sessionCookieJar = jsonThing.cookies
  # print("cookie: " + sessionCookieJar['_otwarchive_session'])
  authenticity_token = jsonThing.json()['token']
  # print('authenticity_token: '+ authenticity_token)

  url = 'https://archiveofourown.org/user_sessions/'
  data = {
    'user_session[login]': username,
    'user_session[password]': password,
    # 'user_session[remember_me]': 1,
    'authenticity_token': authenticity_token #if you don't pass this along nothing works
  }
  headers = {
    "Accept":"text/html,*/*",
    "Host":"archiveofourown.org",
    "Connection":"keep-alive",
    "User-Agent":"ozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"
  }

  print('logging in as ' + username + ' with password ' + password)
  the_page = session.post(url=url,data=data,headers=headers)
  print(the_page.url)


number_urls = 0
if (False): #not running this right now
  while not end:
    # gets the current page from your bookmarks
    res = session.get('http://archiveofourown.org/users/'+username+'/bookmarks?page='+str(currentPage))
    html = res.text
    # finds things that look like
    # <a href="/works/#"> where # is a number
    p = '<a href="\/works\/(\d+)">'
    matches = re.findall(p, html)
    #if there are no matches we've reached the end
    if len(matches) < 1:
        end = True
    for match in matches:
      print('http://archiveofourown.org/works/' + match)
      number_urls += 1
    currentPage += 1

print("Finished! with "+str(number_urls)+" urls")
