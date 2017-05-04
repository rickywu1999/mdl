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
        if command[0] == 'sphere':
            #print 'SPHERE\t' + str(command)
            add_sphere(tmp,
                       float(command[1]), float(command[2]), float(command[3]),
                       float(command[4]), step)
            matrix_mult( stack[-1], tmp )
            draw_polygons(tmp, screen, color)
            tmp = []

        elif command[0] == 'torus':
            #print 'TORUS\t' + str(command)
            add_torus(tmp,
                      float(command[1]), float(command[2]), float(command[3]),
                      float(command[4]), float(command[5]), step)
            matrix_mult( stack[-1], tmp )
            draw_polygons(tmp, screen, color)
            tmp = []
            
        elif command[0] == 'box':
            #print 'BOX\t' + str(command)
            add_box(tmp,
                    float(command[1]), float(command[2]), float(command[3]),
                    float(command[4]), float(command[5]), float(command[6]))
            matrix_mult( stack[-1], tmp )
            draw_polygons(tmp, screen, color)
            tmp = []
            
        elif command[0] == 'circle':
            #print 'CIRCLE\t' + str(command)
            add_circle(tmp,
                       float(command[1]), float(command[2]), float(command[3]),
                       float(command[4]), step)

        elif command[0] == 'hermite' or command[0] == 'bezier':
            #print 'curve\t' + command + ": " + str(command)
            add_curve(tmp,
                      float(command[1]), float(command[2]),
                      float(command[3]), float(command[4]),
                      float(command[5]), float(command[6]),
                      float(command[7]), float(command[8]),
                      step, command)                      
            
        elif command[0] == 'line':            
            #print 'LINE\t' + str(command)

            add_edge( tmp,
                      float(command[1]), float(command[2]), float(command[3]),
                      float(command[4]), float(command[5]), float(command[6]) )

        elif command[0] == 'scale':
            #print 'SCALE\t' + str(command)
            t = make_scale(float(command[1]), float(command[2]), float(command[3]))
            matrix_mult( stack[-1], t )
            stack[-1] = [ x[:] for x in t]

        elif command[0] == 'move':
            #print 'MOVE\t' + str(command)
            t = make_translate(float(command[1]), float(command[2]), float(command[3]))
            matrix_mult( stack[-1], t )
            stack[-1] = [ x[:] for x in t]


        elif command[0] == 'rotate':
            #print 'ROTATE\t' + str(command)
            theta = float(command[2]) * (math.pi / 180)
            
            if command[1] == 'x':
                t = make_rotX(theta)
            elif command[1] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            matrix_mult( stack[-1], t )
            stack[-1] = [ x[:] for x in t]

        elif command[0] == 'push':
            stack.append( [x[:] for x in stack[-1]] )
            
        elif command[0] == 'pop':
            stack.pop()
            
        elif command[0] == 'display' or command[0] == 'save':
            if command[0] == 'display':
                print("displaying now")
                display(screen)
            else:
                save_extension(screen, command[1])
        
