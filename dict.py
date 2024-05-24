def days_to_units(days, unit):
    if unit == "hours":
        return f"{days} days are {days * 24} {unit}"
    elif unit == "mins":
        return f"{days} days are {days * 24 * 60} {unit}"
    else:
        return "unsupported unit"


def my_function():
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


user_input = ""
while user_input != "exit":
    user_input = input("Hey User, enter number of days\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1] }
    my_function()

