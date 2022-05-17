#!/usr/bin/env python3
# Modified Altman Z-Score by Trevon Wilkins
# coding: utf-8

import yfinance as yf
from yahoofinancials import YahooFinancials

'''
This is a modified Altman Z-Score function that substitutes total revenue in place of net sales. Total revenue is used in place of net sales as most organizations do not publicize their net sales. This function works particularly well for defense contracting organizations where discounts, returns, and allowances are not a large part of the business due to the contractual nature of the work, thus may be insignificant enough to provide a well-rounded gauge of bankruptcy risk when compared to organizations of the same business interest.

Traditional Altman Z-Score
= 1.2A + 1.4B + 3.3C + 0.6D + 1.0E

Where:

A = working capital / total assets
B = retained earnings / total assets
C = earnings before interest and tax / total assets
D = market value of equity / total liabilities
E = sales / total assets

*With modification E = (total revenue / total assets)

Cite: 
https://www.investopedia.com/terms/a/altman.asp#:~:text=The%20formula%20for%20Altman%20Z,*(sales%20%2F%20total%20assets).

How To Use:
Call Function: altz_score("Enter a Ticker Symbol") -- > altz_score("MSFT")
Output: MSFT modified Altman Z-Score = X.XX

'''

def altz_score(x):
    
    try:
        ticker = yf.Ticker(x)
        ticker_financials = ticker.financials
        ticker_balance = ticker.balance_sheet

        t_rev = float(ticker_financials.loc[['Total Revenue']].iloc[0][:][0])
        ebit = float(ticker_financials.loc[['Ebit']].iloc[0][:][0])
        tot_assets= float(ticker_balance.loc[['Total Assets']].iloc[0][:][0])
        tot_liab = float(ticker_balance.loc[['Total Liab']].iloc[0][:][0])
        ret_earnings = float(ticker_balance.loc[['Retained Earnings']].iloc[0][:][0])
        working_cap = float((ticker_balance.loc[['Total Current Assets']].iloc[0][:][0]) - (ticker_balance.loc[['Total Current Liabilities']].iloc[0][:][0]))
        market_cap = ticker.info['marketCap']

        A = working_cap / tot_assets
        B = ret_earnings / tot_assets
        C = ebit / tot_assets
        D = market_cap / tot_liab
        E = t_rev / tot_assets
        altz_score = (1.2*A) + (1.4*B) + (3.3*C) + (0.6*D) + (1.0*E)
        return "{} modified Altman Z-Score = {}".format(x,"{:.2f}".format(altz_score))
    
    except:
        return "None"
