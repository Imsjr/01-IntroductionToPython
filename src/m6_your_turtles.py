"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Jason Ims
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

redTurtle = rg.SimpleTurtle('turtle')
redTurtle.pen = rg.Pen('red', 3)
redTurtle.speed = 20

for k in range(5):

    redTurtle.right(216)
    redTurtle.forward(100)

blueTurtle = rg.SimpleTurtle('turtle')
blueTurtle.pen = rg.Pen('blue',2)
blueTurtle.speed = 40

side = 110
for k in range(100):

    blueTurtle.forward(20)
    blueTurtle.right(side)
    side = side + 20

window.close_on_mouse_click()