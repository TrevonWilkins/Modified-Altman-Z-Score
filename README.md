# Modified-Altman-Z-Score

This is a modified Altman Z-Score function that substitutes total revenue in place of net sales. Total revenue is used in place of net sales as most organizations do not publicize their net sales. This function works particularly well for defense contracting organizations where discounts, returns, and allowances are not a large part of the business due to the contractual nature of the work, thus the alteration is ideally insignificant enough to provide a well-rounded gauge of probability of bankruptcy when compared to organizations of the same business interest.

"
Altman Z-Score = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E

Where:

A = working capital / total assets
B = retained earnings / total assets
C = earnings before interest and tax / total assets
D = market value of equity / total liabilities
E = sales / total assets
"
Cite: 
Kenton, W. (2003, November 18). What is the Altman Z-score? Investopedia. Retrieved April 12, 2022, from https://www.investopedia.com/terms/a/altman.asp#:~:text=The%20formula%20for%20Altman%20Z,*(sales%20%2F%20total%20assets)


*With modification E = (total revenue / total assets)

How To Use:
Step 1: altz_score("Enter a Ticker Symbol") -- > altz_score("MSFT")
Output: MSFT modified Altman Z-Score = X.XX
