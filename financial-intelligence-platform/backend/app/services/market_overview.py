import yfinance as yf

def get_market_overview():
    symbols = {
        "NIFTY50": "^NSEI",
        "SENSEX": "^BSESN",
        "RELIANCE": "RELIANCE.NS",
        "TCS": "TCS.NS",
        "INFY": "INFY.NS",
        "HDFCBANK": "HDFCBANK.NS"
    }

    result = []

    for name, symbol in symbols.items():
        try:
            stock = yf.Ticker(symbol)
            info = stock.info

            result.append({
                "name": name,
                "symbol": symbol,
                "price": info.get("currentPrice")
            })

        except Exception as e:
            result.append({
                "name": name,
                "error": str(e)
            })

    return result