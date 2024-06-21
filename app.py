from datetime import datetime, timedelta

def calculate_future_date(days_from_now):
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the future date
    future_date = current_date + timedelta(days=days_from_now)
    
    return future_date

# Input number of days from the user
days = int(input("Enter the number of days from now: "))

# Calculate the future date
future_date = calculate_future_date(days)

# Print the result in full date format
print(f"The date {days} days from now will be: {future_date.strftime('%d %B %Y')}")
