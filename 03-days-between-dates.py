#!/usr/bin/env python3
# Day 03 

# Calculate the number of days between two dates

from datetime import datetime

def days_between_dates(date1, date2):
    # Convert the date strings to datetime objects
    date1_obj = datetime.strptime(date1, '%Y-%m-%d')
    date2_obj = datetime.strptime(date2, '%Y-%m-%d')
    
    # Calculate the difference between the two dates
    delta = date2_obj - date1_obj
    
    # Return the number of days as an absolute value
    return abs(delta.days)

# Example usage:
date1 = '2024-01-01'
date2 = '2024-03-06'

print("Number of days between", date1, "and", date2, ":", days_between_dates(date1, date2))

