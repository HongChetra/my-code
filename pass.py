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
    

  #users = input("Do you want to play games? ('Yes'/'No')").lower()
  #def year_check():
 #if "Yes":

while users != "no":
  
  user_input = input("Enter Your \"age\" OR \"year of birth\": ")

  if len(user_input) > 3:

    year_user_input = int(user_input)

    x = int_timeStampStr - year_user_input

    print("You are {} years old.".format(x))

    users = str(input("play games? ('Yes/No')")).lower()

    if users == "no":
      print("You are out now.")

  if len(user_input) <= 2:

    age_user_intput = int(user_input)

    y = int_timeStampStr - age_user_intput

    print("You were born in {}.".format(y))

    users = str(input("play again លេង? ('Yes/No')")).lower()

    if users == "no":
      print("You are out now.")
