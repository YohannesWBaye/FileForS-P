import yfinance as yf
import pandas as pd
import csv

# Get S&P 500 tickers
def get_sp500_tickers():
    # Fetch the list of S&P 500 companies from Wikipedia
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table = pd.read_html(url)
    sp500_table = table[0]
    sp500_tickers = sp500_table['Symbol'].tolist()

    if not sp500_tickers:
        print("Unable to retrieve tickers. Ensure 'pandas' is installed and configured correctly.")
        return []
    else:
        return sp500_tickers

# Fetch and format tickers
tickers = get_sp500_tickers()

# Create a CSV file with the tickers
with open('sp500_tickers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Ticker'])
    for ticker in tickers:
        writer.writerow([ticker])

tickers_str = ", ".join(tickers)
print(f"S&P 500 Tickers:\n{tickers_str}")
