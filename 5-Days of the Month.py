days_month = {
    1: 31, 2: 28, 3: 31, 
    4: 30, 5: 31, 6: 30, 
    7: 31, 8: 31, 9: 30, 
    10: 31, 11: 30, 12: 31
}

input_month_number = int(input("Enter the month number (1-12): "))

if input_month_number in days_month:
    print(f"In {input_month_number}th month, there are: {days_month[input_month_number]} days")     
else:
    print("Invalid. Enter a real month number")

    
