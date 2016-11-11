from twitter import *

auth = OAuth(
    consumer_key='asdf',
    consumer_secret='asdf',
    token='asdf',
    token_secret='asdf'
)

twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')
for msg in twitter_userstream.user():
    if 'direct_message' in msg:
        name = msg["direct_message"]['sender_screen_name']
        text = msg["direct_message"]['text']
        message = name +'   '+ text
        t = open("list.txt", 'a')
        t.write(message)
        t.write('\n')
        t.close()
