# Empty list which items are added and removed from through functions. 
inventory = [""]

# Starting health.
health = 100


def intro():
    """
    Function for intro of the game. Input is required by the user.
    If input is "y" the game starts and if input is "n" the game quits.
    Any other input leads to demand for input from user again.
    """
    print("You wake up and open your eyes but you can't see anything")
    print("You stretch your arms up to your head and feel something weird.")
    print("A helmet of some sort is on your head.")
    print("You try to remove it but you can't.")
    print("You try to pull it of with all of your strength but it's stuck.\n")
    print('"... What is this... Where am I... What is going on?"\n')
    print('"... I do not remember anything... Not even my name..."\n')

    global answer

    answer = str.lower((input("Do you want to start to feel your way around? (y/n): ")))

    if answer == "y":
        box_or_search()
    elif answer == "n":
        print("\nYou give up and accept your fate.")
        print("Days go by and you finally close your eyes and never wake up.")
        game_over()
    else:
        print("Incorrect input! Please answer y/n")
        intro()


def game_over():
    """
    Prints game over message to terminal and quits game.
    """
    print("YOU DIED! GAME OVER!")
    quit()


def box_or_search():
    """
    Function that leads user to different places depending on input.
    Demands user input. While loop that runs until user input is "y" or "n".
    In any other case the user will get a message, 
    that tells them to input "y" or "n".
    """
    print("\nYou realize you will not get the helmet of.")
    print("You start using your hands to feel around.")
    print("Crawling around on your knees, you find what feels like a box.\n")
    while True:
        answer = input("Do you open the box? (y/n): ")
        if answer == "y":
            open_box()
            break
        elif answer == "n":
            print("search")
            break
        else:
            print("Incorrect input! Please answer y/n")


def open_box():
    """
    Function that leads to the following buttons game. 
    Print statements and then a function call. 
    """

    print("The box seems to be made of metal.")
    print("You can feel three buttons on the top.")
    print("You press one and suddenly a voice starts speaking to you from the box.\n")
    print('"WELCOME TO YOUR FIRST TEST."')
    print('"PLEASE ENTER PRESS THE BUTTONS IN THE RIGHT SEQUENCE!\n')
    print('"...My first test..?"')
    print('"...I guess I have to find the right sequence then..?"\n')
    buttons_game()


def search():
    """
    Function that lets the user search around the room. 
    If "key" is in the inventory list the computer_scene function is called. 
    If not, the user will have to provide input if they want to
    keep searching or return to the box.
    If they choose the box, the open_box function is called.  
    """
    print("\nYou let go of the box and keep feeling your way through the room")
    print("When moving around you feel that something is pulling lightly onto the helmet")
    print("You touch the back of your head and you can feel a small cord connected to the helmet.\n")
    print('..."What is this thing..?"\n')
    print("You keep moving around and bump into something.")
    print("It seems to be a desk and you can feel a bunch of wires.\n")
    print('"... It must be a computer..!"\n')
    print("Blindly feeling around, you some feel some sort of cavity.")
    print('"A key hole!"\n')

    while True:
        if "key" in inventory:
            print("You put the key in the key hole.")
            remove_from_inventory("key")
            print("Key was removed from your inventory\n")
            computer_scene()
            break
        else:
            answer = input("You have no key, Do you want to keep exploring or go to the box? (explore/box): ")

            if answer == "explore":
                print("You walk around but can't find anything but the box")
                answer = input("Do you want to open the box? (y/n): ")
                if answer == "y":
                    open_box()
                    break
                elif answer == "n":
                    search()
                    break

            elif answer == "box":
                open_box()
                break
            else:
                print("Incorrect input! Please answer y/n")


def add_to_inventory(item):
    """
    Adds items to inventory list.
    """
    inventory.append(item)


def remove_from_inventory(item):
    """
    Removes items to inventory list.
    """
    inventory.remove(item)


def buttons_game():
    """
    Function that gives the user 10 attempts to get the right sequence of the buttons.
    If answer is wrong, attempts decreases and if this reaches 0 the game_over function is called
    and game quits. If the user gets the right sequence, the attempts is set to 0 to
    quit the while loop and a key is added to players inventory.
    """

    attempts_left = 10
    while attempts_left > 0:
        answer = (input("Enter the button sequence (example 123): "))
        if answer != "312":
            attempts_left -= 1
            print(f'"YOU HAVE {attempts_left} ATTEMPTS LEFT"')
        else:
            attempts_left = 0
            print("\nThe box starts to buzz and then opens with a click!")
            print("You carefully put your hand inside.")
            print("You directly recognize the shape of a key!")

            add_to_inventory("key")
            search()
            computer_scene()
            break

        if attempts_left == 0:
            print("A loud buzz comes from the box.")
            print("Followed by a slow ticking noice.")
            print("The ticking intensifies.")
            print("In a blink of an eye everything around you explodes.")
            game_over()


def computer_scene():
    """
    The user enters the computer scene.
    Requires user input for choosing one of four alternatives.
    Any other input than the four alternatives gives an error message, 
    and the user must try again.


    """
    print("On the display you can see four choices\n")
    print("LOGIN\n"
          "INFORMATION\n"
          "PLAY\n"
          "LEAVE\n")
    answer = input("What do you choose? (login/information/play/leave): ")
    if answer == "login":
        print(f"You choose {answer.upper()}")

        username = "ava"
        password = "1965"

        username_guess = input("ENTER USERNAME: ")
        password_guess = input("ENTER PASSWORD: ")

        if username_guess == username and password_guess == password:
            print("USERNAME: CORRECT")
            print("PASSWORD: CORRECT")
        elif username_guess != username and password_guess == password:
            print("USERNAME: INCORRECT")
            print("PASSWORD: CORRECT")
        elif username_guess == username and password_guess != password:
            print("USERNAME: CORRECT")
            print("PASSWORD: INCORRECT")
            print("A small hatch opens")
            print("There is something inside.")
            print('"...An access card..!"')
            global access_card
            access_card = {"name": "Ava",
                           "age": "27",
                           "profession": "research scientist"}
            add_to_inventory(access_card)
            print("\nThe access card was added to your inventory.\n")
            print("At the top of the card there is a picture.")
            print('\n"...That is... me..."\n')
            print("You look at the information on the card.\n")
            for key, value in access_card.items():
                print(key, ' : ', value)
            print('"...My name is... Ava and I am a scientist."')
            print("Interrupting your thoughts, a door appears on the other side of the room.")
            computer_scene()
        else:
            print("USERNAME: INCORRECT")
            print("PASSWORD: INCORRECT")
    
    elif answer == "information":
        print("\nYOU HAVE BEEN PUT HERE TO BE TESTED.")
        print("THE TESTS WILL BE HARD AND CHALLENGING.")
        print("SOME TESTS MIGHT KILL YOU AT ONCE.")
        print("SOME TESTS MIGHT JUST HARM YOU.")
        print("FINAL TEST WILL BE GIVEN WHEN LOGGED IN.\n")
        print("A sharp pain shoots through your head")
        print("Some sort of electric chock buzz you through the helmet\n")
        decrease_health()
        computer_scene()

    elif answer == "play":
        play = True
        while play:
            print("\nYOU CHOSE PLAY, WELCOME TO THE GAME")
            print("YOU WILL BE ASKED THREE RIDDLES.")
            print("ANSWER WISELY\n")
            question_1 = "candle"
            question_1_guess = input(" I'M TALL WHEN I'm YOUNG, AND I'M SHORT WHEN I'M OLD. WHAT AM I? (candle/mountain/glass): ")
            if question_1 == question_1_guess:
                print("CORRECT! ANSWER: A candle")
            elif question_1 == "mountain" or "glass":
                print("INCORRECT!")
                print("You feel a sharp pain.")
                decrease_health()
            else:
                print("INCORRECT INPUT")
                print("You feel a sharp pain.")
                decrease_health()

            question_2 = "verb"
            question_2_guess = input(" I RUN, I WALK, I TALK. WHAT AM I? (child/verb/ghost): ")
            if question_2 == question_2_guess:
                print("CORRECT! ANSWER: V erb")
            elif question_2 == "child" or "ghost":
                print("INCORRECT!")
                print("You feel a sharp pain.")
                decrease_health()
            else:
                print("INCORRECT INPUT")
                print("You feel a sharp pain.")
                decrease_health()

            question_3 = "echo"
            question_3_guess = input(" WHAT CAN'T TALK BUT WILL REPLY WHEN SPOKEN TO? (echo/mute/scream): ")
            if question_3 == question_3_guess:
                print("CORRECT! ANSWER: A n echo")
            elif question_3 == "mute" or "scream":
                print("INCORRECT!")
                print("You feel a sharp pain.")
                decrease_health()
            else:
                print("INCORRECT INPUT")
                print("You feel a sharp pain.")
                decrease_health()

            if question_1 == question_1_guess and question_2 == question_2_guess and question_3 == question_3_guess:
                print("\nALL RIDDLES WAS ANSWERED CORRECTLY.")
                print("The computer starts to whir and a small note is printed.")
                computer_scene()
                break

            else:
                print("\nONE OR MORE INCORRECT ANSWERS, TRY AGAIN\n")


def decrease_health():
    """
    Decreases player health. Prints the health to the terminal.
    If health reaches 0 the game_over function is called.
    """
    global health
    health -= 10
    print(f"Your health: {health}\n")

    if health == 0:
        print("The pain is so sharp.")
        print("You feel panicked and fall to the ground.")
        print("Everything goes dark.")
        game_over()


def main():
    """
    Main fuction to run the other functions.
    """
    intro()


main()
