from datetime import datetime,timedelta
today=datetime.now()
print("Today's date:", today)
after_7_days=today+timedelta(days=7)
print("Date after 7 days:", after_7_days)
yesterday=today-timedelta(days=1)
print("Yesterday's date:", yesterday)

# today is the current date and time.
# timedelta(days=1) means "a time difference of 1 day."
# Subtracting timedelta(days=1) from today gives you yesterday’s date.
# In simple words:
# timedelta is like saying "how much time to add or subtract."
# If you do today - timedelta(days=1), you get the date one day before today (yesterday).
# If you do today + timedelta(days=7), you get the date seven days after today.