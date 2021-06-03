import os

welcome_message = """
****************************************************************************************
* Welcome,stranger.                                                                    *
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons. *
* In a country where magic rules, anything is possible if you wish so.                 *
* It all depends on you, brave hero.                                                   *
****************************************************************************************
"""
print(welcome_message)
print("Would You like to start the adventure?")
user_answer = input("Yes or No -> ")
if user_answer.upper() == "YES":
    print("OK")
    os.system("cls")  # windows
else:
    print("Thank You, good bye!")
