import sys
sys.path.insert(0,'/Users/ernestmoney/ohmystock')
import pipe.common as cm

'''
module:
list all the possible beta prices for tomorrow
by beta strength : 1(weakest), 5(strongest)
on ma5, or ma10, or ma20 etc

    To forcast tomorrow's possible price pp:
    1. get the past 5th close price (the one to keep ma horizontal)
    2. get the distance percentage pd between todayP and 5thP
    2. if todayP is bigger than 6thP, then (todayP - 5thP)/todayP
       if todayP is smaller than 6thP, then (5thP - todayP)/5thP
    3. get the possible distance expansion pde from pd
       from the pd, expand up by adding 1%, and down by minus 1%
    4. locate the pp by direction and beta strength
    5. calculate possible price pp by
       for up: [todayP * (1 + pde)]
       for down: todayP * (1 - pde)
'''

beta_table = {
                (0.60, 1.00) : (0.00, 0.70, 1.00),
                (1.01, 1.50) : (1.00, 1.50, 2.20),
                (1.51, 1.80) : (1.60, 2.30, 4.00),
                (1.81, 2.20) : (2.50, 4.20, 7.00)
             }
#ma = 5 or 20 or 30 or 60
def forcast_next_price(data, today, is_up, beta, ma):
    #get today index in data
    today_index = cm.get_today_index(data, today)
    scp = 0
    for i in range(today_index - ma,ma):
        print(data[i][5])
        scp = scp + data[i][5]
    avp = round(scp / ma, 2)

    #locate the pp by direction and beta strength
    #and calculate possible price pp by
    m = []
    for k, v in beta_table.items():
        if beta >= k[0] and beta<=k[1]:
            m = v
    
    prices = []
    if is_up :
        prices.append(('weak'  ,round(data[today_index][5] * (1 + m[0]*0.01),2)))
        prices.append(('medium',round(data[today_index][5] * (1 + m[1]*0.01),2)))
        prices.append(('strong',round(data[today_index][5] * (1 + m[2]*0.01),2)))
    else:
        prices.append(('weak'  ,round(data[today_index][5] * (1 - m[0]*0.01),2)))
        prices.append(('medium',round(data[today_index][5] * (1 - m[1]*0.01),2)))
        prices.append(('strong',round(data[today_index][5] * (1 - m[2]*0.01),2)))

    print('Given tomorrow UP? : %s' %is_up)
    # print('Day 1 price : %s' %(data[today_index-4][5]))
    print('Today price : %s' %data[today_index][5])
    print('Forcast prices:%s' %prices)
    return prices

if __name__ == '__main__':
    
    data = [
    ('M', '2023-02-10', 23.4,  24.22, 22.1,  212.65, 13222400), 
    ('M', '2023-02-13', 23.4,  24.22, 22.1,  217.88, 13222400), 
    ('M', '2023-02-14', 24.26, 20.77, 23.97, 229.71, 6087900), 
    ('M', '2023-02-15', 24.3,  25.12, 24.27, 227.64, 9382400), 
    ('M', '2023-02-16', 24.14, 10.27, 23.72, 220.02, 4318037)
    ]
    today = '2023-02-16'
    is_up = False
    beta = 1.79
    ma = 5
    forcast_next_price(data, today, is_up, beta, ma)
    #actual result for 02-17 is 213.88 (MA a little bit above )