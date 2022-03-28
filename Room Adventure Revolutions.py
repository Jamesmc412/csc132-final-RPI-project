#################################################################
# Name:
# Date:
# Description:
#################################################################
from tkinter import *

#the room class
class Room:
    #the constructor
    def __init__(self, name, image):
        #rooms have a name, an image, exits, exit locations, item descriptions, and grabbables
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []

    #getters and setter for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, value):
        self._items = value
    
    @property
    def grabbables(self):
        return self._grabbables
    
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
    
    #adds an exit to the room
    #the item is a string
    #the room is an instance of a room
    def addExit(self, exit, room):
        #append the exit and room to the appropriate
        #dictionary
        self._exits[exit] = room
    
    #adds an item to the room as a string and the desc is a string as well to describe the item
    def addItem(self, item, desc):
        #append the item and desc to appropriate dictionary
        self._items[item] = desc
    
    #adds a grabbable as a string
    def addGrabbable(self, item):
        #append the item to the list
        self._grabbables.append(item)
        
    #removes a grabbable
    def delGrabbable(self, item):
        #removes grabbable from list
        self._grabbables.remove(item)
    
    #returns a string description of the room
    def __str__(self):
        #the room name
        s = "You are in {}.\n".format(self.name)
        
        #the visible items
        s += "You see: "
        for item in self.items,keys():
            s += item + " "
        s += "\n"
        
        #the exits from the room
        s += "Exits: "
        for exit in self.exits.keys.keys():
            s += exit + " "
        return s

#the game class
#inherits from the Fram class of Tkinter


    
##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600
# create the window
window = Tk()
window.title("Room Adventure")
# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()
