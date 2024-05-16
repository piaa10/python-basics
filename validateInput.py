to_hours = 24
mins_units = "hours"


def days_to_units(days):
    if days > 0:
        return f"{days} days are {days * to_hours} {mins_units}"
    elif days == 0:
        return "zero is not a valid answer"
    #else:
    #    return "negative value not expected"


user_input = input("Hey User, enter number of days\n")
if user_input.isdigit():
    int_input = int(user_input)
    #final_value = days_to_units(int(user_input))
    final_value = days_to_units(int_input)
    print(final_value)
else:
    print("invalid input")
