from datetime import datetime, timedelta

def get_future_date(days_ahead):
    """Returns the date a specified number of days in the future."""
    target_date = datetime.now() + timedelta(days=days_ahead)
    return target_date.strftime("%Y-%m-%d")

# Program execution
print("Date 10 days from now:", get_future_date(10))