from datetime import datetime

user_input = input("Enter you goal with deadline\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
#calculate how many days from now to deadline

now = datetime.today()
remaining_time = deadline_date - now

print(f"Time remaining for your goal: {goal} is {remaining_time.days} days")


