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

# Fetch historical data for each ticker
def fetch_historical_data(tickers, start_date, end_date):
    all_data = []
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        data = yf.download(ticker, start=start_date, end=end_date)
        data['Ticker'] = ticker
        all_data.append(data)
    return pd.concat(all_data)

# Main function
def main():
    tickers = get_sp500_tickers()
    start_date = '2006-01-01'
    end_date = '2010-12-31'
    historical_data = fetch_historical_data(tickers, start_date, end_date)

    # Save to CSV
    historical_data.to_csv('sp500_historical_data_2006_2010.csv')
    print("Data saved to sp500_historical_data_2006_2010.csv")

if __name__ == "__main__":
    main()
