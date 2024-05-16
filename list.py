to_hours = 24
mins_units = "hours"


def days_to_units(days):
    return f"{days} days are {days * to_hours} {mins_units}"


def my_function():
    try:
            int_input = int(num_of_days)
            if int_input > 0:
                final_value = days_to_units(int_input)
                print(final_value)
            elif int_input == 0:
                print("zero is not a valid answer")
            else:
                print("you are wrong")

    except ValueError:
        print("Invalid Input")


user_input = ""
while user_input != "exit":
    user_input = input("Hey User, enter number of days\n")
    for num_of_days in user_input.split(","):
        my_function()
