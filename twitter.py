import re
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urlib2
from urlib2 import urlopen

cd = CookieJar()
opener =  urlib2.build_opener(urllib2.HTTPCookieProcessor(cd))
opener.addheaders = {('User-agent',,'Mozilla/5.0')}

keyword = "Obama"
startingLink = 'https://twittercomsearch/realtime?q= '

def main()
    try:
    sourCode = opener.open('https://twitter.com/search/realtime?q=' +keyWord+ '&src=hash').read())
    print sourceCode

    splitSource= re.findall(r'<p class = Js-tweet-text tewee-text">(.*?)</p>',sourceCode)
    for item in splitSource:
        print item
        time.sleep(555)

    expect Excetion, e:
    print str(e)
    print 'errored in the main try'
    time.sleep(555)
