from datetime import datetime

def year_check():
	dateTimeObj = datetime.now()
	timeStampStr = dateTimeObj.strftime("%Y")
	int_timeStampStr = int(timeStampStr)

	user_input = input("Enter Your age/year of birth: ")
	while True:
		if len(user_input) > 3:

			year_user_input = int(user_input)

			x = int_timeStampStr - year_user_input

			print("You are {} years old".format(x))
			break

		if len(user_input) <= 2:

			age_user_intput = int(user_input)

			y = int_timeStampStr - age_user_intput

			print("You were born in {}".format(y))
			break

		#if len(user_input) <= 3:
			#year_user_input = int(user_input)
			#z = int_timeStampStr - year_user_input
			#print("That happened in {}".format(z))
			#break 

print(" ***Welcome to our the AI of Len() Function!!!!*** ")
year_check()
