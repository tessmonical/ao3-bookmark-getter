import re
import sys
import json
import requests
import time
import AO3

session = requests.Session() #stores cookies so that we can login

username = sys.argv[1] #your username
password = ""
if len(sys.argv) > 2:
  password = sys.argv[2] #your password
currentPage = 1 #the page of bookmarks to start with

raw_series = input("Would you like to output the URLs of series? type y for yes\n")
series = (raw_series == 'y')

raw_metadata_q = input("Would you like metadata in addition to URLs? type y for yes\n")
metadata_q = (raw_metadata_q == 'y')

delay_every_10 = 0
delay_every_100 = 0

delay_enabled = input("Would you like to add a pause every 10 seconds + every 100 seconds? this might be useful if you get a rate limited error.\nif you are retreving metadata, this is needed\n")

if (delay_enabled == 'y'):
    delay_every_10 = int(input("delay every 10 works (in seconds)\n"))
    delay_every_100 = int(input("delay every 100 works (in seconds)\n"))

def encode_decode(input_string):
    #this function encodes and then decodes an input string. it does this to get rid of katakana and other non ascii characters that cause problems if not handled
    #encoding turns things into bytes or something, decoding turns things back into python strings.
    #i'm using ascii as the encoding mode because UTF-8 gave me an error for some reason

    input_string = input_string.encode(encoding='ascii', errors='replace')

    return input_string.decode(encoding='ascii', errors='replace')

# a little function to make it easier to print metadata later
def print_with_metadata_works(url, metadata, workid):
  titleprint = 'title: ' + metadata['title']
  #TODO add a print statement for the fandom
  try:
    work = AO3.Work(workid, session=ao3_session, load_chapters=False)
    fandomprint = "fandoms:"  + ' | '.join(work.fandoms)

    print(encode_decode(titleprint)) #decode to turn the bytes back into a python string
    print("word count: " + str(work.words))
    print(encode_decode(fandomprint)) #decode to turn the bytes back into a python string
    print('url: '+ url, flush=True)
  except AttributeError:
    print('girl help, something went wrong')

  print('')

def print_with_metadata_series(url, metadata, seriesid):
  titleprint = 'title: ' + metadata['title']
   #TODO add a print statement for the fandom
  try:
      worklist = AO3.Series(seriesid, session=ao3_session, load=False).work_list
      workexample = worklist[0].fandoms
      fandomprint = 'fandoms: ' + ' | '.join(workexample)

      print(encode_decode(titleprint))
      print('word count: ' + str(worklist.word_count))
      print(encode_decode(fandomprint))
      print('url: '+ url, flush=True)
  except AttributeError:
      print('girl help, something went wrong')
  print('')

ao3_session = AO3.Session(username, password) #get a session object compatable with the AO3 library

#login stuff
if (password != ''):
  # get an "authenticity token"
  authenticity_token = {}
  url_token = 'http://archiveofourown.org/token_dispenser.json'
  jsonThing = session.get(url_token)
  authenticity_token = jsonThing.json()['token']

  #log in
  url = 'https://archiveofourown.org/users/login'
  data = {
    'user[login]': username,
    'user[password]': password,
    'authenticity_token': authenticity_token #if you don't pass this along nothing works
  }

  headers = {
    "Accept":"text/html,*/*",
    "Host":"archiveofourown.org",
    "Connection":"keep-alive",
    "User-Agent":"ozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"
  }
  print("Logging in")
  the_page = session.post(url=url,data=data,headers=headers)

  if ('users/'+username) not in the_page.url:
    print("Login error!")
  else:
    print("Logged in!")

#actually grab all the bookmarks!
print('fetching urls', flush=True)
number_urls = 0

# finds things that look like
# <a href="/works/#"> where # is a number
p_works  = """<a href=\"/works/(\d+)\">([^<>]+)</a>\n\s*?by"""
p_series = """<a href=\"/series/(\d+)\">([^<>]+)</a>\n\s*?by"""
#p_fandoms =  """<a href=\"/tags/([^<>])/works\">([^<>]+)</a>\n\s*?&nbsp""" #TODO FIX. this regex would work if there's only one fandom, problem is there can be as many as they want per work.

end = False
while not end:
  # gets the current page from your bookmarks
  res = session.get('http://archiveofourown.org/users/'+username+'/bookmarks?page='+str(currentPage))
  html = res.text
  matches = re.findall(p_works, html) #this is what pulls the URL and the title. TODO update this if i want to get the fandom
  #fandoms = re.findall(p_fandoms, html)


  if ((number_urls % 10) == 0): #this is a potential fix for large ao3 libraries running into cl
    time.sleep(delay_every_10)
    if ((number_urls % 100) == 0):
      time.sleep(delay_every_100)


  #if there are no matches we've reached the end
  if len(matches) < 1:
      end = True
  for match in matches:
    if metadata_q:
        #TODO update htis line to support printing the fandom

      #Match[0] is a WorkID
      print_with_metadata_works('http://archiveofourown.org/works/' + match[0], {'title': match[1]}, match[0])
    else:
      print('http://archiveofourown.org/works/' + match[0])
    number_urls += 1
  if(series):
    matches_s = re.findall(p_series, html)
    for match_s in matches_s:
      if metadata_q:
          #TODO update this line to support pringint the fandom
        print_with_metadata_series('http://archiveofourown.org/series/' + match_s[0], {'title': match_s[1]}, match[0])
      else:
        print('http://archiveofourown.org/series/' + match_s[0])
      number_urls += 1

  currentPage += 1

print("Finished! with "+str(number_urls)+" urls")
