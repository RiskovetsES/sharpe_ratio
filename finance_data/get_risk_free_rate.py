import yfinance as yf

def get_risk_free_rate(selection):
    try:
        if selection == "US (1-Year Treasury Bond)":
            ticker = yf.Ticker("^TNX")  # Ticker for the 1-year US Treasury Bond
            rate = ticker.history(period="1y")["Close"].iloc[-1] / 100
            return rate
        elif selection == "EU (1-Year European Government Bonds)":
            ticker = yf.Ticker("BNDX")  # ETF for international bonds, including Europe
            rate = ticker.history(period="1y")["Close"].iloc[-1] / 100
            return rate
        elif selection == "Emerging Markets (1-Year Government Bonds)":
            ticker = yf.Ticker("EMB")  # Ticker for emerging markets government bonds (ETF)
            rate = ticker.history(period="1y")["Close"].iloc[-1] / 100
            return rate
        elif selection == "Corporate Bonds (1-Year Low Risk)":
            ticker = yf.Ticker("LQD")  # Ticker for investment-grade corporate bonds (ETF)
            rate = ticker.history(period="1y")["Close"].iloc[-1] / 100
            return rate
        elif selection == "S&P 500 (1-Year Average Return)":
            # Calculate the average return of S&P 500 over the last 1 year
            ticker = yf.Ticker("^GSPC")  # Ticker for the S&P 500 index
            history = ticker.history(period="1y")
            if history.empty:
                raise ValueError("Failed to retrieve data for S&P 500 index")
            start_price = history["Close"].iloc[0]
            end_price = history["Close"].iloc[-1]
            years = 1
            avg_annual_return = ((end_price / start_price) ** (1 / years)) - 1
            return avg_annual_return
    except Exception as e:
        print(f"Error while retrieving risk-free rate: {e}")
    return None
