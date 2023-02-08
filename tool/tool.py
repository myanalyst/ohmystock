import os
from report import Report
import json
import collections
from datetime import datetime

class Tool:
    def __init__(self):
        self.tickers = {}
        self.group = {'Russell2000 Value Stock Index ETF':'RUS', 'S&P SmallCap 600 Index ETF':'S&PS', 'Vanguard U.S. Value Factor ETF':'VAN'}    
        original_dir = os.getcwd()
        os.chdir('../')#change to ohmystock_dev (project root) to read/write /config/
        # q = {1:[1,2,3], 2:[4,5,6], 3:{7,8,9}, 4:[10,11,12]}
    def merge(self):
        report = Report()
        for t in self.tickers:
            data = report.read('{0}_key_statistics.json'.format(t))
            if data:
                if 'group' in data:
                    data['group'].join(self.tickers[t])
                else:
                    data['group'] = self.tickers[t]
                report.write('{0}_key_statistics.json'.format(t), data)
            print(data)
    def merge(self):
        report = Report()
        for t in self.tickers:
            data = report.read('{0}_key_statistics.json'.format(t))
            if data:
                if 'group' in data:
                    data['group'].join(self.tickers[t])
                else:
                    data['group'] = self.tickers[t]
                report.write('{0}_key_statistics.json'.format(t), data)
            print(data)     

    #from yyyy-mm-dd to mm/dd/yyyy
    #file should be like 
    '''
    [
      {
       "Date": "2021-10-01",
       "gdp": "23992.355"
      },
      {
       "Date": "2021-07-01",
       "gdp": "23202.344"
      }
    ]
    when you run t.unitfy_date_format('/data/', 'gdp_by_quarter.json', 'Date', 'gdp')
    Date is k1
    gdp is k2
  '''
    def unitfy_date_format(self, path, fname, k1='Date', k2='Price'):
        res = {}
        report = Report()
        data = report.read(path, fname)
        for d in data:
            #yyyy-mm-dd
            if '-' in d[k1]:
                p = d[k1].split('-')
                if len(p[0]) == 4: #if yyyy-mm-dd
                    res['%s/%s/%s' %(p[1],p[2],p[0])] = float(d[k2])
            elif '/' in d[k1]:
                p = d[k1].split('/')
                if len(p[2]) == 4: #if mm/dd/yyyy
                    v = 0
                    if ',' in d[k2]:
                        v = d[k2].replace(',','')
                    else:
                        v = d[k2]
                    mm = p[0]
                    if len(mm) == 1: mm = '0' + mm
                    dd = p[1]
                    if len(dd) == 1: dd = '0' + dd
                    res[mm +'/'+ dd +'/'+ p[2]] = float(v)
        report.write('/data/', fname.split('.')[0] + '_' + 'formated.' + fname.split('.')[1], res)

    '''
    data (by month) from multpl.com
    Before converted: sp500_pe_by_month.csv
        May 1, 2010 17.30
        Jun 1, 1871 18
    After converted: sp500_pe_by_month_formated.json
        {
          "Date": "1/28/2022",
          "open": 4336.19,
          "high": 4432.72,
          "low": 4292.46,
          "close": 4431.85,
          "vol": 3936030000
         },
    '''
    def convert_multpl_data_format(self, path, fname):
        m = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        res = []
        report = Report()
        data = report.read_lines(path, fname)
        # print(data)
        for d in data:
            if 'Date' not in d:
                p = d.split(' ')
                mm = str(m[p[0]])
                if ',' in mm: mm = mm[0:len(mm)]
                dd = str(p[1])
                if ',' in dd: dd = dd[0:len(dd)-1]
                yyyy = str(p[2])
                if ',' in dd: yyyy = yyyy[0:len(yyyy)]
                pe = p[3]
                if pe:
                    dic = {}
                    dic['Date'] = mm +'/'+ dd +'/'+ yyyy
                    dic['Value'] = float(pe)
                    res.insert(len(res),dic)
        # print(res)
        report.write('/data/', fname.split('.')[0] + '_' + 'formated.json', res)

    '''
    sp500_price_by_day.csv
    fist we need use Sublime to replace all four spaces with one spaces, then
    run this method, because the decilima is supposed to be one space
    Before converted: sp500_pe_by_month.csv
        May 1, 2010 17.30
        Jun 1, 1871 18
    After converted: sp500_pe_by_month_formated.json
        {
           "Date": "5/1/2010",
           "Value": 17.30
        },
        {
           "Date": "6/1/1871",
           "Value": 18
        }
    '''
    def convert_yahoo_sp500_daily_price_format(self, path, fname):
        m = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        res = []
        report = Report()
        data = report.read_lines(path, fname)
        # print(data)
        for d in data:
            if 'Date' not in d:
                p = d.split(' ')
                print(p)
                mm = str(m[p[0]])
                if ',' in mm: mm = mm[0:len(mm)]
                dd = str(p[1])
                if ',' in dd: dd = dd[0:len(dd)-1]
                yyyy = str(p[2])
                if ',' in dd: yyyy = yyyy[0:len(yyyy)]
                ope = float(p[3].replace(',',''))
                high = p[4]
                if high:
                    high = float(float(p[4].replace(',','')))
                else:
                    high = 0.0
                low  = float(p[5].replace(',',''))
                adjclose = float(p[7].replace(',',''))
                vol = p[8]
                if vol == '-': 
                    vol = 0 
                else: 
                    vol = int(p[8].replace(',',''))
                dic = {}
                dic['Date'] = mm +'/'+ dd +'/'+ yyyy
                dic['open'] = ope
                dic['high'] = high
                dic['low'] = low
                dic['adjclose'] = adjclose
                dic['vol'] = vol
                res.insert(len(res),dic)
        print(res)
        report.write('/data/', fname.split('.')[0] + '_' + 'formated.json', res)
    '''
    finiz.csv
    '''
    def convert_finiz_sector_statistics_format(self, path, fname):
        now = datetime.now()
        report = Report()
        ks = list(report.read('/config/', 'industry_map_symbol.json').keys())
        i = report.read('/data/', 'industry_statistics_formated.json')
        data = report.read_download_folder(path, fname)
        r = 0
        for d in data:
            r = r + 1
            if r == 1:
                continue
            p = d.split(',')
            # print(p)
            industry = p[1].replace('"','').strip()
            if industry in ks:
                dic = {}
                dic['date']= now.strftime("%Y-%m-%d")
                dic['pe'] = float(p[3])
                dic['forward_pe'] = float(p[4])
                dic['peg'] = float(p[5])
                if industry not in i:
                    i[industry] = [dic]
                else:
                    
                    i[industry].append(dic)
        # print(i)
        report.write('/data/', 'industry_statistics_formated.json', i)

    '''
    morning star valuation
    '''
    def convert_morningstar_stock_valuation(self, path, fname):
        report = Report()
        f = report.read_download_folder(path, fname)
        if not f:
            print(path + fname +" not exist!")
            return
        nfname = '%s_valuation.json' %(fname.lower())
        ks = list(report.read('/data/stock/', nfname).keys())
        
        i = 0 #line index
        cur_cursor = 0 #current line index
        #append date
        dates = []
        for d in f:
            cur_cursor = cur_cursor + 1
            if d == 'Calendar':
                continue
            if len(d)==4 and d[0:2] == '20':
                dates.append(d)
            else:
                if 'price' in d.lower() or 'ratio' in d.lower() or 'earnings' in d.lower() or 'value' in d.lower():
                    break
        print(dates)
        #append ps
        ps = {}
        k = 0
        for d in f:
            i = i + 1
            # print('%s,%s' %(i, cur_cursor))
            if i == cur_cursor: # until go to line on Price/Sales
                cur_cursor = cur_cursor + 1
                # print(d)
                if d == 'Price/Sales':
                    continue
                if len(d) <=6 and k < len(dates):
                    if d =='––':
                        d = 'n/a'
                    ps[dates[k]] = d
                    k = k + 1
                else:
                    cur_cursor = cur_cursor + 2
                    break
        print(ps)
        #append pe
        pe = {}
        k = 0
        i = 0
        for d in f:
            i = i + 1
            # print('%s,%s' %(i, cur_cursor))
            if i == cur_cursor: # until go to line on Price/Sales
                cur_cursor = cur_cursor + 1
                # print(d)
                if d.strip() == 'Price/Earnings':
                    continue
                if len(d) <=6 and k < len(dates):
                    if d =='––':
                        d = 'n/a'
                    pe[dates[k]] = d
                    k = k + 1
                else:
                    cur_cursor = cur_cursor + 2
                    break
        print(pe)
        #append pc
        pc = {}
        k = 0
        i = 0
        for d in f:
            i = i + 1
            # print('%s,%s' %(i, cur_cursor))
            if i == cur_cursor: # until go to line on Price/Sales
                cur_cursor = cur_cursor + 1
                # print(d)
                if d.strip() == 'Price/Cash Flow':
                    continue
                if len(d) <=6 and k < len(dates):
                    if d =='––':
                        d = 'n/a'
                    pc[dates[k]] = d
                    k = k + 1
                else:
                    cur_cursor = cur_cursor + 2
                    break
        print(pc)
        #append pb
        pb = {}
        k = 0
        i = 0
        for d in f:
            i = i + 1
            # print('%s,%s' %(i, cur_cursor))
            if i == cur_cursor: # until go to line on Price/Sales
                cur_cursor = cur_cursor + 1
                # print(d)
                if d.strip() == 'Price/Book':
                    continue
                if len(d) <=6 and k < len(dates):
                    if d =='––':
                        d = 'n/a'
                    pb[dates[k]] = d
                    k = k + 1
                else:
                    cur_cursor = cur_cursor + 2
                    break
        print(pb)
        #append pe forward
        pef = {}
        k = 0
        i = 0
        for d in f:
            i = i + 1
            # print('%s,%s' %(i, cur_cursor))
            if i == cur_cursor: # until go to line on Price/Sales
                cur_cursor = cur_cursor + 1
                # print(d)
                if d.strip() == 'Price/Forward Earnings':
                    continue
                if len(d) <=6 and k < len(dates):
                    if d =='––':
                        d = 'n/a'
                    pef[dates[k]] = d
                    k = k + 1
                else:
                    cur_cursor = cur_cursor + 2
                    break
        print(pef)
        #append peg
        peg = {}
        k = 0
        i = 0
        for d in f:
            i = i + 1
            # print('%s,%s' %(i, cur_cursor))
            if i == cur_cursor: # until go to line on Price/Sales
                cur_cursor = cur_cursor + 1
                # print(d)
                if d.strip() == 'PEG Ratio':
                    continue
                if len(d) <=6 and k < len(dates):
                    if d =='––':
                        d = 'n/a'
                    peg[dates[k]] = d
                    k = k + 1
                else:
                    cur_cursor = cur_cursor + 2
                    break
        print(peg)
        #append earnings Yield %
        ey = {}
        k = 0
        i = 0
        for d in f:
            i = i + 1
            # print('%s,%s' %(i, cur_cursor))
            if i == cur_cursor: # until go to line on Price/Sales
                cur_cursor = cur_cursor + 1
                # print(d)
                if d.strip() == 'Earnings Yield %':
                    continue
                if len(d) <=10 and k < len(dates):
                    if d =='––':
                        d = 'n/a'
                    ey[dates[k]] = d
                    k = k + 1
                else:
                    cur_cursor = cur_cursor + 2
                    break
        print(ey)
        #append EV
        evebita = {}
        start=False
        k = 0
        for d in f:
            # print('%s,%s' %(i, cur_cursor))
            # print(d)
            if d.strip() == 'Enterprise Value/EBITDA':
                start = True
                continue
            
            if start:
                if len(d) <=6 and k < len(dates):
                    if d =='––':
                        d = 'n/a'
                    evebita[dates[k]] = d
                    k = k + 1
                else:
                    break
            # else:
            #     break
        print(evebita)
        x={}
        x['PS'] = ps
        x['PE'] = pe
        x['PEF'] = pef
        x['PEG'] = peg
        x['PC'] = pc
        x['PB'] = pb
        x['Earnings'] = ey
        x['EV/EBITDA'] = evebita
        report.write('/data/stock/', nfname, x)

if __name__ == '__main__':
    t = Tool()
    # t.unitfy_date_format('/data/', 'gdp_by_quarter.json', 'Date', 'gdp')
    # t.unitfy_date_format('/data/', 's&p500_price_by_month.json', 'Date', 'Price')
    # t.convert_multpl_data_format('/data/', 'sp500_pe_by_month.csv')
    # t.convert_yahoo_sp500_daily_price_format('/data/', 'sp500_price_by_day.csv')
    # t.convert_finiz_sector_statistics_format('/Users/neoo/Downloads/', 'finviz.csv')
    t.convert_morningstar_stock_valuation('/Users/neoo/Downloads/', 'abg')