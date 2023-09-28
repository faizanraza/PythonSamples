import yfinance as yf

stock = yf.Ticker("INFY.NS")
print(stock.info)
print("Fin >>", stock.financials)
print("Reco >>", stock.recommendations)
print("History >>", stock.history)
print("History >>")
print(stock.history(period="1mo", interval="1d"))