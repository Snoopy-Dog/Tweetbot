from twitter import *

auth = OAuth(
    consumer_key='7fX7vzW4v6KKXPC3S3aJB0StT',
    consumer_secret='oHfxsfwCgHQeFtvDK6g0xtSH5VpHT1EPTkON5o8YA1xNVMliIo',
    token='796504375971745792-MSIyWeUeyHq2ccKshZZBu8k0LPI2DBv',
    token_secret='fWesYZ10fkLF5LbzaAuiVtnx9aDjw4egZFf5w4toVk1PX'
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