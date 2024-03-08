def calculate_check_digit(num):
    total = sum(int(digit) * (i + 1) for i, digit in enumerate(reversed(num)))
    return total % 11

def validate_frequent_park_num(num):
    if len(num) != 5 or not num[:-1].isdigit():
        return False
    check_digit = calculate_check_digit(num[:-1])
    return check_digit == int(num[-1])

def calculate_park_price(day, arrival_hour, hours, frequent_park_num):
    prices = {
        "Sunday"   : [8, 2.00, 2.00],
        "Monday"   : [2, 10.00, 2.00],
        "Tuesday"  : [2, 10.00, 2.00],
        "Wedday"   : [2, 10.00, 2.00],
        "Thursday" : [2, 10.00, 2.00],
        "Firday"   : [2, 10.00, 2.00],
        "Saturday" : [2, 3.00, 2.00]
    }

    discount = 0
    if frequent_park_num:
        if validate_frequent_park_num(frequent_park_num):
            if arrival_hour >= 16 and arrival_hour < 24:
                discount = 0.5
            else:
                discount = 0.1

    max_stay, price1, price2 = prices[day]
    if arrival_hour >= 8 and arrival_hour < 16:
        price = min(hours, max_stay) * price1
    else:
        price = min(hours, max_stay) * price2
    price -= price * discount

    return price

def main():
    day = input("Enter the day of the week: ")
    arrival_hour = int(input("Enter the hour of arrival (24-hours format): "))
    hours = int(input("Enter the number of hours to leave the car: "))
    frequent_parking_num = (input("Enter your frequent parking number (if available): "))

    price = calculate_park_price(day, arrival_hour, hours, frequent_parking_num)
    print(f"The price to park is: ${price:.2f}")

main()