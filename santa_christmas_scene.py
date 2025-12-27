import turtle
import random
import math

class ChristmasScene:
    """🎄 Magical Christmas Scene with Santa 🎅"""
    
    def __init__(self):
        self.setup_screen()
        self.lights_phase = 0
        
    def setup_screen(self):
        """Setup the graphics window"""
        self.screen = turtle.Screen()
        self.screen.setup(1200, 900)
        self.screen.bgcolor('#1a2847')  # Deep blue night sky
        self.screen.title("🎄 Merry Christmas 🎅")
        self.screen.colormode(255)
        self.screen.tracer(0)
        
    def draw_star_shape(self, x, y, size, color='yellow', glow=True):
        """Draw a 5-pointed star"""
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(90)
        turtle.color(color)
        turtle.begin_fill()
        
        for _ in range(5):
            turtle.forward(size)
            turtle.right(144)
        
        turtle.end_fill()
        
        # Add glow effect
        if glow:
            turtle.pensize(2)
            turtle.color(255, 255, 200)
            for i in range(3):
                turtle.penup()
                turtle.goto(x, y)
                turtle.setheading(90)
                turtle.pendown()
                for _ in range(5):
                    turtle.forward(size + i*2)
                    turtle.right(144)
    
    def draw_sparkle(self, x, y, size=10):
        """Draw a sparkle/twinkle effect"""
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.pensize(2)
        turtle.color(255, 255, 200)
        
        # Horizontal line
        turtle.goto(x - size, y)
        turtle.goto(x + size, y)
        
        # Vertical line
        turtle.penup()
        turtle.goto(x, y - size)
        turtle.pendown()
        turtle.goto(x, y + size)
        
    def draw_moon(self, x, y, radius=50):
        """Draw a glowing moon"""
        # Outer glow
        for i in range(3):
            turtle.penup()
            turtle.goto(x, y - radius - i*5)
            turtle.pendown()
            brightness = 200 + i*15
            turtle.color(brightness, brightness, 180)
            turtle.pensize(1)
            turtle.begin_fill()
            turtle.circle(radius + i*5)
            turtle.end_fill()
        
        # Main moon
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.pendown()
        turtle.color(255, 252, 230)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        
    def draw_snow_particles(self):
        """Draw falling snow"""
        turtle.pensize(1)
        for _ in range(100):
            x = random.randint(-600, 600)
            y = random.randint(-200, 400)
            size = random.randint(2, 6)
            
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.color('white')
            turtle.dot(size)
    
    def draw_ground(self):
        """Draw snowy ground"""
        turtle.penup()
        turtle.goto(-600, -250)
        turtle.pendown()
        turtle.color('white')
        turtle.begin_fill()
        
        # Create wavy snow surface
        for x in range(-600, 601, 20):
            y = -250 + math.sin(x * 0.05) * 10
            turtle.goto(x, y)
        
        turtle.goto(600, -450)
        turtle.goto(-600, -450)
        turtle.goto(-600, -250)
        turtle.end_fill()
        
    def draw_christmas_tree(self, x, y, height=200):
        """Draw a decorated Christmas tree"""
        # Tree trunk
        turtle.penup()
        turtle.goto(x - 15, y - height * 0.2)
        turtle.pendown()
        turtle.color(101, 67, 33)
        turtle.begin_fill()
        turtle.goto(x + 15, y - height * 0.2)
        turtle.goto(x + 15, y)
        turtle.goto(x - 15, y)
        turtle.goto(x - 15, y - height * 0.2)
        turtle.end_fill()
        
        # Tree layers (triangles)
        layers = 3
        layer_colors = [(34, 139, 34), (0, 128, 0), (50, 205, 50)]
        
        for i in range(layers):
            layer_y = y + i * height / 4
            layer_width = (height - i * 40) * 0.8
            
            turtle.penup()
            turtle.goto(x - layer_width / 2, layer_y)
            turtle.pendown()
            turtle.color(layer_colors[i % 3])
            turtle.pensize(3)
            turtle.color(0, 100, 0)
            
            # Draw zigzag edge for texture
            turtle.begin_fill()
            
            # Left zigzag edge
            steps = 8
            for j in range(steps):
                dx = layer_width / 2 / steps
                dy = height / 4 / steps
                turtle.goto(x - layer_width / 2 + j * dx + random.randint(-5, 5), 
                           layer_y + j * dy + random.randint(-3, 3))
            
            # Top point
            turtle.goto(x, layer_y + height / 4)
            
            # Right zigzag edge
            for j in range(steps):
                dx = layer_width / 2 / steps
                dy = height / 4 / steps
                turtle.goto(x + layer_width / 2 - (steps - j) * dx + random.randint(-5, 5),
                           layer_y + (steps - j) * dy + random.randint(-3, 3))
            
            turtle.goto(x - layer_width / 2, layer_y)
            turtle.end_fill()
        
        # Add star on top
        star_y = y + height * 0.75
        self.draw_star_shape(x, star_y, 25, 'gold', True)
        
        # Add ornaments
        ornament_colors = ['red', 'blue', 'yellow', 'orange', 'cyan']
        for i in range(8):
            ox = x + random.randint(-int(height * 0.3), int(height * 0.3))
            oy = y + random.randint(int(height * 0.1), int(height * 0.6))
            color = random.choice(ornament_colors)
            
            # Ornament ball
            turtle.penup()
            turtle.goto(ox, oy)
            turtle.pendown()
            turtle.color(color)
            turtle.begin_fill()
            turtle.circle(8)
            turtle.end_fill()
            
            # Ornament hook
            turtle.penup()
            turtle.goto(ox, oy + 8)
            turtle.pendown()
            turtle.color('black')
            turtle.pensize(2)
            turtle.goto(ox, oy + 12)
        
        # Add lights (string lights)
        self.draw_tree_lights(x, y, height)
        
    def draw_tree_lights(self, x, y, height):
        """Draw string lights on tree"""
        light_colors = [(255, 255, 100), (100, 200, 255), (255, 200, 100)]
        
        # Draw wavy light strings
        for layer in range(3):
            layer_y = y + layer * height / 4 + 20
            layer_width = (height - layer * 40) * 0.6
            
            points = []
            for i in range(8):
                lx = x - layer_width / 2 + i * layer_width / 8
                ly = layer_y + math.sin(i * 0.8) * 15
                points.append((lx, ly))
            
            # Draw the wire
            turtle.penup()
            turtle.goto(points[0][0], points[0][1])
            turtle.pendown()
            turtle.color(100, 100, 100)
            turtle.pensize(1)
            for px, py in points[1:]:
                turtle.goto(px, py)
            
            # Draw light bulbs
            for i, (px, py) in enumerate(points):
                turtle.penup()
                turtle.goto(px, py - 5)
                turtle.pendown()
                color = light_colors[i % len(light_colors)]
                turtle.color(color)
                turtle.begin_fill()
                turtle.circle(5)
                turtle.end_fill()
                
                # Glow effect
                turtle.pensize(1)
                light_glow = (min(255, color[0] + 50), min(255, color[1] + 50), min(255, color[2] + 50))
                turtle.color(light_glow)
                turtle.circle(7, steps=6)
    
    def draw_santa(self, x, y, scale=1.0):
        """Draw Santa Claus"""
        s = scale
        
        # Santa's body (red suit)
        turtle.penup()
        turtle.goto(x - 30*s, y)
        turtle.pendown()
        turtle.color(220, 20, 60)
        turtle.begin_fill()
        turtle.goto(x + 30*s, y)
        turtle.goto(x + 30*s, y + 60*s)
        turtle.goto(x - 30*s, y + 60*s)
        turtle.goto(x - 30*s, y)
        turtle.end_fill()
        
        # Belt
        turtle.penup()
        turtle.goto(x - 30*s, y + 20*s)
        turtle.pendown()
        turtle.color('black')
        turtle.begin_fill()
        turtle.goto(x + 30*s, y + 20*s)
        turtle.goto(x + 30*s, y + 30*s)
        turtle.goto(x - 30*s, y + 30*s)
        turtle.goto(x - 30*s, y + 20*s)
        turtle.end_fill()
        
        # Belt buckle
        turtle.penup()
        turtle.goto(x - 10*s, y + 22*s)
        turtle.pendown()
        turtle.color('gold')
        turtle.begin_fill()
        turtle.goto(x + 10*s, y + 22*s)
        turtle.goto(x + 10*s, y + 28*s)
        turtle.goto(x - 10*s, y + 28*s)
        turtle.goto(x - 10*s, y + 22*s)
        turtle.end_fill()
        
        # Arms
        turtle.color(220, 20, 60)
        
        # Left arm
        turtle.penup()
        turtle.goto(x - 30*s, y + 50*s)
        turtle.pendown()
        turtle.pensize(int(15*s))
        turtle.goto(x - 50*s, y + 40*s)
        
        # Right arm
        turtle.penup()
        turtle.goto(x + 30*s, y + 50*s)
        turtle.pendown()
        turtle.goto(x + 50*s, y + 40*s)
        
        # Hands (black gloves)
        turtle.color('black')
        turtle.penup()
        turtle.goto(x - 50*s, y + 40*s)
        turtle.pendown()
        turtle.dot(int(15*s))
        
        turtle.penup()
        turtle.goto(x + 50*s, y + 40*s)
        turtle.pendown()
        turtle.dot(int(15*s))
        
        # Head (face)
        turtle.penup()
        turtle.goto(x, y + 60*s)
        turtle.pendown()
        turtle.color(255, 218, 185)
        turtle.begin_fill()
        turtle.circle(35*s)
        turtle.end_fill()
        
        # Santa hat
        turtle.penup()
        turtle.goto(x - 35*s, y + 95*s)
        turtle.pendown()
        turtle.color(220, 20, 60)
        turtle.begin_fill()
        turtle.goto(x + 35*s, y + 95*s)
        turtle.goto(x, y + 130*s)
        turtle.goto(x - 35*s, y + 95*s)
        turtle.end_fill()
        
        # Hat brim
        turtle.penup()
        turtle.goto(x - 38*s, y + 93*s)
        turtle.pendown()
        turtle.color('white')
        turtle.pensize(int(8*s))
        turtle.goto(x + 38*s, y + 93*s)
        
        # Hat pom-pom
        turtle.penup()
        turtle.goto(x, y + 130*s)
        turtle.pendown()
        turtle.color('white')
        turtle.dot(int(15*s))
        
        # Beard
        turtle.penup()
        turtle.goto(x, y + 60*s)
        turtle.pendown()
        turtle.color('white')
        turtle.begin_fill()
        turtle.circle(25*s, 180)
        turtle.goto(x - 25*s, y + 60*s)
        turtle.end_fill()
        
        # Mustache
        turtle.penup()
        turtle.goto(x - 15*s, y + 85*s)
        turtle.pendown()
        turtle.color('white')
        turtle.begin_fill()
        turtle.circle(10*s, 180)
        turtle.end_fill()
        
        turtle.penup()
        turtle.goto(x + 15*s, y + 85*s)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(-10*s, 180)
        turtle.end_fill()
        
        # Eyes
        turtle.penup()
        turtle.goto(x - 12*s, y + 88*s)
        turtle.pendown()
        turtle.color('black')
        turtle.dot(int(5*s))
        
        turtle.penup()
        turtle.goto(x + 12*s, y + 88*s)
        turtle.pendown()
        turtle.dot(int(5*s))
        
        # Nose
        turtle.penup()
        turtle.goto(x, y + 80*s)
        turtle.pendown()
        turtle.color(220, 20, 60)
        turtle.dot(int(8*s))
        
        # Legs (black pants)
        turtle.penup()
        turtle.goto(x - 20*s, y)
        turtle.pendown()
        turtle.color('black')
        turtle.pensize(int(18*s))
        turtle.goto(x - 20*s, y - 35*s)
        
        turtle.penup()
        turtle.goto(x + 20*s, y)
        turtle.pendown()
        turtle.goto(x + 20*s, y - 35*s)
        
        # Boots
        turtle.penup()
        turtle.goto(x - 20*s, y - 35*s)
        turtle.pendown()
        turtle.color('black')
        turtle.dot(int(20*s))
        
        turtle.penup()
        turtle.goto(x + 20*s, y - 35*s)
        turtle.pendown()
        turtle.dot(int(20*s))
        
        # Gift sack
        turtle.penup()
        turtle.goto(x - 55*s, y + 30*s)
        turtle.pendown()
        turtle.color(139, 69, 19)
        turtle.begin_fill()
        turtle.goto(x - 80*s, y)
        turtle.goto(x - 80*s, y + 40*s)
        turtle.goto(x - 55*s, y + 50*s)
        turtle.goto(x - 55*s, y + 30*s)
        turtle.end_fill()
        
        # Sack tie
        turtle.penup()
        turtle.goto(x - 65*s, y + 48*s)
        turtle.pendown()
        turtle.color('red')
        turtle.pensize(int(4*s))
        turtle.goto(x - 70*s, y + 52*s)
        turtle.goto(x - 60*s, y + 52*s)
    
    def draw_present(self, x, y, width, height, color1, color2):
        """Draw a gift box"""
        # Box
        turtle.penup()
        turtle.goto(x - width/2, y)
        turtle.pendown()
        turtle.color(color1)
        turtle.begin_fill()
        turtle.goto(x + width/2, y)
        turtle.goto(x + width/2, y + height)
        turtle.goto(x - width/2, y + height)
        turtle.goto(x - width/2, y)
        turtle.end_fill()
        
        # Ribbon horizontal
        turtle.penup()
        turtle.goto(x - width/2, y + height/2)
        turtle.pendown()
        turtle.color(color2)
        turtle.pensize(8)
        turtle.goto(x + width/2, y + height/2)
        
        # Ribbon vertical
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x, y + height)
        
        # Bow
        turtle.penup()
        turtle.goto(x, y + height)
        turtle.pendown()
        turtle.color(color2)
        turtle.begin_fill()
        turtle.circle(8)
        turtle.end_fill()
        
        turtle.penup()
        turtle.goto(x - 10, y + height + 5)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(6)
        turtle.end_fill()
        
        turtle.penup()
        turtle.goto(x + 10, y + height + 5)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(6)
        turtle.end_fill()
    
    def draw_banner(self, x, y, text="Merry Christmas"):
        """Draw decorative banner with text"""
        # Banner ribbon
        turtle.penup()
        turtle.goto(x - 250, y)
        turtle.pendown()
        turtle.color(218, 165, 32)  # Gold
        turtle.pensize(3)
        
        # Left ribbon end
        turtle.begin_fill()
        turtle.goto(x - 220, y + 15)
        turtle.goto(x - 200, y)
        turtle.goto(x - 220, y - 15)
        turtle.goto(x - 250, y)
        turtle.end_fill()
        
        # Main banner
        turtle.penup()
        turtle.goto(x - 200, y - 20)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(x + 200, y - 20)
        turtle.goto(x + 200, y + 20)
        turtle.goto(x - 200, y + 20)
        turtle.goto(x - 200, y - 20)
        turtle.end_fill()
        
        # Right ribbon end
        turtle.penup()
        turtle.goto(x + 200, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(x + 220, y + 15)
        turtle.goto(x + 250, y)
        turtle.goto(x + 220, y - 15)
        turtle.goto(x + 200, y)
        turtle.end_fill()
        
        # Text
        turtle.penup()
        turtle.goto(x, y - 10)
        turtle.pendown()
        turtle.color('red')
        turtle.write(text, align="center", font=("Arial", 36, "bold"))
    
    def draw_scene(self):
        """Draw the complete Christmas scene"""
        turtle.hideturtle()
        turtle.speed(0)
        
        # Sky and stars
        self.draw_snow_particles()
        
        # Add sparkles
        sparkle_positions = [
            (-450, 350), (450, 380), (-300, 320), (200, 360),
            (-150, 300), (350, 340), (-500, 280), (480, 300)
        ]
        for sx, sy in sparkle_positions:
            self.draw_sparkle(sx, sy, random.randint(8, 15))
        
        # Moon
        self.draw_moon(-350, 300, 45)
        
        # Ground
        self.draw_ground()
        
        # Christmas trees
        self.draw_christmas_tree(-250, -50, 220)
        self.draw_christmas_tree(250, -50, 250)
        
        # Santa in the middle
        self.draw_santa(0, -100, 1.2)
        
        # Presents
        presents_data = [
            (120, -220, 40, 35, 'red', 'green'),
            (80, -220, 35, 30, 'green', 'red'),
            (180, -220, 30, 40, 'blue', 'gold'),
            (160, -220, 38, 28, 'yellow', 'red'),
            (200, -215, 25, 25, 'orange', 'white')
        ]
        
        for px, py, pw, ph, c1, c2 in presents_data:
            self.draw_present(px, py, pw, ph, c1, c2)
        
        # Merry Christmas banner
        self.draw_banner(0, -320, "Merry Christmas")
        
        self.screen.update()

def main():
    """Main function to run the Christmas scene"""
    scene = ChristmasScene()
    scene.draw_scene()
    
    print("🎄 Merry Christmas! 🎅")
    print("Click on the window to close...")
    
    scene.screen.exitonclick()

if __name__ == "__main__":
    main()
