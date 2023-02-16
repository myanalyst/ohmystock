import numpy as np

'''
data=[('M', '2023-02-01', 23.4, 24.22, 22.1, 24.03, 13222400)]
'''
def get_gap(today_price, data):
    gap = []
    for i in range(0,len(data)):
        if i < len(data)-1:
            #we define a meaningful gap up is "yesterday's low - next day's high>=$1"
            if data[i][4] - data[i+1][3] >= 1:
                print(today_price)
                print(data[i+1][3])
                print((today_price - data[i+1][3])/today_price)
                dis = round((today_price - data[i+1][3])/today_price * 100, 2) 
                if dis < 0:
                    gap.append(('pressure', data[i+1][1], "%s%%" %(np.absolute(dis))))
                else:
                    gap.append(('support', data[i+1][1], "%s%%" %(dis)))
    return gap

        
if __name__ == '__main__':
    data = [
    ('M', '2023-02-01', 23.4,  24.22, 22.1,  24.03, 13222400), 
    ('M', '2023-02-02', 24.26, 20.77, 23.97, 24.41, 6087900), 
    ('M', '2023-02-03', 24.3,  25.12, 24.27, 24.46, 9382400), 
    ('M', '2023-02-06', 24.14, 10.27, 23.72, 24.12, 4318037)
    ]
    today_price = 30.2
    print(get_gap(today_price, data))