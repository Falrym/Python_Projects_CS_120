import time, random, os

room_items_dictionary = {"1": "key", "2": "candle", "3": "gold ingot"}
inventory_list  = []
items_list = ["key", "candle", "gold ingot"]

def main():
    choice = play_game()
    start_time = time.time()
    while True:
        get_time(start_time, time.time())
        if choice == "1":
            choice = enter_porch()
        elif choice == "2":
            choice = enter_entryway()
        elif choice == "3":
            choice = enter_kitchen()
        elif choice == "4":
            choice = enter_diningroom()
        elif choice == "5":
            choice = enter_livingroom()
        elif choice == "6":
            choice = enter_hallway()
        elif choice == "7":
            choice = enter_bedroom()
        elif choice == "8":
            choice = enter_masterbedroom()
        elif choice == "9":
            choice = enter_masterbath()
        else:
            break
    print("Thanks for playing!\nGOODBYE!")

def play_game():
    print("""
    Hello and welcome to  the Adventure House!
    In each room, you will be told which directions you can go.
    You can move N (north), S (south), E (east), or w (west) by
    typing the upper or lower case letter.
    Type 'Q' to end the program.
    Type 'S' to start the program!""")
    while True:
        choice = input("Enter your choice\n>>").upper()
        if choice in ["S", "Q"]:
            break
        else:
            print("Please enter a valid choice: 'S' or 'Q'\n")
    if choice == "S":
        return "1"
    else:
        return "Q"

def print_room_header(room):
    line = '=' * 25
    print(f"\n{line}{room}{line}")

def check_inventory():
    if set(inventory_list) == set(items_list):
        print("\n\nCongratulations! You've found all the items!")
        os._exit(0)

def get_time(start_time, current_time):
    minutes = 2
    time_allowed = minutes * 60
    if current_time >= start_time + time_allowed:
        print("""
        SORRY, OUT OF TIME
        GAME OVER
        YOU LOSE""")
        os._exit(0)
    else:
        seconds_left = int(time_allowed -  (time.time() - start_time))
        minutes = seconds_left // 60
        seconds = seconds_left % 60
        print(f"Time remaining: {minutes:02}:{seconds:02}")

def enter_porch():
    global room_items_dictionary, items_list, inventory_list
    print_room_header("Porch")
    print("""
    You are on the porch of a frightening looking house.
    The windows are broken. It's a dark and stormy night.
    You can go N into the house. If you dare.\n
    Your options:
    Press 'N' to enter the house
    Press 'Q' to quit the game\n""")
    option = input('Select "L" to leave or "S" to search the room.\n>> ').upper()
    if option == 'S':
        if "1" in room_items_dictionary:
            print("Searching room...")
            time.sleep(2)
            if random.randint(1, 1) == 1:
                item = room_items_dictionary.get("1")
                print(f"You found a {item}")
                inventory_list.append(item)
                del room_items_dictionary["1"]
                check_inventory()
            else:
                print("You didn't find any items")
        else:
            print("No items in  room")
    while True:
        choice = input("Enter our choice\n>> ").upper()
        if choice in ["N","Q"]:
            break
        else:
            print("Please enter a valid choice\n")
    if choice == "N":
        return "2"
    else:
        return "Q"

def enter_entryway():
    global room_items_dictionary, items_list, inventory_list
    print_room_header("Entryway")
    print("""
    You are in  the entryway of the house. There are cobwebs in the corner.
    You feel a sense of dread.
    There is a passageway to the N and another to the E.
    The porch is behind you to the S.\n""")
    option = input('Select "L" to leave or "S" to search the room.\n>> ').upper()
    if option == 'S':
        if "2" in room_items_dictionary:
            print("Searching room...")
            time.sleep(2)
            if random.randint(1, 1) == 1:
                item = room_items_dictionary.get("2")
                print(f"You found a {item}")
                inventory_list.append(item)
                del room_items_dictionary["2"]
                check_inventory()
            else:
                print("You didn't find any items")
        else:
            print("No items in  room")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["N","Q","S","E"]:
            if choice == "N":
                print("The door is locked...")
                time.sleep(2)
                if "key" in inventory_list:
                    print("You use the key to unlock the door")
                    time.sleep(2)
                    break
                else:
                    print("You can't open the door")
            elif choice == "E":
                print('The door is locked.\nSuddenly a voice speaks:\n\
                "To proceed you must answer this riddle..."')
                time.sleep(2)
                print('"The room contains a match, a kerosene lamp, a candle,  and a fireplace.\n\
                What would you light first?"')
                answer = input("Your answer:\n>> ").lower()
                if answer in ["match", "the match", "a match", "matches"]:
                    print('The voice says: "Correct. You may proceed!"\n')
                    print("You open the door and enter the next room...")
                    time.sleep(2)
                    break
                else:
                    print('The voice says: "Incorrect. You may not pass".\n')
                    time.sleep(2)
            else:
                break
        else:
            print("You can't go that way.\n")
    if choice == "N":
        return "3"
    elif choice == "S":
        return "1"
    elif choice == "E":
        return "5"
    else:
        return "Q"

def enter_kitchen():
    print_room_header("Kitchen")
    print("""
    You are in the kitchen.
    All of  the surfaces are covered with pots, pans, pieces of food, and pools of blood.
    You think you hear something up the stairs that go up the west side of the room.
    It's like a scraping noise, like something being dragged on  the floor.
    You can go U up the stairs or to the S or to the E.\n""")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q","S","E","U"]:
            if choice == "E":
                print('The door is locked.\nSuddenly a voice speaks:\n\
                "To proceed you must answer this riddle..."')
                time.sleep(2)
                print('"What gets wet while drying?"')
                answer = input("Your answer:\n>> ").lower()
                if answer in ["a towel", "towel"]:
                    print('The voice says: "Correct. You may proceed!"\n')
                    print("You open the door and enter the next room...")
                    time.sleep(2)
                    break
                else:
                    print('The voice says: "Incorrect. You may not pass".\n')
                    time.sleep(2)
            else:
                break
        else:
            print("You can't go that way.\n")
    if choice == "S":
        return "2"
    elif choice == "E":
        return "4"
    elif choice == "U":
        return "6"
    else:
        return "Q"

def enter_diningroom():
    print_room_header("Diningroom")
    print("""
    You are in the diningroom.
    There are couches, chairs, and small tables.
    There are remains of a meal on  the table.
    You can't tell what it is and maybe don't want to.
    Was that a thump to the west?
    You can go S or W.\n""")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q","S","W"]:
            break
        else:
            print("You can't go that way.\n")
    if choice == "S":
        return "5"
    elif choice == "W":
        return "3"
    else:
        return "Q"

def enter_livingroom():
    print_room_header("Livingroom")
    print("""
    You are in a livingroom. There  are couches, chairs, and small tables.
    Everything is covered in dust and spiderwebs.
    You hear a crashing noise in another room.
    You can go N or W.\n""")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q","N","W"]:
            break
        else:
            print("You can't go that way.\n")
    if choice == "N":
        return "4"
    elif choice == "W":
        return "2"
    else:
        return "Q"

def enter_hallway():
    print_room_header("Hallway")
    print("""
    You entered the hallway on the second floor.
    There are two doors, one for the normal bedroom and one for the master bedroom.
    There is one broken dangling light that shines on the blood splatter
    leading up to the master bedroom.
    You can go D downstairs or N to the bedroom or S to the master bedroom.\n""")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q","N","S","D"]:
            if choice == "N":
                print('The door is locked.\nSuddenly a voice speaks:\n\
                "To proceed you must answer this riddle..."')
                time.sleep(2)
                print('"David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?"')
                answer = input("Your answer:\n>> ").lower()
                if answer in ["david"]:
                    print('The voice says: "Correct. You may proceed!"\n')
                    print("You open the door and enter the next room...")
                    time.sleep(2)
                    break
                else:
                    print('The voice says: "Incorrect. You may not pass".\n')
                    time.sleep(2)
            else:
                break
        else:
            print("You can't go that way.\n")
    if choice == "N":
        return "7"
    elif choice == "S":
        return "8"
    elif choice == "D":
        return "3"
    else:
        return "Q"

def enter_bedroom():
    print_room_header("Bedroom")
    print("""
    You enter the bedroom.
    You take a blast of dust in the face and it clears to reveal
    a bed and tables planted to the ceiling.
    You see a note of  the empty floor that reads MB.
    What could that mean?
    Your only choice is S.\n""")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q","S"]:
            break
        else:
            print("You can't go that way.\n")
    if choice == "S":
        return "6"
    else:
        return "Q"

def enter_masterbedroom():
    print_room_header("Masterbedroom")
    print("""
    You enter the Masterbedroom.
    The sight is unbelievable, all you see is absolute white.
    It looks as if the room is infinite.
    The only thing that keeps you grounded is the blood red door knob
    to the bathroom and the door ro the hallway.
    The bathroom door creaked open.
    Travel N to the hallway or continue S to the bathroom.\n""")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q","S","N"]:
            break
        else:
            print("You can't go that way.\n")
    if choice == "S":
        return "9"
    elif choice == "N":
        return "6"
    else:
        return "Q"

def enter_masterbath():
    print_room_header("Masterbath")
    print("""
    You enter the Master bath...


    To a transparent beast who slams you against the door!
    It opens it's wide jaws to take a bite, but a distant gun shot
    made the beast jump of out the window.
    You stumble and take a look at around the bathroom.
    Full of blood and parts, a broken window.
    You take a deep breathe...    It's time to leave.\n""")
    option = input('Select "L" to leave or "S" to search the room.\n>> ').upper()
    if option == 'S':
        if "3" in room_items_dictionary:
            print("Searching room...")
            time.sleep(2)
            if random.randint(1, 1) == 1:
                item = room_items_dictionary.get("3")
                print(f"You found a {item}")
                inventory_list.append(item)
                del room_items_dictionary["3"]
                check_inventory()
            else:
                print("You didn't find any items")
        else:
            print("No items in  room")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q","N"]:
            break
        else:
            print("You can't go that way.\n")
    if choice == "N":
        return "8"
    else:
        return "Q"

main()