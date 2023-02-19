import sys
sys.path.insert(0,'/Users/ernestmoney/ohmystock')
import numpy as np
import pipe.common as cm
'''
this method is only for today, that's meaningful
from today_price, back-checking day by day, list all the gap up/down in given data
'''
def get_gap(today, data):
    gap = []
    #check today is in data
    today_price = 0
    for d in data:
        if d[1] == today:
            today_price = d[5]
    if today_price:
        for i in range(0,len(data)-1):
            #we define a meaningful gap up is "yesterday's low - next day's high>=$1"
            if data[i][4] - data[i+1][3] >= 1:
                dis = round((today_price - data[i+1][3])/today_price * 100, 2) 
                if dis < 0:
                    gap.append(('pressure', data[i+1][1], "%s%%" %(np.absolute(dis))))
                else:
                    gap.append(('support', data[i+1][1], "%s%%" %(dis)))
    print(gap)
    return gap

'''
ma = [5,10,20,30]
find back 5 days and get the price for ma5
find back 10 days and get the price for ma10
find back 20 days and get the price for ma20
that price is the benchmark price
Only when tomorrow's price is equal to the benchmark price, 
the ma line is at balance(horizontal level)
when we forcast tomorrow's price, we need consider:
    pressure2(including ma5, ma10, ma20, gap_down, yesterday_price voletilaty)
    pressure1(including ma5, ma10, ma20, gap_down, yesterday_price voletilaty)
    benchmark
    support1(including ma5,ma10, ma20, gap_up)
    support2(including ma5,ma10, ma20, gap_up)

stock has yesterday_price voletilaty(YPV), ranging from 1%,2%,3%,5% etc.
Since every stock has the beta
in different beta has different strength level
we use the strength level to define if  the strength of YPV
NVDA's beta=1.79, so 3% is middle-high YPV
CVS's beta=0.65, so 1% is middle-high YPV
'''

def get_benchmark_prices(data, today, ma):
    r = []
    index_today = cm.get_today_index(data, today)

    for m in ma:
        r.append((data[index_today-(m-1)][1],data[index_today-(m-1)][5]))
    return r

