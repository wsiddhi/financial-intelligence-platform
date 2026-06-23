import yfinance as yf

def get_stock_data(symbol: str):
    stock = yf.Ticker(symbol)

    info = stock.info

    return {
        "symbol": symbol,
        "name": info.get("longName"),
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "sector": info.get("sector")
    }