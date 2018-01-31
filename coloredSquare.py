#Matthew Suriawinata
#1/30/18
#coloredSquare.py - generates a colored square

from ggame import *
from random import randint

number = randint(1,3) 
if number == 1:
    col = Color(0xff0000, 1)
elif number == 2:
    col = Color(0x191970, 1)
else:
    col = Color(0x7fffd4, 1)




line = LineStyle(3, col)
rectangle = RectangleAsset(100, 100, line, col)
#makes the rectangle display
Sprite(rectangle)
myApp = App()
myApp.run()
