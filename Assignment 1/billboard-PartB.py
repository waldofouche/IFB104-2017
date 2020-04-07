
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9950095
#    Student name: Waldo Fouche
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  BILLBOARD
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "paste_up".
#  You are required to complete this function so that when the
#  program is run it produces an image of an advertising billboard
#  whose arrangement is determined by data stored in a list which
#  specifies how individual paper sheets are to be pasted onto the
#  backing.  See the instruction sheet accompanying this file for
#  full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

sheet_width = 200 # pixels
sheet_height = 500 # pixels
backing_margin = 20 # pixels
backing_width = sheet_width * 4 + backing_margin * 2
backing_height = sheet_height + backing_margin * 2
canvas_top_and_bottom_border = 150 # pixels
canvas_left_and_right_border = 300 # pixels`
canvas_width = (backing_width + canvas_left_and_right_border)
canvas_height = (backing_height + canvas_top_and_bottom_border)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(mark_centre_points = True):

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 5 # pixels
    grass_height = 100 # pixels
    penup()
    goto(-(canvas_width // 2 + overlap),
         -(canvas_height // 2 + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_height + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_height + overlap)
    end_fill()

    # Draw a nice warm sun peeking into the image
    penup()
    goto(-canvas_width // 2, canvas_height // 2)
    color('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height // 3)
    color('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Draw the billboard's wooden backing as four frames
    # and some highlighted coordinates
    #
    # Outer rectangle
    goto(- backing_width // 2, - backing_height // 2) # bottom left
    pencolor('sienna'); fillcolor('tan'); width(3)
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height)
    right(90) # face east
    forward(backing_width)
    right(90) # face south
    forward(backing_height)
    right(90) # face west
    forward(backing_width)
    end_fill()

    # Inner rectangle
    penup()
    goto(- backing_width // 2 + backing_margin,
         - backing_height // 2 + backing_margin) # bottom left
    fillcolor('gainsboro')
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height - backing_margin * 2)
    right(90) # face east
    forward(backing_width - backing_margin * 2)
    right(90) # face south
    forward(backing_height - backing_margin * 2)
    right(90) # face west
    forward(backing_width - backing_margin * 2)
    end_fill()

    # Draw lines separating the locations where the sheets go
    width(1); pencolor('dim grey')
    for horizontal in [-sheet_width, 0, sheet_width]:
        penup()
        goto(horizontal, sheet_height // 2)
        pendown()
        setheading(270) # point south
        forward(sheet_height)
         
    # Mark the centre points of each sheet's location, if desired
    if mark_centre_points:
        penup()
        points = [[[round(-sheet_width * 1.5), 0], 'Location 1'],
                  [[round(-sheet_width * 0.5), 0], 'Location 2'],
                  [[round(sheet_width * 0.5), 0], 'Location 3'],
                  [[round(sheet_width * 1.5), 0], 'Location 4']]
        for centre_point, label in points:
            goto(centre_point)
            dot(4)
            write('  ' + label + '\n  (' + str(centre_point[0]) + ', 0)',
                  font = ('Arial', 12, 'normal'))
     
    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)


# End the program by hiding the cursor and releasing the canvas
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data------------------------------------------------------#
#
# The list in this section contains the data sets you will use to
# test your code.  Each of the data sets is a list specifying the
# way in which sheets are pasted onto the billboard:
#
# 1. The name of the sheet, from 'Sheet A' to 'Sheet D'
# 2. The location to paste the sheet, from 'Location 1' to
#    'Location 4'
# 3. The sheet's orientation, either 'Upright' or 'Upside down'
#
# Each data set does not necessarily mention all four sheets.
#
# In addition there is an extra value, either 'X' or 'O' at the
# start of each data set.  The purpose of this value will be
# revealed only in Part B of the assignment.  You should ignore it
# while completing Part A.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Note that your solution must work for all the data sets below
# AND ANY OTHER DATA SETS IN THE SAME FORMAT!
#

data_sets = [
    # These two initial data sets don't put any sheets on the billboard
    # Data sets 0 - 1
    ['O'],
    ['X'],
    # These data sets put Sheet A in all possible locations and orientations
    # Data sets 2 - 9
    ['O', ['Sheet A', 'Location 1', 'Upright']],
    ['O', ['Sheet A', 'Location 2', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright']],
    ['O', ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 2', 'Upside down']],
    ['O', ['Sheet A', 'Location 3', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down']],
    # These data sets put Sheet B in all possible locations and orientations
    # Data sets 10 - 17
    ['O', ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet B', 'Location 2', 'Upright']],
    ['O', ['Sheet B', 'Location 3', 'Upright']],
    ['O', ['Sheet B', 'Location 4', 'Upright']],
    ['O', ['Sheet B', 'Location 1', 'Upside down']],
    ['O', ['Sheet B', 'Location 2', 'Upside down']],
    ['O', ['Sheet B', 'Location 3', 'Upside down']],
    ['O', ['Sheet B', 'Location 4', 'Upside down']],
    # These data sets put Sheet C in all possible locations and orientations
    # Data sets 18 - 25
    ['O', ['Sheet C', 'Location 1', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 3', 'Upright']],
    ['O', ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upside down']],
    ['O', ['Sheet C', 'Location 3', 'Upside down']],
    ['O', ['Sheet C', 'Location 4', 'Upside down']],
    # These data sets put Sheet D in all possible locations and orientations
    # Data sets 26 - 33
    ['O', ['Sheet D', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 2', 'Upright']],
    ['O', ['Sheet D', 'Location 3', 'Upright']],
    ['O', ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet D', 'Location 2', 'Upside down']],
    ['O', ['Sheet D', 'Location 3', 'Upside down']],
    ['O', ['Sheet D', 'Location 4', 'Upside down']],
    # These data sets place two sheets in various locations and orientations
    # Data sets 34 - 38
    ['O', ['Sheet D', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'], 
          ['Sheet B', 'Location 1', 'Upright']], 
    ['O', ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    # These data sets place three sheets in various locations and orientations
    # Data sets 39 - 43
    ['O', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']], 
    ['O', ['Sheet B', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 2', 'Upside down'],
          ['Sheet C', 'Location 1', 'Upside down']], 
    ['X', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upright']],
    # These data sets place four sheets in various locations and orientations
    # Data sets 44 - 48
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],     
    # These data sets draw the entire image upside down
    # Data sets 49 - 50
    ['X', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    # These are the final, 'correct' arrangements of sheets
    # Data sets 51 - 52
    ['X', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']]
    ]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "paste_up" function.
#

##Sheets
def bg_sheet_color(x,y):
    goto(x,y) #needs to change dependant on panel
    penup()
    setheading(90)
    forward(250)
    left(90)
    forward(100)
    pendown()
    color("Black")
    begin_fill()
    left(180)
    forward(200)
    right(90)
    forward(500)
    right(90)
    forward(200)
    right(90)
    forward(500)
    end_fill()
    penup() 
        
def Sheet_A():
###########################
    #Slanted Square
###########################
###########################
    #Grey Outline 10px
###########################
    color("grey")
    penup()
    forward(150)
    right(90)
    forward(30)
    right(110)
    pendown()
    begin_fill()
    forward(290)
    left(110)#Diagonal
    forward(170)
    left(90)
    forward(10)
    left(90)
    forward(160) #Bottom Distance
    right(110)#Diagonal
    forward(270)
    right(70)
    forward(67)
    left(90)
    forward(10)
    left(90)
    forward(67)# Top distance
    end_fill()
###########################
    #White Outline 10px
###########################
    penup()
    left(90)
    forward(10)
    left(90)
    pendown()
    color("white")
    begin_fill()
    forward(67)
    right(90)
    forward(10)
    right(90)
    forward(60)
    left(70)
    forward(250)
    left(110)#Diagonal
    forward(145)
    right(90)
    forward(10)
    right(90)
    forward(160)
    right(110)#Diagonal
    forward(270)
    end_fill()
    penup()
###########################
    #Red Fill 10px
###########################
    color("firebrick")
    right(160)
    forward(10)
    left(90)
    forward(10)
    pendown()
    begin_fill()
    forward(59)
    right(90)
    forward(233)
    right(90)
    forward(145)
    right(110)#Diagonal
    forward(250)
    end_fill()
    penup()
    
def Sheet_B():
#########################
    #Grey Outline 10px
#########################
    color("grey")
    penup()
    forward(100)
    right(90)
    forward(151)
    right(90)
    pendown()
    begin_fill()
    forward(160)
    right(110) #Diagonal
    forward(290)
    right(70)
    forward(64)
    right(90)
    forward(10)
    right(90)
    forward(60)
    left(70)
    forward(270)
    left(110)
    forward(160)
    right(90)
    forward(10)
    end_fill()
    penup()
###########################
    #White Outline 10px
###########################
    color("white")
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    pendown()
    begin_fill()
    forward(150)
    right(110)
    forward(270)
    right(70)
    forward(60)
    right(90)
    forward(8)
    right(90)
    forward(50)
    left(70)
    forward(250)
    left(110)
    forward(135)
    end_fill()
    penup()
###########################
    #Red Fill 10px
###########################
    color("firebrick")
    left(90)
    pendown()
    begin_fill()
    forward(233)
    left(90)
    forward(50)
    left(70)
    forward(245)
    left(110)
    forward(135)
    end_fill()
###########################
    #Letter R White 40px
###########################
    #Slanted Left
    penup()
    color("white")
    left(90)
    forward(40)
    left(90)
    forward(50)
    right(110)
    pendown()
    begin_fill()
    forward(160)
    left(110)
    forward(50)
    left(70)
    forward(165)
    left(110)
    forward(50)
    end_fill()
    penup()
    #Top Curve
    begin_fill()
    left(180)
    forward(50)
    pendown()
    forward(50)
    circle(-50,180)
    forward(90)
    right(110)
    forward(20)
    right(70)
    forward(60)
    circle(30,180)
    forward(50)
    end_fill()
    #Bottom Curve
    #color("grey")#Locating Curser
    penup()
    right(180)
    forward(10)
    right(110)
    forward(83)
    left(110)
    pendown()
    begin_fill()
    forward(90)
    circle (-30,90)
    right(10)
    forward(35)
    right(80)
    forward(40)
    right(100)
    forward(40)
    circle(10,90)
    left(10)
    forward(80)
    right(110)
    forward(20)
    end_fill()
    penup()
#################################
    #Letter R Grey outline 5px
#################################
    color("grey")
    pensize(5)
    forward(15)
    right(70)
    forward(10)
    pendown()
    forward(51)
    circle(30,180)
    forward(30)
    left(70)
    forward(60)
    penup()
    forward(40)
    pendown()
    forward(45)
    right(70)
    forward(50)
    right(110)
    forward(165)
    right(70)
    forward(100)
    circle(-50,180)
    right(180)
    circle (-30,90)
    right(10)
    forward(35)
    right(80)
    forward(45)
    right(100)
    forward(40)
    circle(10,90)
    left(10)
    forward(65)
    penup()
    
def Sheet_C():
######################
    #S White 40px
######################
    pensize(1)
    penup()
    color("white")
    right(90)
    forward(90)
    left(90)
    pendown()
    begin_fill()
    forward(30)
    circle(40, 90)
    forward(10)
    circle(30, 90)
    forward(60)
    circle(-15, 90)
    forward(10)
    circle(-15, 90)
    forward(40)
    circle(-15, 90)
    forward(5)
    left(90)
    forward(30)
    left(90)
    forward(20)
    circle(30, 90)
    forward(60)
    circle(40, 90)
    forward(25)
    circle(30, 90)
    forward(55)
    circle(-15, 90)
    circle(-15, 90)
    forward(35)
    circle(-15, 90)
    left(90)
    forward(30)
    left(90)
    forward(10)
    circle(30, 90)
    forward(30)
    end_fill()

    # S Grey Outline
    pensize(5)
    color("grey")
    forward(30)
    circle(40, 90)
    forward(10)
    circle(30, 90)
    forward(60)
    circle(-15, 90)
    forward(10)
    circle(-15, 90)
    forward(40)
    circle(-15, 90)
    forward(5)
    left(90)
    forward(30)
    left(90)
    forward(20)
    circle(30, 90)
    forward(60)
    circle(40, 90)
    forward(25)
    circle(30, 90)
    forward(55)
    circle(-15, 90)
    circle(-15, 90)
    forward(35)
    circle(-15, 90)
    left(90)
    forward(30)
    left(90)
    forward(10)
    circle(30, 90)
    forward(30)
    pensize(1)

def Sheet_D():
    color("white")
    penup()
    right(90)
    forward(100)
    right(90)
    pendown()
    begin_fill()
    forward(40)
    circle(-40, 180)
    right(180)
    circle(-40, 180)
    forward(60)
    circle(-25, 90)
    forward(20)
    right(90)
    forward(40)
    right(90)
    circle(25, 90)
    forward(10)
    circle(20, 180)
    forward(20)
    right(90)
    forward(40)
    right(90)
    forward(20)
    circle(20, 180)
    forward(10)
    circle(25, 90)
    right(90)
    forward(40)
    right(90)
    forward(20)
    circle(-25, 90)
    forward(20)
    end_fill()
    # Grey 5px
    pensize(5)
    color('grey')
    forward(40)
    circle(-40, 180)
    right(180)
    circle(-40, 180)
    forward(60)
    circle(-25, 90)
    forward(20)
    right(90)
    forward(40)
    right(90)
    circle(25, 90)
    forward(10)
    circle(20, 180)
    forward(20)
    right(90)
    forward(40)
    right(90)
    forward(20)
    circle(20, 180)
    forward(10)
    circle(25, 90)
    right(90)
    forward(40)
    right(90)
    forward(20)
    circle(-25, 90)
    forward(20)
    
  
  

    
def graffiti():
    penup()
    color("green")
    goto(-300, 150)
    pensize(50)
    right(60)
    pendown()
    forward(250)
    left(90)
    forward(100)
    right(90)
    forward(70)
    left(110)
    forward(250)
    penup()
    setheading(0)
    forward(100)
    pendown()
    forward(130)
    right(180)
    forward(130)
    left(90)
    forward(100)
    left(90)
    forward(60)
    left(180)
    forward(60)
    left(90)
    forward(100)

    


# Paste the sheets onto the billboard as per the provided data set
def paste_up(data_sets):
    sheet_num = 1
    for data in range(len(data_sets)-1):
        if (data_sets[sheet_num][1]) == 'Location 1':
            bg_sheet_color(-300,0)
            penup()
            goto(-300,0)
            pendown()
                        
        if (data_sets[sheet_num][1]) == 'Location 2':
            bg_sheet_color(-100,0)
            penup()
            goto(-100,0)
            pendown()
            
            
        if (data_sets[sheet_num][1]) == 'Location 3':
            bg_sheet_color(100,0)
            penup()
            goto(100,0)
            pendown()
            
            
        if (data_sets[sheet_num][1]) == 'Location 4':
            bg_sheet_color(300,0)
            penup()
            goto(300,0)
            pendown()
            

        if data_sets[sheet_num][2] == 'Upside down':
            if (data_sets[sheet_num][0]) == 'Sheet A' and (data_sets[sheet_num][2]) == 'Upside down':
                setheading(270)
                pendown()
                Sheet_A()
                penup()
            elif (data_sets[sheet_num][0]) == 'Sheet B' and (data_sets[sheet_num][2]) == 'Upside down':
                setheading(0)
                pendown()
                Sheet_B()
                penup()
            elif (data_sets[sheet_num][0]) == 'Sheet C' and (data_sets[sheet_num][2]) == 'Upside down':
                setheading(0)
                pendown()
                Sheet_C()
                penup()
            elif (data_sets[sheet_num][0]) == 'Sheet D' and (data_sets[sheet_num][2]) == 'Upside down':
                setheading(0)
                pendown()
                Sheet_D()
                penup()

        if data_sets[sheet_num][2] == 'Upright':
            if data_sets[sheet_num][0] == 'Sheet A':
                    pendown()
                    Sheet_A()
                    penup()
            if data_sets[sheet_num][0] == 'Sheet B':
                    pendown()
                    left(90)
                    Sheet_B()
            if data_sets[sheet_num][0] == 'Sheet C':
                    pendown()
                    left(90)
                    Sheet_C()
                    penup()
            if data_sets[sheet_num][0] == 'Sheet D':
                    pendown()
                    left(90)
                    Sheet_D()
                    penup()
                                 
        sheet_num = sheet_num + 1
    if 'X' in data_sets:
        graffiti()
        

    

        
   
        
            

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your billboard.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the centre points of each sheet on the backing
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with one that describes the image
# ***** displayed on your billboard when the sheets are pasted
# ***** correctly
title("Describe your billboard's image here")

### Call the student's function to display the billboard
### ***** Change the number in the argument to this function
### ***** to test your code with a different data set
paste_up(data_sets[51])

# Exit gracefully
#release_drawing_canvas()

#
#--------------------------------------------------------------------#

