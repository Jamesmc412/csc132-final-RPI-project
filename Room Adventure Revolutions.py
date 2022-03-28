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
