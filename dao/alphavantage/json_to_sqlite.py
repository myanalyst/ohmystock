from dao.database import DataBase
from tool.report import Report

class Converter():
    def __init__(self, ticker):
        self.ticker = ticker
        self.report = Report()
        self.db = DataBase()

    def write_profile(self):
        d = self.report.read('/data/alphavantage/', '{0}_overview.json'.format(self.ticker))
        data = []
        print(d)
        data = self.__set_profile_table_cols(d)
        print(data)
        self.db.insert_profile(data)

    def __set_profile_table_cols(self, d):
        data = []
        r =[d['Symbol'],d['Name'],d['Description'],\
        d['Sector'],d['Industry'],\
        d['FiscalYearEnd'],\
        d['LatestQuarter'],d['DividendPerShare'],\
        d['ProfitMargin'],d['OperatingMarginTTM'],d['ReturnOnAssetsTTM'],\
        d['ReturnOnEquityTTM'],d['AnalystTargetPrice'],d['TrailingPE'],\
        d['ForwardPE'],d['Beta'],\
        d['52WeekHigh'],d['52WeekLow'],\
        d['SharesOutstanding'],\
        d['DividendDate'],d['ExDividendDate']]
                
        for i in range(len(r)):
            if r[i] == 'None':
                r[i] = 0

        if not self.db.is_exist('TICKER', d['Symbol'], 'STOCK_PROFILE'):
            data.append(r)
        else:
            print('find %s, not to work on it.' %(d['symbol']))

        return data

    def write_balance(self):
        ds = self.report.read('/data/alphavantage/', '{0}_balance_sheet.json'.format(self.ticker))
        data = []
        data = self.__set_balance_table_cols(ds, 'annualReports') + self.__set_balance_table_cols(ds, 'quarterlyReports')
        print(data)
        self.db.insert_balance(data)

    def __set_balance_table_cols(self, ds, report_type):
        data = []
        for d in ds[report_type]:
            if report_type == 'annualReports':
                is_annual = 1
            else:
                is_annual = 0

            r =[ds['symbol'],is_annual, d['fiscalDateEnding'],d['totalAssets'],d['totalCurrentAssets'],d['cashAndCashEquivalentsAtCarryingValue'],d['cashAndShortTermInvestments'],\
                d['inventory'],d['currentNetReceivables'],d['totalNonCurrentAssets'],d['propertyPlantEquipment'],d['accumulatedDepreciationAmortizationPPE'],\
                d['intangibleAssets'],d['intangibleAssetsExcludingGoodwill'],d['goodwill'],d['investments'],d['longTermInvestments'],\
                d['shortTermInvestments'],d['otherCurrentAssets'],d['otherNonCurrentAssets'],d['totalLiabilities'],d['totalCurrentLiabilities'],\
                d['currentAccountsPayable'],d['deferredRevenue'],d['currentDebt'],d['shortTermDebt'],d['totalNonCurrentLiabilities'],\
                d['capitalLeaseObligations'],d['longTermDebt'],d['currentLongTermDebt'],d['longTermDebtNoncurrent'],\
                d['shortLongTermDebtTotal'],d['otherCurrentLiabilities'],d['otherNonCurrentLiabilities'],d['totalShareholderEquity'],\
                d['treasuryStock'],d['retainedEarnings'],d['commonStock'],d['commonStockSharesOutstanding']]
                
            for i in range(len(r)):
                if r[i] == 'None':
                    r[i] = 0

            if not self.db.is_fiscal_date_ending_exist(ds['symbol'], d['fiscalDateEnding'], 'BALANCE_SHEET'):
                data.append(r)
            else:
                print('find %s, %s, %s, not to work on it.' %(ds['symbol'], report_type, d['fiscalDateEnding']))

        return data

    def write_income(self):
        ds = self.report.read('/data/alphavantage/', '{0}_income_statement.json'.format(self.ticker))
        data = []
        data = self.__set_income_table_cols(ds, 'annualReports') + self.__set_income_table_cols(ds, 'quarterlyReports')
        # print(data)
        self.db.insert_income(data)

    def __set_income_table_cols(self, ds, report_type):
        data = []
        for d in ds[report_type]:
            if report_type == 'annualReports':
                is_annual = 1
            else:
                is_annual = 0

            r =[ds['symbol'],is_annual, d['fiscalDateEnding'],d['grossProfit'],d['totalRevenue'],d['costOfRevenue'],d['costofGoodsAndServicesSold'],\
                d['operatingIncome'],d['sellingGeneralAndAdministrative'],d['researchAndDevelopment'],d['operatingExpenses'],d['investmentIncomeNet'],\
                d['netInterestIncome'],d['interestIncome'],d['interestExpense'],d['nonInterestIncome'],d['otherNonOperatingIncome'],\
                d['depreciation'],d['depreciationAndAmortization'],d['incomeBeforeTax'],d['incomeTaxExpense'],d['interestAndDebtExpense'],\
                d['netIncomeFromContinuingOperations'],d['comprehensiveIncomeNetOfTax'],d['ebit'],d['ebitda'],d['netIncome']]
                
            for i in range(len(r)):
                if r[i] == 'None':
                    r[i] = 0

            if not self.db.is_fiscal_date_ending_exist(ds['symbol'], d['fiscalDateEnding'], 'INCOME_SHEET'):
                data.append(r)
            else:
                print('find %s, %s, %s, not to work on it.' %(ds['symbol'], report_type, d['fiscalDateEnding']))

        return data

    def write_cashflow(self):
        ds = self.report.read('/data/alphavantage/', '{0}_cash_flow.json'.format(self.ticker))
        data = []
        data = self.__set_cashflow_table_cols(ds, 'annualReports') + self.__set_cashflow_table_cols(ds, 'quarterlyReports')
        print(data)
        self.db.insert_cashflow(data)

    def __set_cashflow_table_cols(self, ds, report_type):
        data = []
        for d in ds[report_type]:
            if report_type == 'annualReports':
                is_annual = 1
            else:
                is_annual = 0

            r =[ds['symbol'],is_annual, d['fiscalDateEnding'],d['operatingCashflow'],\
            d['paymentsForOperatingActivities'],d['proceedsFromOperatingActivities'],\
            d['changeInOperatingLiabilities'],\
            d['changeInOperatingAssets'],d['depreciationDepletionAndAmortization'],\
            d['capitalExpenditures'],d['changeInReceivables'],d['changeInInventory'],\
            d['profitLoss'],d['cashflowFromInvestment'],d['cashflowFromFinancing'],\
            d['proceedsFromRepaymentsOfShortTermDebt'],d['paymentsForRepurchaseOfCommonStock'],\
            d['paymentsForRepurchaseOfEquity'],d['paymentsForRepurchaseOfPreferredStock'],\
            d['dividendPayout'],\
            d['dividendPayoutCommonStock'],d['dividendPayoutPreferredStock'],\
            d['proceedsFromIssuanceOfCommonStock'],d['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'],\
            d['proceedsFromIssuanceOfPreferredStock'],d['proceedsFromRepurchaseOfEquity'],\
            d['proceedsFromSaleOfTreasuryStock'],d['changeInCashAndCashEquivalents'],\
            d['netIncome']]
                
            for i in range(len(r)):
                if r[i] == 'None':
                    r[i] = 0

            if not self.db.is_fiscal_date_ending_exist(ds['symbol'], d['fiscalDateEnding'], 'CASHFLOW_SHEET'):
                data.append(r)
            else:
                print('find %s, %s, %s, not to work on it.' %(ds['symbol'], report_type, d['fiscalDateEnding']))

        return data

    
    def write_eps(self):
        ds = self.report.read('/data/alphavantage/', '{0}_earnings.json'.format(self.ticker))
        data = []
        data = self.__set_eps_table_cols(ds, 'annualEarnings') + self.__set_eps_table_cols(ds, 'quarterlyEarnings')
        print(data)
        self.db.insert_eps(data)

    def __set_eps_table_cols(self, ds, report_type):
        data = []
        for d in ds[report_type]:
            if report_type == 'annualEarnings':
                r =[self.ticker,1, d['fiscalDateEnding'],d['reportedEPS'],'None']
            else:
                r =[self.ticker,0, d['fiscalDateEnding'],d['reportedEPS'],d['estimatedEPS']]
                
            for i in range(len(r)):
                if r[i] == 'None':
                    r[i] = 0

            if not self.db.is_fiscal_date_ending_exist(ds['symbol'], d['fiscalDateEnding'], 'EPS'):
                data.append(r)
            else:
                print('find %s, %s, %s, not to work on it.' %(self.ticker, report_type, d['fiscalDateEnding']))

        return data

