import feedparser
import notify2
import os
import time
def parseFeed():
    feed = feedparser.parse("http://rss.cnn.com/rss/cnn_topstories.rss")
    ICON_PATH = os.getcwd() + "/icon.ico"
    notify2.init('News Notify')
    for newsitem in feed['items']: 
        notification = notify2.Notification(newsitem['title'], 
                                 newsitem['summary'], 
                                 icon=ICON_PATH 
                                 )
    	notification.set_urgency(notify2.URGENCY_NORMAL)
    	notification.show()
    	notification.set_timeout(15000)
    	time.sleep(20)

if __name__ == '__main__':
    parseFeed()     
