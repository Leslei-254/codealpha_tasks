import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 200
}

portfolio = []
total_investment = 0

print("=" * 45)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 45)

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        portfolio.append([
            stock,
            quantity,
            stock_prices[stock],
            investment
        ])

        print(f"{stock} added successfully!")

    except ValueError:
        print("Please enter a valid number.")

# Display Summary
print("\n" + "=" * 45)
print("PORTFOLIO SUMMARY")
print("=" * 45)

for item in portfolio:
    print(
        f"Stock: {item[0]} | "
        f"Quantity: {item[1]} | "
        f"Price: ${item[2]} | "
        f"Value: ${item[3]}"
    )

print("-" * 45)
print(f"Total Investment Value: ${total_investment}")

# Save to CSV
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Stock",
        "Quantity",
        "Price",
        "Investment"
    ])

    writer.writerows(portfolio)

print("\nPortfolio saved successfully to portfolio.csv")
