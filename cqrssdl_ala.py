#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Album downloader for /r/CuteKorean subreddit

@author: You

Ver. 0.04
10/01/2017 - Need fix folder issue, and add try/except for TypeError
10/02/2017 - Fixed folder and TypeError, next create "a la carte" version
10/03/2017 - Need fix a-la-carte download issue.
10/04/2017 - All bugs fixed, ready for public beta

Description: Reddit /r/CuteKorean album download bot. Automatically download
all the latest albums. 

Thanks to "imguralbum" and "imgurdownloader" authors script to make this bot
possible. 

License: MIT

"""

from bs4 import BeautifulSoup
import requests, feedparser, os, time

#list of models, subject to your preference

success = False

#initiate feedparser on rss
cqrss = feedparser.parse('https://www.reddit.com/r/cutekorean/new.rss')

while not success:
    try:
        for submission in cqrss.entries:
            folder_name = submission.title #use for create folder
            reddit_url = submission.link
            source = requests.get(reddit_url)
            plain_text = source.content
            soup = BeautifulSoup(plain_text, 'lxml')
            title = soup.find('a', 'title may-blank outbound', href=True)
            if title and 'imgur.com' in title['href']:
                imgur_link = title['href'] #album download link
                dl_command = "python imgurdownloader.py albums" + imgur_link
                print("Start downloading " + folder_name + ".")
                os.system(dl_command)
                print(folder_name + " download finishied.")
        success = True
    except TypeError:
        pass
        print("An error has appeared. Let's try again in 3, 2, 1~")
        time.sleep(3)
                
print("Mission Complete!")