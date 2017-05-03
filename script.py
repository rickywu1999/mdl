import mdl
from display import *
from matrix import *
from draw import *

#Time to start working on mdl! Implement the following mdl commands:

#    push
#        push a copy of the current top of the origins stack onto the origins stack (a full copy, not just a reference to the current top)
#    pop
#        removes the top of the origins stack (nothing needs to be done with this data)
#    move/rotate/scale
#        create a translation/rotation/scale matrix and multiply the current top by it
#    box/sphere/torus
#        add a box/sphere/torus to a temporary polygon matrix, multiply it by the current top and draw it to the screen 
#    line
#        add a line to a temporary edge matrix, multiply it by the current top and draw it to the screen
#    save
#        save the screen with the provided file name
#    display
#        show the image

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    ident(tmp)
    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    tmp = []
    step = 0.1
    for command in commands:
        print command
        if command == "push":
            stack.append(commands)
        if command == "pop":
            stack.pop()
        if command == "move":
            pass
        if command == "rotate":
            pass
        if command == "scale":
            pass
        if command == "line":
            pass
        if command == "box":
            pass
        if command == "sphere":
            pass
        if command == "torus":
            pass
        if command == "save":
            pass
        if command == "display":
            pass
        
        
