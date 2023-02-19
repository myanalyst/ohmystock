import os
import sqlite3
from sqlite3 import Error


class DataBase():
    
    def __init__(self):
        self.conn = self._get_connection()

    def _get_connection(self):
        cur_username = os.path.expanduser('~')
        db_file = cur_username+"/ohmystock/data/db.sqlite3"
        print(db_file)
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    def select(self, sql):        
        cur = self.conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


    def insert_many(self, sql, data):
        """
        insert a list of data into table
        :param sql
        :param data:
        :return: the last record id
        """
        cur = self.conn.cursor()
        cur.executemany(sql, data)
        self.conn.commit()
        return cur.lastrowid

    def insert_profile(self, data):
        sql ='''INSERT INTO STOCK_PROFILE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        return self.insert_many(sql, data)
        
    def insert_stock_daily_prices(self, data):
        sql = ''' INSERT INTO STOCK_DAILY_PRICE VALUES(?,?,?,?,?,?,?) '''
        return self.insert_many(sql, data)

    def insert_balance(self, data):
        sql = ''' INSERT INTO BALANCE_SHEET VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
        return self.insert_many(sql, data)

    def insert_income(self, data):
        sql = ''' INSERT INTO INCOME_SHEET VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
        return self.insert_many(sql, data)

    def insert_cashflow(self, data):
        sql = "INSERT INTO CASHFLOW_SHEET VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        return self.insert_many(sql, data)

    def insert_eps(self, data):
        sql = ''' INSERT INTO EPS(TICKER,IS_ANNUAL,FISCAL_DATE_ENDING,ACTUAL_EPS,ESTIMATED_EPS) VALUES(?,?,?,?,?) '''
        return self.insert_many(sql, data)

    def is_fiscal_date_ending_exist(self, ticker, fiscal_date_ending, table_name):
        cur = self.conn.cursor()
        sql = "SELECT COUNT(*) FROM '"+ table_name +"' WHERE TICKER='"+ ticker +"' AND FISCAL_DATE_ENDING='" + fiscal_date_ending +"'"
        print(sql)
        cur.execute(sql)
        # print(cur.fetchone()[0])
        return cur.fetchone()[0]

    def is_exist(self, col_name, col_value, table_name):
        cur = self.conn.cursor()
        sql = "SELECT COUNT(*) FROM '"+ table_name +"' WHERE '"+ col_name +"'='"+ col_value +"'"
        print(sql)
        cur.execute(sql)
        # print(cur.fetchone()[0])
        return cur.fetchone()[0]


if __name__ == '__main__':
    db = DB()
    daily_prices = [('M','2022-02-07',21.4,25.9,25.0,25.5,8475600),('M','2022-02-08',22.4,25.9,25.0,24.8,8475600)]
    db.insert_prices(daily_prices)
