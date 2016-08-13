import time
from TwitterAPI import TwitterAPI, TwitterRestPager

SEARCH_TERM = 'olympics'


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

target = open('timefiles.txt', 'w')

api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)
start = time.time()
pager = TwitterRestPager(api, 'search/tweets', {'q': SEARCH_TERM})
#print('time for rest pager= '+ str(time.time()-start))
i = 0
for item in pager.get_iterator():
    i = i+1
    if i == 100:
        break;
#    temp = time.time()
    target.write(item['created_at'] if 'created_at' in item else item)
    target.write('\n')
    #print(item)
target.close()
print('time for writing one is:' +str(time.time()-start))
