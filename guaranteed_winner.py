import turtle
import random
import math
import time

# 🎄 GUARANTEED WINNER - ULTIMATE CHRISTMAS TREE 🏆

def position(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def mega_star(size, color):
    """⭐ Create mega stars with multiple layers"""
    # Outer glow
    turtle.color('white')
    turtle.pensize(3)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size + 10)
        turtle.right(144)
    turtle.end_fill()
    
    # Main star
    turtle.color(color)
    turtle.pensize(2)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()
    
    # Inner shine
    turtle.color('yellow')
    turtle.pensize(1)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size * 0.5)
        turtle.right(144)
    turtle.end_fill()

def rainbow_light(size, color_index):
    """🌈 Create rainbow lights"""
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pink', 'cyan', 'magenta']
    color = colors[color_index % len(colors)]
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def diamond_ornament(size, color1, color2):
    """💎 Create diamond ornaments"""
    # Main ornament
    turtle.color(color1)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    
    # Inner shine
    turtle.color(color2)
    turtle.begin_fill()
    turtle.circle(size * 0.6)
    turtle.end_fill()
    
    # Core sparkle
    turtle.color('white')
    turtle.begin_fill()
    turtle.circle(size * 0.3)
    turtle.end_fill()

def create_snow_system():
    """❄️ Create advanced snow system"""
    snow_particles = []
    for i in range(20):
        particle = turtle.Turtle()
        particle.shape("circle")
        particle.shapesize(random.uniform(0.3, 1.0))
        particle.color("white")
        particle.penup()
        particle.speed(0)
        particle.goto(random.randint(-600, 600), random.randint(400, 800))
        particle.dx = random.uniform(-1, 1)
        particle.dy = random.uniform(-3, -1)
        snow_particles.append(particle)
    return snow_particles

def draw_luxury_presents():
    """🎁 Draw luxury presents"""
    presents = [
        (-150, -230, 50, 40, 'red', 'gold'),
        (-80, -230, 45, 35, 'green', 'silver'),
        (-10, -230, 55, 45, 'blue', 'gold'),
        (60, -230, 48, 38, 'purple', 'silver'),
        (130, -230, 42, 32, 'orange', 'gold')
    ]
    
    for x, y, w, h, box_color, ribbon_color in presents:
        # Present box
        position(x, y)
        turtle.color(box_color)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
        turtle.end_fill()
        
        # Ribbon
        turtle.color(ribbon_color)
        turtle.pensize(4)
        position(x + w//2, y)
        turtle.goto(x + w//2, y + h)
        position(x, y + h//2)
        turtle.goto(x + w, y + h//2)
        
        # Bow
        position(x + w//2, y + h)
        turtle.color(ribbon_color)
        turtle.dot(15)

# Setup screen
screen = turtle.Screen()
screen.setup(1200, 1000)
screen.bgpic('trees.png')
screen.bgcolor('#000033')
screen.title("🎄 GUARANTEED WINNER - ULTIMATE CHRISTMAS MASTERPIECE 🏆")
turtle.speed(0)

print("🎄 Loading Ultimate Christmas Masterpiece...")
print("🏆 Guaranteed Winner Loading...")
print("✨ Prepare to be amazed!")

# 🌟 SPECTACULAR TREE TOPPER 🌟
position(-50, 400)
mega_star(80, 'gold')

# 🌟 CONSTELLATION OF STARS 🌟
star_positions = [
    (-250, 370), (200, 380), (-300, 320), (250, 340),
    (-200, 300), (220, 310), (-280, 250), (270, 260),
    (-180, 200), (200, 210), (-300, 150), (280, 160),
    (-160, 100), (180, 110), (-320, 50), (300, 60)
]

for i, (x, y) in enumerate(star_positions):
    position(x, y)
    mega_star(random.randint(20, 35), 'yellow')

# 🎄 RAINBOW LIGHT STRINGS 🎄
# Top tier
for i in range(12):
    x = -140 + i * 20
    y = 350 + 10 * math.sin(i * 0.5)
    position(x, y)
    rainbow_light(10, i)

# Second tier
for i in range(15):
    x = -170 + i * 22
    y = 280 + 8 * math.sin(i * 0.4)
    position(x, y)
    rainbow_light(10, i + 3)

# Third tier
for i in range(18):
    x = -200 + i * 22
    y = 210 + 12 * math.sin(i * 0.6)
    position(x, y)
    rainbow_light(10, i + 6)

# Fourth tier
for i in range(20):
    x = -230 + i * 23
    y = 140 + 6 * math.sin(i * 0.3)
    position(x, y)
    rainbow_light(10, i + 9)

# Bottom tier
for i in range(22):
    x = -260 + i * 24
    y = 70 + 15 * math.sin(i * 0.7)
    position(x, y)
    rainbow_light(10, i + 12)

# 💎 DIAMOND ORNAMENTS 💎
ornament_positions = [
    (-90, 330, 18, 'red', 'pink'),
    (60, 340, 20, 'blue', 'cyan'),
    (-120, 260, 22, 'green', 'lime'),
    (90, 270, 16, 'purple', 'magenta'),
    (-150, 190, 24, 'orange', 'yellow'),
    (120, 200, 19, 'red', 'orange'),
    (-180, 120, 17, 'blue', 'aqua'),
    (150, 130, 25, 'purple', 'pink'),
    (-210, 50, 21, 'green', 'lime'),
    (180, 60, 18, 'gold', 'yellow')
]

for x, y, size, color1, color2 in ornament_positions:
    position(x, y)
    diamond_ornament(size, color1, color2)

# 🎀 PREMIUM GARLANDS 🎀
def draw_garland(start_x, start_y, width):
    turtle.color('forest green')
    turtle.pensize(8)
    position(start_x, start_y)
    
    for i in range(width):
        x = start_x + i
        y = start_y - 20 * (1 - math.cos(i * 0.02))
        turtle.goto(x, y)
    
    # Add decorations
    turtle.pensize(1)
    for i in range(0, width, 30):
        x = start_x + i
        y = start_y - 20 * (1 - math.cos(i * 0.02))
        position(x, y)
        turtle.color('gold')
        turtle.dot(8)

draw_garland(-220, 310, 340)
draw_garland(-250, 230, 400)
draw_garland(-280, 150, 460)

# 🎁 LUXURY PRESENTS 🎁
draw_luxury_presents()

# ❄️ SNOW SYSTEM ❄️
turtle.tracer(0)
snow_particles = create_snow_system()

# Add main snowfall
turtle.addshape("snowFall.gif")
main_snow = turtle.Turtle()
main_snow.shape("snowFall.gif")
main_snow.penup()
main_snow.goto(0, 600)
main_snow.speed(0)

# 🎵 ULTIMATE ANIMATION LOOP 🎵
frame_count = 0
while True:
    turtle.update()
    frame_count += 1
    
    # Animate main snowfall
    main_snow.forward(1.5)
    if main_snow.ycor() < -600:
        main_snow.goto(random.randint(-300, 300), 600)
    
    # Animate snow particles
    for particle in snow_particles:
        particle.goto(
            particle.xcor() + particle.dx + 0.3 * math.sin(frame_count * 0.02),
            particle.ycor() + particle.dy
        )
        
        if particle.ycor() < -600:
            particle.goto(random.randint(-600, 600), random.randint(600, 900))
            particle.dx = random.uniform(-1, 1)
            particle.dy = random.uniform(-3, -1)
    
    # Animate twinkling stars
    if frame_count % 30 == 0:
        for i, (x, y) in enumerate(random.sample(star_positions, 5)):
            position(x, y)
            colors = ['yellow', 'white', 'gold', 'light yellow']
            mega_star(random.randint(15, 30), random.choice(colors))
    
    # Animate rainbow lights
    if frame_count % 20 == 0:
        # Re-draw some light strings with new colors
        for i in range(8):
            x = -140 + i * 20
            y = 350 + 10 * math.sin(i * 0.5)
            position(x, y)
            rainbow_light(10, (i + frame_count // 20) % 10)
    
    # Flash tree topper
    if frame_count % 60 == 0:
        position(-50, 400)
        flash_color = 'white' if (frame_count // 60) % 2 == 0 else 'gold'
        mega_star(80, flash_color)
    
    time.sleep(0.03)  # 33 FPS smooth animation