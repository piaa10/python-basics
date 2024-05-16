to_mins = 24 * 60
mins_units = "minutes"

def days_to_units(days):
    return f"{days} days is {days * to_mins} {mins_units}"

var1 = days_to_units(20)
print(var1)

