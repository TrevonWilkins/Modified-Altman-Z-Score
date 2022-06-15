#!/usr/bin/env python3
# Modified Altman Z-Score by Trevon Wilkins
# coding: utf-8

from yahoofinancials import YahooFinancials

def altz_score(x):
    
    '''
    This is a modified Altman Z-Score function that substitutes total revenue in place of net sales.
    Total revenue is used in place of net sales as most organizations do not publicize their net sales.
    This function works particularly well for defense contracting organizations where discounts, 
    returns, and allowances are not a large part of the business due to the contractual nature of the 
    work, thus the aformentioned values may be insignificant enough to provide a well-rounded gauge of 
    bankruptcy risk when compared to organizations of the same business interest.
    
    Traditional Altman Z-Score = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E

        Where:
            A = working capital / total assets
            B = retained earnings / total assets
            C = earnings before interest and tax / total assets
            D = market value of equity / total liabilities
            E = sales / total assets

            *With modification E = (total revenue / total assets)
            
    How To Use:
        - Call Function: altz_score("Enter a Ticker Symbol") -- > altz_score("MSFT")
        - Output: MSFT modified Altman Z-Score = X.XX

    ---------------------------------------------------------------------------------------------------
    
    References:
        https://www.investopedia.com/terms/a/altman.asp#
        https://pypi.org/project/yahoofinancials/

    '''
    try:
        statements = YahooFinancials(x).get_financial_stmts('annual', ['balance','income'], reformat=True)
        ticker_balance = statements['balanceSheetHistory'][x][0][list(statements['balanceSheetHistory'][x][0].keys())[0]]
        ticker_financials = statements['incomeStatementHistory'][x][0][list(statements['balanceSheetHistory'][x][0].keys())[0]]

        t_rev = ticker_financials['totalRevenue']
        ebit = ticker_financials['ebit']
        tot_assets = ticker_balance['totalAssets']
        tot_liab = ticker_balance['totalLiab']
        ret_earnings = ticker_balance['retainedEarnings']
        working_cap = ticker_balance['totalCurrentAssets'] - ticker_balance['totalCurrentLiabilities']
        market_cap = YahooFinancials(x).get_market_cap()

        A = working_cap / tot_assets
        B = ret_earnings / tot_assets
        C = ebit / tot_assets
        D = market_cap / tot_liab
        E = t_rev / tot_assets
        altz_score = (1.2*A) + (1.4*B) + (3.3*C) + (0.6*D) + (1.0*E)
        return "{} modified Altman Z-Score = {}".format(x,"{:.2f}".format(altz_score))
    
    except:
        return "None"
