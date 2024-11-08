import yfinance as yf

def get_risk_free_rate(selection):
    try:
        if selection == "US (10-Year Treasury Bond)":
            ticker = yf.Ticker("^TNX")  # Ticker for the 10-year US Treasury Bond
            rate = ticker.history(period="1d")["Close"].iloc[-1] / 100
            return rate
        elif selection == "EU (European Government Bonds)":
            ticker = yf.Ticker("BNDX")  # ETF for international bonds, including Europe
            rate = ticker.history(period="1d")["Close"].iloc[-1] / 100
            return rate
        elif selection == "Emerging Markets (Government Bonds)":
            ticker = yf.Ticker("EMB")  # Ticker for emerging markets government bonds (ETF)
            rate = ticker.history(period="1d")["Close"].iloc[-1] / 100
            return rate
        elif selection == "Corporate Bonds (Low Risk)":
            ticker = yf.Ticker("LQD")  # Ticker for investment-grade corporate bonds (ETF)
            rate = ticker.history(period="1d")["Close"].iloc[-1] / 100
            return rate
        elif selection == "S&P 500 (10-Year Average Return)":
            # Calculate the average return of S&P 500 over the last 10 years (10-Year Average Return)
            ticker = yf.Ticker("^GSPC")  # Ticker for the S&P 500 index
            history = ticker.history(period="10y")
            if history.empty:
                raise ValueError("Failed to retrieve data for S&P 500 index")
            start_price = history["Close"].iloc[0]
            end_price = history["Close"].iloc[-1]
            years = 10
            avg_annual_return = ((end_price / start_price) ** (1 / years)) - 1
            return avg_annual_return
    except Exception as e:
        print(f"Error while retrieving risk-free rate: {e}")
    return None
