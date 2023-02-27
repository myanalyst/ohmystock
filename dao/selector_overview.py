import sys
sys.path.insert(0,'/Users/ernestmoney/ohmystock')
from dao.database import DataBase

class Overview_Selector():
    def __init__(self):
        self.db = DataBase()

    def select_daily_price(self, ticker, datef, datet):
        sql = "SELECT * FROM STOCK_DAILY_PRICE WHERE TICKER='%s' AND TRADE_DATE >= '%s' AND TRADE_DATE <='%s'" %(ticker,datef, datet)
        return self.db.select(sql)

    def select_stock_summary(self, ticker):
        sql = "SELECT TICKER,SECTOR,INDUSTRY,FISCAL_YEAR_END,LATEST_QUARTER,DIVIDEND_PERSHARE,PROFIT_MARGIN,OPERATING_MARGIN_TTM,RETURN_ON_ASSETS_TTM,RETURN_ON_EQUITY_TTM,ANALYST_TARGETPRICE,TRAILING_PE,FORWARD_PE,BETA,DIVIDEND_DATE FROM STOCK_PROFILE WHERE TICKER= '%s'" %(ticker)
        rs = self.db.select(sql)[0]
        # print(rs)
        s = {}
        s['TICKER'] = rs[0]
        s['SECTOR'] = rs[1]
        s['INDUSTRY'] = rs[2]
        s['FISCAL_YEAR_END'] = rs[3]
        s['LATEST_QUARTER'] = rs[4]
        s['DIVIDEND_PERSHARE'] = rs[5]
        s['PROFIT_MARGIN'] = rs[6]
        s['OPERATING_MARGIN_TTM'] = rs[7]
        s['RETURN_ON_ASSETS_TTM'] = rs[8]
        s['RETURN_ON_EQUITY_TTM'] = rs[9]
        s['ANALYST_TARGETPRICE'] = rs[10]
        s['TRAILING_PE'] = rs[11]
        s['FORWARD_PE'] = rs[12]
        s['BETA'] = rs[13]
        s['DIVIDEND_DATE'] = rs[14]
        return s

if __name__ == '__main__':
    #when run from here, remember to replace dao.database with database
    os = Overview_Selector()
    print(os.select_daily_price('M', '2022-12-01', '2022-12-31'))
    s = os.select_stock_summary('CVS')
    print(s)
    print(s['BETA'])
    
