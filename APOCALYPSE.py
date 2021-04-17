# TRISTAN PARRY - TURTLE GAME - APOCALYPSE (DODGING GAME)


# BEFORE RUNNING THIS CODE, PLEASE ENSURE THAT ALL ASSET FILES ARE DOWNLOADED AND PLACED IN THE CORRECT FOLDER, PICTURES.
#READ THE "READ_ME" FILE ATTACHED FOR MORE INFORMATION BEFORE USING THIS CODE


# THIS IS A GAME, CREATED WITH PYTHON AND TURTLE, IN WHICH YOU MUST DODGE FALLING FIREBALLS AND COLLECT FALLING COINS. USING LEFT AND RIGHT ARROW KEYS TO MOVE, OBTAIN A SCORE OF 500 TO WIN.


# HAVE FUN & ENJOY THE GAME









# Importing Python Modules

import random # Random is a python module that allows the computer to make a random choice between a range/list of given options, every time the code is run (see below)
import time # Time is a python module that allows the computer to track the time, in seconds, that the code is run, allowing for time manipulation within the code (see below)
import turtle # Turtle is a python module that allows for the creation and integration of a GUI, or graphics-based activity, within a code/program (this module allows the game to run in a graphics window, with graphic commands/sequences, see below)
import winsound # Winsound is a python module that allows the computer to play sounds on occasion or command within a program (see below)










# Creating a Window for the Program to run in (using Turtle)

window=turtle.Screen() # This sets the variable, "window", to the turtle function _Screen(), effectively creating an external window for the program's graphics to run in (the console cannot handle this activity)
window.bgcolor("Black") # Defining an attribute of the window, its background colour. Here, the window's background colour is set to black (Hex. 000000)
window.title("TRISTAN PARRY - APOCALYPSE") # Defining an attribute of the window, its title. Here, I have set the title of the window to "TRISTAN PARRY - APOCALYPSE"
window.setup(width=1000, height=700)# Defining an attribute of the window, its resolution. Here, I have set the width of the window (in pixels), to 1000, and the height of the window (in pixels), to 700
window.tracer() # Defining an attribute of the window, its refresh rate. Here, the _tracer() function is used to show/time screen refreshes, and turtle animations. Tracer's default is set to (1,10), in which the window will show animations










# Registering the images from the code ASSETS folder, to allow python to subsitute player shapes/images for these images
# The turtle module can only import and register .gif picture files
# These shapes are registered in the turtle-created window, allowing the window to identify, access and utilize the images (in the ASSETS folder), later in the code

window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_1.gif") # The image for character 1 (the red character) facing forwards
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_2.gif") # The image for character 2 (the blue character) facing forwards
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_3.gif") # The image for character 3 (the green character) facing forwards
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_1_SMALL.gif") # The image for character 1 (the red character) facing forwards, small size (for in-game movement)
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_2_SMALL.gif") # The image for character 2 (the blue character) facing forwards, small size (for in-game movement)
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_3_SMALL.gif") # The image for character 3 (the green character) facing forwards, small size (for in-game movement)
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_1_side_left_SMALL.gif") # The image for character 1 (the red character) facing left, small size (for in-game movement)
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_1_side_right_SMALL.gif") # The image for character 1 (the red character) facing right, small size (for in-game movement)
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_2_side_left_SMALL.gif") # The image for character 1 (the blue character) facing left, small size (for in-game movement)
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_2_side_right_SMALL.gif") # The image for character 1 (the blue character) facing right, small size (for in-game movement)
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_3_side_left_SMALL.gif") # The image for character 1 (the green character) facing left, small size (for in-game movement)
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_3_side_right_SMALL.gif") # The image for character 1 (the green character) facing right, small size (for in-game movement)
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\fireball.gif") # The image for the fireball
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\coin.gif")# The image for the coin
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\fireball_SMALL.gif") # The image for the fireball, small size (for in-game collision)
window.register_shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\coin_SMALL.gif") # The image for the coin, small size (for in-game collision)










# Create the Pre-Game Story (Introduction) (New function)
# This story serves as an introduction to the game, and gives the user a cinematic background before playing the game

def story():
    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\Overture.wav",winsound.SND_ASYNC)
    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
    
    # Define the pen
    
    pen=turtle.Pen() # This turtle command uses the function, _Pen, to create a virtual pen (using the variable name pen) to draw with and create shapes in the turtle window.
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.speed(0) # This command sets the pen's speed to its fastest, 0. Animations are hard to see at this speed
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,0) # This command makes the pen travel to the centre of the turtle window
    
    
    pen.write("Hello.",False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    time.sleep(2) # This command uses the time module, to stop all action in the turtle window, for 2 seconds
    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
    
    pen.write("In a time of darkness and despair...",False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    time.sleep(3) # This command uses the time module, to stop all action in the turtle window, for 3 seconds
    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
    
    pen.write("The heavens sent peril to rain upon the earth.",False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    time.sleep(3) # This command uses the time module, to stop all action in the turtle window, for 3 seconds
    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
    
    pen.write("SURVIVE.",False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    time.sleep(4) # This command uses the time module, to stop all action in the turtle window, for 4 seconds
    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
    menu() # This command allows for a program transition, to the function created below, menu(). There is no prompt for changing the function, the code executes it in the turtle window










# Creating the Game Menu (new function)

def menu():
    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
    window.bgpic(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\menu_background.gif") # The turtle module can only import and register .gif picture files
    # This command uses the turtle module, and its _bgpic function, to set the turtle window's background to a picture stored on the computer. 
    # This function uses one argument: the picture being used from the computer's directory, as the turtle window's background picture
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    
    def no_effect_keys():
        None # A function within the menu, that does not allow any actions for some keys (that are used in other menu functions). This function defines what will happen when the specific keys are pressed, nothing.
    
    window.onkey(no_effect_keys,"1") # If the 1 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"2") # If the 2 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"3") # If the 3 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"Escape") # If the esc key is pressed in the turtle window, the no_effect_keys function will be used
    window.listen() # This command allows for the turtle window to listen for key inputs, making the no_effect_keys function work
    
    pen=turtle.Pen() # This turtle command uses the function, _Pen, to create a virtual pen (using the variable name pen) to draw with and create shapes in the turtle window.
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.speed(0) # This command sets the pen's speed to its fastest, 0. Animations are hard to see at this speed
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,150) # This command makes the pen travel to the horizontal centre of the turtle window, while moving up 150 pixels
    
    
    pen.write("A P O C A L Y P S E",False,"center",font=("Rockwell Nova",65,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    pen.width(5) # This command changes the size (or thickness/width) of the pen. Here, it is set to a width of 5 pixels.
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(-375,50) # This command makes the pen travel horizontally left 375 pixels in the turtle window, while moving up 50 pixels
    
    
    pen.begin_fill() # This command uses the turtle function begin_fill  to start filling in the shape that the pen makes after this line, it will fill with the same colour as the pen
    for i in range(2): # This is a for loop, it is set to the range 2, meaning that the computer will run through the loop 2 times
        pen.forward(240) # This makes the pen move forward by 240 pixels
        pen.left(270) # This makes the pen move left by 270 pixels
        pen.forward(90) # This makes the pen move forward by 90 pixels
        pen.left(270) # This makes the pen move left by 270 pixels
    pen.end_fill() # This command uses the turtle function end_fill  to stop filling in the shape that the pen made in the previous lines, it has filled with the same colour as the pen
    
    
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(375,50) # This command makes the pen travel horizontally right 375 pixels in the turtle window, while moving up 50 pixels
    
    
    pen.begin_fill() # This command uses the turtle function begin_fill  to start filling in the shape that the pen makes after this line, it will fill with the same colour as the pen
    for i in range(2): # This is a for loop, it is set to the range 2, meaning that the computer will run through the loop 2 times
        pen.forward(-240) # This makes the pen move forward by -240 pixels (technically backwards by 240 pixels)
        pen.left(-270) # This makes the pen move left by -270 pixels (technically right by 270 pixels)
        pen.forward(-90) # This makes the pen move forward by -90 pixels (technically backwards by 90 pixels)
        pen.left(-270) # This makes the pen move left by -270 pixels (technically right by 270 pixels)
    pen.end_fill() # This command uses the turtle function end_fill  to stop filling in the shape that the pen made in the previous lines, it has filled with the same colour as the pen
    
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(-120,-150) # This command makes the pen travel horizontally left 120 pixels in the turtle window, while moving down 150 pixels
    
    
    pen.begin_fill() # This command uses the turtle function begin_fill  to start filling in the shape that the pen makes after this line, it will fill with the same colour as the pen
    for i in range(2): # This is a for loop, it is set to the range 2, meaning that the computer will run through the loop 2 times
        pen.forward(240) # This makes the pen move forward by 240 pixels
        pen.left(270) # This makes the pen move left by 270 pixels
        pen.forward(90) # This makes the pen move forward by 90 pixels
        pen.left(270) # This makes the pen move left by 270 pixels
    pen.end_fill() # This command uses the turtle function end_fill  to stop filling in the shape that the pen made in the previous lines, it has filled with the same colour as the pen
    
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.color("Black") # This command sets the pen's color to black (Hex: 000000)
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(-255,-25) # This command makes the pen travel horizontally left 255 pixels in the turtle window, while moving down 25 pixels
    
    pen.write("P L A Y",False,"center",font=("Rockwell Nova",40,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(-255,-100) # This command makes the pen travel horizontally left 255 pixels in the turtle window, while moving down 100 pixels
    
    pen.write("[Press P]",False,"center",font=("Rockwell Nova",25,"italic")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    # Defining the Play button action
    
    def play_button(): # A function within the menu, that allows the user to play the game with the play button (goes to function play_game_random()
        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
        winsound.PlaySound(None,winsound.SND_PURGE)
        # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
        # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
        # Here, "None" is used, as I do not want to play a set sound. I want no sound to play, and the menu music to stop.
        # The winsound flag, "windsound.SND_PURGE, is used to stop other sound in the program/window.
        play_game_random() # This command allows for a program transition, to the function created below, play_game_random(). There is no prompt for changing the function, the code executes it in the turtle window
        
    window.listen() # This command allows for the turtle window to listen for key inputs, making the play_button function work
    window.onkey(play_button, "p") # If the p key is pressed in the turtle window, the play_button function will be used
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.color("Black") # This command sets the pen's color to black (Hex: 000000)
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(255,-15) # This command makes the pen travel horizontally right 255 pixels in the turtle window, while moving down 15 pixels
    
    pen.write("W A R R I O R S",False,"center",font=("Rockwell Nova",20,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(255,-100) # This command makes the pen travel horizontally right 255 pixels in the turtle window, while moving down 100 pixels
    
    pen.write("[Press W]",False,"center",font=("Rockwell Nova",25,"italic")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    # Define the warrior button
    
    def warrior_button(): # A function within the menu, that allows the user to go into the warrior menu with the warrior button (goes to function warrior_selection()
        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
        warrior_selection() # This command allows for a program transition, to the function created below, warrior_selection(). There is no prompt for changing the function, the code executes it in the turtle window
        
    window.listen() # This command allows for the turtle window to listen for key inputs, making the warrior_button function work
    window.onkey(warrior_button, "w") # If the w key is pressed in the turtle window, the warrior_button function will be used
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.color("Black") # This command sets the pen's color to black (Hex: 000000)
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,-215) # This command makes the pen travel to the horizontal centre of the turtle window, while moving down 215 pixels
    
    pen.write("C O N T R O L S",False,"center",font=("Rockwell Nova",20,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,-300) # This command makes the pen travel to the horizontal centre of the turtle window, while moving down 300 pixels
    
    pen.write("[Press C]",False,"center",font=("Rockwell Nova",25,"italic")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    def controls_button(): # A function within the menu, that allows the user to go into the controls menu with the controls button (goes to function controls_button()
        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
        controls() # This command allows for a program transition, to the function created below, controls(). There is no prompt for changing the function, the code executes it in the turtle window
    
    window.listen() # This command allows for the turtle window to listen for key inputs, making the controls_button function work
    window.onkey(controls_button, "c") # If the c key is pressed in the turtle window, the controls_button function will be used











# Creating the warrior menu for the game (New function)

def warrior_selection():
    pen=turtle.Pen() # This turtle command uses the function, _Pen, to create a virtual pen (using the variable name pen) to draw with and create shapes in the turtle window.
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.speed(0) # This command sets the pen's speed to its fastest, 0. Animations are hard to see at this speed
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,200) # This command makes the pen travel to the horizontal centre of the turtle window, while moving up 200 pixels
    
    pen.write("CHOOSE YOUR WARRIOR",False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(-350,50) # This command makes the pen travel horizontally left 350 pixels of the turtle window, while moving up 50 pixels
    
    pen.write("PRESS 1",False,"center",font=("Papyrus",20,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,50) # This command makes the pen travel to the horizontal centre of the turtle window, while moving up 50 pixels
    
    pen.write("PRESS 2",False,"center",font=("Papyrus",20,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(350,50) # This command makes the pen travel horizontally right 350 pixels of the turtle window, while moving up 50 pixels
    
    pen.write("PRESS 3",False,"center",font=("Papyrus",20,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,-325) # This command makes the pen travel to the horizontal centre of the turtle window, while moving down 325 pixels
    
    pen.write("[Press esc to return to menu]",False,"center",font=("Papyrus",15,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
    
    character1=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
    character1.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_1.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above.
    character1.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
    character1.goto(-350,-100) # This command makes the turtle travel left horizontally by 350 pixels in the turtle window, while moving down 100 pixels
    
    character2=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
    character2.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_2.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above.
    character2.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
    character2.goto(0,-100) # This command makes the turtle to travel to the horizontal centre of the turtle window, while moving down 100 pixels
    
    character3=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
    character3.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_3.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above.
    character3.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
    character3.goto(350,-100) # This command makes the turtle travel right horizontally by 350 pixels in the turtle window, while moving down 100 pixels
    
    def warrior_option_1(): # A new function that allows the program to transfer when the first warrior is selected.
        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
        character1.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        character2.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        character3.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
        winsound.PlaySound(None,winsound.SND_PURGE)
        # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
        # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
        # Here, "None" is used, as I do not want to play a set sound. I want no sound to play, and the menu music to stop.
        # The winsound flag, "windsound.SND_PURGE, is used to stop other sound in the program/window.
        play_game_character_1() # This command allows for a program transition, to the function created below, play_game_character_1(). There is no prompt for changing the function, the code executes it in the turtle window
    
    def warrior_option_2(): # A new function that allows the program to transfer when the second warrior is selected.
        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
        character1.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        character2.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        character3.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
        winsound.PlaySound(None,winsound.SND_PURGE)
        # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
        # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
        # Here, "None" is used, as I do not want to play a set sound. I want no sound to play, and the menu music to stop.
        # The winsound flag, "windsound.SND_PURGE, is used to stop other sound in the program/window.
        play_game_character_2() # This command allows for a program transition, to the function created below, play_game_character_2(). There is no prompt for changing the function, the code executes it in the turtle window
    
    def warrior_option_3(): # A new function that allows the program to transfer when the third warrior is selected.
        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
        character1.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        character2.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        character3.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
        winsound.PlaySound(None,winsound.SND_PURGE)
        # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
        # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
        # Here, "None" is used, as I do not want to play a set sound. I want no sound to play, and the menu music to stop.
        # The winsound flag, "windsound.SND_PURGE, is used to stop other sound in the program/window.
        play_game_character_3() # This command allows for a program transition, to the function created below, play_game_character_3(). There is no prompt for changing the function, the code executes it in the turtle window
    
    window.listen() # This command allows for the turtle window to listen for key inputs, making the warrior_option functions work
    window.onkey(warrior_option_1,"1") # If the 1 key is pressed in the turtle window, the warrior_option_1 function will be used
    window.onkey(warrior_option_2,"2") # If the 2 key is pressed in the turtle window, the warrior_option_2 function will be used
    window.onkey(warrior_option_3,"3") # If the 3 key is pressed in the turtle window, the warrior_option_3 function will be used
    
    def no_effect_keys():
        None # A function within the menu, that does not allow any actions for some keys (that are used in other menu functions). This function defines what will happen when the specific keys are pressed, nothing.
    
    window.onkey(no_effect_keys,"w") # If the 1 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"p") # If the 2 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"c") # If the 3 key is pressed in the turtle window, the no_effect_keys function will be used
    window.listen()  # This command allows for the turtle window to listen for key inputs, making the no_effect_keys function work
    
    def esc_button():
        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
        character1.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        character2.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        character3.hideturtle() # This command hides the turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        menu() # This command allows for a program transition, to the function created below, menu(). There is no prompt for changing the function, the code executes it in the turtle window
    
    window.onkey(esc_button,"Escape") # If the esc key is pressed in the turtle window, the esc_button function will be used
    window.listen() # This command allows for the turtle window to listen for key inputs, making the no_effect_keys function work










# Creating the controls/info screen for the game (New function)

def controls():
    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
    
    pen=turtle.Pen() # This turtle command uses the function, _Pen, to create a virtual pen (using the variable name pen) to draw with and create shapes in the turtle window.
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.speed(0) # This command sets the pen's speed to its fastest, 0. Animations are hard to see at this speed
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,200) # This command makes the turtle to travel to the horizontal centre of the turtle window, while moving up 200 pixels
    
    pen.write("CONTROLS",False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,100) # This command makes the turtle to travel to the horizontal centre of the turtle window, while moving up 100 pixels
    
    pen.write("Left Arrow - Move Left",False,"center",font=("Papyrus",20,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,50) # This command makes the turtle to travel to the horizontal centre of the turtle window, while moving up 50 pixels
    
    pen.write("Right Arrow - Move Right",False,"center",font=("Papyrus",20,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,-150) # This command makes the turtle to travel to the horizontal centre of the turtle window, while moving down 150 pixels
    
    pen.write("You have 5 lives.\nAVOID THE FALLING FIREBALLS.\nCOLLECT THE FALLING COINS.",False,"center",font=("Papyrus",20,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,-250) # This command makes the turtle to travel to the horizontal centre of the turtle window, while moving down 250 pixels
    
    pen.write("To win, achieve a score of 500.",False,"center",font=("Papyrus",20,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,-325) # This command makes the turtle to travel to the horizontal centre of the turtle window, while moving down 325 pixels
    
    pen.write("[Press esc to return to menu]",False,"center",font=("Papyrus",15,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    window.tracer(1,10)  # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
    
    fire=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
    fire.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\fireball.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above.
    fire.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
    fire.goto(-350,200) # This command makes the turtle travel left horizontally by 350 pixels in the turtle window, while moving up 200 pixels
    
    coin=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
    coin.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\coin.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above.
    coin.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
    coin.goto(350,175) # This command makes the turtle travel right horizontally by 350 pixels in the turtle window, while moving up 175 pixels
    
    def no_effect_keys():
        None # A function within the menu, that does not allow any actions for some keys (that are used in other menu functions). This function defines what will happen when the specific keys are pressed, nothing.
    
    window.onkey(no_effect_keys,"w") # If the 1 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"p") # If the 2 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"c") # If the 3 key is pressed in the turtle window, the no_effect_keys function will be used
    window.listen()  # This command allows for the turtle window to listen for key inputs, making the no_effect_keys function work
    
    def esc_button():
        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
        fire.hideturtle() # This command hides the fire turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        menu() # This command allows for a program transition, to the function created below, menu(). There is no prompt for changing the function, the code executes it in the turtle window
    
    window.onkey(esc_button,"Escape") # If the esc key is pressed in the turtle window, the esc_button function will be used
    window.listen() # This command allows for the turtle window to listen for key inputs, making the no_effect_keys function work










# Defining the global variable, score

score=0
# Here, "score" is set to the value 0, as a global variable (it is not defined in any other python function throughout this code.
# This means it is set on the global level, and can be used in functions throughout the rest of the program, by calling "global score" at the beginning of each function using the score variable.








# Creating the Game

# Creating the new function for playing the game with a random character (when user presses P)

def play_game_random():
    global score # This command allows the function, play_game_random(), to use and change the global variable, "score"
    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\gong.wav",winsound.SND_ASYNC)
    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
    
    pen=turtle.Pen() # This turtle command uses the function, _Pen, to create a virtual pen (using the variable name pen) to draw with and create shapes in the turtle window.
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.speed(0) # This command sets the pen's speed to its fastest, 0. Animations are hard to see at this speed
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,0) # This command makes the pen travel to the centre of the turtle window
    
    pen.write("Good luck.",False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    time.sleep(2) # This command uses the time module, to stop all action in the turtle window, for 2 seconds
    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
    
    def no_effect_keys():
        None # A function within the menu, that does not allow any actions for some keys (that are used in other menu functions). This function defines what will happen when the specific keys are pressed, nothing.
    
    window.onkey(no_effect_keys,"w") # If the 1 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"p") # If the 2 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"c") # If the 3 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"1") # If the 1 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"2") # If the 2 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"3") # If the 3 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"Escape") # If the esc key is pressed in the turtle window, the no_effect_keys function will be used
    window.listen() # This command allows for the turtle window to listen for key inputs, making the no_effect_keys function work
    
    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
    
    backgrounds=[r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_1.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_2.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_3.gif"] # Here, I have made a list of three random backgrounds, to be picked randomly and be used as the game background, in the code later. The "r" before each file path is used to turn the file location into string literal, so the backslashes do not get mistaken for string commands (ex. "\n")
    window.bgpic(random.choice(backgrounds)) # The turtle module can only import and register .gif picture files
    # This command uses the turtle module, and its _bgpic function, to set the turtle window's background to a random picture stored on the computer, in the python list "backgrounds". 
    # This function uses one argument: the picture being used from the computer's directory, as the turtle window's background picture
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    
    player=["1","2","3"] # Here, I have made a list of three player numbers, to be picked randomly and be used as the game player, in the code later. The "r" before each file path is used to turn the file location into string literal, so the backslashes do not get mistaken for string commands (ex. "\n")
    player=random.choice(player) # The random module picks either a "1", "2", or "3" from the player list, to find what player will be used for the game
    if player=="1": # If the random module chooses "1" from the players list:
        player=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
        playershapes=[r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_1_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_1_side_left_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_1_side_right_SMALL.gif"] # Here, I have made a list of three player movement images, to be used in the code later, for the player turtle's shape. The "r" before each file path is used to turn the file location into string literal, so the backslashes do not get mistaken for string commands (ex. "\n")
        player.shape(playershapes[0]) # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above, the first image index of the player list.
        player.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
        player.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
        player.goto(0,-290) # This command moves the player turtle to the horizontal centre of the turtle window, while moving it down 290 pixels
        def player_move_left(): # This command allows for player movement in the game. This function is to move the player left.
            player.setheading=270 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 270 degrees sets the turtle to look to the left.
        
        def player_move_right(): # This command allows for player movement in the game. This function is to move the player right.
            player.setheading=90 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 90 degrees sets the turtle to look to the right.
        
        window.listen() # This command allows for the turtle window to listen for key inputs, making the player_move_left and player_move_right functions work
        window.onkey(player_move_left,"Left") # If the left arrow key is pressed in the turtle window, the player_move_left function will be used
        window.onkey(player_move_right,"Right") # If the right arrow key is pressed in the turtle window, the player_move_right function will be used
    
    
        fireballs=[] # Here, I have created an empty list, to be appended with fireball turtles for the game.
        
        for i in range(14): # This range command makes it so that this for loop is run through 14 times, effectively creating and appending 14 fireball turtles to the list, fireballs
            fireball=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
            fireball.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
            fireball.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
            fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
            fireball.speed(random.randint(1,5)) # This changes the fireball turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
            fireball.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\fireball_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
            fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
            fireballs.append(fireball) # This command appends the fireball turtle, with all of its specified parameters, into the list of fireballs
        
        
        coins=[] # Here, I have created an empty list, to be appended with coin turtles for the game.
        
        for i in range(5): # This range command makes it so that this for loop is run through 5 times, effectively creating and appending 5 coin turtles to the list, coins
            coin=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
            coin.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
            coin.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
            coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
            coin.speed(random.randint(1,5)) # This changes the coin turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
            coin.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\coin_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
            coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
            coins.append(coin) # This command appends the coin turtle, with all of its specified parameters, into the list of coins
        
        
        lives=5 # Here, I have created a variable for the game, lives, and have set it to become 5. The user will start the game with 5 lives
        
        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
        
        
        
        while lives>0 and score<500: # While the lives variable is greater than 0, and the score variable is less than 500, this loop will run, it will break after these ranges are exceeded.
            if player.setheading==270: # From the defined functions above, when player_move_left is in effect:
                player.shape(playershapes[1]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the left facing player picture that I have registered in the turtle window.
                x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
                x_coordinate-=4 # While the player is facing left, The x coordinate will move 4 pixels to the left, horizontally, in the turtle window.
                if x_coordinate<-450: # If the x coordinate of the player is at the left side of the screen (-450 pixels):
                    x_coordinate=-450 # Keep resetting the x coordinate to -450 (keep the player on the screen)
                    player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
                player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
            
            if player.setheading==90: # From the defined functions above, when player_move_left is in effect:
                player.shape(playershapes[2]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the right facing player picture that I have registered in the turtle window.
                x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
                x_coordinate+=4 # While the player is facing right, The x coordinate will move 4 pixels to the right, horizontally, in the turtle window.
                if x_coordinate>450: # If the x coordinate of the player is at the right side of the screen (450 pixels):
                    x_coordinate=450 # Keep resetting the x coordinate to 450 (keep the player on the screen)
                    player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
                player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
            
            
            window.tracer(1,0) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
            
            for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list:
                y_coordinate=fireball.ycor() # I created a variable to represent the fireball's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
                y_coordinate-=3 # The y coordinate of the fireball is going vertically down by 3 pixels, continuously, the for loop is in a while loop
                fireball.sety(y_coordinate) # Set the y coordinate of the fireball to the variable, y_coordinate
                
                if y_coordinate<-300: # If the fireball's y coordinate is less (lower) than -300 pixels:
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                    fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
                
                if fireball.distance(player)<50: # If the fireball turtle is within 50 pixels of the player turtle (collision):
                    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\sword.wav",winsound.SND_ASYNC)
                    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                    fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
                    lives-=1 # Every time a fireball hits the player, the player loses a life (lives-=1 is the same as lives=lives-1)
                    if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                        winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\heartbeat.wav",winsound.SND_ASYNC)
                        # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                        # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                        # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                        # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                        window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for coin in coins: # For every one of the 5 coins in the "coins" list: 
                            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                    elif lives>1: # If the lives variable is greater than 1: 
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
            
            
            for coin in coins: # For every one of the 5 coins in the "coins" list: 
                y_coordinate=coin.ycor() # I created a variable to represent the coin's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
                y_coordinate-=3 # The y coordinate of the coin is going vertically down by 3 pixels, continuously, the for loop is in a while loop
                coin.sety(y_coordinate) # Set the y coordinate of the coin to the variable, y_coordinate
                
                if y_coordinate<-300: # If the coin's y coordinate is less (lower) than -300 pixels:
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                    coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
                
                if coin.distance(player)<50: # If the coin turtle is within 50 pixels of the player turtle (collision):
                    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\coin_hit.wav",winsound.SND_ASYNC)
                    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                    coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
                    score+=5 # Every time a coin hits the player, the player gains 5 points (score+=5 is the same as score=score+5)
                    if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                        window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for coin in coins: # For every one of the 5 coins in the "coins" list: 
                            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                    elif lives>1: # If the lives variable is greater than 1: 
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    if score>=500:
                        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                        window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for coin in coins: # For every one of the 5 coins in the "coins" list: 
                            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        win_screen() # This command allows for a program transition, to the function created below, win_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the score variable is 500, the code will also break out of the while loop, and not keep running the main game.
            
            
            window.update() # This command at the end of the full while game loop allows the window to update itself every time the loop is run through (it uses the turtle window function, _update()).
    
    
    
    
    
    
    
    
    
    
    elif player=="2": # If the random module chooses "2" from the players list:
        player=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
        playershapes=[r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_2_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_2_side_left_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_2_side_right_SMALL.gif"] # Here, I have made a list of three player movement images, to be used in the code later, for the player turtle's shape. The "r" before each file path is used to turn the file location into string literal, so the backslashes do not get mistaken for string commands (ex. "\n")
        player.shape(playershapes[0]) # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above, the first image index of the player list.
        player.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
        player.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
        player.goto(0,-300) # This command moves the player turtle to the horizontal centre of the turtle window, while moving it down 290 pixels
        def player_move_left(): # This command allows for player movement in the game. This function is to move the player left.
            player.setheading=270 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 270 degrees sets the turtle to look to the left.
        
        def player_move_right(): # This command allows for player movement in the game. This function is to move the player right.
            player.setheading=90 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 90 degrees sets the turtle to look to the right.
        
        window.listen() # This command allows for the turtle window to listen for key inputs, making the player_move_left and player_move_right functions work
        window.onkey(player_move_left,"Left") # If the left arrow key is pressed in the turtle window, the player_move_left function will be used
        window.onkey(player_move_right,"Right") # If the right arrow key is pressed in the turtle window, the player_move_right function will be used
    
    
        fireballs=[] # Here, I have created an empty list, to be appended with fireball turtles for the game.
        
        for i in range(14): # This range command makes it so that this for loop is run through 14 times, effectively creating and appending 14 fireball turtles to the list, fireballs
            fireball=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
            fireball.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
            fireball.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
            fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
            fireball.speed(random.randint(1,5)) # This changes the fireball turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
            fireball.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\fireball_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
            fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
            fireballs.append(fireball) # This command appends the fireball turtle, with all of its specified parameters, into the list of fireballs
        
        
        coins=[] # Here, I have created an empty list, to be appended with coin turtles for the game.
        
        for i in range(5): # This range command makes it so that this for loop is run through 5 times, effectively creating and appending 5 coin turtles to the list, coins
            coin=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
            coin.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
            coin.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
            coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
            coin.speed(random.randint(1,5)) # This changes the coin turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
            coin.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\coin_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
            coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
            coins.append(coin) # This command appends the coin turtle, with all of its specified parameters, into the list of coins
        
        
        lives=5 # Here, I have created a variable for the game, lives, and have set it to become 5. The user will start the game with 5 lives
        
        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
        
        
        
        while lives>0 and score<500: # While the lives variable is greater than 0, and the score variable is less than 500, this loop will run, it will break after these ranges are exceeded.
            if player.setheading==270: # From the defined functions above, when player_move_left is in effect:
                player.shape(playershapes[1]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the left facing player picture that I have registered in the turtle window.
                x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
                x_coordinate-=4 # While the player is facing left, The x coordinate will move 4 pixels to the left, horizontally, in the turtle window.
                if x_coordinate<-450: # If the x coordinate of the player is at the left side of the screen (-450 pixels):
                    x_coordinate=-450 # Keep resetting the x coordinate to -450 (keep the player on the screen)
                    player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
                player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
            
            if player.setheading==90: # From the defined functions above, when player_move_left is in effect:
                player.shape(playershapes[2]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the right facing player picture that I have registered in the turtle window.
                x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
                x_coordinate+=4 # While the player is facing right, The x coordinate will move 4 pixels to the right, horizontally, in the turtle window.
                if x_coordinate>450: # If the x coordinate of the player is at the right side of the screen (450 pixels):
                    x_coordinate=450 # Keep resetting the x coordinate to 450 (keep the player on the screen)
                    player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
                player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
            
            
            window.tracer(1,0) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
            
            for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list:
                y_coordinate=fireball.ycor() # I created a variable to represent the fireball's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
                y_coordinate-=3 # The y coordinate of the fireball is going vertically down by 3 pixels, continuously, the for loop is in a while loop
                fireball.sety(y_coordinate) # Set the y coordinate of the fireball to the variable, y_coordinate
                
                if y_coordinate<-300: # If the fireball's y coordinate is less (lower) than -300 pixels:
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                    fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
                
                if fireball.distance(player)<50: # If the fireball turtle is within 50 pixels of the player turtle (collision):
                    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\sword.wav",winsound.SND_ASYNC)
                    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                    fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
                    lives-=1 # Every time a fireball hits the player, the player loses a life (lives-=1 is the same as lives=lives-1)
                    if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                        winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\heartbeat.wav",winsound.SND_ASYNC)
                        # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                        # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                        # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                        # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                        window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for coin in coins: # For every one of the 5 coins in the "coins" list: 
                            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                    elif lives>1: # If the lives variable is greater than 1: 
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
            
            
            for coin in coins: # For every one of the 5 coins in the "coins" list: 
                y_coordinate=coin.ycor() # I created a variable to represent the coin's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
                y_coordinate-=3 # The y coordinate of the coin is going vertically down by 3 pixels, continuously, the for loop is in a while loop
                coin.sety(y_coordinate) # Set the y coordinate of the coin to the variable, y_coordinate
                
                if y_coordinate<-300: # If the coin's y coordinate is less (lower) than -300 pixels:
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                    coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
                
                if coin.distance(player)<50: # If the coin turtle is within 50 pixels of the player turtle (collision):
                    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\coin_hit.wav",winsound.SND_ASYNC)
                    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                    coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
                    score+=5 # Every time a coin hits the player, the player gains 5 points (score+=5 is the same as score=score+5)
                    if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                        window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for coin in coins: # For every one of the 5 coins in the "coins" list: 
                            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                    elif lives>1: # If the lives variable is greater than 1: 
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    if score>=500:
                        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                        window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for coin in coins: # For every one of the 5 coins in the "coins" list: 
                            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        win_screen() # This command allows for a program transition, to the function created below, win_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the score variable is 500, the code will also break out of the while loop, and not keep running the main game.
            
            
            window.update() # This command at the end of the full while game loop allows the window to update itself every time the loop is run through (it uses the turtle window function, _update()).
    
    
    
    
    
    
    
    
    
    
    elif player=="3": # If the random module chooses "3" from the players list:
        player=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
        playershapes=[r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_3_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_3_side_left_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_3_side_right_SMALL.gif"] # Here, I have made a list of three player movement images, to be used in the code later, for the player turtle's shape. The "r" before each file path is used to turn the file location into string literal, so the backslashes do not get mistaken for string commands (ex. "\n")
        player.shape(playershapes[0]) # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above, the first image index of the player list.
        player.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
        player.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
        player.goto(0,-300) # This command moves the player turtle to the horizontal centre of the turtle window, while moving it down 290 pixels
        def player_move_left(): # This command allows for player movement in the game. This function is to move the player left.
            player.setheading=270 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 270 degrees sets the turtle to look to the left.
        
        def player_move_right(): # This command allows for player movement in the game. This function is to move the player right.
            player.setheading=90 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 90 degrees sets the turtle to look to the right.
        
        window.listen() # This command allows for the turtle window to listen for key inputs, making the player_move_left and player_move_right functions work
        window.onkey(player_move_left,"Left") # If the left arrow key is pressed in the turtle window, the player_move_left function will be used
        window.onkey(player_move_right,"Right") # If the right arrow key is pressed in the turtle window, the player_move_right function will be used
    
    
        fireballs=[] # Here, I have created an empty list, to be appended with fireball turtles for the game.
        
        for i in range(14): # This range command makes it so that this for loop is run through 14 times, effectively creating and appending 14 fireball turtles to the list, fireballs
            fireball=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
            fireball.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
            fireball.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
            fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
            fireball.speed(random.randint(1,5)) # This changes the fireball turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
            fireball.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\fireball_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
            fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
            fireballs.append(fireball) # This command appends the fireball turtle, with all of its specified parameters, into the list of fireballs
        
        
        coins=[] # Here, I have created an empty list, to be appended with coin turtles for the game.
        
        for i in range(5): # This range command makes it so that this for loop is run through 5 times, effectively creating and appending 5 coin turtles to the list, coins
            coin=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
            coin.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
            coin.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
            coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
            coin.speed(random.randint(1,5)) # This changes the coin turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
            coin.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\coin_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
            coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
            coins.append(coin) # This command appends the coin turtle, with all of its specified parameters, into the list of coins
        
        
        lives=5 # Here, I have created a variable for the game, lives, and have set it to become 5. The user will start the game with 5 lives
        
        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
        
        
        
        while lives>0 and score<500: # While the lives variable is greater than 0, and the score variable is less than 500, this loop will run, it will break after these ranges are exceeded.
            if player.setheading==270: # From the defined functions above, when player_move_left is in effect:
                player.shape(playershapes[1]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the left facing player picture that I have registered in the turtle window.
                x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
                x_coordinate-=4 # While the player is facing left, The x coordinate will move 4 pixels to the left, horizontally, in the turtle window.
                if x_coordinate<-450: # If the x coordinate of the player is at the left side of the screen (-450 pixels):
                    x_coordinate=-450 # Keep resetting the x coordinate to -450 (keep the player on the screen)
                    player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
                player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
            
            if player.setheading==90: # From the defined functions above, when player_move_left is in effect:
                player.shape(playershapes[2]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the right facing player picture that I have registered in the turtle window.
                x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
                x_coordinate+=4 # While the player is facing right, The x coordinate will move 4 pixels to the right, horizontally, in the turtle window.
                if x_coordinate>450: # If the x coordinate of the player is at the right side of the screen (450 pixels):
                    x_coordinate=450 # Keep resetting the x coordinate to 450 (keep the player on the screen)
                    player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
                player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
            
            
            window.tracer(1,0) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
            
            for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list:
                y_coordinate=fireball.ycor() # I created a variable to represent the fireball's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
                y_coordinate-=3 # The y coordinate of the fireball is going vertically down by 3 pixels, continuously, the for loop is in a while loop
                fireball.sety(y_coordinate) # Set the y coordinate of the fireball to the variable, y_coordinate
                
                if y_coordinate<-300: # If the fireball's y coordinate is less (lower) than -300 pixels:
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                    fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
                
                if fireball.distance(player)<50: # If the fireball turtle is within 50 pixels of the player turtle (collision):
                    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\sword.wav",winsound.SND_ASYNC)
                    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                    fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
                    lives-=1 # Every time a fireball hits the player, the player loses a life (lives-=1 is the same as lives=lives-1)
                    if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                        winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\heartbeat.wav",winsound.SND_ASYNC)
                        # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                        # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                        # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                        # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                        window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for coin in coins: # For every one of the 5 coins in the "coins" list: 
                            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                    elif lives>1: # If the lives variable is greater than 1: 
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
            
            
            for coin in coins: # For every one of the 5 coins in the "coins" list: 
                y_coordinate=coin.ycor() # I created a variable to represent the coin's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
                y_coordinate-=3 # The y coordinate of the coin is going vertically down by 3 pixels, continuously, the for loop is in a while loop
                coin.sety(y_coordinate) # Set the y coordinate of the coin to the variable, y_coordinate
                
                if y_coordinate<-300: # If the coin's y coordinate is less (lower) than -300 pixels:
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                    coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
                
                if coin.distance(player)<50: # If the coin turtle is within 50 pixels of the player turtle (collision):
                    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\coin_hit.wav",winsound.SND_ASYNC)
                    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                    coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                    coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
                    score+=5 # Every time a coin hits the player, the player gains 5 points (score+=5 is the same as score=score+5)
                    if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                        window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for coin in coins: # For every one of the 5 coins in the "coins" list: 
                            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                    elif lives>1: # If the lives variable is greater than 1: 
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                        pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                        pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                        pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                        pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    if score>=500:
                        time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                        window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                        player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                            fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        for coin in coins: # For every one of the 5 coins in the "coins" list: 
                            coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                        win_screen() # This command allows for a program transition, to the function created below, win_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the score variable is 500, the code will also break out of the while loop, and not keep running the main game.
            
            
            window.update() # This command at the end of the full while game loop allows the window to update itself every time the loop is run through (it uses the turtle window function, _update()).










# Creating the new function for playing the game with character 1 (from the warrior menu, when user presses 1)

def play_game_character_1():
    global score # This command allows the function, play_game_random(), to use and change the global variable, "score"
    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\gong.wav",winsound.SND_ASYNC)
    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
    
    pen=turtle.Pen() # This turtle command uses the function, _Pen, to create a virtual pen (using the variable name pen) to draw with and create shapes in the turtle window.
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.speed(0) # This command sets the pen's speed to its fastest, 0. Animations are hard to see at this speed
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,0) # This command makes the pen travel to the centre of the turtle window
    
    pen.write("Good luck.",False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    time.sleep(2) # This command uses the time module, to stop all action in the turtle window, for 2 seconds
    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
    
    def no_effect_keys():
        None # A function within the menu, that does not allow any actions for some keys (that are used in other menu functions). This function defines what will happen when the specific keys are pressed, nothing.
    
    window.onkey(no_effect_keys,"w") # If the 1 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"p") # If the 2 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"c") # If the 3 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"1") # If the 1 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"2") # If the 2 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"3") # If the 3 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"Escape") # If the esc key is pressed in the turtle window, the no_effect_keys function will be used
    window.listen() # This command allows for the turtle window to listen for key inputs, making the no_effect_keys function work
    
    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
    
    backgrounds=[r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_1.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_2.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_3.gif"] # Here, I have made a list of three random backgrounds, to be picked randomly and be used as the game background, in the code later. The "r" before each file path is used to turn the file location into string literal, so the backslashes do not get mistaken for string commands (ex. "\n")
    window.bgpic(random.choice(backgrounds)) # The turtle module can only import and register .gif picture files
    # This command uses the turtle module, and its _bgpic function, to set the turtle window's background to a random picture stored on the computer, in the python list "backgrounds". 
    # This function uses one argument: the picture being used from the computer's directory, as the turtle window's background picture
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    
    player=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
    playershapes=[r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_1_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_1_side_left_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_1_side_right_SMALL.gif"] # Here, I have made a list of three player movement images, to be used in the code later, for the player turtle's shape. The "r" before each file path is used to turn the file location into string literal, so the backslashes do not get mistaken for string commands (ex. "\n")
    player.shape(playershapes[0]) # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above, the first image index of the player list.
    player.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
    player.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
    player.goto(0,-290) # This command moves the player turtle to the horizontal centre of the turtle window, while moving it down 290 pixels
    def player_move_left(): # This command allows for player movement in the game. This function is to move the player left.
        player.setheading=270 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 270 degrees sets the turtle to look to the left.
    
    def player_move_right(): # This command allows for player movement in the game. This function is to move the player right.
        player.setheading=90 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 90 degrees sets the turtle to look to the right.
    
    window.listen() # This command allows for the turtle window to listen for key inputs, making the player_move_left and player_move_right functions work
    window.onkey(player_move_left,"Left") # If the left arrow key is pressed in the turtle window, the player_move_left function will be used
    window.onkey(player_move_right,"Right") # If the right arrow key is pressed in the turtle window, the player_move_right function will be used
    
    
    fireballs=[] # Here, I have created an empty list, to be appended with fireball turtles for the game.
    
    for i in range(14): # This range command makes it so that this for loop is run through 14 times, effectively creating and appending 14 fireball turtles to the list, fireballs
        fireball=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
        fireball.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        fireball.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
        fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
        fireball.speed(random.randint(1,5)) # This changes the fireball turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
        fireball.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\fireball_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
        fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
        fireballs.append(fireball) # This command appends the fireball turtle, with all of its specified parameters, into the list of fireballs
    
    
    coins=[] # Here, I have created an empty list, to be appended with coin turtles for the game.
    
    for i in range(5): # This range command makes it so that this for loop is run through 5 times, effectively creating and appending 5 coin turtles to the list, coins
        coin=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
        coin.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        coin.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
        coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
        coin.speed(random.randint(1,5)) # This changes the coin turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
        coin.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\coin_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
        coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
        coins.append(coin) # This command appends the coin turtle, with all of its specified parameters, into the list of coins
    
    
    lives=5 # Here, I have created a variable for the game, lives, and have set it to become 5. The user will start the game with 5 lives
    
    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
    
    
    
    while lives>0 and score<500: # While the lives variable is greater than 0, and the score variable is less than 500, this loop will run, it will break after these ranges are exceeded.
        if player.setheading==270: # From the defined functions above, when player_move_left is in effect:
            player.shape(playershapes[1]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the left facing player picture that I have registered in the turtle window.
            x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
            x_coordinate-=4 # While the player is facing left, The x coordinate will move 4 pixels to the left, horizontally, in the turtle window.
            if x_coordinate<-450: # If the x coordinate of the player is at the left side of the screen (-450 pixels):
                x_coordinate=-450 # Keep resetting the x coordinate to -450 (keep the player on the screen)
                player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
            player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
        
        if player.setheading==90: # From the defined functions above, when player_move_left is in effect:
            player.shape(playershapes[2]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the right facing player picture that I have registered in the turtle window.
            x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
            x_coordinate+=4 # While the player is facing right, The x coordinate will move 4 pixels to the right, horizontally, in the turtle window.
            if x_coordinate>450: # If the x coordinate of the player is at the right side of the screen (450 pixels):
                x_coordinate=450 # Keep resetting the x coordinate to 450 (keep the player on the screen)
                player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
            player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
        
        
        window.tracer(1,0) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
        
        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list:
            y_coordinate=fireball.ycor() # I created a variable to represent the fireball's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
            y_coordinate-=3 # The y coordinate of the fireball is going vertically down by 3 pixels, continuously, the for loop is in a while loop
            fireball.sety(y_coordinate) # Set the y coordinate of the fireball to the variable, y_coordinate
            
            if y_coordinate<-300: # If the fireball's y coordinate is less (lower) than -300 pixels:
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
            
            if fireball.distance(player)<50: # If the fireball turtle is within 50 pixels of the player turtle (collision):
                winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\sword.wav",winsound.SND_ASYNC)
                # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
                lives-=1 # Every time a fireball hits the player, the player loses a life (lives-=1 is the same as lives=lives-1)
                if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\heartbeat.wav",winsound.SND_ASYNC)
                    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                    window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for coin in coins: # For every one of the 5 coins in the "coins" list: 
                        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                elif lives>1: # If the lives variable is greater than 1: 
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
        
        
        for coin in coins: # For every one of the 5 coins in the "coins" list: 
            y_coordinate=coin.ycor() # I created a variable to represent the coin's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
            y_coordinate-=3 # The y coordinate of the coin is going vertically down by 3 pixels, continuously, the for loop is in a while loop
            coin.sety(y_coordinate) # Set the y coordinate of the coin to the variable, y_coordinate
            
            if y_coordinate<-300: # If the coin's y coordinate is less (lower) than -300 pixels:
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
            
            if coin.distance(player)<50: # If the coin turtle is within 50 pixels of the player turtle (collision):
                winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\coin_hit.wav",winsound.SND_ASYNC)
                # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
                score+=5 # Every time a coin hits the player, the player gains 5 points (score+=5 is the same as score=score+5)
                if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                    window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for coin in coins: # For every one of the 5 coins in the "coins" list: 
                        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                elif lives>1: # If the lives variable is greater than 1: 
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                if score>=500:
                    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                    window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for coin in coins: # For every one of the 5 coins in the "coins" list: 
                        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    win_screen() # This command allows for a program transition, to the function created below, win_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the score variable is 500, the code will also break out of the while loop, and not keep running the main game.
            
            
            window.update() # This command at the end of the full while game loop allows the window to update itself every time the loop is run through (it uses the turtle window function, _update()).










# Creating the new function for playing the game with character 1 (from the warrior menu, when user presses 1)

def play_game_character_2():
    global score # This command allows the function, play_game_random(), to use and change the global variable, "score"
    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\gong.wav",winsound.SND_ASYNC)
    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
    
    pen=turtle.Pen() # This turtle command uses the function, _Pen, to create a virtual pen (using the variable name pen) to draw with and create shapes in the turtle window.
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.speed(0) # This command sets the pen's speed to its fastest, 0. Animations are hard to see at this speed
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,0) # This command makes the pen travel to the centre of the turtle window
    
    pen.write("Good luck.",False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    time.sleep(2) # This command uses the time module, to stop all action in the turtle window, for 2 seconds
    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
    
    def no_effect_keys():
        None # A function within the menu, that does not allow any actions for some keys (that are used in other menu functions). This function defines what will happen when the specific keys are pressed, nothing.
    
    window.onkey(no_effect_keys,"w") # If the 1 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"p") # If the 2 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"c") # If the 3 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"1") # If the 1 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"2") # If the 2 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"3") # If the 3 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"Escape") # If the esc key is pressed in the turtle window, the no_effect_keys function will be used
    window.listen() # This command allows for the turtle window to listen for key inputs, making the no_effect_keys function work
    
    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
    
    backgrounds=[r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_1.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_2.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_3.gif"] # Here, I have made a list of three random backgrounds, to be picked randomly and be used as the game background, in the code later. The "r" before each file path is used to turn the file location into string literal, so the backslashes do not get mistaken for string commands (ex. "\n")
    window.bgpic(random.choice(backgrounds)) # The turtle module can only import and register .gif picture files
    # This command uses the turtle module, and its _bgpic function, to set the turtle window's background to a random picture stored on the computer, in the python list "backgrounds". 
    # This function uses one argument: the picture being used from the computer's directory, as the turtle window's background picture
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    
    player=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
    playershapes=[r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_2_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_2_side_left_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_2_side_right_SMALL.gif"] # Here, I have made a list of three player movement images, to be used in the code later, for the player turtle's shape. The "r" before each file path is used to turn the file location into string literal, so the backslashes do not get mistaken for string commands (ex. "\n")
    player.shape(playershapes[0]) # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above, the first image index of the player list.
    player.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
    player.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
    player.goto(0,-290) # This command moves the player turtle to the horizontal centre of the turtle window, while moving it down 290 pixels
    def player_move_left(): # This command allows for player movement in the game. This function is to move the player left.
        player.setheading=270 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 270 degrees sets the turtle to look to the left.
    
    def player_move_right(): # This command allows for player movement in the game. This function is to move the player right.
        player.setheading=90 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 90 degrees sets the turtle to look to the right.
    
    window.listen() # This command allows for the turtle window to listen for key inputs, making the player_move_left and player_move_right functions work
    window.onkey(player_move_left,"Left") # If the left arrow key is pressed in the turtle window, the player_move_left function will be used
    window.onkey(player_move_right,"Right") # If the right arrow key is pressed in the turtle window, the player_move_right function will be used
    
    
    fireballs=[] # Here, I have created an empty list, to be appended with fireball turtles for the game.
    
    for i in range(14): # This range command makes it so that this for loop is run through 14 times, effectively creating and appending 14 fireball turtles to the list, fireballs
        fireball=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
        fireball.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        fireball.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
        fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
        fireball.speed(random.randint(1,5)) # This changes the fireball turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
        fireball.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\fireball_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
        fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
        fireballs.append(fireball) # This command appends the fireball turtle, with all of its specified parameters, into the list of fireballs
    
    
    coins=[] # Here, I have created an empty list, to be appended with coin turtles for the game.
    
    for i in range(5): # This range command makes it so that this for loop is run through 5 times, effectively creating and appending 5 coin turtles to the list, coins
        coin=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
        coin.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        coin.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
        coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
        coin.speed(random.randint(1,5)) # This changes the coin turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
        coin.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\coin_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
        coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
        coins.append(coin) # This command appends the coin turtle, with all of its specified parameters, into the list of coins
    
    
    lives=5 # Here, I have created a variable for the game, lives, and have set it to become 5. The user will start the game with 5 lives
    
    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
    
    
    
    while lives>0 and score<500: # While the lives variable is greater than 0, and the score variable is less than 500, this loop will run, it will break after these ranges are exceeded.
        if player.setheading==270: # From the defined functions above, when player_move_left is in effect:
            player.shape(playershapes[1]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the left facing player picture that I have registered in the turtle window.
            x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
            x_coordinate-=4 # While the player is facing left, The x coordinate will move 4 pixels to the left, horizontally, in the turtle window.
            if x_coordinate<-450: # If the x coordinate of the player is at the left side of the screen (-450 pixels):
                x_coordinate=-450 # Keep resetting the x coordinate to -450 (keep the player on the screen)
                player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
            player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
        
        if player.setheading==90: # From the defined functions above, when player_move_left is in effect:
            player.shape(playershapes[2]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the right facing player picture that I have registered in the turtle window.
            x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
            x_coordinate+=4 # While the player is facing right, The x coordinate will move 4 pixels to the right, horizontally, in the turtle window.
            if x_coordinate>450: # If the x coordinate of the player is at the right side of the screen (450 pixels):
                x_coordinate=450 # Keep resetting the x coordinate to 450 (keep the player on the screen)
                player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
            player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
        
        
        window.tracer(1,0) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
        
        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list:
            y_coordinate=fireball.ycor() # I created a variable to represent the fireball's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
            y_coordinate-=3 # The y coordinate of the fireball is going vertically down by 3 pixels, continuously, the for loop is in a while loop
            fireball.sety(y_coordinate) # Set the y coordinate of the fireball to the variable, y_coordinate
            
            if y_coordinate<-300: # If the fireball's y coordinate is less (lower) than -300 pixels:
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
            
            if fireball.distance(player)<50: # If the fireball turtle is within 50 pixels of the player turtle (collision):
                winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\sword.wav",winsound.SND_ASYNC)
                # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
                lives-=1 # Every time a fireball hits the player, the player loses a life (lives-=1 is the same as lives=lives-1)
                if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\heartbeat.wav",winsound.SND_ASYNC)
                    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                    window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for coin in coins: # For every one of the 5 coins in the "coins" list: 
                        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                elif lives>1: # If the lives variable is greater than 1: 
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
        
        
        for coin in coins: # For every one of the 5 coins in the "coins" list: 
            y_coordinate=coin.ycor() # I created a variable to represent the coin's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
            y_coordinate-=3 # The y coordinate of the coin is going vertically down by 3 pixels, continuously, the for loop is in a while loop
            coin.sety(y_coordinate) # Set the y coordinate of the coin to the variable, y_coordinate
            
            if y_coordinate<-300: # If the coin's y coordinate is less (lower) than -300 pixels:
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
            
            if coin.distance(player)<50: # If the coin turtle is within 50 pixels of the player turtle (collision):
                winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\coin_hit.wav",winsound.SND_ASYNC)
                # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
                score+=5 # Every time a coin hits the player, the player gains 5 points (score+=5 is the same as score=score+5)
                if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                    window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for coin in coins: # For every one of the 5 coins in the "coins" list: 
                        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                elif lives>1: # If the lives variable is greater than 1: 
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                if score>=500:
                    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                    window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for coin in coins: # For every one of the 5 coins in the "coins" list: 
                        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    win_screen() # This command allows for a program transition, to the function created below, win_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the score variable is 500, the code will also break out of the while loop, and not keep running the main game.
            
            
            window.update() # This command at the end of the full while game loop allows the window to update itself every time the loop is run through (it uses the turtle window function, _update()).










# Creating the new function for playing the game with character 1 (from the warrior menu, when user presses 1)

def play_game_character_3():
    global score # This command allows the function, play_game_random(), to use and change the global variable, "score"
    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\gong.wav",winsound.SND_ASYNC)
    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
    
    pen=turtle.Pen() # This turtle command uses the function, _Pen, to create a virtual pen (using the variable name pen) to draw with and create shapes in the turtle window.
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.speed(0) # This command sets the pen's speed to its fastest, 0. Animations are hard to see at this speed
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,0) # This command makes the pen travel to the centre of the turtle window
    
    pen.write("Good luck.",False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    time.sleep(2) # This command uses the time module, to stop all action in the turtle window, for 2 seconds
    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
    
    def no_effect_keys():
        None # A function within the menu, that does not allow any actions for some keys (that are used in other menu functions). This function defines what will happen when the specific keys are pressed, nothing.
    
    window.onkey(no_effect_keys,"w") # If the 1 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"p") # If the 2 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"c") # If the 3 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"1") # If the 1 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"2") # If the 2 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"3") # If the 3 key is pressed in the turtle window, the no_effect_keys function will be used
    window.onkey(no_effect_keys,"Escape") # If the esc key is pressed in the turtle window, the no_effect_keys function will be used
    window.listen() # This command allows for the turtle window to listen for key inputs, making the no_effect_keys function work
    
    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
    
    backgrounds=[r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_1.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_2.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\level_background_3.gif"] # Here, I have made a list of three random backgrounds, to be picked randomly and be used as the game background, in the code later. The "r" before each file path is used to turn the file location into string literal, so the backslashes do not get mistaken for string commands (ex. "\n")
    window.bgpic(random.choice(backgrounds)) # The turtle module can only import and register .gif picture files
    # This command uses the turtle module, and its _bgpic function, to set the turtle window's background to a random picture stored on the computer, in the python list "backgrounds". 
    # This function uses one argument: the picture being used from the computer's directory, as the turtle window's background picture
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    
    player=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
    playershapes=[r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_3_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_3_side_left_SMALL.gif",r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\character_3_side_right_SMALL.gif"] # Here, I have made a list of three player movement images, to be used in the code later, for the player turtle's shape. The "r" before each file path is used to turn the file location into string literal, so the backslashes do not get mistaken for string commands (ex. "\n")
    player.shape(playershapes[0]) # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above, the first image index of the player list.
    player.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
    player.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
    player.goto(0,-300) # This command moves the player turtle to the horizontal centre of the turtle window, while moving it down 290 pixels
    def player_move_left(): # This command allows for player movement in the game. This function is to move the player left.
        player.setheading=270 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 270 degrees sets the turtle to look to the left.
    
    def player_move_right(): # This command allows for player movement in the game. This function is to move the player right.
        player.setheading=90 # If the program goes into this function, use the turtle command, _setheading(), to change the direction the turtle is facing. Here, 90 degrees sets the turtle to look to the right.
    
    window.listen() # This command allows for the turtle window to listen for key inputs, making the player_move_left and player_move_right functions work
    window.onkey(player_move_left,"Left") # If the left arrow key is pressed in the turtle window, the player_move_left function will be used
    window.onkey(player_move_right,"Right") # If the right arrow key is pressed in the turtle window, the player_move_right function will be used
    
    
    fireballs=[] # Here, I have created an empty list, to be appended with fireball turtles for the game.
    
    for i in range(14): # This range command makes it so that this for loop is run through 14 times, effectively creating and appending 14 fireball turtles to the list, fireballs
        fireball=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
        fireball.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        fireball.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
        fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
        fireball.speed(random.randint(1,5)) # This changes the fireball turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
        fireball.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\fireball_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
        fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
        fireballs.append(fireball) # This command appends the fireball turtle, with all of its specified parameters, into the list of fireballs
    
    
    coins=[] # Here, I have created an empty list, to be appended with coin turtles for the game.
    
    for i in range(5): # This range command makes it so that this for loop is run through 5 times, effectively creating and appending 5 coin turtles to the list, coins
        coin=turtle.Turtle() # This command uses the turtle module function, _Turtle(), to create a turtle, or object, to be seen in the turtle window
        coin.speed(0) # This command sets the turtle's speed to 0, the fastest speed possible. Animations are hard to see at this speed
        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
        coin.penup() # This command makes it so that the turtle pen does not draw until told to, with the command, turtle.pendown()
        coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically
        coin.speed(random.randint(1,5)) # This changes the coin turtle's speed to a random one, between the speeds of 1 (lowest), and 5 (a little bit faster)
        coin.shape(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\coin_SMALL.gif") # This command uses the turtle module function, _shape(), to define the shape, or in this case image, of the defined turtle. I have set the shape to a registered window image from above
        coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
        coins.append(coin) # This command appends the coin turtle, with all of its specified parameters, into the list of coins
    
    
    lives=5 # Here, I have created a variable for the game, lives, and have set it to become 5. The user will start the game with 5 lives
    
    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
    
    
    
    while lives>0 and score<500: # While the lives variable is greater than 0, and the score variable is less than 500, this loop will run, it will break after these ranges are exceeded.
        if player.setheading==270: # From the defined functions above, when player_move_left is in effect:
            player.shape(playershapes[1]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the left facing player picture that I have registered in the turtle window.
            x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
            x_coordinate-=4 # While the player is facing left, The x coordinate will move 4 pixels to the left, horizontally, in the turtle window.
            if x_coordinate<-450: # If the x coordinate of the player is at the left side of the screen (-450 pixels):
                x_coordinate=-450 # Keep resetting the x coordinate to -450 (keep the player on the screen)
                player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
            player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
        
        if player.setheading==90: # From the defined functions above, when player_move_left is in effect:
            player.shape(playershapes[2]) # The player turtle's _shape() will change to a different one in the above list, playershapes. It will become the right facing player picture that I have registered in the turtle window.
            x_coordinate=player.xcor() # I created a variable to represent the player's x coordinate, it uses the turtle funcion, _xcor(), to perform its functions
            x_coordinate+=4 # While the player is facing right, The x coordinate will move 4 pixels to the right, horizontally, in the turtle window.
            if x_coordinate>450: # If the x coordinate of the player is at the right side of the screen (450 pixels):
                x_coordinate=450 # Keep resetting the x coordinate to 450 (keep the player on the screen)
                player.shape(playershapes[0]) # Set the shape of the player back to its original, facing forward image (in the list playershapes)
            player.setx(x_coordinate) # Set the x coordinate of the player to the variable, x_coordinate
        
        
        window.tracer(1,0) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
        
        for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list:
            y_coordinate=fireball.ycor() # I created a variable to represent the fireball's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
            y_coordinate-=3 # The y coordinate of the fireball is going vertically down by 3 pixels, continuously, the for loop is in a while loop
            fireball.sety(y_coordinate) # Set the y coordinate of the fireball to the variable, y_coordinate
            
            if y_coordinate<-300: # If the fireball's y coordinate is less (lower) than -300 pixels:
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
            
            if fireball.distance(player)<50: # If the fireball turtle is within 50 pixels of the player turtle (collision):
                winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\sword.wav",winsound.SND_ASYNC)
                # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                fireball.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the fireball turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the fireball at a random position in the sky) 
                fireball.showturtle() # This command shows the fireball turtle, so it may be seen in the turtle window
                lives-=1 # Every time a fireball hits the player, the player loses a life (lives-=1 is the same as lives=lives-1)
                if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\heartbeat.wav",winsound.SND_ASYNC)
                    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                    window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for coin in coins: # For every one of the 5 coins in the "coins" list: 
                        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                elif lives>1: # If the lives variable is greater than 1: 
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
        
        
        for coin in coins: # For every one of the 5 coins in the "coins" list: 
            y_coordinate=coin.ycor() # I created a variable to represent the coin's y coordinate, it uses the turtle funcion, _ycor(), to perform its functions
            y_coordinate-=3 # The y coordinate of the coin is going vertically down by 3 pixels, continuously, the for loop is in a while loop
            coin.sety(y_coordinate) # Set the y coordinate of the coin to the variable, y_coordinate
            
            if y_coordinate<-300: # If the coin's y coordinate is less (lower) than -300 pixels:
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
            
            if coin.distance(player)<50: # If the coin turtle is within 50 pixels of the player turtle (collision):
                winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\coin_hit.wav",winsound.SND_ASYNC)
                # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
                # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
                # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
                # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
                window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
                coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                coin.goto(random.randint(-475,475),random.randint(400,700)) # This command sends the coin turtle to a random location between -475 and 475 pixels horizontally, and a random location between 400 and 700 pixels vertically (resets the coin at a random position in the sky) 
                coin.showturtle() # This command shows the coin turtle, so it may be seen in the turtle window
                score+=5 # Every time a coin hits the player, the player gains 5 points (score+=5 is the same as score=score+5)
                if lives==1: # If the player turtle has one life left (the lives variable is equal to 1):
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                elif lives<1: # If the player turtle has less than one life left (the lives variable is less than 1):
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("Red") # This command sets the pen's color to white (Hex: FF0000)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                    window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for coin in coins: # For every one of the 5 coins in the "coins" list: 
                        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    game_over_screen() # This command allows for a program transition, to the function created below, game_over_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the lives variable is 0, the code will also break out of the while loop, and not keep running the main game.
                elif lives>1: # If the lives variable is greater than 1: 
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    pen.penup() # This command makes it so that the pen does not draw until told to, with the command, pen.pendown()
                    pen.goto(-375,300) # This command makes the pen travel left horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("SCORE: "+str(score),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current score.
                    pen.goto(375,300) # This command makes the pen travel right horizontally by 375 pixels in the turtle window, while moving up 300 pixels
                    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
                    pen.write("LIVES: "+str(lives),False,"center",font=("Rockwell Nova",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc. It writes the current lives.
                if score>=500:
                    time.sleep(1) # This command uses the time module, to stop all action in the turtle window, for 1 second
                    window.tracer(1,10) # By setting the turtle function, _tracer(), to (1,10), this command allows for the turtle window to show screen refreshes/animations at a certain speed
                    pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
                    player.hideturtle() # This command hides the player turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for fireball in fireballs: # For every one of the 14 fireballs in the "fireballs" list: 
                        fireball.hideturtle() # This command hides the fireball turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    for coin in coins: # For every one of the 5 coins in the "coins" list: 
                        coin.hideturtle() # This command hides the coin turtle, which otherwise would be seen in the window (mainly a cosmetic difference)
                    win_screen() # This command allows for a program transition, to the function created below, win_screen(). There is no prompt for changing the function, the code executes it in the turtle window. Because the score variable is 500, the code will also break out of the while loop, and not keep running the main game.
            
            
            window.update() # This command at the end of the full while game loop allows the window to update itself every time the loop is run through (it uses the turtle window function, _update()).










# Creating the new function for the game over screen (when the user loses all of their lives in game, and dies)

def game_over_screen():
    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
    global score # This command allows the function, play_game_random(), to use and change the global variable, "score"
    window.bgpic(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\menu_background.gif") # The turtle module can only import and register .gif picture files
    # This command uses the turtle module, and its _bgpic function, to set the turtle window's background to a random picture stored on the computer, in the python list "backgrounds". 
    # This function uses one argument: the picture being used from the computer's directory, as the turtle window's background picture
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\gong.wav",winsound.SND_ASYNC)
    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
    
    pen=turtle.Pen() # This turtle command uses the function, _Pen, to create a virtual pen (using the variable name pen) to draw with and create shapes in the turtle window.
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.speed(0) # This command sets the pen's speed to its fastest, 0. Animations are hard to see at this speed
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,0) # This command makes the pen travel to the centre of the turtle window
    pen.write("G A M E   O V E R",False,"center",font=("Papyrus",50,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    pen.goto(0,-75) # This command makes the pen travel to the horizontal centre of the turtle window, while moving down 75 pixels
    pen.write("SCORE: "+str(score),False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    pen.goto(0,-200) # This command makes the pen travel to the horizontal centre of the turtle window, while moving down 200 pixels
    pen.write("THE APOCALYPSE TAKES  OVER",False,"center",font=("Papyrus",20,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    pen.goto(0,-325) # This command makes the pen travel to the horizontal centre of the turtle window, while moving down 325 pixels
    pen.write("[Press esc to return to menu]",False,"center",font=("Papyrus",15,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    
    def esc_button():
        global score # This command allows the function, play_game_random(), to use and change the global variable, "score"
        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
        score=0 # This command sets the global variable, score, back to 0. This allows for the user to go back to the menu, and play another game, with the score starting at 0.
        menu() # This command allows for a program transition, to the function created below, menu(). There is no prompt for changing the function, the code executes it in the turtle window
    
    window.onkey(esc_button,"Escape") # If the esc key is pressed in the turtle window, the esc_button function will be used
    window.listen() # This command allows for the turtle window to listen for key inputs, making the no_effect_keys function work










# Creating the new function for the win screen (when the user obtains 500 points from collecting coins in game, and wins)

def win_screen():
    window.tracer(0,0) # By setting the turtle function, _tracer(), to (0,0), this command allows for the turtle window to not show screen refreshes/animations
    global score # This command allows the function, play_game_random(), to use and change the global variable, "score"
    window.bgpic(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\VISUAL\menu_background.gif") # The turtle module can only import and register .gif picture files
    # This command uses the turtle module, and its _bgpic function, to set the turtle window's background to a random picture stored on the computer, in the python list "backgrounds". 
    # This function uses one argument: the picture being used from the computer's directory, as the turtle window's background picture
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    winsound.PlaySound(r"C:\Users\trist\Pictures\APOCALYPSE\ASSETS\AUDIO\win.wav",winsound.SND_ASYNC)
    # This command uses the winsound module, and its _PlaySound function, to play the introduction song for the game. 
    # This function uses two arguments: the first being the sound for the computer to play, and the second being the way to play the sound (winsound flag). 
    # Here, the "r" before the file location is used to turn the location into string literal form, so the backslashes are not mistaken for string commands (ex: "\n")
    # The winsound flag, "windsound.SND_ASYNC" is used to play the sound asynchronously, to return the sound immediately. Since the song is over a minute long, it will play into the menu() function, until it stops later.
    
    pen=turtle.Pen() # This turtle command uses the function, _Pen, to create a virtual pen (using the variable name pen) to draw with and create shapes in the turtle window.
    pen.color("White") # This command sets the pen's color to white (Hex: FFFFFF)
    pen.speed(0) # This command sets the pen's speed to its fastest, 0. Animations are hard to see at this speed
    
    pen.up() # This command makes it so that the pen does not draw until told to, with the command, pen.down()
    pen.hideturtle() # This command hides the tip of the pen, which otherwise would be seen in the window (mainly a cosmetic difference)
    pen.goto(0,0) # This command makes the pen travel to the centre of the turtle window
    pen.write("Y O U   W I N",False,"center",font=("Papyrus",50,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    pen.goto(0,-75) # This command makes the pen travel to the horizontal centre of the turtle window, while moving down 75 pixels
    pen.write("SCORE: "+str(score),False,"center",font=("Papyrus",30,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    pen.goto(0,-200) # This command makes the pen travel to the horizontal centre of the turtle window, while moving down 200 pixels
    pen.write("YOU HAVE DEFEATED THE APOCALYPSE",False,"center",font=("Papyrus",20,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    pen.goto(0,-325) # This command makes the pen travel to the horizontal centre of the turtle window, while moving down 325 pixels
    pen.write("[Press esc to return to menu]",False,"center",font=("Papyrus",15,"bold")) # This line uses the turtle function to write text in the turtle window. The text to be written can be seen as the first argument of the function, while the other arguments define the text's alignment, size, font, font type, etc.
    
    
    def esc_button():
        global score # This command allows the function, play_game_random(), to use and change the global variable, "score"
        pen.clear() # This command uses the turtle function, _clear(), to erase the pen's marks, writing, or drawings, from the turtle window
        score=0 # This command sets the global variable, score, back to 0. This allows for the user to go back to the menu, and play another game, with the score starting at 0.
        menu() # This command allows for a program transition, to the function created below, menu(). There is no prompt for changing the function, the code executes it in the turtle window
    
    window.onkey(esc_button,"Escape") # If the esc key is pressed in the turtle window, the esc_button function will be used
    window.listen() # This command allows for the turtle window to listen for key inputs, making the no_effect_keys function work










# Starting the program at the first function, "story()". This will start the program at its beginning, and allow for function transitions within the rest of the code (see above)

story() # This command allows the program to run, starting at the story() function. The rest of the transitions happen within the other functions in the program










# Enabling the turtle-generated window to run the program

turtle.mainloop() # This command uses the turtle function, _mainloop(), to start and run the loop for the turtle program