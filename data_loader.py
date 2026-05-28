import ccxt
import pandas as pd

def fetch_futures_data(symbol="BTC/USDT", timeframe="1h", limit=1000):
    """Binance Futures'tan geçmiş verileri çeker."""
    exchange = ccxt.binance({'options': {'defaultType': 'future'}})
    
    print(f"{symbol} için {timeframe} zaman diliminde veri çekiliyor...")
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df
