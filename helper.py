def days_to_units(days, unit):
    if unit == "hours":
        return f"{days} days are {days * 24} {unit}"
    elif unit == "mins":
        return f"{days} days are {days * 24 * 60} {unit}"
    else:
        return "unsupported unit"


def my_function(days_and_unit_dict):
    int_input = int(days_and_unit_dict["days"])
    try:
        if int_input > 0:
            final_value = days_to_units(int_input, days_and_unit_dict["unit"])
            print(final_value)
        elif int_input == 0:
            print("zero is not a valid answer")
        else:
            print("ugh invalid input")
    except ValueError:
        print("Invalid Input")


user_input_message = "Hey User, enter number of days\n"