def show_welcome():
    print("Welcome to the Daily Stock Analyzer!")

show_welcome()

def show_stock(stock_name):
    print("Stock: ", stock_name)

show_stock("ABC Corporation")
show_stock("XYZ Holdings")

def calculate_change(open_price, close_price):
    change = close_price - open_price
    return change

def calculate_percent_change(open_price, close_price):
    change = close_price - open_price
    return (change / open_price) * 100

def get_market_status(change):
    if change > 0:
        return "GAIN"
    elif change < 0:
        return "LOSS"
    else:
        return "NO CHANGE"

def display_summary(
    stock_name, open_price, close_price, change, percent_change, status
):
    print("\nDAILY STOCK SUMMARY")
    print("Stock:", stock_name)
    print("Opening Price:", open_price)
    print("Closing Price:", close_price)
    print("Change:", change)
    print("Percent Change:", f"{percent_change:.2f}%")
    print("Status:", status)

stock_name = input("Enter stock name: ")
open_price = float(input("Enter opening price: "))
close_price = float(input("Enter closing price: "))

change = calculate_change(open_price, close_price)
percent_change = calculate_percent_change(open_price, close_price)
status = get_market_status(change)

display_summary(
    stock_name, open_price, close_price, change, percent_change, status
)