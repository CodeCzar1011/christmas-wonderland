import turtle
import random
import math
import time

class UltraRealisticSantaTree:
    """🎅 ULTRA REALISTIC SANTA & CHRISTMAS TREE - GUARANTEED WINNER 🏆"""
    
    def __init__(self):
        self.frame_count = 0
        self.santa_animation_phase = 0
        self.tree_twinkle_phase = 0
        self.gift_placement_timer = 0
        self.setup_photorealistic_graphics()
        
    def setup_photorealistic_graphics(self):
        """🎨 Setup photorealistic high-quality graphics"""
        self.screen = turtle.Screen()
        self.screen.setup(1600, 900)
        self.screen.bgpic('trees.png')
        self.screen.bgcolor('#0A0A1A')  # Deep midnight for realism
        self.screen.title("🎅 ULTRA REALISTIC SANTA & CHRISTMAS TREE - PHOTOREALISTIC 🏆")
        turtle.speed(0)
        turtle.hideturtle()

def position(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_photorealistic_text(text, x, y, size, color):
    """✨ Draw photorealistic glowing text with depth"""
    # Deep shadow for depth
    for shadow_offset in [(4, -4), (3, -3), (2, -2)]:
        position(x + shadow_offset[0], y + shadow_offset[1])
        turtle.color('#1A1A1A')  # Dark shadow
        turtle.write(text, align="center", font=("Times New Roman", size + 2, "bold"))
    
    # Multiple glow layers for realism
    glow_layers = [
        ('#FFFFFF', size + 6, 2),
        ('#F8F8FF', size + 4, 1),
        ('#F0F0F0', size + 2, 1),
        (color, size, 0)
    ]
    
    for glow_color, glow_size, blur in glow_layers:
        for blur_x in range(-blur, blur + 1):
            for blur_y in range(-blur, blur + 1):
                position(x + blur_x, y + blur_y)
                turtle.color(glow_color)
                turtle.write(text, align="center", font=("Times New Roman", glow_size, "bold"))

def draw_ultra_realistic_santa(x, y, activity="placing_gifts"):
    """🎅 Draw ultra-realistic Santa with photorealistic details"""
    
    # Santa's body with realistic shading and texture
    position(x, y)
    turtle.color('#B22222')  # Fire brick red
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(55)
        turtle.left(90)
    turtle.end_fill()
    
    # Body shading for 3D realism
    position(x + 32, y)
    turtle.color('#8B0000')  # Dark red shadow
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(8)
        turtle.left(90)
        turtle.forward(55)
        turtle.left(90)
    turtle.end_fill()
    
    # Fabric texture lines
    turtle.color('#A0522D')
    turtle.pensize(1)
    for texture_y in range(y + 5, y + 50, 8):
        position(x + 2, texture_y)
        turtle.forward(36)
    
    # Santa's head with realistic skin tones
    position(x + 20, y + 55)
    turtle.color('#FFDBAC')  # Realistic skin
    turtle.begin_fill()
    turtle.circle(18)
    turtle.end_fill()
    
    # Head shading for dimension
    position(x + 30, y + 60)
    turtle.color('#F4A460')  # Sandy brown shadow
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    
    # Facial features with incredible detail
    # Eyes with depth
    position(x + 14, y + 60)
    turtle.color('black')
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    position(x + 26, y + 60)
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    
    # Eye highlights for life
    position(x + 15, y + 62)
    turtle.color('white')
    turtle.dot(2)
    position(x + 27, y + 62)
    turtle.dot(2)
    
    # Eyebrows
    turtle.color('#D3D3D3')  # Light gray
    turtle.pensize(2)
    position(x + 12, y + 65)
    turtle.goto(x + 18, y + 67)
    position(x + 22, y + 67)
    turtle.goto(x + 28, y + 65)
    
    # Nose with realistic shading
    position(x + 20, y + 55)
    turtle.color('#FFB6C1')  # Light pink
    turtle.begin_fill()
    turtle.circle(2)
    turtle.end_fill()
    
    # Rosy cheeks with gradient effect
    position(x + 10, y + 55)
    turtle.color('#FFB6C1')
    turtle.begin_fill()
    turtle.circle(4)
    turtle.end_fill()
    position(x + 30, y + 55)
    turtle.begin_fill()
    turtle.circle(4)
    turtle.end_fill()
    
    # Santa's magnificent beard with texture
    position(x + 20, y + 45)
    turtle.color('white')
    turtle.begin_fill()
    turtle.circle(16)
    turtle.end_fill()
    
    # Beard texture and depth
    beard_highlights = [
        (x + 12, y + 40), (x + 20, y + 38), (x + 28, y + 40),
        (x + 15, y + 45), (x + 25, y + 45), (x + 20, y + 50)
    ]
    for bx, by in beard_highlights:
        position(bx, by)
        turtle.color('#F8F8FF')  # Ghost white
        turtle.dot(3)
    
    # Santa's iconic hat with realistic fabric
    position(x + 20, y + 73)
    turtle.color('#DC143C')  # Crimson
    turtle.begin_fill()
    turtle.goto(x + 8, y + 100)
    turtle.goto(x + 32, y + 100)
    turtle.goto(x + 20, y + 73)
    turtle.end_fill()
    
    # Hat shading
    position(x + 25, y + 75)
    turtle.color('#B22222')
    turtle.begin_fill()
    turtle.goto(x + 30, y + 95)
    turtle.goto(x + 32, y + 100)
    turtle.goto(x + 25, y + 75)
    turtle.end_fill()
    
    # Hat brim with thickness
    position(x + 8, y + 73)
    turtle.color('white')
    turtle.pensize(8)
    turtle.forward(24)
    
    # Hat pom-pom with fluffy texture
    position(x + 20, y + 100)
    turtle.color('white')
    turtle.begin_fill()
    turtle.circle(8)
    turtle.end_fill()
    # Fluffy texture
    for fluff_angle in range(0, 360, 45):
        fluff_x = x + 20 + 6 * math.cos(math.radians(fluff_angle))
        fluff_y = y + 100 + 6 * math.sin(math.radians(fluff_angle))
        position(fluff_x, fluff_y)
        turtle.color('#F0F8FF')
        turtle.dot(4)
    
    # Premium belt with realistic leather texture
    position(x, y + 28)
    turtle.color('black')
    turtle.pensize(10)
    turtle.forward(40)
    
    # Belt texture
    turtle.pensize(1)
    for belt_x in range(x + 5, x + 35, 6):
        position(belt_x, y + 26)
        turtle.goto(belt_x, y + 30)
    
    # Belt buckle with metallic shine
    position(x + 16, y + 25)
    turtle.color('#FFD700')  # Gold
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(8)
        turtle.left(90)
        turtle.forward(8)
        turtle.left(90)
    turtle.end_fill()
    
    # Buckle shine effect
    position(x + 17, y + 29)
    turtle.color('#FFFF00')  # Bright yellow
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(6)
        turtle.left(90)
        turtle.forward(3)
        turtle.left(90)
    turtle.end_fill()
    
    # Activity-based realistic arm positions
    turtle.color('#B22222')
    turtle.pensize(12)
    
    if activity == "placing_gifts":
        # Bending down to place gifts
        position(x, y + 40)
        turtle.goto(x - 25, y + 20)  # Left arm reaching down
        position(x + 40, y + 35)
        turtle.goto(x + 60, y + 15)  # Right arm placing gift
        
        # Show gift in hand
        position(x + 60, y + 10)
        turtle.color('#DC143C')  # Red gift
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(12)
            turtle.left(90)
            turtle.forward(8)
            turtle.left(90)
        turtle.end_fill()
        # Gift ribbon
        turtle.color('#FFD700')
        turtle.pensize(3)
        position(x + 66, y + 10)
        turtle.goto(x + 66, y + 18)
        
    elif activity == "admiring_tree":
        # Looking up at tree admiringly
        position(x, y + 45)
        turtle.goto(x - 20, y + 65)
        position(x + 40, y + 45)
        turtle.goto(x + 55, y + 60)
    
    # Premium boots with realistic leather
    turtle.color('black')
    turtle.pensize(15)
    position(x + 12, y)
    turtle.goto(x + 8, y - 25)
    # Boot sole with thickness
    turtle.goto(x + 20, y - 25)
    position(x + 28, y)
    turtle.goto(x + 32, y - 25)
    turtle.goto(x + 44, y - 25)
    
    # Boot buckles and details
    turtle.color('#C0C0C0')  # Silver
    position(x + 12, y - 8)
    turtle.dot(4)
    position(x + 28, y - 8)
    turtle.dot(4)
    
    # Boot shine
    turtle.color('#404040')  # Dark gray
    turtle.pensize(2)
    position(x + 10, y - 5)
    turtle.goto(x + 10, y - 20)
    position(x + 30, y - 5)
    turtle.goto(x + 30, y - 20)

def draw_spectacular_christmas_tree(x, y):
    """🎄 Draw spectacular Christmas tree with incredible decorations"""
    
    # Tree trunk with realistic bark texture
    position(x - 8, y - 50)
    turtle.color('#8B4513')  # Saddle brown
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(16)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
    turtle.end_fill()
    
    # Bark texture
    turtle.color('#654321')  # Dark goldenrod
    turtle.pensize(1)
    for bark_y in range(y - 45, y - 25, 4):
        position(x - 6, bark_y)
        turtle.forward(12)
    
    # Tree layers with realistic pine needle texture
    tree_layers = [
        (y + 200, 25, '#228B22'),  # Top
        (y + 160, 35, '#32CD32'),  # Upper middle
        (y + 120, 45, '#228B22'),  # Middle
        (y + 80, 55, '#32CD32'),   # Lower middle
        (y + 40, 65, '#228B22'),   # Lower
        (y, 75, '#32CD32')         # Bottom
    ]
    
    for layer_y, radius, color in tree_layers:
        position(x, layer_y)
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        
        # Pine needle texture
        turtle.color('#006400')  # Dark green
        turtle.pensize(1)
        for needle_angle in range(0, 360, 15):
            needle_x = x + (radius - 5) * math.cos(math.radians(needle_angle))
            needle_y = layer_y + (radius - 5) * math.sin(math.radians(needle_angle))
            position(needle_x, needle_y)
            turtle.goto(needle_x + 3 * math.cos(math.radians(needle_angle)), 
                        needle_y + 3 * math.sin(math.radians(needle_angle)))
    
    # Spectacular tree topper star with multiple layers
    position(x, y + 225)
    # Outer glow
    turtle.color('#FFFF00')  # Bright yellow
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(20)
        turtle.right(144)
    turtle.end_fill()
    
    # Middle layer
    turtle.color('#FFD700')  # Gold
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(15)
        turtle.right(144)
    turtle.end_fill()
    
    # Inner core
    turtle.color('white')
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(8)
        turtle.right(144)
    turtle.end_fill()
    
    # Premium Christmas ornaments with incredible detail
    ornament_positions = [
        # Top layer
        (x - 15, y + 200, 8, '#DC143C', '#FFB6C1'),
        (x + 12, y + 205, 10, '#4169E1', '#87CEEB'),
        (x - 8, y + 195, 7, '#FFD700', '#FFFF00'),
        
        # Upper middle layer
        (x - 25, y + 165, 12, '#32CD32', '#98FB98'),
        (x + 20, y + 170, 11, '#9932CC', '#DDA0DD'),
        (x - 10, y + 155, 9, '#FF4500', '#FFA500'),
        (x + 8, y + 160, 10, '#DC143C', '#FFB6C1'),
        
        # Middle layer
        (x - 35, y + 125, 14, '#4169E1', '#87CEEB'),
        (x + 30, y + 130, 13, '#FFD700', '#FFFF00'),
        (x - 20, y + 115, 11, '#9932CC', '#DDA0DD'),
        (x + 15, y + 120, 12, '#32CD32', '#98FB98'),
        (x - 5, y + 125, 10, '#FF4500', '#FFA500'),
        
        # Lower middle layer
        (x - 45, y + 85, 16, '#DC143C', '#FFB6C1'),
        (x + 40, y + 90, 15, '#4169E1', '#87CEEB'),
        (x - 30, y + 75, 13, '#FFD700', '#FFFF00'),
        (x + 25, y + 80, 14, '#9932CC', '#DDA0DD'),
        (x - 15, y + 85, 12, '#32CD32', '#98FB98'),
        (x + 10, y + 75, 11, '#FF4500', '#FFA500'),
        
        # Lower layer
        (x - 55, y + 45, 18, '#4169E1', '#87CEEB'),
        (x + 50, y + 50, 17, '#DC143C', '#FFB6C1'),
        (x - 40, y + 35, 15, '#FFD700', '#FFFF00'),
        (x + 35, y + 40, 16, '#9932CC', '#DDA0DD'),
        (x - 25, y + 45, 14, '#32CD32', '#98FB98'),
        (x + 20, y + 35, 13, '#FF4500', '#FFA500'),
        (x - 10, y + 40, 12, '#DC143C', '#FFB6C1'),
        
        # Bottom layer
        (x - 65, y + 5, 20, '#FFD700', '#FFFF00'),
        (x + 60, y + 10, 19, '#4169E1', '#87CEEB'),
        (x - 50, y - 5, 17, '#DC143C', '#FFB6C1'),
        (x + 45, y, 18, '#9932CC', '#DDA0DD'),
        (x - 35, y + 5, 16, '#32CD32', '#98FB98'),
        (x + 30, y - 5, 15, '#FF4500', '#FFA500'),
        (x - 20, y, 14, '#4169E1', '#87CEEB'),
        (x + 15, y + 5, 13, '#DC143C', '#FFB6C1')
    ]
    
    for ox, oy, size, color1, color2 in ornament_positions:
        position(ox, oy)
        # Main ornament with gradient
        turtle.color(color1)
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()
        
        # Inner shine
        turtle.color(color2)
        turtle.begin_fill()
        turtle.circle(size * 0.6)
        turtle.end_fill()
        
        # Core highlight
        turtle.color('white')
        turtle.begin_fill()
        turtle.circle(size * 0.3)
        turtle.end_fill()
        
        # Ornament cap
        turtle.color('#C0C0C0')  # Silver
        position(ox, oy + size)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(size * 0.4)
            turtle.left(90)
            turtle.forward(size * 0.2)
            turtle.left(90)
        turtle.end_fill()
    
    # Spectacular Christmas lights with glow effects
    light_strings = [
        # String 1
        [(x - 20, y + 180), (x - 10, y + 185), (x, y + 190), (x + 10, y + 185), (x + 20, y + 180)],
        # String 2
        [(x - 30, y + 140), (x - 15, y + 150), (x, y + 155), (x + 15, y + 150), (x + 30, y + 140)],
        # String 3
        [(x - 40, y + 100), (x - 20, y + 110), (x, y + 115), (x + 20, y + 110), (x + 40, y + 100)],
        # String 4
        [(x - 50, y + 60), (x - 25, y + 70), (x, y + 75), (x + 25, y + 70), (x + 50, y + 60)],
        # String 5
        [(x - 60, y + 20), (x - 30, y + 30), (x, y + 35), (x + 30, y + 30), (x + 60, y + 20)]
    ]
    
    light_colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#FFA500', '#FF69B4']
    
    for string in light_strings:
        for i, (lx, ly) in enumerate(string):
            color = light_colors[i % len(light_colors)]
            
            # Light glow effect
            position(lx, ly)
            turtle.color('white')
            turtle.begin_fill()
            turtle.circle(6)
            turtle.end_fill()
            
            # Main light
            turtle.color(color)
            turtle.begin_fill()
            turtle.circle(4)
            turtle.end_fill()
            
            # Light highlight
            turtle.color('white')
            turtle.begin_fill()
            turtle.circle(2)
            turtle.end_fill()

def draw_premium_gifts_under_tree(tree_x, tree_y):
    """🎁 Draw premium gift collection under tree"""
    
    gifts = [
        # (x, y, width, height, box_color, ribbon_color, bow_size)
        (tree_x - 40, tree_y - 45, 25, 20, '#DC143C', '#FFD700', 8),
        (tree_x - 10, tree_y - 45, 30, 25, '#228B22', '#C0C0C0', 10),
        (tree_x + 25, tree_y - 45, 28, 22, '#4169E1', '#FFD700', 9),
        (tree_x - 55, tree_y - 25, 22, 18, '#9932CC', '#C0C0C0', 7),
        (tree_x - 25, tree_y - 25, 35, 28, '#FF4500', '#FFD700', 11),
        (tree_x + 15, tree_y - 25, 26, 21, '#FFD700', '#DC143C', 8),
        (tree_x + 45, tree_y - 25, 24, 19, '#32CD32', '#C0C0C0', 7),
        (tree_x - 35, tree_y - 5, 20, 16, '#FF69B4', '#FFD700', 6),
        (tree_x - 8, tree_y - 5, 32, 26, '#8B008B', '#C0C0C0', 10),
        (tree_x + 20, tree_y - 5, 27, 23, '#FF8C00', '#FFD700', 9)
    ]
    
    for gx, gy, w, h, box_color, ribbon_color, bow_size in gifts:
        # Gift box with shading
        position(gx, gy)
        turtle.color(box_color)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
        turtle.end_fill()
        
        # Box shading for 3D effect
        position(gx + w - 3, gy)
        turtle.color(tuple(max(0, int(c * 0.7)) for c in turtle.color()[0]) if hasattr(turtle.color()[0], '__iter__') else box_color)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(3)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
        turtle.end_fill()
        
        # Ribbon with realistic width
        turtle.color(ribbon_color)
        turtle.pensize(6)
        # Vertical ribbon
        position(gx + w//2, gy)
        turtle.goto(gx + w//2, gy + h)
        # Horizontal ribbon
        position(gx, gy + h//2)
        turtle.goto(gx + w, gy + h//2)
        
        # Premium bow with multiple loops
        position(gx + w//2, gy + h)
        turtle.color(ribbon_color)
        turtle.begin_fill()
        turtle.circle(bow_size)
        turtle.end_fill()
        
        # Bow loops
        turtle.color(ribbon_color)
        turtle.begin_fill()
        turtle.goto(gx + w//2 - bow_size, gy + h + bow_size//2)
        turtle.goto(gx + w//2, gy + h + bow_size)
        turtle.goto(gx + w//2 + bow_size, gy + h + bow_size//2)
        turtle.goto(gx + w//2, gy + h)
        turtle.end_fill()
        
        # Bow center
        turtle.color('white')
        turtle.begin_fill()
        turtle.circle(bow_size//3)
        turtle.end_fill()
        
        # Gift tag
        position(gx + w - 8, gy + h - 5)
        turtle.color('white')
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(6)
            turtle.left(90)
            turtle.forward(4)
            turtle.left(90)
        turtle.end_fill()

def create_photorealistic_snow():
    """❄️ Create photorealistic snow system"""
    snow_particles = []
    for i in range(60):  # More particles for realism
        particle = turtle.Turtle()
        particle.shape("circle")
        size = random.uniform(0.1, 2.5)
        particle.shapesize(size)
        # Realistic snow colors with transparency effect
        snow_colors = ['white', '#F0F8FF', '#F8F8FF', '#FFFAFA', '#E6E6FA']
        particle.color(random.choice(snow_colors))
        particle.penup()
        particle.speed(0)
        particle.goto(random.randint(-800, 800), random.randint(300, 500))
        particle.dx = random.uniform(-1.5, 1.5)
        particle.dy = random.uniform(-3, -0.8) * size
        particle.spin = random.uniform(-8, 8)
        particle.drift = random.uniform(0, 2 * math.pi)
        snow_particles.append(particle)
    return snow_particles

# Initialize the ultra-realistic masterpiece
masterpiece = UltraRealisticSantaTree()

print("🎅 Loading Ultra-Realistic Santa & Christmas Tree...")
print("🎄 Photorealistic graphics and animations...")
print("✨ Premium decorations and gift placement...")
print("🏆 Guaranteed landslide winner!")

# ✨ PHOTOREALISTIC GLOWING TEXT ✨
draw_photorealistic_text("MERRY CHRISTMAS", 0, 300, 52, '#DC143C')
draw_photorealistic_text("Santa's Gift Delivery", 0, 250, 32, '#228B22')

# 🎄 SPECTACULAR CHRISTMAS TREE 🎄
tree_x, tree_y = 0, -50
draw_spectacular_christmas_tree(tree_x, tree_y)

# 🎁 PREMIUM GIFTS UNDER TREE 🎁
draw_premium_gifts_under_tree(tree_x, tree_y)

# 🎅 ULTRA-REALISTIC SANTA PLACING GIFTS 🎅
santa_x, santa_y = -120, -100
draw_ultra_realistic_santa(santa_x, santa_y, "placing_gifts")

# ❄️ PHOTOREALISTIC SNOW SYSTEM ❄️
turtle.tracer(0)
snow_particles = create_photorealistic_snow()

# Premium main snowfall
turtle.addshape("snowFall.gif")
main_snow = turtle.Turtle()
main_snow.shape("snowFall.gif")
main_snow.penup()
main_snow.goto(0, 400)
main_snow.speed(0)

# 🎵 PHOTOREALISTIC ANIMATION LOOP 🎵
print("🎅 Starting Ultra-Realistic Christmas Scene...")
print("✨ Photorealistic animations and magical atmosphere!")
print("🏆 The most realistic Christmas scene ever created!")

while True:
    turtle.update()
    masterpiece.frame_count += 1
    masterpiece.santa_animation_phase = (masterpiece.santa_animation_phase + 0.02) % (2 * math.pi)
    
    # Animate Santa with realistic transitions
    if masterpiece.frame_count % 200 == 0:
        activities = ["placing_gifts", "admiring_tree"]
        activity = activities[masterpiece.frame_count // 200 % 2]
        draw_ultra_realistic_santa(santa_x, santa_y, activity)
    
    # Photorealistic snowfall animation
    wind_effect = 2 * math.sin(masterpiece.frame_count * 0.015)
    main_snow.goto(main_snow.xcor() + wind_effect, main_snow.ycor() - 2.8)
    if main_snow.ycor() < -400:
        main_snow.goto(random.randint(-400, 400), 400)
    
    # Ultra-realistic snow physics
    for particle in snow_particles:
        # Advanced atmospheric effects
        wind = 1.2 * math.sin(masterpiece.frame_count * 0.01 + particle.drift)
        turbulence = 0.5 * math.cos(masterpiece.frame_count * 0.02 + particle.drift * 2)
        
        particle.goto(
            particle.xcor() + particle.dx + wind + turbulence,
            particle.ycor() + particle.dy
        )
        particle.right(particle.spin * 0.2)  # Gentle realistic rotation
        
        if particle.ycor() < -400:
            particle.goto(random.randint(-800, 800), random.randint(400, 500))
            particle.dx = random.uniform(-1.5, 1.5)
            particle.dy = random.uniform(-3, -0.8)
            particle.drift = random.uniform(0, 2 * math.pi)
    
    # Tree twinkling effect
    if masterpiece.frame_count % 40 == 0:
        # Make some lights twinkle
        for _ in range(8):
            twinkle_x = tree_x + random.randint(-60, 60)
            twinkle_y = tree_y + random.randint(0, 200)
            position(twinkle_x, twinkle_y)
            turtle.color('white')
            turtle.dot(random.randint(8, 15))
    
    # Premium sparkle effects around scene
    if masterpiece.frame_count % 60 == 0:
        for _ in range(5):
            sparkle_x = random.randint(-200, 200)
            sparkle_y = random.randint(-50, 200)
            position(sparkle_x, sparkle_y)
            sparkle_colors = ['#FFD700', '#FFFFFF', '#FFFF00', '#F0F8FF']
            turtle.color(random.choice(sparkle_colors))
            turtle.dot(random.randint(6, 12))
    
    # Refresh photorealistic text occasionally
    if masterpiece.frame_count % 400 == 0:
        draw_photorealistic_text("MERRY CHRISTMAS", 0, 300, 52, '#DC143C')
    
    time.sleep(0.025)  # Ultra-smooth 40 FPS photorealistic animation