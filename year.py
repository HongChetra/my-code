from datetime import datetime


class all_conditions():

    def first_message(self):
        print('\n')
        print("Welecome to Our Smart_Caculator!!")

    def test_message(self):
        print("\n")

        users = input("Do you want to Try...? ('Yes/No')").lower()

        print('\n')

        if users == "yes":
            print("You are in the game now.")

            print('\n')

        if users == "no":
            print("Oh Sad!@@@")


        DateTimeObj = datetime.now()
        TimeToStr = DateTimeObj.strftime("%Y")
        Int_TimeToStr = int(TimeToStr)

        while users != "no":
            try:
                users_input = int(input("Enter age or year of birth: "))
                print('\n')

                if len(str(users_input)) == 4: # to find how old is the user

                    result_of_age = Int_TimeToStr - users_input

                    print("You are {} years old.".format(result_of_age))

                    print('\n')

                    users = input("Play Again? ('Yes/No')").lower()
                    print('\n')

                    if users == "no":
                        print("You are out of game now.")


                if len(str(users_input)) == 3: # find when thing happended

                    result_of_time = Int_TimeToStr - users_input

                    print("That happended in {}.".format(result_of_time))

                    print('\n')

                    users = input("Play Again? ('Yes/No')").lower()

                    print('\n')

                    if users == "no":
                        print("You are out of game now.")
                
                if len(str(users_input)) == 2: # to find what year is the user was born

                    result_of_year = Int_TimeToStr - users_input

                    print("You were born in {}.".format(result_of_year))
                    print('\n')

                    users = input("Play Again? ('Yes/No')").lower()
                    print('\n')

                    if users == "no":
                        print("You are out of game now.")

            except ValueError:
                print('\n')
                print({"Error": "Can't Enter Letters!"})
                print('\n')

year = all_conditions()
year.first_message()
year.test_message()
#year.test_users_input()
