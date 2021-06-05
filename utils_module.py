import os


def welcome_message():
    welcome = """
    ****************************************************************************************
    *                                   Welcome,stranger.                                  *
    * Here in Hinderlands, You'll get to fight dragons and conquer the deadliest dungeons. *
    *        In a country where magic rules, anything is possible if you wish so.          *
    *                          It all depends on you, brave hero.                          *
    ****************************************************************************************
    """
    print(welcome)


def start_adventure():
    print("Would You like to start the adventure?")
    user_answer = input("Yes or No -> ")
    if user_answer.upper() == "YES":
        print("OK")
        os.system("cls")  # windows
        # os.system("clear")  # mac/linux/bash
    else:
        print("Thank You, good bye!")
