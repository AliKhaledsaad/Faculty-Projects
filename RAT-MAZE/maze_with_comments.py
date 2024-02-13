import turtle
"""
turtle:
turtle is a built-in module in Python that provides a way to create graphics and shapes using a turtle-based drawing board. It is a beginner-friendly library that provides a simple way to create drawings, animations, and games by using turtle graphics.

The turtle module provides a set of turtle commands that allow the user to create graphics and shapes, draw lines and curves, set colors and fonts, and more. Here are some of the key features of turtle:

It provides a turtle canvas on which the user can draw lines and shapes.
Users can control the turtle's movement by specifying its direction, speed, and position.
It provides various methods for drawing lines, circles, and shapes.
It allows the user to set the turtle's color and fill style.
It provides a way to write text on the canvas.
It supports keyboard and mouse events for interactivity.
"""


# Ask for the level
level_choice_prompt = """Choose the level:
1-easy
2-medium
3-hard
"""
level_choice = input(level_choice_prompt)

# If the user entered something other than 1, 2, and 3
while level_choice not in ["1", "2", "3"]:
    level_choice = input("Please choose a valid level (1, 2, or 3): ")

level_choice = int(level_choice)

window = turtle.Screen()
window.title("OUR MAZE GAME")
window.setup(700, 700)
window.bgcolor("black")

#shapes
turtle.register_shape("player.gif")
turtle.register_shape("goal.gif")
turtle.register_shape("wall.gif")
# Create class pen child of class Turtle
class pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)    # initialize super class Turtle
        #self.shape("square")            # shape of the walls
        self.shape("wall.gif")
        self.color("red")               # colors
        self.penup()                    # allow not to draw between walls 
        self.speed(0)

        # Create Player child of class Turtle (for player with yellow color)
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        #self.shape("arrow")
        self.shape("player.gif")
        self.color("yellow")
        self.penup()
        self.speed(0)

        # Define the go_up method for moving the player upward
    def go_up(self):
        # Get the current x-coordinate of the player
        move_to_x = self.xcor()
        # Calculate the new y-coordinate by adding 24 to the current y-coordinate
        move_to_y = self.ycor() + 24

        # Check if the new position is not within the walls
        if (move_to_x, move_to_y) not in walls:
            # Move the player to the new position
            self.goto(move_to_x, move_to_y)
            # Check if the player has reached the goal
            self.check_goal()

                # Define the go_dowindow method for moving the player dowindowward
    def go_down(self):
                # Get the current x-coordinate of the player
        move_to_x = self.xcor()
                # Calculate the new y-coordinate by subtracting 24 from the current y-coordinate
        move_to_y = self.ycor() - 24

                    # Check if the new position is not within the walls
        if (move_to_x, move_to_y) not in walls:
                    # Move the player to the new position
            self.goto(move_to_x, move_to_y)
                    # Check if the player has reached the goal
            self.check_goal()

                    # Define the go_right method for moving the player to the right
    def go_right(self):
                    # Calculate the new x-coordinate by adding 24 to the current x-coordinate
        move_to_x = self.xcor() + 24
            # Get the current y-coordinate of the player
        move_to_y = self.ycor()

                        # Check if the new position is not within the walls
        if (move_to_x, move_to_y) not in walls:
                        # Move the player to the new position
            self.goto(move_to_x, move_to_y)
                        # Check if the player has reached the goal
            self.check_goal()

                # Define the go_left method for moving the player to the left
    def go_left(self):
            move_to_x = self.xcor() - 24
            move_to_y = self.ycor()

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
                self.check_goal()

    def check_goal(self):
        if self.pos() == goal.pos():
            print("""
                 ' ' ' ' ' ' ' ' ' ' ' ' ' ' 
                 
                  Congratulations, you won!
                  
                 ' ' ' ' ' ' ' ' ' ' ' ' ' '
                  """)
            window.bye()  # Close the game window
        
                    # Create levels list and inside it will be put what i choose
            # Initialize an empty list for levels
levels = [""]

        # Create empty lists for easy, medium, and hard levels
level_easy = [
"XXXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXX            XXX",
"X  XXXXXXX  XXXXXX  XX XXX",
"X       XX  XXXXXX  X XXXX",
"X       XX  XXX        XXX",
"XXXXXX  XX  XXX        XXX",
"XXXXXX  XX  XXXXXX  XXXXXX",
"XXXXXX  XX    XXXX  XXXXXX",
"X  XXX        XXXX  XXXXXX",
"X  XXX  XXXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXXX",
"X                XXXXXXXXX",
"XXXXXXXXXXXX     XXXXX  XX",
"XXXXXXXXXXXXXXX  XXXXX  XX",
"XXX  XXXXXXXXXX         XX",
"XXX                     XX",
"XXX         XXXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXXX",
"XXXXXXXXXX              XX",
"XX   XXXXX              XX",
"XX   XXXXXXXXXXXXX  XXXXXX",
"XX    YXXXXXXXXXXX  XXXXXX",
"XX          XXXX        XX",
"XXXX                    XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXX"
]
level_medium = [
"XXXXXXXXXXXXXXXXXXXXXXXXXX",
"XP                       X",
"X  X X X X  X XX X  XX XXX",
"X        X  X X X   X X  X",
"X X XX  XX       X       X",
"X X  X  XX  X X X X     XX",
"XXXXXX  XX  XXXXXX  XXXXXX",
"XXXXXX  XX    XXXX  XXXXXX",
"X  XXX        XXXX  XXXXXX",
"X  XXX  XXXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXXX",
"X                XXXXXXXXX",
"XXXXXXXXXXXX     XXXXX  XX",
"XX  X X X X X X X X  X X X",
"X XX X X X              XX",
"XXX         X X X X X X  X",
"X X X X XX  XX X X XXX X X",
"XXXXXXXXXX  XXXXXXXXXXXXXX",
"XXXXXXXXXX              XX",
"XX   XXXXX              XX",
"X XX XX X XXX  X XX      X",
"XX          X XXX X XXX XX",
"X  X X X XXX    XX  X   XX",
"XX X  X X X X X  X XXXX XX",
"XX    X         X       XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXX"
]
level_hard = [
"XXXXXXXXXXXXXXXXXXXXXXXXXX",
"XP                       X",
"X  X X X X  X XX X  XX XXX",
"X        X  X X X   X X  X",
"X X XX  XX       X       X",
"X X  X  XX  X X X X     XX",
"X XX X  X X X       XXX  X",
"X    X X X   XX XX  X    X",
"XX X XX  X   X   X X  XX X",
"X X X X X X XX  X XX X XXX",
"X         XXX XXX X     XX",
"X                  XXXX XX",
"XX X X X X X X X X X    XX",
"X  X X X X X X X X X XX XX",
"XX  X X X X X X X X  X X X",
"X XX X X X              XX",
" XX         X X X X X X  X",
"X X X X XX  XX X X XXX X X",
"XX   X X X XX X X X X XXXX",
"X    X                  XX",
"XX   X X XX X X X X X X XX",
"X XX XX X XXX  X XX      X",
"XX          X XXX X XXX XX",
"X  X X X XXX    XX  X   XX",
" X X  X X X X X  X XXXXXXX",
"XX    X         X       XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXX"
]

        # Add the level lists to the main levels list
levels.append(level_easy)
levels.append(level_medium)
levels.append(level_hard)

                # Function to set up the maze based on the level chosen
def setup_maze(level):
                # Iterate through each row in the level
    for y in range(len(level)):
                 # Iterate through each character in the row
        for x in range(len(level[y])):
                # Get the character at the current position
            char = level[y][x]
                # Calculate the screen y-coordinate based on the current row
            screen_y = 288 - (y * 24)
                # Calculate the screen x-coordinate based on the current column
            screen_x = -288 + (x * 24)
                 # Check if the character is an "X" (representing a wall)
            if char == "X":
                    # Move the pen to the calculated position
                pen.goto(screen_x, screen_y)
                    # draw the pen at the position to create a wall
                pen.shape("wall.gif")
                pen.stamp()
                    # Add the wall position to the walls list
                walls.append((screen_x, screen_y))

                    # Check if the character is a "P" (representing the player)
            if char == "P":
                    # Move the player to the calculated position
                player.goto(screen_x, screen_y)

                    # Check if the character is a "G" (representing the goal)
            if char == "G":
                        # Move the goal to the calculated position
                goal.goto(screen_x, screen_y)
                        # Set the goal color to red
                goal.shape("goal.gif")
                goal.color("blue")
                         # Stamp the goal at the position
                goal.stamp()
                """
                what is stamp()    and pen :
                    `stamp()` and `pen` are related to the Turtle graphics library in Python.
                    The Turtle graphics library is a popular tool for teaching programming concepts, as it allows users to visually represent code execution through simple graphics and movement.

                    `pen` is an instance of a custom class called `game`, which is a subclass of the `turtle.Turtle` class.
                    The `game` class is used for drawing the walls of the maze on the screen. It has all the built-in methods and attributes of the `turtle.Turtle` class, such as `goto()`, `forward()`, `left()`, etc., which are used to control its movement and drawing behavior.
                    `stamp()` is a method of the `turtle.Turtle` class. When called, it leaves an impression of the turtle's shape at its current position on the screen. In the context of the maze game, the `stamp()` method is used to draw the walls and the goal in the maze:
                    1. When drawing the walls, the `pen` instance moves to the position of a wall and calls the `stamp()` method to leave a square shape on the screen, representing a wall segment.
                    2. When drawing the goal, the `goal` instance (another subclass of `turtle.Turtle`) moves to the goal position and calls the `stamp()` method to leave a square shape on the screen, representing the goal.
                    In summary, `stamp()` is a method used to leave a visual mark on the screen at the current position of a Turtle object, and `pen` is an instance of a custom class used to draw elements of the maze, such as walls and the goal.
                """
                """
                why 288  and -288:
                The numbers 288 and -288 are used to set the initial position of the pen and other elements on the screen.
                In this particular case, the screen has a size of 576x576 units.
                To set the origin at the top-left corner of the screen, these values are used:
                The x-coordinate starts at -288 (left edge) and goes to 288 (right edge).
                 The y-coordinate starts at 288 (top edge) and goes to -288 (bottom edge).
                Using these values, the screen is divided into 24x24 cells, and the pen is moved to the corresponding cell positions based on the maze layout. As a result, the maze is drawindow on the screen with the correct alignment.
                """

        # Create instances of the game and Player classes
pen = pen()
player = Player()

        # Create a list to store wall coordinates
walls = []

        # Create the goal turtle
goal = turtle.Turtle()
#goal.shape("circle")
goal.shape("goal.gif")
goal.color("blue")
goal.penup()
goal.speed(0)
goal.goto(264, -264)

        # Set up the level based on the user's choice
setup_maze(levels[level_choice])

        # Bind the player movement methods to keyboard keys
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

        # Turn off screen updates
window.tracer(0)

        # Main game loop
while True:
         # Update the screen every iteration and keeps the game continue
    window.update()