import os
import time
from datetime import date, timedelta
import requests
import json
from tool.report import Report
import wx

class Downloader():
    def __init__(self):
        self.report = Report()

    def download(self, ticker, func):
        url = "https://www.alphavantage.co/query?function=%s&symbol=%s&apikey=J436HJY6UCBYJ45P" %(func, ticker)
        if func == "TIME_SERIES_DAILY_ADJUSTED":
            url = "https://www.alphavantage.co/query?function=%s&symbol=%s&outputsize=full&apikey=J436HJY6UCBYJ45P" %(func, ticker)
        print(url)
        j = requests.get(url).content
        r = json.loads(j)
        if r and 'Information' not in r:
            report_name = '%s_%s.json' %(ticker.lower(), func.lower())
            self.report.write('/data/alphavantage/',report_name, r)
        else:
            print(r)