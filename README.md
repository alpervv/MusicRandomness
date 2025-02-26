# Randomness
## Summary
This is a tool to generate binary sequences based on cryptocurrency price data. Candlesticks are fetched, and "1" is written 
on output file if the candle is green, "0" is written if it is red. Different configurations (currency, time interval) can be used.

## My Tests
I tested randomness patterns in BTCUSDT pairs. One million 1minute candles were fetched and put to NIST randomness tests. 
While most tests were successful, some key tests failed: Frequency, BlockFrequency and CumulativeSums. This is understanable since
the price of BTC has been on an uptrend in tested period.
