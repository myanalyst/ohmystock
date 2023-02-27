import sys
sys.path.insert(0,'/Users/ernestmoney/ohmystock')
from datetime import date
from tool.report import Report
from dao.selector_overview import Overview_Selector
import pipe.ma_support as masp
import pipe.price_support as prs
import pipe.price_momentum as prm

class Profile():
    def __init__(self):
        self.r = Report()
        self.s = Overview_Selector()
    
    def get_summary(self, ticker):
        return self.s.select_stock_summary(ticker)
        
    #vols: the number of big vols that support might find at
    def get_ma_support(self, ticker, datef, datet, vols):
        return masp.get_support_by_big_vols(self.s.select_daily_price(ticker, datef, datet), vols)

    def get_basic_finance(self, ticker, datef, datet):
        pass
    #find the gap up and gap down 
    def get_gap(self, ticker, today_price, datef, datet):
        return prs.get_gap(today_price, self.s.select_daily_price(ticker, datef, datet))
    
    def forcast_next_price(self, ticker, datef, datet, ma):
        s = self.s.select_stock_summary(ticker)
        is_up = True
        return prs.forcast_next_price(self.s.select_daily_price(ticker, datef, datet), date.today(), is_up, s['BETA'], ma)


