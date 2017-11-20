# AO3 bookmark grabber

This python script is able to provide you with a list of links (just urls, to start with) of every public bookmark you have on AO3.

## How do I use it?

So if you're not tech-savvy this may be hard, fair warning. I had all these tools installed already.

### Install Python 3

You will need python 3 installed. This is installed by default with MacOS and many (most?) linux flavors. If you're using Windows you will need to install python 3 to be able to use this. On Mac, I would recommend installing the latest version as well. Python 3 can be found at [python.org](https://www.python.org).

### Install SSL stuff

In addition, once you have installed Python, on Mac (probably Windows as well) you will need to install certificates in order to allow Python to make web requests. On Mac, go into your Applications folder and find the Python 3.x.x folder (the x.x will change but will be numbers). There will be a file named "Install Certificates.command" in that folder. Double click it to run it.

If you're on Windows, I'm not sure where this command might be. I don't have a PC to test this on right now.

### Run the command

Finally, open up your terminal. Navigate to where you've downloaded the files from this repository.

(On Mac you can probably type the command `cd Downloads` to get there, assuming you put it in the downloads folder).

run the command `python3 ao3downloader.py username` where you type your username instead of "username".

If all goes well, this should print out a list of urls after a pause of a few seconds (if you have a LOT of bookmarks, give it a minute or two). Those URLs are every one of your bookmarks. You can copy and paste them into other programs or files.

## That's great, but what is this useful for?

So, once you have a list of URLs, you can use other tools to download epubs of each of those files. I use a combination of [Calibre](https://calibre-ebook.com/download), which is a free ebook reading program, and a plugin that you can install for it, called FanFicFare (installed from the plugins menu of Calibre). With FanficFare, you give it a list of urls and it will download ebooks from each url. It works with tons of fanfic sites including AO3.

## How can I get my private bookmarks though?

I haven't figured that one out yet. Sorry!

## It stopped working!

Uh-oh! Let me know ASAP if this happens.
