# AO3 Bookmark Getter

This python script is able to provide you with a list of links to every bookmark you have on [Archive Of Our Own](https://archiveofourown.org), as well as the title of the work and the fandom if desired. The script is continuously updated - [shoot me a DM on twitter](https://twitter.com/syrtis_) if you have a question or feature request.

## That's great, but what is this useful for?

So, once you have a list of URLs, you can use other tools to download epubs of each of those files. I use a combination of [Calibre](https://calibre-ebook.com/download), which is a free ebook reading program, and a plugin that you can install for it, called FanFicFare (installed from the plugins menu of Calibre). With FanficFare, you give it a list of urls and it will download ebooks from each url. It works with tons of fanfic sites including AO3, so it's a great way to back up your favorite works for later (and read them on kindle, too!) [Here's a tutorial on how to do this.](https://www.reddit.com/r/FanFiction/comments/3pv06c/meta_a_tutorial_on_using_calibre_to_save_and_read/)

I might add the ability to download epubs or pdfs of everything you've bookmarked in a future update - I'm already planning on doing a big rewrite at some point to improve speed.

## How do I use it?

So if you're not tech-savvy this may be hard, fair warning. I had all these tools installed already. I've done my best to make this easy but installing stuff is always a pain.

### Install Python 3

You will need Python 3 installed. Python 3 can be found at [python.org](https://www.python.org).

This is installed by default with MacOS, but I would recommend installing the latest version- it'll make installing the SSL certificate easier in the next step.

If you're using Windows you will definitely need to install Python 3 to be able to use this.

### Install "Requests" and "AO3" module
Open up your terminal.

On Mac, type `pip3 install requests ` and hit enter to install the requests module. Wait a second or two for it to finish. Type `pip3 install ao3_api ` and hit enter to install the ao3 api module.

On Windows, type `python pip install requests` to install it. Wait a second or two for it to finish. Type `python pip install ao3_api ` and hit enter to install the ao3 api module.

### Install SSL certificates (Mac Only)

In addition, once you have installed Python, on Mac you will need to install certificates in order to allow Python to make web requests. On Mac, go into your Applications folder and find the Python 3.x.x folder (the x.x will change but will be numbers). There will be a file named "Install Certificates.command" in that folder. Double click it to run it.

If you're on Windows, you don't need to do this AFAIK.

### Run the code

Open up your terminal, if it isn't already open. Navigate to where you've downloaded the files from this repository.

(On Mac you can probably type the command `cd Downloads` to get there, assuming you put it in the downloads folder).

On Mac, run the command `python3 ao3downloader.py username password` where you type your username instead of "username" and password instead of "password".

On Windows, run the command `python ao3downloader.py username password` where you type your username instead of "username" and password instead of "password".

(If you just want your public bookmarks, don't type your password, and it won't log you in to fetch the private ones)

It will prompt you to ask if you would like to include series and if you would like metadata to be printed in addition to URLs. If you want to import URLs into calibre, don't get titles- you just want a list of URLs. If you are using some other tool, the metadata might be helpful. The metadata includes the title and the list of fandoms - any non utf-8 characters (think katakana) are replaced with a ?.

**If you select that you would like to include metadata, it will take significantly longer, and may even give you a warning. This is normal -- just leave it alone for a while. In the future, I want to rewrite the script so it doesn't take the absurd amount of time it currently does when printing with metadata**

If you have more than 400 or so works, ao3 might have trouble processing the high volume of requests. It will ask you if you would like to add a pause every 10 works and 100 works. 30 seconds every 10 and 200 every 100 was recommended by one user with 3000 bookmarks, but mess around and find what works for you.

If all goes well, this should print out a list of urls for each work/series you have bookmarked. Those URLs are every one of your bookmarks. You can copy and paste them into other programs or files.

## Limitations
Currently, because of the way this script searches for titles (regular expressions, instead of actually parsing HTML), any works with titles that contain the characters "<" or ">" in them won't be included. If you have works with funky titles, you may have to download those ones manually. If you bookmarked a series, it won't pull the URL of every work in the series, but rather the series as a whole.
