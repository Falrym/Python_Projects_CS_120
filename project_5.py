import time, random, os

room_items_dictionary = {"1": "key", "2": "water bucket", "3": "steel sword", "4": "note", "5": "chest"}
door_check_dictionary = {"1": "nothing", "2": "door check", "3": "door check2", "4": "door check3"}
all_life_dictionary = {"goblin": 10, "king goblin": 50, "player": 20}
weapon_dictionary = {"wood sword": 5, "steel sword": 25}
inventory_list  = []
check_list = []
items_list = ["key", "water bucket", "steel sword", "note", "chest"]
weapon_list  = [weapon_dictionary['wood sword']]

def main():
    choice = play_game()
    start_time = time.time()
    while True:
        get_time(start_time, time.time())
        if choice == "1":
            choice = enter_entrance()
        elif choice == "2":
            choice = enter_room1()
        elif choice == "3":
            choice = enter_room2()                      #rooms
        elif choice == "4":
            choice = enter_stairway()
        elif choice == "5":
            choice = enter_corridor()
        elif choice == "6":
            choice = enter_bossroom()
        else:
            break
    print("Thank you for play the Dungeon!\nGOODBYE!")

def play_game():
    print("""
    Welcome to the Dungeon!
    Each room you can travel to with a simple direction  choice.
    Note(There will be riddles, items, and monsters) Keep an eye out.
    You can move N (north), S (south), E (east), or w (west) by
    typing the upper or lower case letter.

    A couple more things, you may or may not get an item from a room everytime.
    Fleeing from a battle will result in traveling to the room before it.

    Type Q to end the program.
    Type S to start the program!\n""")
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
    line = '=' * 30
    print(f"\n{line}{room}{line}")          #room header

def check_inventory():
    if set(inventory_list) == set(items_list):
        print("\nCongratulations! You've found all the items! You won the game!")           #check inventory
        os._exit(0)

class Monster:

    player_damage = 0

    def __init__(self, name, total_health, damage):
        self.name = name
        self.health = int(total_health)
        self.damage = damage

    def get_name(self):
        return f"{self.name}"                                   #class monster for the only two monsters

    def get_health(self):
        return self.health                                      #no inheritence because only two monsters

    def get_damage(self):
        return self.damage

    def set_player_damage(self):
        global weapon_list
        self.player_damage = max(weapon_list)

    def take_damage(self):
        self.set_player_damage()
        self.health = int(self.health - self.player_damage)

monster_1 = Monster("Goblin", 10, 2)
monster_2 = Monster("King Goblin", 50, 6)


def battle(monster):
    if monster in [monster_1, monster_2]:
        while True:
            attack = input(f"Press A to attack the {monster.get_name()}\n>>").upper()               #battle function to battle  the monsters
            if attack in ["A"]:
                damage = max(weapon_list)
                monster.take_damage()
                print(f"You deal {damage} damage, the goblin's health is now at {monster.get_health()}.")
                if monster.get_health() <= 0:
                    print(f"you have defeated the {monster.get_name()}")
                    break
                all_life_dictionary['player'] -= monster.get_damage()
                print(f"The goblin deals {monster.get_damage()} damage, you are at {all_life_dictionary['player']} health remaining\n")
                check_player_life()
            else:
                print("you cannot escape")


def check_player_life():
    if all_life_dictionary['player'] <= 0:
        print("You have died to the King Goblin, game over")                #check for death, if you die, you lose
        os._exit(0)

def get_time(start_time, current_time):
    minutes = 2
    time_allowed = minutes * 90
    if current_time >= start_time + time_allowed:                              #gets  time, if you run out of 3min you lose
        print("""
        SORRY, OUT OF TIME
        GAME OVER
        YOU LOSE""")
        os._exit(0)
    else:
        seconds_left = int(time_allowed -  (time.time() - start_time))
        minutes = seconds_left // 60
        seconds = seconds_left % 60
        print(f"\nTime remaining: {minutes:02}:{seconds:02}")

def enter_entrance():
    global room_items_dictionary, items_list, inventory_list
    print_room_header("Dungeon Entrance")
    print("""
    You are on the entrance to a Dungeon, to enter requires intelligence.
    But what will you do once in, can you fight?, we will find out. You
    start out with a wooden sword that does 5 damage and you have a health of 20.\n
    Options:
    Press S to search a room
    Press L to not search the room\n""")
    if "key" in inventory_list:
        print("you have already found the item in this room")
    else:
        option = ""
        while option not in ["S", "L"]:
            option = input("Will you search the room or not\n>>").upper()               #All rooms contain a search room input
        if option == 'S':                                                               #All contain a direction input
            if "1" in room_items_dictionary:                                            #one contains a riddle input
                print("\nSearching room...")                                            #two door are locked, one needs a key, the other needs most items
                time.sleep(2)
                if random.randint(1,2) == 1:
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
        choice = input("""
    Options:
    Press N to enter the dungeon.
    Press Q to quit the game.

Enter the dungeon or leave?\n>> """).upper()
        if choice in ["N","Q"]:
            break
        else:
            print("Please enter a valid choice")
    if choice == "N":
        return "2"
    else:
        return "Q"

def enter_room1():
    global room_items_dictionary, items_list, inventory_list
    print_room_header("Room 1")
    print("""
    You enter the first room of the house, but you see an ugly goblin!!
    what will you do? The goblin does 2 damage! Will you live?\n
    Options:
    Press E to enter battle
    Press F to flee back to the entrance
    """)
    monster = monster_1
    if monster.get_health() <= 0:
        print("The goblin is dead, you are safe.")
    else:
        decision = ""
        while decision not in ["E", "F"]:
            decision = input("Will you enter the battle or flee?\n>>").upper()
        if decision in ["E", "F"]:
            if decision == "E":
                battle(monster)
            if decision == "F":
                return "1"
    if "water bucket" in inventory_list:
        print("you have already found the item in this room")
    else:
        option = ""
        while option not in ["S", "L"]:
            option = input("""
    Options:
    Press S to search the room.
    Press L to not  search the room.

Will you search the room or not\n>>""").upper()
        if option == 'S':
            if "2" in room_items_dictionary:
                print("Searching room...")
                time.sleep(2)
                if random.randint(1,2) == 1:
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
        choice = input("""
    Options:
    Press N to travel north.
    Press E to travel East.
    Press S to travel South to the entrance.

Which direction?\n>> """).upper()
        if choice in ["N","Q","S","E"]:
            if choice == "N":
                if "door check" in check_list:
                    print("the door opens")
                    time.sleep(2)
                    break
                else:
                    print("The door is locked...")
                    time.sleep(2)
                    if "key" in inventory_list:
                        print("You use the key to unlock the door")
                        time.sleep(1)
                        item = door_check_dictionary.get("2")
                        check_list.append(item)
                        del door_check_dictionary["2"]
                        break
                    else:
                        print("You can't open the door")
            elif choice == "E":
                if "door check2" in check_list:
                    print("the door opens")
                    time.sleep(2)
                    break
                else:
                    print("The door is locked.")
                    print("Suddenly a voice speaks:\n")
                    print('''"To proceed you must answer this riddle..."''')
                    time.sleep(2)
                    print('"What, breathes, consumes, and grows, but was and never will be alive."')
                    answer = input("Your answer: ").lower()
                    if answer in ["fire", "the fire", "a fire"]:
                        item = door_check_dictionary.get("3")
                        check_list.append(item)
                        del door_check_dictionary["3"]
                        print('\nThe voice says: "Correct. You may proceed!"')
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
        return "4"
    elif choice == "S":
        return "1"
    elif choice == "E":
        return "3"
    else:
        return "Q"

def enter_room2():
    print_room_header("Room 2")
    print("""
    You enter the second room, there is a large fire scorching in the room.
    How will you search the room? Only one way to find out.

    Options:
    Press S to search the room.
    Press L to not search  the room.\n""")
    if "steel sword" in inventory_list:
        print("you have already found the item in this room")
    else:
        option = ""
        while option not in ["S", "L"]:
            option = input("Will you search the room or not\n>>").upper()
        if option == 'S':
            time.sleep(2)
            if "water bucket" in inventory_list:
                print("You use the bucket to take out the fire.\n")
                time.sleep(2)
                if "3" in room_items_dictionary:
                    print("Searching room...")
                    time.sleep(2)
                    if random.randint(1,2) == 1:
                        item = room_items_dictionary.get("3")
                        item2 = weapon_dictionary.get("steel sword")
                        print(f"You found a {item}")
                        inventory_list.append(item)
                        weapon_list.append(item2)
                        del room_items_dictionary["3"]
                        check_inventory()
                    else:
                        print("You didn't find any items")
                else:
                    print("No items in room")
            else:
                print("you cannot search the room")
    while True:
        choice = input("""
    Options:
    Press W to go west.

Which direction?\n>> """).upper()
        if choice in ["Q","W"]:
            break
        else:
            print("You can't go that way.")
    if choice == "W":
        return "2"
    else:
        return "Q"

def enter_stairway():
    print_room_header("Stairway")
    print("""
    You have entered a dark stairway leading downward, what awaits you?

    Options:
    Press S to search the room.
    Press L to not search the room.\n""")
    if "nothing" in check_list:
        print("you have already searched this room")
    else:
        option = ""
        while option not in ["S", "L"]:
            option = input("Will you search the room or not\n>>").upper()
        if option == 'S':
            if "1" in door_check_dictionary:
                print("Searching room...")
                time.sleep(2)
                if random.randint(1,2) == 1:
                    item = door_check_dictionary.get("1")
                    print("no items in room\n")
                    check_list.append(item)
                    del door_check_dictionary["1"]
    while True:
        choice = input("""
    Options:
    Press S to travel south.
    Press D to travel down the stairs.

Which direction?\n>> """).upper()
        if choice in ["Q","S","D"]:
            break
        else:
            print("You can't go that way.")
    if choice == "S":
        return "2"
    elif choice == "D":
        return "5"
    else:
        return "Q"

def enter_corridor():
    print_room_header("Corridor")
    print("""
    You are in the corridor, will a giant door to tour south and the stairs to go up.
    The only thing left to do is to open the door, have to got everything you need?

    Options:
    Press S to search the room.
    Press L to not search the room\n""")
    if "note" in inventory_list:
        print("you have already found the item in this room")
    else:
        option = ""
        while option not in ["S", "L"]:
            option = input("Will you search the room or not\n>>").upper()
        if option == 'S':
            if "4" in room_items_dictionary:
                print("Searching room...")
                time.sleep(2)
                if random.randint(1,2) == 1:
                    item = room_items_dictionary.get("4")
                    print(f"You found a {item}\n")
                    inventory_list.append(item)
                    del room_items_dictionary["4"]
                    check_inventory()
                else:
                    print("You didn't find any items")
            else:
                print("No items in  room")
    while True:
        choice = input("""
    Options:
    Press S to open the door.
    Press U to travel up the stairs.

Which direction?\n>> """).upper()
        if choice in ["Q","U","S"]:
            if choice == "S":
                if "door check3" in check_list:
                    print("the door opens")
                    time.sleep(2)
                    break
                elif "key" and "water bucket" and "note" in inventory_list:
                    print("You have all the items, the door unlocks")
                    time.sleep(2)
                    item = door_check_dictionary.get("4")
                    check_list.append(item)
                    del door_check_dictionary["4"]
                    break
                else:
                    print("The door is locked...")
                    print("You can't open the door")
                    time.sleep(2)
            else:
                break
        else:
            print("You can't go that way.")
    if choice == "U":
        return "4"
    elif choice == "S":
        return "6"
    else:
        return "Q"

def enter_bossroom():
    print_room_header("BOSSROOM")
    print("""
    ... You are met with the biggest Goblin you have ever seen.
    It appears to have armour, will your sword do well?

    Options:
    Press E to enter the battle.
    Press L to flee the battle.\n""")
    monster = monster_2
    if monster.get_health() <= 0:
        print("king goblin defeated")
    else:
        decision = ""
        while decision not in ["E", "F"]:
            decision = input("Will you enter the battle or flee?\n>>").upper()
        if decision in ["E", "F"]:
            if decision == "E":
                battle(monster)
            if decision == "F":
                return "5"
    if "chest" in inventory_list:
        print("you have already found the item in this room")
    else:
        option = ""
        while option not in ["S", "L"]:
            option = input("""
    Options:
    Press S to search the room.
    Press L to not search the room.

Will you search the room or not\n>>""").upper()x
        if option == 'S':
            if "5" in room_items_dictionary:
                print("Searching room...")
                time.sleep(2)
                if random.randint(1,1) == 1:
                    item = room_items_dictionary.get("5")                                   #bossroom you win, if you have all items
                    print(f"You found a {item}\n")                                          #finally there is safe gaurds for if you have already opened
                    time.sleep(2)                                                           #a door, you dont have to go through that sequence again
                    inventory_list.append(item)                                             #same with defeating a monster
                    del room_items_dictionary["5"]
                    check_inventory()
                else:
                    print("You didn't find any items")
            else:
                print("No items in  room")
    while True:
        choice = input("""
    Options:
    Press N to go north.

Which direction?\n>> """).upper()
        if choice in ["Q","N"]:
            break
        else:
            print("You can't go that way.")
    if choice == "N":
        return "5"
    else:
        return "Q"

main()