#these are global variables
to_mins = 24 * 60
mins_units = "minutes"

#define function
#you can also provide multiple paraneters to the function
#variables defined inside function are local variables
def days_to_units(days, msg):
    print(f"{days} days is {days * to_mins} {mins_units}")
    print(msg)

#call function
days_to_units(20, "hello")
days_to_units(50, "hey")
days_to_units(70, "hallu")

#this function can only access global vars, and not the local vars defined in some other function. The days defined here is different than days defined in other funtion
def scope_check(days):
    my_vars = "variable inside function"
    print(days)
    print(mins_units)
    print(my_varsbbbb)

scope_check(2)





