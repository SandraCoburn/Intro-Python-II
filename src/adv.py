from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def game():
    room_name = "outside"
    #directions = ["n", "s", "e", "w"]
    yes_no = ["yes", "no"]
    current_room = room[room_name]

    #introduction:   
    name = input("What is your name?\n")
   
    player1 = Player(name, current_room)
    print(f"Greetings, {player1.name}. Let us start the adventure!")
    print(f"You are currently {player1.current_room}")
    
    
          
    #Start of game:
    response = ""
    while response not in yes_no:
        response = input("Would you like to start the game?\nyes/no\n")
        if response == "yes":
            print("You will step into the first room. What are you gonna find?")
        elif response == "no":
            print("You are not ready for this adventure. Good bye!")
            quit()
        else: 
            print("I didn't understant that. Type yes or no. \n")
    response = ""
    while response != "q":
        response = input("Which direction you want to go? [n], [s], [e] or [w]")
        if response == "n":
            current_room = current_room.n_to
            print(f"You are heading to the {current_room}")
        else:
            print("I didn't understand that. Enter n, s, e, or w to move or q to quit.\n")
    print("Thanks for playing!")
game()


