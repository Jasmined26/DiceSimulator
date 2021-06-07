# Developed by Jasmine Jenkins
# https://github.com/Jasmined26

# Import modules needed to run program
import tkinter
from random import randint
import tkinter.font as tkFont

class DieSimulator:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()
        
        # Define window properties
        self.main_window.title("Dice Simulator V1")
        self.main_window.geometry("265x200")
        self.main_window['background'] = '#00ebff'

        # Define window fonts
        window_font = tkFont.Font(family = 'Bahnschrift', size = 50)
        window_font2 = tkFont.Font(family = 'Bahnschrift', size = 14)
        window_font3 = tkFont.Font(family = 'Bahnschrift', size = 14)

        # Create window widgets
        self.welcomeLabel = tkinter.Label(text = "Dice Simulator", font = window_font2, background = '#006aff', fg = '#ffffff')
        self.dice = tkinter.StringVar()
        self.diceLabel = tkinter.Label(textvariable = self.dice, font = window_font, background = '#00ebff', fg = '#006aff')
        self.rollBtn = tkinter.Button(text = 'ROLL!', command = lambda: self.rollDie(6), font = window_font3, background = '#006aff', fg = '#ffffff', relief = 'raised')

        # Configure column and rows
        self.main_window.columnconfigure(0, weight = 1)
        self.main_window.columnconfigure(1, weight = 1)
        self.main_window.columnconfigure(2, weight = 1)
        self.main_window.rowconfigure(0, weight = 1)
        self.main_window.rowconfigure(1, weight = 1)
        self.main_window.rowconfigure(2, weight = 1)

        # Place widgets in grid
        self.welcomeLabel.grid(columnspan = 3, sticky = 'NSEW')
        self.diceLabel.grid(columnspan = 3, sticky = 'NSEW')
        self.rollBtn.grid(column = 1, sticky = 'NSEW')
    
        # Main loop
        tkinter.mainloop()

    # Function to roll the die
    def rollDie(self, num):
        randNum = randint(1, num)
        self.dice.set(str(randNum))

# Create an instance of the tkinter GUI class
myGUI = DieSimulator()