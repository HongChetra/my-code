from datetime import datetime

print("Welcome to Mind_Game: ")

users = str(input("Do you want to play games? ('Yes/No')")).lower()

dateTimeObj = datetime.now()
timeStampStr = dateTimeObj.strftime("%Y")
int_timeStampStr = int(timeStampStr)

if users == "no":
  print("you are not in the game.", "\nSad to see you go!")


if users == "yes":
  print("you are in the game now")


while users != "no":
	try:

		users = input("Enter Your \"age\" OR \"year of birth\": ")
	

		if len(users) > 3 or len(users) > 2:

			year_user_input = int(users)

			x = int_timeStampStr - year_user_input

			print("You are {} years old.".format(x))

			users = str(input("Play Again? ('Yes/No') ")).lower()

			if users == "no":
				print("You are out of game now")
	
		
		if len(users) <= 2:

			age_user_input = int(users)

			y = int_timeStampStr - age_user_input 

			print("You were born in {}.".format(y))

			users = str(input("Play Again? ('Yes/No')")).lower()

			if users == "no":
				print("You are out of now")
	except ValueError:
		print("Opps! can't enter letters here.")
		print(" Try Again.....!!!")



