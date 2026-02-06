def stock_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 320
    }

    total_value = 0
    portfolio = {}

    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' to finish.\n")

    while True:
        stock = input("Enter stock name: ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not available.\n")
            continue

        quantity = int(input("Enter quantity: "))

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_value += stock_prices[stock] * quantity

        print("Stock added successfully.\n")

    print("\nPortfolio Summary")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        print(f"{stock}: {quantity} shares × ${price}")

    print(f"\nTotal Investment Value: ${total_value}")

if __name__ == "__main__":
    stock_tracker()
