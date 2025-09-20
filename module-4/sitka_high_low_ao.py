import csv
import matplotlib.pyplot as plt
from datetime import datetime
import sys

# Set file name
filename = 'sitka_weather_07-2018_simple.csv'

# Read the CSV data
dates, highs, lows = [], [], []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {row[2]}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Menu function
def show_menu():
    print("\nMenu Options:")
    print("1 - Show High Temperatures")
    print("2 - Show Low Temperatures")
    print("3 - Exit")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        plt.style.use('seaborn-v0_8')  # safe seaborn style
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        ax.set_title("Daily High Temperatures - July 2018", fontsize=24)
        ax.set_xlabel('', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (F)", fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == "2":
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        ax.set_title("Daily Low Temperatures - July 2018", fontsize=24)
        ax.set_xlabel('', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Temperature (F)", fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == "3":
        print("Exiting the program. Have a great day!")
        sys.exit()

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


