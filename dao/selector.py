from database import DataBase

class Overview_Selector():
    def __init__(self):
        self.db = DataBase()

    def select_daily_price(self, ticker, datef, datet):
        sql = "SELECT * FROM STOCK_DAILY_PRICE WHERE TICKER='%s' AND TRADE_DATE >= '%s' AND TRADE_DATE <='%s'" %(ticker,datef, datet)
        return self.db.select_daily_price(sql)


if __name__ == '__main__':
    s = Overview_Selector()
    data = s.select_daily_price('M', '2023-01-31', '2023-02-06')
    print(data)