# AO3 bookmark getter

This python script is able to provide you with a list of links to every bookmark you have on [Archive Of Our Own](https://archiveofourown.org).

## That's great, but what is this useful for?

So, once you have a list of URLs, you can use other tools to download epubs of each of those files. I use a combination of [Calibre](https://calibre-ebook.com/download), which is a free ebook reading program, and a plugin that you can install for it, called FanFicFare (installed from the plugins menu of Calibre). With FanficFare, you give it a list of urls and it will download ebooks from each url. It works with tons of fanfic sites including AO3, so it's a great way to back up your favorite works for later (and read them on kindle, too!) [Here's a tutorial on how to do this.](https://www.reddit.com/r/FanFiction/comments/3pv06c/meta_a_tutorial_on_using_calibre_to_save_and_read/)

## How do I use it?

So if you're not tech-savvy this may be hard, fair warning. I had all these tools installed already. I've done my best to make this easy but installing stuff is always a pain.

### Install Python 3

Python 3 can be found at [python.org](https://www.python.org).

You will need Python 3 installed. This is installed by default with MacOS, but I would recommend installing the latest version- it'll make installing the SSL certificate easier in the next step.

If you're using Windows you will definitely need to install Python 3 to be able to use this. If you have Visual Studio installed, you can install Python through that.

### Install "Requests" module
Open up your terminal.

On Mac, type `pip3 install requests ` to install it. Wait a second or two for it to finish. 

On Windows, type `py -m pip install requests` to install it. Wait a second or two for it to finish.

### Install SSL certificates

In addition, once you have installed Python, on Mac you will need to install certificates in order to allow Python to make web requests. On Mac, go into your Applications folder and find the Python 3.x.x folder (the x.x will change but will be numbers). There will be a file named "Install Certificates.command" in that folder. Double click it to run it.

If you're on Windows, you don't need to do this (probably).

### Run the code

Open up your terminal, if it isn't already open. Navigate to where you've downloaded the files from this repository.

(On Mac you can probably type the command `cd Downloads` to get there, assuming you put it in the downloads folder).

On Mac, run the command `python3 ao3downloader.py username password` where you type your username instead of "username" and password instead of "password".

On Windows, run the command `ao3downloader.py username password` where you type your username instead of "username" and password instead of "password".

(If you just want your public bookmarks, don't type your password, and it won't log you in to fetch the private ones)

It will prompt you to ask if you would like to include series and if you would like metadata (just titles for now) in addition to URLs. If you want to import URLs into calibre, don't get metadata- you just want a list of URLs. If you are using some other tool, the title might be helpful.

If all goes well, this should print out a list of urls for each work/series you have bookmarked. Those URLs are every one of your bookmarks. You can copy and paste them into other programs or files.

## Limitations
Currently, because of the way this script searches for titles (regular expressions, instead of actually parsing HTML), any works with titles that contain the characters "<" or ">" in them won't be included. If you have works with funky titles, you may have to download those ones manually.
