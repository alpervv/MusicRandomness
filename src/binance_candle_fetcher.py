import os
from binance.client import Client

API_KEY = 'your_api_key'  # Replace with your Binance API key
API_SECRET = 'your_api_secret'  # Replace with your Binance secret key

def fetch_candlestick_data(client, symbol, interval, limit, start_time):
    try:
        klines = client.get_klines(symbol=symbol, interval=interval, limit=limit, startTime=start_time)
        return klines
    except Exception as e:
        print(e.message)

def process_candlestick_data(klines):
    """
    Processes candlestick data to determine green and red candles.
    Returns an list of 1 (green) and 0's (red). 
    """
    candle_colors = []
    for kline in klines:
        open_price = float(kline[1])
        close_price = float(kline[4])
        candle_colors.append("1" if close_price > open_price else "0")
    return candle_colors


def main(output_file):
    client = Client(API_KEY, API_SECRET)
    symbol = 'BTCUSDT'
    interval = Client.KLINE_INTERVAL_1MINUTE # Adjust according to your needs
    limit = 1000  # Maximum limit per API call

    # Fetch 1,000,000 candles (split into chunks)
    total_candles = 1_000_000 # Be careful when setting this value, there may not be enough candles historically
    chunks = total_candles // limit
    start_time = None

    print("Fetching candlestick data from Binance...")
    with open(output_file, 'w') as file:
        for i in range(chunks):
            # Fetch chunk of candlestick data
            candles = fetch_candlestick_data(client, symbol, interval, limit,start_time)
            candle_colors = process_candlestick_data(candles)
            file.write("".join(candle_colors))
            file.flush()

            # Adjust starting timestamp for the next chunk
            last_timestamp = candles[0][0]
            start_time = last_timestamp - limit*60000
            

            print(f"Fetched {(i+1)*limit} candles so far...")

    print(f"Data written to {output_file}")

if __name__ == "__main__":
    main("btc_data.txt")
