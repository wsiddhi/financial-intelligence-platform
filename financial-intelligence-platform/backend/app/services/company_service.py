import pandas as pd
import yfinance as yf

COMPANIES_CSV = "data/companies.csv"

_df_cache = None


def get_dataframe():
    global _df_cache

    if _df_cache is None:
        df = pd.read_csv(COMPANIES_CSV)
        df = df.fillna("")

        df["symbol"] = df["symbol"].astype(str)
        df["name"] = df["name"].astype(str)

        _df_cache = df

    return _df_cache


def search_companies(query: str, limit: int = 15):

    df = get_dataframe()

    query = query.lower().strip()

    if not query:
        return []

    # Exact matches first
    exact_matches = df[
        (df["symbol"].str.lower() == query) |
        (df["name"].str.lower() == query)
    ]

    # Partial matches
    partial_matches = df[
        (df["symbol"].str.lower().str.contains(query, na=False)) |
        (df["name"].str.lower().str.contains(query, na=False))
    ]

    # Combine and remove duplicates
    result = pd.concat([exact_matches, partial_matches])
    result = result.drop_duplicates(subset=["symbol"])

    companies = []

    for _, row in result.head(limit).iterrows():
        companies.append({
            "symbol": row["symbol"],
            "name": row["name"]
        })

    return companies


def get_company_details(symbol: str):
    try:
        ticker = yf.Ticker(f"{symbol}.NS")

        info = ticker.info

        return {
            "symbol": symbol,
            "name": info.get("longName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "market_cap": info.get("marketCap"),
            "current_price": info.get("currentPrice"),
            "pe_ratio": info.get("trailingPE"),
            "week52_high": info.get("fiftyTwoWeekHigh"),
            "week52_low": info.get("fiftyTwoWeekLow"),
            "website": info.get("website")
        }

    except Exception as e:
        return {
            "error": str(e)
        }