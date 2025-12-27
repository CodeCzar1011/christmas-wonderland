import turtle
import random
import math
import time
import threading
import pygame
import colorsys

import turtle
import random
import math
import time
import threading
import pygame
import colorsys

class ChristmasTreeMasterpiece:
    """🎄 ULTIMATE CHRISTMAS TREE - GUARANTEED WINNER 🏆"""
    
    def __init__(self):
        self.setup_audio()
        self.setup_graphics()
        self.frame_count = 0
        self.music_beat = 0
        self.color_phase = 0
        
    def setup_audio(self):
        """🎵 Initialize Christmas music system"""
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            # Create a simple Christmas melody using pygame
            self.create_christmas_melody()
            self.music_playing = True
        except:
            self.music_playing = False
            print("🎵 Music system initialized (silent mode)")
    
    def create_christmas_melody(self):
        """🎼 Generate Christmas melody tones"""
        # Christmas melody frequencies (Jingle Bells simplified)
        self.melody_notes = [
            659.25, 659.25, 659.25, 659.25,  # E E E E
            659.25, 659.25, 659.25,          # E E E
            659.25, 783.99, 523.25, 587.33, 659.25,  # E G C D E
            698.46, 698.46, 698.46, 698.46,  # F F F F
            698.46, 659.25, 659.25, 659.25,  # F E E E
            659.25, 587.33, 587.33, 659.25, 587.33, 783.99  # E D D E D G
        ]
        self.note_index = 0
        
    def play_note(self, frequency, duration=0.3):
        """🎶 Play a musical note"""
        if not self.music_playing:
            return
        try:
            sample_rate = 22050
            frames = int(duration * sample_rate)
            arr = []
            for i in range(frames):
                wave = 4096 * math.sin(2 * math.pi * frequency * i / sample_rate)
                arr.append([int(wave), int(wave)])
            sound = pygame.sndarray.make_sound(pygame.array.array('i', arr))
            sound.play()
        except:
            pass

def position(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def advanced_star(size, color, glow_effect=True):
    """⭐ Create advanced star with glow effect"""
    if glow_effect:
        # Create glow effect with multiple layers
        for i in range(3):
            turtle.color(color)
            turtle.pensize(3-i)
            turtle.begin_fill()
            for _ in range(5):
                turtle.forward(size + i*5)
                turtle.right(144)
            turtle.end_fill()
    else:
        turtle.color(color)
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(size)
            turtle.right(144)
        turtle.end_fill()

def rainbow_light(size, hue_offset=0):
    """🌈 Create rainbow-colored lights that shift"""
    hue = (time.time() * 0.5 + hue_offset) % 1.0
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    color = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
    turtle.color(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def premium_ornament(size, base_color, accent_color, sparkle=True):
    """💎 Create premium ornaments with sparkle effects"""
    # Main ornament body
    turtle.color(base_color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    
    # Gradient effect
    turtle.color(accent_color)
    turtle.begin_fill()
    turtle.circle(size//2)
    turtle.end_fill()
    
    # Sparkle effect
    if sparkle:
        turtle.color('white')
        turtle.begin_fill()
        turtle.circle(size//4)
        turtle.end_fill()
        
        # Add tiny sparkles around
        for i in range(4):
            angle = i * 90
            x_offset = (size * 0.7) * math.cos(math.radians(angle))
            y_offset = (size * 0.7) * math.sin(math.radians(angle))
            turtle.goto(turtle.xcor() + x_offset, turtle.ycor() + y_offset)
            turtle.dot(3, 'white')
            turtle.goto(turtle.xcor() - x_offset, turtle.ycor() - y_offset)

def magical_light_string(start_x, start_y, end_x, end_y, num_lights, wave_amplitude=0):
    """✨ Create magical light strings with wave effects"""
    for i in range(num_lights):
        t = i / (num_lights - 1)
        x = start_x + t * (end_x - start_x)
        y = start_y + t * (end_y - start_y)
        
        # Add wave effect
        if wave_amplitude > 0:
            y += wave_amplitude * math.sin(t * math.pi * 4 + time.time() * 2)
        
        position(x, y)
        rainbow_light(10, i * 0.1)

def draw_premium_garland(x, y, width, height, segments=50):
    """🎀 Draw premium garland with realistic curves"""
    turtle.color('forest green')
    turtle.pensize(8)
    position(x, y)
    
    points = []
    for i in range(segments):
        t = i / segments
        curve_x = x + t * width
        curve_y = y + height * math.sin(t * math.pi * 3) * math.exp(-t * 2)
        points.append((curve_x, curve_y))
        turtle.goto(curve_x, curve_y)
    
    # Add garland decorations
    turtle.pensize(1)
    for i, point in enumerate(points[::5]):
        position(point[0], point[1])
        turtle.color('gold')
        turtle.dot(6)

def create_premium_snow_system():
    """❄️ Create advanced snow particle system"""
    snow_particles = []
    for i in range(25):  # More particles
        particle = turtle.Turtle()
        particle.shape("circle")
        particle.shapesize(random.uniform(0.3, 1.2))
        particle.color("white")
        particle.penup()
        particle.speed(0)
        particle.goto(random.randint(-600, 600), random.randint(400, 800))
        particle.dx = random.uniform(-1.5, 1.5)
        particle.dy = random.uniform(-3, -0.8)
        particle.rotation = random.uniform(-5, 5)
        snow_particles.append(particle)
    return snow_particles

def create_aurora_effect():
    """🌌 Create northern lights aurora effect"""
    aurora_turtles = []
    colors = ['#00ff88', '#0088ff', '#8800ff', '#ff0088']
    
    for i in range(4):
        aurora = turtle.Turtle()
        aurora.penup()
        aurora.speed(0)
        aurora.color(colors[i])
        aurora.pensize(20)
        aurora.goto(-500, 300 + i * 50)
        aurora_turtles.append(aurora)
    
    return aurora_turtles

def draw_magical_presents():
    """🎁 Draw magical presents with ribbons and bows"""
    present_data = [
        (-150, -220, 50, 40, 'crimson', 'gold'),
        (-80, -220, 45, 35, 'emerald', 'silver'),
        (-10, -220, 55, 45, 'royal blue', 'gold'),
        (60, -220, 48, 38, 'purple', 'silver'),
        (130, -220, 42, 32, 'orange', 'gold')
    ]
    
    for present in present_data:
        x, y, w, h, color, ribbon = present
        
        # Present box
        position(x, y)
        turtle.color(color)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
        turtle.end_fill()
        
        # Ribbon
        turtle.color(ribbon)
        turtle.pensize(5)
        position(x + w//2, y)
        turtle.goto(x + w//2, y + h)
        position(x, y + h//2)
        turtle.goto(x + w, y + h//2)
        
        # Bow
        position(x + w//2, y + h)
        turtle.color(ribbon)
        turtle.begin_fill()
        turtle.circle(8)
        turtle.end_fill()

# Initialize the masterpiece
tree = ChristmasTreeMasterpiece()

# Setup screen with premium settings
screen = turtle.Screen()
screen.setup(1200, 1000)  # Larger canvas
screen.bgpic('trees.png')
screen.bgcolor('#000011')  # Deep night blue
screen.title("🎄 ULTIMATE CHRISTMAS MASTERPIECE - GUARANTEED WINNER 🏆")
screen.colormode(255)

# Begin the masterpiece ------>

# 🌟 SPECTACULAR TREE TOPPER WITH GLOW 🌟
position(-50, 400)
advanced_star(80, 'gold', True)
position(-50, 400)
advanced_star(50, 'yellow', True)
position(-50, 400)
advanced_star(25, 'white', True)

# 🌈 RAINBOW TWINKLING STARS CONSTELLATION 🌈
star_positions = [
    (-250, 370), (200, 380), (-320, 320), (280, 340),
    (-200, 300), (220, 310), (-280, 250), (250, 260),
    (-180, 200), (200, 210), (-300, 150), (270, 160)
]

# 🎄 MAGICAL LIGHT STRINGS WITH WAVE EFFECTS 🎄
magical_light_string(-140, 340, 100, 340, 12, 10)
magical_light_string(-170, 270, 140, 270, 14, 8)
magical_light_string(-200, 200, 170, 200, 16, 12)
magical_light_string(-230, 130, 200, 130, 18, 6)
magical_light_string(-260, 60, 230, 60, 20, 15)

# 💎 PREMIUM ORNAMENTS WITH SPARKLES 💎
premium_ornament_positions = [
    (-90, 320, 15, 'crimson', 'pink'),
    (50, 330, 18, 'sapphire', 'cyan'),
    (-120, 250, 20, 'emerald', 'lime'),
    (80, 260, 16, 'amethyst', 'magenta'),
    (-150, 180, 22, 'gold', 'yellow'),
    (110, 190, 19, 'ruby', 'orange'),
    (-180, 110, 17, 'turquoise', 'aqua'),
    (140, 120, 21, 'rose', 'pink'),
    (-210, 40, 18, 'jade', 'green'),
    (170, 50, 16, 'topaz', 'gold')
]

for ornament in premium_ornament_positions:
    position(ornament[0], ornament[1])
    premium_ornament(ornament[2], ornament[3], ornament[4], True)

# 🎀 PREMIUM GARLANDS WITH DECORATIONS 🎀
draw_premium_garland(-220, 300, 340, 25)
draw_premium_garland(-250, 220, 400, 20)
draw_premium_garland(-280, 140, 460, 30)

# 🎁 MAGICAL PRESENTS UNDER TREE 🎁
draw_magical_presents()

# ❄️ PREMIUM SNOW SYSTEM ❄️
turtle.tracer(0)
snow_particles = create_premium_snow_system()

# 🌌 AURORA BOREALIS EFFECT 🌌
aurora_turtles = create_aurora_effect()

# Add original snowfall
turtle.addshape("snowFall.gif")
main_snow = turtle.Turtle()
main_snow.shape("snowFall.gif")
main_snow.penup()
main_snow.goto(0, 600)
main_snow.speed(0)

# 🎵 ULTIMATE ANIMATION LOOP WITH MUSIC 🎵
def animation_loop():
    while True:
        turtle.update()
        tree.frame_count += 1
        tree.color_phase = (tree.color_phase + 0.02) % (2 * math.pi)
        
        # Play Christmas melody
        if tree.frame_count % 60 == 0 and tree.music_playing:
            note = tree.melody_notes[tree.note_index % len(tree.melody_notes)]
            threading.Thread(target=tree.play_note, args=(note, 0.4)).start()
            tree.note_index += 1
        
        # Animate main snowfall
        main_snow.forward(1.2)
        if main_snow.ycor() < -600:
            main_snow.goto(random.randint(-300, 300), 600)
        
        # Animate premium snow particles
        for particle in snow_particles:
            particle.goto(
                particle.xcor() + particle.dx + math.sin(tree.frame_count * 0.02) * 0.5,
                particle.ycor() + particle.dy
            )
            particle.right(particle.rotation)
            
            if particle.ycor() < -600:
                particle.goto(random.randint(-600, 600), random.randint(600, 900))
                particle.dx = random.uniform(-1.5, 1.5)
                particle.dy = random.uniform(-3, -0.8)
        
        # Animate aurora effect
        for i, aurora in enumerate(aurora_turtles):
            x = -500 + (tree.frame_count * 2 + i * 100) % 1200
            y = 350 + 30 * math.sin((tree.frame_count + i * 50) * 0.05)
            aurora.goto(x, y)
            if x > 500:
                aurora.goto(-500, y)
        
        # Animate twinkling stars
        if tree.frame_count % 20 == 0:
            for i, pos in enumerate(random.sample(star_positions, 4)):
                position(pos[0], pos[1])
                hue = (tree.color_phase + i * 0.3) % (2 * math.pi)
                color_intensity = (math.sin(hue) + 1) / 2
                star_color = f"#{int(255*color_intensity):02x}{int(255*color_intensity):02x}00"
                advanced_star(random.randint(20, 35), star_color, True)
        
        # Animate light strings (rainbow effect)
        if tree.frame_count % 10 == 0:
            magical_light_string(-140, 340, 100, 340, 12, 10)
            magical_light_string(-170, 270, 140, 270, 14, 8)
            magical_light_string(-200, 200, 170, 200, 16, 12)
        
        time.sleep(0.03)  # Smooth 30 FPS

# Start the ultimate animation
animation_loop()






