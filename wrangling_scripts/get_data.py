import yfinance as yf

def get_stock_info(name="MSFT"):
  ticker=yf.Ticker(name)
  return ticker.history(period="1y")