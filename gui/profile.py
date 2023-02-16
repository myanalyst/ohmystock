import sys
sys.path.insert(0,'/Users/ernestmoney/ohmystock')
from tool.report import Report
from dao.selector_overview import Overview_Selector
import pipe.ma_support as masp
import pipe.price_support as prs

class Profile():
    def __init__(self):
        self.r = Report()
        self.s = Overview_Selector()
    
    #vols: the number of big vols that support might find at
    def get_ma_support(self, ticker, datef, datet, vols):
        return masp.get_support(self.s.select_daily_price(ticker, datef, datet), vols)

    def get_gap_up(self, ticker, datef, datet):
        pass

    def get_price(self, ticker, today_price, datef, datet):
        return prs.get_gap(today_price, self.s.select_daily_price(ticker, datef, datet))
        