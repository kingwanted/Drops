import datetime
import csv
import os

FILENAME = "period_history.csv"

# Function to calculate next period date (assumes 28-day cycle)
def calculate_next_period(start_date, cycle_length=28):
    return start_date + datetime.timedelta(days=cycle_length)

# Function to save to file
def save_period(start_date, next_date):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([start_date.strftime("%Y-%m-%d"), next_date.strftime("%Y-%m-%d")])

# Function to show history
def show_history():
    if not os.path.exists(FILENAME):
        print("No history found.")
        return
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        print("\nPeriod History:")
        print("Start Date\t\tNext Expected")
        for row in reader:
            print(f"{row[0]}\t\t{row[1]}")
    print()

# Main program
def main():
    print("Dr🩸p")

    while True:
        print("\nWhat would you like to do?")
        print("1. Track a new period")
        print("2. View period history")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            date_input = input("Enter the first day of your last period (YYYY-MM-DD): ")
            try:
                start_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
                next_period = calculate_next_period(start_date)
                print(f"Your next expected period is on: {next_period}")
                save_period(start_date, next_period)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("Goodbye! Stay healthy and hydrated3! 🌸")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
