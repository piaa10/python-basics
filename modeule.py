#import helper
from helper import my_function, user_input_message

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1] }
    #helper.my_function(days_and_unit_dict)
    my_function(days_and_unit_dict)