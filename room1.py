class Room:
    number_of_rooms = 0
    number_of_exits = 1

    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

        Room.number_of_rooms += 1 # every time you add a room,  it will count it.

    def get_description(self):
        return f"Name: {self.name}\nDescription: {self.description}\nExits: {self.exits}\n"

    def num_of_exits(self):
        self.exits = int(self.exits * self.number_of_exits)

room_1 = Room("Main  Hall", "dusty", 3)
room_2 = Room("Fire Room", "burnt", 1)

room_1.number_of_exits = 2
room_1.num_of_exits()

print(f"Number of rooms: {Room.number_of_rooms}\n") # will print the number of room you have created
print(room_1.get_description()) # the number of exits is changed
# print(room_2.get_description())