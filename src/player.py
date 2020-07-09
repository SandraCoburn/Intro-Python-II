# Write a class to hold player information, e.g. what room they are in
# currently.
from snake import main
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        attribute = direction + '_to'

        if hasattr(self.current_room, attribute):
            self.current_room = getattr(self.current_room, attribute)
        

        # if getattr(self.current_room, f'{direction}_to'):
        #     current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print("Sorry, you cannot move in that direction")
    
    def __str__(self):
        return f"{self.name} is in {self.current_room}"
    