import os
from os import path
import json
from datetime import datetime
import statistics as st
'''
1. download 
'''

class Yahoo_Data_Helper():
    def __init__(self, ticker):
        self.ticker = ticker
    
    #from list to file line by line
    def write_csv(self, file_path, file_name, data):
        p = os.getcwd() + file_path + file_name
        if os.path.exists(p):
            os.remove(p)
        with open(p, 'w') as f:
            for d in data:
                f.write(f"{d}\n")

    def _read_download_folder(self, file_name):
        result = []
        f = open(file_name, 'r')
        lines = f.readlines()
        for line in lines:
            result.append(line.strip())
        f.close()
        return result

    '''
    file: .csv
    content: monthly historical price
    process: 
        1. download monthly historical price from Yahoo finance
        2. change M.csv to M(monthly).csv
        3. run switch_monthly_price_to_horizontal()
    usage: compare the stock price volatility among the months
    '''    
    def switch_monthly_price_to_horizontal(self, file_name):
        return self.get_monthly_volatility(file_name)

    '''
    file: .csv
    content: daily historical price
    process: for every month, sum up its daily price, then get Mean and Stdev, and then switch col/row
             to make it look like: 
             'Year,01,02,03,04,05,06,07,08,09,10,11,12,Mean,Stdev'
             the monthly stock price is a subtotal, we dont need a real price
    usage: compare the stock price volatility among the months
    '''
    def get_monthly_volatility(self, rs):
        entries = ['Ticker,Year,01,02,03,04,05,06,07,08,09,10,11,12,Mean,Stdev'] #year,01,02,03,04,05,06,07,08,09,10,11,12
        y=''
        self._init_m()
        for r in rs:
            #Ticker,Date,Open,High,Low,Close,Volume
            ds = r[1].split('-')
            if not y:
                y = ds[0]
            if ds[0] == y:
                self._sum_daily(ds[1], r[5])
            else:
                #mean and stdev for 12 months in this year
                ms = [self.m1,self.m2,self.m3,self.m4,self.m5,self.m6,self.m7,self.m8,self.m9,self.m10,self.m11,self.m12]
                mean = st.mean(ms)
                stdev = st.stdev(ms)
                e = '%s,%s,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%s,%s' \
                %(self.ticker, y,round(self.m1,1),round(self.m2,1),round(self.m3,1),round(self.m4,1),round(self.m5,1),round(self.m6,1),round(self.m7,1),round(self.m8,1),round(self.m9,1),round(self.m10,1),round(self.m11,1),round(self.m12,1),round(mean,1),round(stdev,1))
                entries.append(e)
                #reset year and month price_sum
                self._init_m()
                y = ds[0]
                self._sum_daily(ds[1], r[5])

        #mean and stdev for 12 months in this year
        ms = [self.m1,self.m2,self.m3,self.m4,self.m5,self.m6,self.m7,self.m8,self.m9,self.m10,self.m11,self.m12]
        mean = st.mean(ms)
        stdev = st.stdev(ms)
        e = '%s,%s,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%s,%s' \
        %(self.ticker, y,round(self.m1,1),round(self.m2,1),round(self.m3,1),round(self.m4,1),round(self.m5,1),round(self.m6,1),round(self.m7,1),round(self.m8,1),round(self.m9,1),round(self.m10,1),round(self.m11,1),round(self.m12,1),round(mean,1),round(stdev,1))
        entries.append(e)
        #since Stdev requires at least two rows(years), if there are, add bottom Mean and Stdev
        if len(entries)>=3: #including header
            self._init_m()
            m1s=[]
            m2s=[]
            m3s=[]
            m4s=[]
            m5s=[]
            m6s=[]
            m7s=[]
            m8s=[]
            m9s=[]
            m10s=[]
            m11s=[]
            m12s=[]
            for entry in entries:
                e = entry.split(',')
                if e[0] == 'Year':
                    continue
                m1s.append(float(e[1]))
                m2s.append(float(e[2]))
                m3s.append(float(e[3]))
                m4s.append(float(e[4]))
                m5s.append(float(e[5]))
                m6s.append(float(e[6]))
                m7s.append(float(e[7]))
                m8s.append(float(e[8]))
                m9s.append(float(e[9]))
                m10s.append(float(e[10]))
                m11s.append(float(e[11]))
                m12s.append(float(e[12]))

            m = 'Mean,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f' \
            %(st.mean(m1s),st.mean(m2s),st.mean(m3s),st.mean(m4s),st.mean(m5s),st.mean(m6s),st.mean(m7s),st.mean(m8s),st.mean(m9s),st.mean(m10s),st.mean(m11s),st.mean(m12s))

            s = 'Stdev,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f' \
            %(st.stdev(m1s),st.stdev(m2s),st.stdev(m3s),st.stdev(m4s),st.stdev(m5s),st.stdev(m6s),st.stdev(m7s),st.stdev(m8s),st.stdev(m9s),st.stdev(m10s),st.stdev(m11s),st.stdev(m12s))

            entries.append(m)
            entries.append(s)

        return entries

    '''
    file: .csv
    content: daily historical price
    process: read csv into db.sqlite3
    usage: daily price is original data
    '''
    def read_daily_price(self, file_name):
        rs = self._read_download_folder(file_name)
        entries = [] #'TICKER, TRADE_DATE, OPEN, HIGH, LOW, CLOSE, VOLUME'
        for r in rs:
            if 'Date' in r:
                continue #Date,Open,High,Low,Close,Adj Close,Volume
            cols = r.split(',')
            e = [
            self.ticker, \
            cols[0],\
            round(float(cols[1]),2),\
            round(float(cols[2]),2),\
            round(float(cols[3]),2),\
            round(float(cols[4]),2),\
            int(cols[6])
            ]
            entries.append(e)

        return entries

    def _init_m(self):
        self.m1=0.0
        self.m2=0.0
        self.m3=0.0
        self.m4=0.0
        self.m5=0.0
        self.m6=0.0
        self.m7=0.0
        self.m8=0.0
        self.m9=0.0
        self.m10=0.0
        self.m11=0.0
        self.m12=0.0

    def _sum_daily(self,month, price):
        if month == '01':
            self.m1 = self.m1 + float(price)
        elif month == '02':
            self.m2 = self.m2 + float(price)
        elif month == '03':
            self.m3 = self.m3 + float(price)
        elif month == '04':
            self.m4 = self.m4 + float(price)
        elif month == '05':
            self.m5 = self.m5 + float(price)
        elif month == '06':
            self.m6 = self.m6 + float(price)
        elif month == '07':
            self.m7 = self.m7 + float(price)
        elif month == '08':
            self.m8 = self.m8 + float(price)
        elif month == '09':
            self.m9 = self.m9 + float(price)
        elif month == '10':
            self.m10 = self.m10 + float(price)
        elif month == '11':
            self.m11 = self.m11 + float(price)
        elif month == '12':
            self.m12 = self.m12 + float(price)


if __name__ == '__main__':
    report = Yahoo_Data_Helper()
    data = report.read_daily_price('M(daily).csv')
    print(data)
    # data = report.sum_daily_price_into_monthly('M(daily).csv')
    # report.write_csv('/stocks/', 'Macys-dailly-switch.csv', data)

    # data =report.switch_monthly_price_to_horizontal('M(monthly).csv')
    #report.write_csv('/stocks/', 'Macys-monthly-switch.csv', data)
    