import pandas as pd
import numpy as np
import matplotlib.pyplot as mlt
import matplotlib.patches as mpatches

def getHour(item):
    return item.split(' ')

class times:
    def __init__(self, str):
        li = str.split(':')
        self.hour = li[0]
        self.minute = li[1]
        self.second = li[2]



def getFreq(fileName):
    file = pd.read_csv(fileName)
    column = file.created_at
    list = []
    for item in column:
        list.append(item)

    item = list[0]
    #print(item)
    temp = getHour(item)
    t = times(temp[1])
    #print('hour')
    #print(t.hour)
    freq = [0]*24

    for item in list:
        temp = getHour(item)
        t = times(temp[1])
        freq[int(t.hour)] = freq[int(t.hour)]+1
    return freq




xaxis = []
for i in range(24):
    xaxis.append(i)

phelps = getFreq('MichaelPhelps_tweets.csv')

lochte = getFreq('RyanLochte_tweets.csv')
bolt = getFreq('usainbolt_tweets.csv')

random_ppl = getFreq('random_tweets.csv')
print(random_ppl)

mlt.style.use('ggplot')
mlt.plot(xaxis, phelps, 'b-', xaxis, random_ppl, 'r-')
mlt.xticks(np.arange(0, 25, 2.0))
mlt.yticks(np.arange(0, 350, 25.0))
mlt.xlabel("Time of Day")
mlt.ylabel("Number of Tweets")
mlt.title("Tweet Like an Olympian")

red_patch = mpatches.Patch(color='red', label='Followers of Phelps')
blue_patch = mpatches.Patch(color='blue', label='Michael Phelps')
mlt.legend(handles=[red_patch, blue_patch], loc=2)

mlt.show()
