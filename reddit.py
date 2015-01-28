import  praw
import time
r = praw.reddit(user_agent = "grammar nazi reddit")
r.login()
print ("Loggin in ... ")
words_to_match = ['definately', 'defiantly', 'definatly', 'definetly','definatly']
cache= []

def run_bot ():
    print ("Grabbing subreddit ... ")
    subreddit= r.get_subreddit("test")
    print ("Grabbing comments ...")
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any (string in comment_texxt for string in words_to_match)
        if comment.id not in cache and isMatch:
            print ("Match found Comment ID:" + comment.id)
            comment.reply('I think you mean to say "definitly"')
            print ("Reply successful!")
            cache.append(comment.id)
            print ("Comments found")
while True:
    run_bot()
    time.sleep(10)
