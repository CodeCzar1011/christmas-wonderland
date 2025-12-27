import turtle
import random
import math

def position(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def star(size,color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def light(size,color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def festive_ornament(x, y, size, color1, color2):
    """Create layered ornaments with festive colors"""
    position(x, y)
    turtle.color(color1)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    
    # Add inner decoration
    turtle.color(color2)
    turtle.begin_fill()
    turtle.circle(size//2)
    turtle.end_fill()

def candy_cane_lights(start_x, start_y, count):
    """Create candy cane colored light pattern"""
    colors = ['red', 'white', 'red', 'white', 'green']
    for i in range(count):
        x = start_x + (i * 40)
        y = start_y + (10 * math.sin(i * 0.5))
        position(x, y)
        light(15, colors[i % len(colors)])

# Setup
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgpic('trees.png')
screen.bgcolor('navy')
screen.title("🎄 FESTIVE CHRISTMAS SCENE 🎄")

# Begin editing the code below this line ------>

# 🌟 BRIGHT TREE TOPPER 🌟
position(-50, 380)
star(70, 'gold')

# 🎄 COLORFUL ORNAMENT COLLECTION 🎄
ornament_data = [
    (-100, 300, 18, 'red', 'gold'),
    (50, 310, 16, 'blue', 'silver'),
    (-130, 230, 20, 'green', 'yellow'),
    (80, 240, 14, 'purple', 'pink'),
    (-160, 160, 22, 'orange', 'red'),
    (110, 170, 18, 'cyan', 'blue'),
    (-190, 90, 16, 'magenta', 'white'),
    (140, 100, 20, 'lime', 'green')
]

for ornament in ornament_data:
    festive_ornament(ornament[0], ornament[1], ornament[2], ornament[3], ornament[4])

# 🍭 CANDY CANE LIGHT STRINGS 🍭
candy_cane_lights(-200, 280, 10)
candy_cane_lights(-220, 200, 11)
candy_cane_lights(-240, 120, 12)

# ✨ SPARKLING ACCENT LIGHTS ✨
sparkle_positions = [
    (-80, 350), (70, 360), (-110, 280), (90, 290),
    (-140, 210), (120, 220), (-170, 140), (150, 150),
    (-200, 70), (180, 80)
]

sparkle_colors = ['yellow', 'white', 'gold', 'light yellow']
for pos in sparkle_positions:
    position(pos[0], pos[1])
    light(8, random.choice(sparkle_colors))

# 🎁 PRESENTS UNDER THE TREE 🎁
def draw_present(x, y, width, height, color):
    position(x, y)
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    
    # Add ribbon
    turtle.color('gold')
    turtle.pensize(3)
    position(x + width//2, y)
    turtle.goto(x + width//2, y + height)
    position(x, y + height//2)
    turtle.goto(x + width, y + height//2)

# Draw presents
draw_present(-120, -200, 40, 30, 'red')
draw_present(-60, -200, 35, 25, 'green')
draw_present(20, -200, 45, 35, 'blue')
draw_present(80, -200, 38, 28, 'purple')

turtle.hideturtle()
turtle.done()

