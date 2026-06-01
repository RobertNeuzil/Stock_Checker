import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_price(SPY):
    """
    Fetches the latest stock price using yfinance.
    """
    try:
        stock = yf.Ticker(SPY)
        price = stock.history(period="1d")['Close'].iloc[-1]
        return price
    except Exception as e:
        print(f"Error fetching price for {SPY}: {e}")
        return None

def portfolio_tracker():
    # Step 1: Gather user input with error handling
    while True:
        try:
            num_stocks = int(input("Enter the number of stocks in your portfolio:"))
            if num_stocks <= 0:
                raise ValueError("Number of stocks must be greater than 0.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
    
    # Initialize an empty list to store portfolio data
    portfolio_data = []
    
    for i in range(num_stocks):
        while True:
            try:
                stock = input(f"Enter the ticker symbol of stock {i + 1}: ").upper()
                quantity = int(input(f"Enter the quantity of {stock}: "))
                if quantity <= 0:
                    raise ValueError("Quantity must be greater than 0.")
                
                # Fetch real-time stock price
                price = get_stock_price(stock)
                if price is None:
                    raise ValueError(f"Unable to fetch price for {stock}.")
                
                portfolio_data.append({'Stock': stock, 'Quantity': quantity, 'Price': price})
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
    
    # Step 2: Create a DataFrame
    portfolio_df = pd.DataFrame(portfolio_data)
    
    # Step 3: Calculate Total Value of Each Stock
    portfolio_df['Value'] = portfolio_df['Quantity'] * portfolio_df['Price']
    
    # Step 4: Calculate Total Portfolio Value
    total_portfolio_value = portfolio_df['Value'].sum()
    
    # Step 5: Calculate Percentage Allocation
    portfolio_df['Allocation (%)'] = (portfolio_df['Value'] / total_portfolio_value) * 100
    
    # Step 6: Display Results
    print("\nPortfolio Summary:")
    print(portfolio_df)
    print(f"\nTotal Portfolio Value: ${total_portfolio_value:,.2f}")
    
    # Step 7: Visualization
    plt.figure(figsize=(8, 6))
    plt.pie(portfolio_df['Allocation (%)'], labels=portfolio_df['Stock'], autopct='%1.1f%%', startangle=140)
    plt.title("Portfolio Allocation")
    plt.show()

# Run the Portfolio Tracker

portfolio_tracker()
input("\nPress Enter to exit...")


