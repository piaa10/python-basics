to_hours = 24
mins_units = "hours"

def days_to_units(days):
    return f"{days} days are {days * to_hours} {mins_units}"

user_input = input("Hey User, enter number of days\n")
int_input = int(user_input)
final_value = days_to_units(int_input)
print(final_value)
