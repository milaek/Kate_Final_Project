"""Escape the House!"""
import random
import time

INTRO_TEXT = "script/intro.txt"
BAD_PUNS = "script/py_puns.txt"
R2_INTRO_TEXT = "script/r2_intro.txt"

R1_OBJECTS = ["desk", "computer", "table", "gloves", "bed", "rug", "trapdoor", "mirror", "exit"]
R2_OBJECTS = ["ladder", "buttons", "panel", "chest"]
BUTTONS = ["first", "second", "third", "fourth"]


"""Controls the flow of the escape room."""


def main():
    inventory = []
    rug_up = "down"

    """run intro script"""
    name = intro()

    """run first pass of room one"""
    where_to_go = "room one"
    while True:
        if where_to_go == "room one":
            where_to_go = room_one(inventory, name, rug_up)
        elif where_to_go == "room two":
            if "rug marker" not in inventory:
                inventory.append("rug_marker")
            where_to_go = room_two(inventory, name)
        elif where_to_go == "exit":
            print("Thank you for playing!")
            break




"""Run introduction script and obtain player name"""


def intro():
    print("What is your name?")
    name = str(input(""))
    if name == "":
        name = "Karel"
    name = name.strip()
    wait()
    print("Welcome " + str(name) + ".")
    wait()
    for line in open(INTRO_TEXT):
        line = line.strip()
        print(line)
        wait()
    return name


"""Room One!"""


"""Runs the room one options and dialogue. It is passed the inventory list so that items can be added to it."""


def room_one(inventory, name, rug_up):
    if "rug_marker" in inventory:
        rug_up = "up"
    print("You are in your bedroom")
    wait()
    room_one_objects(rug_up)
    while rug_up != "descend" and rug_up != "exit":
        print("What do you want to interact with? Press enter if you would like to "
              "be reminded of the objects in this room.")
        print("")
        interact = str(input(""))
        interact = clean_input(interact)
        wait()
        while (interact not in R1_OBJECTS and interact != "") or (rug_up == "down" and interact == "trapdoor"):
            print("Try again.")
            print("")
            interact = str(input(""))
            interact = clean_input(interact)
            wait()
        rug_up = play_room_one(inventory, interact, name, rug_up)
    if rug_up == "descend":
        return "room two"
    elif rug_up == "exit":
        return "exit"


"""Interactions for room one"""


def room_one_objects(rug_up):
    print("In this room you see:")
    wait()
    for i in range(len(R1_OBJECTS)):
        if rug_up == "down" and i == 6:
            rug_up == "down"
        elif rug_up == "up" and i == 6:
            print(str(R1_OBJECTS[i]))
            wait()
        else:
            print(str(R1_OBJECTS[i]))
            wait()


"""runs the interactables depending on what user chose"""


def play_room_one(inventory, interact, name, rug_up):
    if interact == "desk":
        print("It's your desk. On it sits your computer. Otherwise, it is very tidy!")
        wait()

    if interact == "computer":
        computer_interaction(name)

    if interact == "table":
        print("Ahh, the majestic side-table.")
        wait()
        print("It looks like you left a pile of x number of gloves on top of it for easy access.")
        wait()

    if interact == "gloves":
        print("You take a number of gloves from the pile. At least two, for sure.")
        wait()
        print("You're not sure if the pile has actually shrunk at all?")
        wait()
        print("That's probably normal...")
        wait()
        if "gloves" not in inventory:
            inventory.append("gloves")

    if interact == "bed":
        print("You can't sleep now! You have things to do!")
        wait()

    if interact == "rug":
        rug_up = rug_interaction(rug_up)

    if interact == "trapdoor" and rug_up == "up":
        print("Ah yes, the trapdoor you definitely forgot was built into your floor.")
        wait()
        print("Would you like to descend?")
        descend = get_input()
        if descend == "yes":
            print("You pull open the trapdoor, and make your way down the creaky ladder leading down")
            wait()
            return "descend"
        else:
            print("You still want to do some things up here.")

    if interact == "mirror":
        print("Even after everything, its still just you " + str(name) + ".")
        wait()
        if "gloves" in inventory:
            print("Cool gloves though.")
            wait()
        elif "mask" in inventory:
            print("Spiffy mask though!")
            wait()

    if interact == "exit":
        rug_up = exit_interaction(inventory, name)

    if interact == "":
        room_one_objects(rug_up)

    return rug_up


"""interactions available through the computer object"""


def computer_interaction(name):
    print("Oh! A computer! It looks like it still has a file open...")
    wait()
    print("Would you like to look at the file? ")
    wait()
    read = get_input()
    if read == "yes":
        print('It appears to be a python file titled "' + str(name) + 's_Code_In_Place.py"')
        wait()
        print('There seems to be enough code here to execute. Would you like to run the program?')
        wait()
        run = get_input()
        if run == "yes":
            bad_puns()
    print("You leave the computer alone. Only shame lies there.")
    wait()


"""prints a random pun from the BAD_PUNS file until user chooses to exit"""


def bad_puns():
    pun_list = []
    for line in open(BAD_PUNS):
        line = line.strip()
        pun_list.append(line)
    while True:
        print("Your terminal prints the following:")
        wait()
        print(str(random.choice(pun_list)))
        wait()
        print("Would you like to run the program again?")
        wait()
        run_again = get_input()
        if run_again == "no":
            break


"""interactions available with the rug object"""


def rug_interaction(rug_up):
    if rug_up == "up":
        print("The rug is rolled up neatly on the floor.")
        wait()
        print("You consider putting it back, but realize it would probably be a waste of time at this point.")
        wait()
    else:
        print("Your rug lies spread out on the floor.")
        wait()
        print("It has a very nice pattern of repeating doors on it.")
        wait()
        print("You could probably roll it up if you felt like it.")
        wait()
        print("Would you like to roll up the rug?")
        wait()
        roll_up = get_input()
        if roll_up == "yes":
            print("You roll up the rug neatly.")
            wait()
            print("You can now see that on the floor where the rug had been covering it, there is a trapdoor.")
            wait()
            print("Huh. You'd think you'd remember having something like that in your room.")
            wait()
            print("Then again, staying in your house all day every day has been making things easier to forget.")
            wait()
            rug_up = "up"
            return rug_up
        else:
            print("You leave the rug alone for now.")
            wait()
            return rug_up


"""interaction with the exit"""


def exit_interaction(inventory, name):
    if "mask" in inventory:
        print("This is it. Are you ready to leave?")
        leaving = get_input()
        if leaving == "yes":
            print("You slide your mask onto your face, and admire your still-gloved hands. You are ready.")
            wait()
            print("You take a deep breath and reach for the doorknob.")
            wait()
            print("The sunlight is beautiful.")
            wait()
            print("Good luck out there " + str(name) + ".")
            wait()
            print("I believe in you")
            return "exit"
        else:
            print("You turn away from the door. There are still some things you want to do before leaving.")
            wait()
    else:
        print("You can't leave yet! You still don't have your mask!")
        wait()


"""room two"""


"""main room to flow"""


def room_two(inventory, name):
    room_two_intro()
    room_two_objects()
    dont_take_ladder = True
    while dont_take_ladder:
        print("What do you want to interact with? Press enter if you would like to "
              "be reminded of the objects in this room.")
        print("")
        interact = str(input(""))
        interact = clean_input(interact)
        while interact not in R2_OBJECTS and interact != "":
            print("Try again.")
            print("")
            interact = str(input(""))
            interact = clean_input(interact)
        dont_take_ladder = play_room_two(inventory, interact, name)
    return "room one"


"""intro to room two"""


def room_two_intro():
    for line in open(R2_INTRO_TEXT):
        line = line.strip()
        print(line)
        wait()


def room_two_objects():
    print("In this room you see:")
    wait()
    for i in range(len(R2_OBJECTS)):
        print(str(R2_OBJECTS[i]))
        wait()


def play_room_two(inventory, interact, name):

    if interact == "ladder":
        print("This is the ladder that leads back up into your bedroom.")
        wait()
        print("Would you like to ascend?")
        ascend = get_input()
        if ascend == "yes":
            print("You climb up the ladder carefully and re-enter your room.")
            wait()
            return False
        else:
            print("You decide to stay down here a while longer")
            wait()

    if interact == "buttons":
        buttons_interaction(inventory)

    if interact == "panel":
        panel_interaction(inventory)

    if interact == "chest":
        chest_interaction(inventory, name)

    if interact == "":
        room_two_objects()

    return True


def buttons_interaction(inventory):
    if "green key" in inventory:
        print("You've already done everything you can with this!")
        wait()
    else:
        print("You see a set of four buttons on the wall. They are arranged in a horizontal line.")
        wait()
        print('The words "Take Initiative, First to Last" are inscribed above them.')
        wait()
        print("Each button has an icosahedron with a number on it etched into it, as well as a number next to it.")
        wait()
        print("The first button has a 16 within the icosahedron, and a +2 next to it.")
        wait()
        print("The second button has a 20 within the icosahedron, and a +0 next to it.")
        wait()
        print("The third button has a 4 within the icosahedron, and a +1 next to it.")
        wait()
        print("The fourth button has a 18 within the icosahedron, and a +4 next to it.")
        wait()
        number_correct = 0
        while number_correct != 4:
            print("Would you like to press the first, second, third, or fourth button?")
            print("")
            button_pressed = str(input(""))
            button_pressed = clean_input(button_pressed)
            wait()
            while button_pressed not in BUTTONS:
                print("Try again.")
                print("")
                button_pressed = str(input(""))
                button_pressed = clean_input(button_pressed)
                wait()
            if number_correct == 0:
                if button_pressed == "second":
                    print("The button turns green.")
                    wait()
                    number_correct += 1
                else:
                    print("All of the buttons flash red, then reset.")
                    wait()
                    number_correct = 0
            elif number_correct == 1:
                if button_pressed == "fourth":
                    print("The button turns green.")
                    wait()
                    number_correct += 1
                else:
                    print("All of the buttons flash red, then reset.")
                    wait()
                    number_correct = 0
            elif number_correct == 2:
                if button_pressed == "first":
                    print("The button turns green.")
                    wait()
                    number_correct += 1
                else:
                    print("All of the buttons flash red, then reset.")
                    wait()
                    number_correct = 0
            elif number_correct == 3:
                if button_pressed == "third":
                    print("The button turns green.")
                    wait()
                    number_correct += 1
                else:
                    print("All of the buttons flash red, then reset.")
                    wait()
                    number_correct = 0
        print("You here a cheerful set of beeps and a small compartment opens next to the line of buttons.")
        wait()
        print("Inside is a green key, which you take.")
        wait()
        inventory.append("green key")


def panel_interaction(inventory):
    if "purple key" in inventory:
        print("You've already done everything you can with this!")
        wait()
    else:
        print("You see a panel in the shape of a hand on the wall.")
        wait()
        print("There appears to be a scanner within the panel.")
        wait()
        print('As you get closer, a cheerful robotic voice sings out "Safety first!"')
        wait()
        print("Would you like to put your hand on the scanner panel?")
        wait()
        scan = get_input()
        if scan == "yes":
            print("You put your hand on the panel, and the robotic voice chimes in again.")
            wait()
            print('"Scanning!"')
            wait()
            print('"Scan failed! Please remember, safety first!"')
            wait()
            if "gloves" in inventory:
                print("You suppose you could try putting on the gloves you have?")
                wait()
                print("Would you like to try again with the gloves on?")
                wait()
                gloves_on = get_input()
                if gloves_on == "yes":
                    print("You slip the gloves on and put your hand on the panel.")
                    wait()
                    print('"Scanning!"')
                    wait()
                    print('"Scan complete! Always remember to wear both gloves AND a mask when leaving the house!"')
                    wait()
                    print("A small compartment slides open next to the scanner panel, inside which is a purple key.")
                    wait()
                    print("You take the purple key.")
                    wait()
                    inventory.append("purple key")
                else:
                    print("You leave this alone for now.")
                    wait()
            else:
                print("You'll have to leave this alone for now.")
                wait()
        else:
            print("You leave this alone for now,")
            wait()


def chest_interaction(inventory, name):
    print("You see a beautiful golden chest with your name, " + str(name) + ", inscribed on top.")
    wait()
    print("There appear to be two keyholes on the chest, one green and one purple.")
    wait()
    if ("green key" in inventory and "purple key" not in inventory) or ("purple key" in inventory and "green key" not in inventory):
        print("You only have one of the two keys right now.")
        wait()
        print("Better find the other one before trying to open it!")
        wait()
    if "green key" in inventory and "purple key" in inventory:
        print("Looks like you have both of the keys.")
        wait()
        print("Would you like to open the chest?")
        wait()
        open_chest = get_input()
        if open_chest == "yes":
            print("You slide both the green and purple key into their respective locks and turn them.")
            wait()
            print("Each lock makes a pleasant clicking noise as it releases, and the top of the chest pops open.")
            wait()
            print("Inside of it, sitting neatly folded, is your mask.")
            wait()
            print("You take your mask out of the chest, and slip it into your pocket.")
            wait()
            inventory.append("mask")
        else:
            print("You'll come back later, there are other things you want to do first.")
            wait()
    else:
        print("Looks like you're going to need to go find those keys!")
        wait()



"""helper code, ie little shorteners for use"""


"""universal time delay between dialogue lines"""


def wait():
    time.sleep(0.7)


"""gets user input and makes sure it is viable"""


def get_input():
    print("")
    yes_no = str(input(""))
    yes_no = clean_input(yes_no)
    while yes_no != "yes" and yes_no != "no":
        print("Try again.")
        print("")
        yes_no = str(input(""))
        yes_no = clean_input(yes_no)
    return yes_no


"""cleans up user input to be read"""


def clean_input(text):
    text = text.strip()
    text = text.lower()
    return text

if __name__ == '__main__':
    main()