class Item:
    def __init__(self,  name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"{self.name}, {self.description}"

    def print_name(self):
        print(f"You have found these items in this room: {self.name}.")
        


   

