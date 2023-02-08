import os
import json
from datetime import datetime

class Report():
    def __init__(self):
        path = os.getcwd()
        self.root_path = path #path=/Users/neoo/ohmystock

    def is_exist(self, file_path, file_name):
        return os.path.exists(self.root_path + file_path + file_name)

    def write(self, file_path, file_name, data):
        p = self.root_path + file_path + file_name
        if os.path.exists(p):
            os.remove(p)
        f = open(p, 'w')
        f.write(json.dumps(data, indent=1))
        f.close()
    
    def write_csv(self, file_path, file_name, data):
        p = self.root_path + file_path + file_name
        if os.path.exists(p):
            os.remove(p)
        f = open(p, 'w')
        print(type(data))
        print(data)
        # f.write(data)
        f.close()

    #t_ype=basic, daily, balance, income
    #data: not updated tickers
    def update_failure(self, file_path, file_name, t_ype, data):
        p = self.root_path + file_path + file_name
        fr = open(p , 'r')
        o = json.load(fr)
        o["update_date"] = datetime.today().strftime('%Y-%m-%d')
        for d in data:
            if d in o["tickers"]:
                o["tickers"][d][t_ype] = False
            else:
                o["tickers"].add(d)
                o["tickers"][d][t_ype] = False
        # print(o)
        fw = open(p , 'w')
        fw.write(json.dumps(o))
        fr.close()
        fw.close()

    #for some special files like :
    # failure/failed_key_statistics.json
    # failure/failed_daily_statistics.json
    # failure/failed_balance_statistics.json
    # failure/failed_income_statistics.json
    def append(self, file_path, file_name, data):
        p = self.root_path + file_path + file_name
        if not os.path.exists(p):
            f = open(p, 'w')
            f.write("\n")
            f.close()
        f = open(p, 'a')
        f.write(data)
        f.close()

    def read(self, file_path, file_name):
        p = self.root_path + file_path + file_name
        # print('reading report ' + p)
        data = {}
        if os.path.exists(p):
            f = open(p, 'r')
            data = json.loads(f.read())
            f.close()
        return data

    #finviz.csv
    def read_download_folder(self, file_path, file_name):
        symbols = []
        p = file_path + file_name
        if os.path.exists(p):
            f = open(p, 'r')
            lines = f.readlines()
            for line in lines:
                symbols.append(line.strip())
            f.close()
        return symbols

    #gdp_by_quarter_formated.json
    def read_gdp_by_quarter_formated_into_month(self, file_path, file_name):
        mt = {'1':'Jan', '2':'Feb', '3':'Mar','4':'Apr', '5':'May', '6':'Jun', '7':'Jul', '8':'Aug', '9':'Sep', '10':'Oct', '11':'Nov', '12':'Dec', '01':'Jan', '02':'Feb', '03':'Mar','04':'Apr', '05':'May', '06':'Jun', '07':'Jul', '08':'Aug', '09':'Sep', }
        p = self.root_path + file_path + file_name
        data = {}
        if os.path.exists(p):
            f = open(p, 'r')
            ds = json.loads(f.read())
            year = 0
            month = 0
            day = 0
            for k,v in ds.items():
                m = k.split('/')[0]
                d = int(k.split('/')[1])
                y = k.split('/')[2]
                if month != m:
                    data[mt[m]+'/'+y] = v
                    month = m
                    day = d
                elif day < d:
                    day = d

            # print(data)
            f.close()
        return data

    #sp500_price_by_day_formated.json
    def read_sp500_price_by_day_formated_into_month(self, file_path, file_name):
        mt = {'1':'Jan', '2':'Feb', '3':'Mar','4':'Apr', '5':'May', '6':'Jun', '7':'Jul', '8':'Aug', '9':'Sep', '10':'Oct', '11':'Nov', '12':'Dec', '01':'Jan', '02':'Feb', '03':'Mar','04':'Apr', '05':'May', '06':'Jun', '07':'Jul', '08':'Aug', '09':'Sep', }
        p = self.root_path + file_path + file_name
        data = {}
        if os.path.exists(p):
            f = open(p, 'r')
            ds = json.loads(f.read())
            year = 0
            month = 0
            day = 0
            for t in ds:
                m = t['Date'].split('/')[0]
                d = int(t['Date'].split('/')[1])
                y = t['Date'].split('/')[2]
                if month != m:
                    data[mt[m]+'/'+y] = t['adjclose']
                    month = m
                    day = d
                elif day < d:
                    day = d

            # print(data)
            f.close()
        return data

    def read_lines(self, file_path, file_name):
        symbols = []
        p = self.root_path + file_path + file_name
        if os.path.exists(p):
            f = open(p, 'r')
            lines = f.readlines()
            for line in lines:
                symbols.append(line.strip())
            f.close()
        return symbols


if __name__ == '__main__':
    report = Report()
    unupdated=[]
    report.update_failure('/config/','update_failure_test.json', 'basic', unupdated)
    '''
    quarter = {
            'quarterDateEnding': '2021-3-31',
            'reportedCurrency': 'USD',
            'totalAssets': '155971000000'}
    annual = {
            'fiscalDateEnding': '2020-12-31',
            'reportedCurrency': 'USD',
            'totalAssets': '155971000000'}
    if 1:
        quarter_report_name = '{0}_quarter_balance_sheet.json'.format("ticker")
        print(report.read(quarter_report_name))
    if 1:
        annual_report_name = '{0}_annual_balance_sheet.json'.format("ticker")
        print(report.read(annual_report_name))
    '''