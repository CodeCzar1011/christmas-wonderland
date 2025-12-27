import os
import pygame
import math
import random
from pygame import gfxdraw

# Initialize Pygame
pygame.init()

# Screen dimensions - using coordinate system from -500 to 500
WIDTH = 700
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Realistic Christmas Wonderland")

# Coordinate system: -500 to 500 on both axes
def to_screen_x(x):
    """Convert from world coordinates (-500 to 500) to screen coordinates (0 to 800)"""
    return int((x + 500) * (WIDTH / 1000))

def to_screen_y(y):
    """Convert from world coordinates (-500 to 500) to screen coordinates (0 to 800)"""
    return int((500 - y) * (HEIGHT / 1000))  # Invert Y axis

# Colors
NIGHT_SKY_TOP = (15, 20, 45)
NIGHT_SKY_BOTTOM = (35, 50, 85)
TREE_GREEN_DARK = (25, 65, 30)
TREE_GREEN_MID = (40, 100, 45)
TREE_GREEN_LIGHT = (60, 140, 65)
TREE_GREEN_HIGHLIGHT = (90, 180, 95)
TRUNK_BROWN_DARK = (60, 40, 20)
TRUNK_BROWN_LIGHT = (100, 70, 40)
SNOW_WHITE = (255, 255, 255)
SNOW_SHADOW = (200, 220, 240)
SNOW_BLUE = (230, 240, 255)
GOLD = (255, 215, 0)
RED = (220, 20, 20)
GREEN = (0, 150, 0)
MUSIC_FILE = "Carol Of The Bells  Christmas Music  Instrumental Version.mp3"
SLEIGH_RED = (180, 0, 20)
SLEIGH_GOLD = (245, 190, 50)
REINDEER_BROWN = (120, 80, 50)
REINDEER_LIGHT = (180, 130, 90)
LEATHER = (90, 50, 20)

# Animation variables
animation_frame = 0


def start_music():
    """Start background music if the MP3 file is available."""
    music_path = os.path.join(os.path.dirname(__file__), MUSIC_FILE)
    if not os.path.exists(music_path):
        return
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.35)
        pygame.mixer.music.play(-1)
    except pygame.error:
        # Silently continue if audio device is unavailable
        pass


class SnowParticle:
    def __init__(self):
        self.reset(top=False)

    def reset(self, top=True):
        self.x = random.uniform(-520, 520)
        # Start near the top for respawns, anywhere for initial fill
        self.y = random.uniform(300, 520) if top else random.uniform(-500, 520)
        # Weighted sizes: mostly small/medium for even visual coverage
        r = random.random()
        if r < 0.7:
            self.size = random.choice([2, 3, 4])
        elif r < 0.95:
            self.size = random.choice([5, 6, 7, 8])
        else:
            self.size = random.choice([10, 12])
        # Speed modestly linked to size so big flakes don’t cluster
        self.speed = random.uniform(0.7, 1.4) * (0.8 + (16 - self.size) / 20)
        self.drift = random.uniform(-0.25, 0.25)
        self.opacity = random.randint(160, 255)
        # Pretty shape options
        self.shape = 'flake' if random.random() < 0.18 and self.size >= 6 else 'circle'
        self.angle = random.uniform(0.0, math.pi * 2)
        self.spin = random.uniform(-0.03, 0.03)
        self.float_phase = random.uniform(0.0, math.pi * 2)
        # Per-particle noise for drift (prevents line alignment)
        self.noise_seed = random.uniform(0.0, math.pi * 2)
        self.noise_speed = random.uniform(0.02, 0.05)
        self.noise_amp_x = random.uniform(0.15, 0.35)
        self.noise_amp_y = random.uniform(0.05, 0.15)

    def update(self, wind_dx=0.0):
        # Fall downward in world coords (toward negative y on screen)
        self.y -= self.speed
        # subtle float sway + per-particle noise drift
        self.noise_seed += self.noise_speed
        sway_x = 0.08 * math.sin(self.float_phase)
        noise_x = self.noise_amp_x * math.sin(self.noise_seed + self.float_phase * 0.8)
        noise_y = self.noise_amp_y * math.sin(self.noise_seed * 1.3 + self.float_phase * 0.6)
        self.x += self.drift + wind_dx + sway_x + noise_x + random.uniform(-0.03, 0.03)
        self.y -= noise_y
        self.angle += self.spin
        self.float_phase += 0.03
        if self.y < -520:
            self.reset(top=True)
        if self.x < -520:
            self.x = 520
        elif self.x > 520:
            self.x = -520
    
    def draw(self, surface):
        screen_x = to_screen_x(self.x)
        screen_y = to_screen_y(self.y)
        
        if self.shape == 'flake':
            # Rotating six-arm snowflake
            arm_len = max(4, int(self.size * 1.2))
            tip_len = max(2, int(self.size * 0.5))
            for k in range(6):
                rad = self.angle + k * math.pi / 3
                ex = screen_x + int(math.cos(rad) * arm_len)
                ey = screen_y + int(math.sin(rad) * arm_len)
                pygame.draw.line(surface, (230, 235, 255), (screen_x, screen_y), (ex, ey), 2)
                # small tips
                tip_rad1 = rad + math.pi / 12
                tip_rad2 = rad - math.pi / 12
                tx1 = ex + int(math.cos(tip_rad1) * tip_len)
                ty1 = ey + int(math.sin(tip_rad1) * tip_len)
                tx2 = ex + int(math.cos(tip_rad2) * tip_len)
                ty2 = ey + int(math.sin(tip_rad2) * tip_len)
                pygame.draw.line(surface, (230, 235, 255), (ex, ey), (tx1, ty1), 1)
                pygame.draw.line(surface, (230, 235, 255), (ex, ey), (tx2, ty2), 1)
            # center and gentle glow
            pygame.draw.circle(surface, (255, 255, 255), (screen_x, screen_y), max(1, self.size // 4))
            if self.size >= 8:
                glow = pygame.Surface((self.size * 6, self.size * 6), pygame.SRCALPHA)
                pygame.draw.circle(glow, (255, 255, 255, 40), (self.size * 3, self.size * 3), self.size * 3)
                surface.blit(glow, (screen_x - self.size * 3, screen_y - self.size * 3))
        else:
            # Pretty circle flakes with soft glow for midsize
            if self.size >= 8:
                pygame.draw.circle(surface, (200, 200, 220), (screen_x, screen_y), self.size, 2)
                pygame.draw.circle(surface, (180, 180, 200), (screen_x, screen_y), self.size - 3, 1)
            color = (self.opacity, self.opacity, min(255, self.opacity + 30))
            pygame.draw.circle(surface, color, (screen_x, screen_y), max(1, self.size // 3))
            if 6 <= self.size < 8:
                glow = pygame.Surface((self.size * 4, self.size * 4), pygame.SRCALPHA)
                pygame.draw.circle(glow, (255, 255, 255, 30), (self.size * 2, self.size * 2), self.size * 2)
                surface.blit(glow, (screen_x - self.size * 2, screen_y - self.size * 2))


def draw_gradient_sky(surface):
    """Draw a gradient sky with stars"""
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(NIGHT_SKY_TOP[0] + (NIGHT_SKY_BOTTOM[0] - NIGHT_SKY_TOP[0]) * ratio)
        g = int(NIGHT_SKY_TOP[1] + (NIGHT_SKY_BOTTOM[1] - NIGHT_SKY_TOP[1]) * ratio)
        b = int(NIGHT_SKY_TOP[2] + (NIGHT_SKY_BOTTOM[2] - NIGHT_SKY_TOP[2]) * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (WIDTH, y))
    
    # Draw stars with twinkling effect
    random.seed(42)
    for _ in range(200):
        x = random.uniform(-500, 500)
        y = random.uniform(200, 500)
        screen_x = to_screen_x(x)
        screen_y = to_screen_y(y)
        size = random.choice([1, 1, 1, 2, 2, 3, 4])
        brightness = random.randint(150, 255)
        
        if size == 1:
            pygame.draw.circle(surface, (brightness, brightness, 255), (screen_x, screen_y), 1)
        elif size == 2:
            pygame.draw.circle(surface, (brightness, brightness, 255), (screen_x, screen_y), 2)
            gfxdraw.filled_circle(surface, screen_x, screen_y, 2, (brightness, brightness, 255, 180))
        elif size == 3:
            # Twinkling star
            pygame.draw.circle(surface, (255, 255, 255), (screen_x, screen_y), 2)
            pygame.draw.line(surface, (255, 255, 200), (screen_x-4, screen_y), (screen_x+4, screen_y), 1)
            pygame.draw.line(surface, (255, 255, 200), (screen_x, screen_y-4), (screen_x, screen_y+4), 1)
        else:
            # Big sparkle
            pygame.draw.circle(surface, (255, 255, 255), (screen_x, screen_y), 3)
            pygame.draw.line(surface, (255, 255, 150), (screen_x-6, screen_y), (screen_x+6, screen_y), 2)
            pygame.draw.line(surface, (255, 255, 150), (screen_x, screen_y-6), (screen_x, screen_y+6), 2)
            pygame.draw.line(surface, (255, 255, 200), (screen_x-4, screen_y-4), (screen_x+4, screen_y+4), 1)
            pygame.draw.line(surface, (255, 255, 200), (screen_x-4, screen_y+4), (screen_x+4, screen_y-4), 1)

def draw_realistic_tree(surface, center_x, base_y, scale=1.0, offset=0):
    """Draw a highly realistic Christmas tree with depth and shading
    center_x and base_y are in world coordinates (-500 to 500)"""
    
    # Tree dimensions
    tree_height = int(280 * scale)
    tree_width = int(200 * scale)
    trunk_width = int(30 * scale)
    trunk_height = int(50 * scale)
    
    # Convert to screen coordinates
    screen_cx = to_screen_x(center_x)
    screen_by = to_screen_y(base_y)
    
    # Draw trunk with 3D effect
    trunk_left = screen_cx - trunk_width // 2
    trunk_right = screen_cx + trunk_width // 2
    
    # Trunk shadow
    shadow_offset = int(5 * scale)
    trunk_shadow = pygame.Surface((trunk_width + shadow_offset, trunk_height), pygame.SRCALPHA)
    pygame.draw.rect(trunk_shadow, (0, 0, 0, 60), (shadow_offset, 0, trunk_width, trunk_height))
    surface.blit(trunk_shadow, (trunk_left, screen_by - trunk_height))
    
    # Trunk gradient
    for i in range(trunk_width):
        ratio = i / trunk_width
        r = int(TRUNK_BROWN_DARK[0] + (TRUNK_BROWN_LIGHT[0] - TRUNK_BROWN_DARK[0]) * ratio)
        g = int(TRUNK_BROWN_DARK[1] + (TRUNK_BROWN_LIGHT[1] - TRUNK_BROWN_DARK[1]) * ratio)
        b = int(TRUNK_BROWN_DARK[2] + (TRUNK_BROWN_LIGHT[2] - TRUNK_BROWN_DARK[2]) * ratio)
        pygame.draw.line(surface, (r, g, b), 
                        (trunk_left + i, screen_by - trunk_height), 
                        (trunk_left + i, screen_by))
    
    # Trunk highlight
    pygame.draw.line(surface, TRUNK_BROWN_LIGHT, (trunk_left + 2, screen_by - trunk_height), 
                    (trunk_left + 2, screen_by), 2)
    
    # Draw tree layers (bottom to top)
    num_layers = 7
    layer_spacing = tree_height // num_layers
    
    for layer in range(num_layers):
        layer_y = screen_by - trunk_height - (layer * layer_spacing)
        layer_width = tree_width - (layer * (tree_width // num_layers))
        layer_height = int(layer_spacing * 1.8)
        
        # Create zigzag edge points
        points = []
        num_zigzags = 8 + layer
        
        # Top point
        points.append((screen_cx, layer_y - layer_height))
        
        # Right side zigzags
        for i in range(num_zigzags):
            ratio = i / num_zigzags
            x = screen_cx + (layer_width // 2) * ratio
            y = layer_y - layer_height + (layer_height * ratio)
            
            # Zigzag effect
            zigzag_depth = random.randint(int(8 * scale), int(15 * scale))
            if i % 2 == 0:
                points.append((int(x + zigzag_depth), int(y)))
            else:
                points.append((int(x - zigzag_depth // 2), int(y)))
        
        # Bottom right
        points.append((screen_cx + layer_width // 2, layer_y))
        
        # Bottom left  
        points.append((screen_cx - layer_width // 2, layer_y))
        
        # Left side zigzags
        for i in range(num_zigzags, 0, -1):
            ratio = i / num_zigzags
            x = screen_cx - (layer_width // 2) * ratio
            y = layer_y - layer_height + (layer_height * ratio)
            
            zigzag_depth = random.randint(int(8 * scale), int(15 * scale))
            if i % 2 == 0:
                points.append((int(x - zigzag_depth), int(y)))
            else:
                points.append((int(x + zigzag_depth // 2), int(y)))
        
        # Draw shadow layer
        shadow_surface = pygame.Surface((layer_width + 40, layer_height + 40), pygame.SRCALPHA)
        shadow_points = [(p[0] - screen_cx + layer_width//2 + 25, p[1] - (layer_y - layer_height) + 5) 
                        for p in points]
        pygame.draw.polygon(shadow_surface, (0, 0, 0, 40), shadow_points)
        surface.blit(shadow_surface, (screen_cx - layer_width//2 - 20, layer_y - layer_height - 5))
        
        # Draw main layer with gradient
        base_color = [
            TREE_GREEN_DARK[0] + (TREE_GREEN_MID[0] - TREE_GREEN_DARK[0]) * (layer / num_layers),
            TREE_GREEN_DARK[1] + (TREE_GREEN_MID[1] - TREE_GREEN_DARK[1]) * (layer / num_layers),
            TREE_GREEN_DARK[2] + (TREE_GREEN_MID[2] - TREE_GREEN_DARK[2]) * (layer / num_layers)
        ]
        pygame.draw.polygon(surface, base_color, points)
        
        # Add highlights on left side
        highlight_points = []
        for i, point in enumerate(points):
            if point[0] < screen_cx and i < len(points) // 3:
                highlight_points.append(point)
        
        if len(highlight_points) > 2:
            highlight_surface = pygame.Surface((layer_width, layer_height), pygame.SRCALPHA)
            offset_points = [(p[0] - (screen_cx - layer_width//2), p[1] - (layer_y - layer_height)) 
                           for p in highlight_points]
            for point in offset_points:
                pygame.draw.circle(highlight_surface, (*TREE_GREEN_LIGHT, 80), point, int(15 * scale))
            surface.blit(highlight_surface, (screen_cx - layer_width//2, layer_y - layer_height))
        
        # Add snow on layer edges
        random.seed(42 + layer + offset)
        for i in range(0, len(points), 2):
            if random.random() > 0.3:
                snow_x, snow_y = points[i]
                # Snow pile
                snow_width = random.randint(int(8 * scale), int(18 * scale))
                snow_height = random.randint(int(4 * scale), int(10 * scale))
                
                # Draw snow with gradient
                for sy in range(snow_height):
                    ratio = sy / snow_height
                    color_val = int(255 - (ratio * 30))
                    snow_color = (color_val, color_val, 255)
                    pygame.draw.ellipse(surface, snow_color,
                                      (snow_x - snow_width//2, snow_y - snow_height + sy,
                                       snow_width, 4))
                
                # Snow highlight
                pygame.draw.ellipse(surface, SNOW_WHITE,
                                  (snow_x - snow_width//2 + 2, snow_y - snow_height,
                                   snow_width - 4, 3))
        
        # Ornaments
        random.seed(100 + layer + offset)
        ornament_colors = [(255, 50, 50), (50, 150, 255), (255, 215, 0), 
                          (255, 140, 0), (180, 50, 255)]
        num_ornaments = random.randint(2, 4)
        
        for _ in range(num_ornaments):
            if random.random() > 0.4:
                orn_x = random.randint(screen_cx - layer_width//3, screen_cx + layer_width//3)
                orn_y = random.randint(layer_y - layer_height + 10, layer_y - 10)
                orn_size = int(random.randint(4, 8) * scale)
                orn_color = random.choice(ornament_colors)
                
                # Ornament shadow
                pygame.draw.circle(surface, (0, 0, 0, 100), (orn_x + 2, orn_y + 2), orn_size)
                
                # Ornament
                pygame.draw.circle(surface, orn_color, (orn_x, orn_y), orn_size)
                
                # Ornament highlight
                pygame.draw.circle(surface, (255, 255, 255), 
                                 (orn_x - orn_size//3, orn_y - orn_size//3), 
                                 max(1, orn_size//3))
                
                # Ornament hanger
                pygame.draw.line(surface, (40, 40, 40), 
                               (orn_x, orn_y - orn_size), (orn_x, orn_y - orn_size - 5), 1)
        
        # Add string lights on some layers
        if layer % 2 == 0:
            random.seed(200 + layer + offset)
            num_lights = random.randint(5, 8)
            for light_i in range(num_lights):
                if random.random() > 0.3:
                    light_x = random.randint(screen_cx - layer_width//3, screen_cx + layer_width//3)
                    light_y = random.randint(layer_y - layer_height + 15, layer_y - 15)
                    light_color = random.choice([(255, 255, 100), (255, 200, 100), (255, 150, 50)])
                    light_size = int(random.randint(3, 5) * scale)
                    
                    # Light glow
                    glow_surf = pygame.Surface((light_size * 6, light_size * 6), pygame.SRCALPHA)
                    for i in range(15, 0, -1):
                        alpha = int((i / 15) * 100)
                        pygame.draw.circle(glow_surf, (*light_color, alpha), 
                                         (light_size * 3, light_size * 3), i * 2)
                    surface.blit(glow_surf, (light_x - light_size * 3, light_y - light_size * 3))
                    
                    # Light bulb
                    pygame.draw.circle(surface, light_color, (light_x, light_y), light_size)
                    pygame.draw.circle(surface, (255, 255, 255), 
                                     (light_x - light_size//2, light_y - light_size//2), 
                                     max(1, light_size//2))
    
    # Draw star on top
    star_y_world = base_y + trunk_height + tree_height
    draw_star(surface, center_x, star_y_world, int(20 * scale))

def draw_star(surface, x, y, size):
    """Draw a glowing star (x, y in world coordinates)"""
    screen_x = to_screen_x(x)
    screen_y = to_screen_y(y)
    
    # Glow effect
    glow_surface = pygame.Surface((size * 6, size * 6), pygame.SRCALPHA)
    for i in range(20, 0, -1):
        alpha = int((i / 20) * 60)
        pygame.draw.circle(glow_surface, (255, 255, 150, alpha), 
                         (size * 3, size * 3), i * 3)
    surface.blit(glow_surface, (screen_x - size * 3, screen_y - size * 3))
    
    # Star shape
    points = []
    for i in range(5):
        angle = math.radians(i * 144 - 90)
        px = screen_x + math.cos(angle) * size
        py = screen_y + math.sin(angle) * size
        points.append((px, py))
        
        # Inner point
        angle = math.radians(i * 144 - 90 + 72)
        px = screen_x + math.cos(angle) * (size * 0.4)
        py = screen_y + math.sin(angle) * (size * 0.4)
        points.append((px, py))
    
    # Draw star
    pygame.draw.polygon(surface, (255, 255, 100), points)
    pygame.draw.polygon(surface, (255, 255, 255), points, 2)
    
    # Star center
    pygame.draw.circle(surface, (255, 255, 255), (int(screen_x), int(screen_y)), size // 4)

def draw_snowy_ground(surface):
    """Draw realistic snowy ground with depth"""
    # Multiple layers of snow (in world coordinates)
    snow_layers = [
        (-320, (230, 235, 245), 30),  # Back layer
        (-360, (240, 245, 255), 40), # Middle layer
        (-400, (250, 252, 255), 50), # Front layer
    ]
    
    for base_y, color, wave_height in snow_layers:
        points = [(0, HEIGHT)]
        
        # Create wavy snow surface
        for x in range(-500, 510, 10):
            wave1 = math.sin(x * 0.02) * (wave_height * 0.3)
            wave2 = math.sin(x * 0.05 + 1) * (wave_height * 0.2)
            wave3 = math.sin(x * 0.01) * (wave_height * 0.5)
            y = base_y + wave1 + wave2 + wave3
            screen_x = to_screen_x(x)
            screen_y = to_screen_y(y)
            points.append((screen_x, int(screen_y)))
        
        points.append((WIDTH, HEIGHT))
        
        # Draw snow layer
        pygame.draw.polygon(surface, color, points)
        
        # Add shadow to wave peaks
        for i in range(1, len(points) - 1):
            if points[i][1] < points[i-1][1] and points[i][1] < points[i+1][1]:
                shadow_surf = pygame.Surface((20, 10), pygame.SRCALPHA)
                pygame.draw.ellipse(shadow_surf, (200, 210, 230, 100), (0, 0, 20, 10))
                surface.blit(shadow_surf, (points[i][0] - 10, points[i][1]))
    
    # Ground snow sparkles
    random.seed(999)
    for _ in range(100):
        x = random.uniform(-500, 500)
        y = random.uniform(-450, -300)
        size = random.choice([1, 1, 2])
        brightness = random.randint(200, 255)
        pygame.draw.circle(surface, (brightness, brightness, 255), 
                         (to_screen_x(x), to_screen_y(y)), size)

def draw_tree_shadow(surface, center_x, base_y, scale=1.0):
    """Draw realistic tree shadow (center_x, base_y in world coordinates)"""
    shadow_width = int(180 * scale)
    shadow_height = int(40 * scale)
    
    screen_cx = to_screen_x(center_x)
    screen_by = to_screen_y(base_y)
    
    shadow_surf = pygame.Surface((shadow_width, shadow_height), pygame.SRCALPHA)
    
    # Elliptical shadow with gradient
    for i in range(shadow_height):
        ratio = i / shadow_height
        alpha = int((1 - ratio) * 80)
        width = int(shadow_width * (1 - ratio * 0.3))
        pygame.draw.ellipse(shadow_surf, (0, 0, 50, alpha),
                          ((shadow_width - width) // 2, i, width, 2))
    
    surface.blit(shadow_surf, (screen_cx - shadow_width // 2, screen_by - 10))

def draw_present(surface, x, y, width, height, box_color, ribbon_color):
    """Draw a gift box with ribbon (x, y in world coordinates)"""
    screen_x = to_screen_x(x)
    screen_y = to_screen_y(y)
    
    # Box shadow
    shadow = pygame.Surface((width + 10, height + 10), pygame.SRCALPHA)
    pygame.draw.rect(shadow, (0, 0, 0, 80), (5, 5, width, height))
    surface.blit(shadow, (screen_x - 5, screen_y - 5))
    
    # Main box
    pygame.draw.rect(surface, box_color, (screen_x, screen_y, width, height))
    
    # Box highlights
    lighter = tuple(min(255, c + 40) for c in box_color)
    pygame.draw.rect(surface, lighter, (screen_x, screen_y, width, height), 2)
    pygame.draw.line(surface, lighter, (screen_x, screen_y), (screen_x + 10, screen_y + 10), 2)
    
    # Ribbon vertical
    ribbon_width = max(8, width // 5)
    pygame.draw.rect(surface, ribbon_color, 
                    (screen_x + width//2 - ribbon_width//2, screen_y, ribbon_width, height))
    
    # Ribbon horizontal
    pygame.draw.rect(surface, ribbon_color,
                    (screen_x, screen_y + height//2 - ribbon_width//2, width, ribbon_width))
    
    # Ribbon bow
    bow_size = ribbon_width * 2
    bow_x = screen_x + width // 2
    bow_y = screen_y + height // 2
    
    # Bow loops
    pygame.draw.circle(surface, ribbon_color, (bow_x - bow_size//2, bow_y), bow_size//2)
    pygame.draw.circle(surface, ribbon_color, (bow_x + bow_size//2, bow_y), bow_size//2)
    
    # Bow center
    pygame.draw.circle(surface, ribbon_color, (bow_x, bow_y), bow_size//3)
    
    # Bow highlight
    lighter_ribbon = tuple(min(255, c + 60) for c in ribbon_color)
    pygame.draw.circle(surface, lighter_ribbon, (bow_x - 3, bow_y - 3), bow_size//4)

def draw_merry_christmas_banner(surface):
    """Draw a beautiful Merry Christmas banner"""
    # Initialize font
    pygame.font.init()
    
    # Banner ribbon coordinates (world coordinates)
    banner_y = -460
    banner_height = 80
    
    # Draw ribbon banner
    ribbon_points = [
        (to_screen_x(-350), to_screen_y(banner_y + 20)),
        (to_screen_x(-380), to_screen_y(banner_y)),
        (to_screen_x(-350), to_screen_y(banner_y - 20)),
        (to_screen_x(350), to_screen_y(banner_y - 20)),
        (to_screen_x(380), to_screen_y(banner_y)),
        (to_screen_x(350), to_screen_y(banner_y + 20))
    ]
    
    # Banner shadow
    shadow_surf = pygame.Surface((800, 100), pygame.SRCALPHA)
    shadow_points = [(p[0] - 100, p[1] - to_screen_y(banner_y) + 50 + 5) for p in ribbon_points]
    pygame.draw.polygon(shadow_surf, (0, 0, 0, 60), shadow_points)
    surface.blit(shadow_surf, (100, to_screen_y(banner_y) - 50))
    
    # Gold ribbon with gradient
    for offset in range(40, 0, -2):
        alpha = int((offset / 40) * 200)
        color_brightness = 180 + int((1 - offset/40) * 75)
        pygame.draw.polygon(surface, (color_brightness, color_brightness - 35, 0), ribbon_points, offset//2)
    
    pygame.draw.polygon(surface, GOLD, ribbon_points)
    pygame.draw.polygon(surface, (255, 240, 100), ribbon_points, 3)
    
    # Ribbon ends
    left_end = [
        (to_screen_x(-380), to_screen_y(banner_y)),
        (to_screen_x(-420), to_screen_y(banner_y - 15)),
        (to_screen_x(-430), to_screen_y(banner_y)),
        (to_screen_x(-420), to_screen_y(banner_y + 15))
    ]
    right_end = [
        (to_screen_x(380), to_screen_y(banner_y)),
        (to_screen_x(420), to_screen_y(banner_y - 15)),
        (to_screen_x(430), to_screen_y(banner_y)),
        (to_screen_x(420), to_screen_y(banner_y + 15))
    ]
    
    pygame.draw.polygon(surface, (200, 170, 0), left_end)
    pygame.draw.polygon(surface, (200, 170, 0), right_end)
    pygame.draw.polygon(surface, GOLD, left_end, 2)
    pygame.draw.polygon(surface, GOLD, right_end, 2)
    
    # Text "Merry Christmas"
    try:
        font = pygame.font.Font(None, 72)
        font_small = pygame.font.Font(None, 48)
    except:
        font = pygame.font.SysFont('arial', 72, bold=True)
        font_small = pygame.font.SysFont('arial', 48, bold=True)
    
    text = "Merry Christmas"
    
    # Render text with outline
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect(center=(WIDTH//2, to_screen_y(banner_y)))
    
    # Text shadow
    shadow_text = font.render(text, True, (80, 0, 0))
    surface.blit(shadow_text, (text_rect.x + 4, text_rect.y + 4))
    
    # Text outline
    outline_color = (139, 0, 0)
    for offset_x in [-2, -1, 0, 1, 2]:
        for offset_y in [-2, -1, 0, 1, 2]:
            if offset_x != 0 or offset_y != 0:
                outline_text = font.render(text, True, outline_color)
                surface.blit(outline_text, (text_rect.x + offset_x, text_rect.y + offset_y))
    
    # Main text
    surface.blit(text_surface, text_rect)
    
    # Text highlight
    highlight = font.render(text, True, (255, 150, 150))
    surface.blit(highlight, (text_rect.x - 1, text_rect.y - 1))
    
    # Add decorative sparkles around banner
    random.seed(777)
    for _ in range(25):
        spark_x = random.randint(-340, 340)
        spark_y = banner_y + random.randint(-35, 35)
        screen_sx = to_screen_x(spark_x)
        screen_sy = to_screen_y(spark_y)
        size = random.choice([2, 3, 4])
        
        pygame.draw.circle(surface, (255, 255, 200), (screen_sx, screen_sy), size)
        pygame.draw.line(surface, (255, 255, 255), (screen_sx - size*2, screen_sy), 
                        (screen_sx + size*2, screen_sy), 1)
        pygame.draw.line(surface, (255, 255, 255), (screen_sx, screen_sy - size*2), 
                        (screen_sx, screen_sy + size*2), 1)

def draw_warm_wishes(surface):
    """Draw warm Christmas wishes at the bottom"""
    pygame.font.init()
    
    try:
        font_large = pygame.font.Font(None, 56)
        font_medium = pygame.font.Font(None, 42)
    except:
        font_large = pygame.font.SysFont('arial', 56, bold=True)
        font_medium = pygame.font.SysFont('arial', 42, bold=True)
    
    # "Wishing you a" text
    wish_text = "Wishing you a"
    wish_surface = font_medium.render(wish_text, True, (255, 240, 200))
    wish_rect = wish_surface.get_rect(center=(WIDTH//2, to_screen_y(-470)))
    
    # Text shadow
    shadow_wish = font_medium.render(wish_text, True, (100, 80, 60))
    surface.blit(shadow_wish, (wish_rect.x + 2, wish_rect.y + 2))
    
    # Main text with outline
    for offset_x in [-1, 0, 1]:
        for offset_y in [-1, 0, 1]:
            if offset_x != 0 or offset_y != 0:
                outline = font_medium.render(wish_text, True, (150, 120, 80))
                surface.blit(outline, (wish_rect.x + offset_x, wish_rect.y + offset_y))
    
    surface.blit(wish_surface, wish_rect)
    
    # "MERRY CHRISTMAS" text - larger and more prominent
    merry_text = "MERRY CHRISTMAS"
    merry_surface = font_large.render(merry_text, True, (255, 50, 50))
    merry_rect = merry_surface.get_rect(center=(WIDTH//2, to_screen_y(-490)))
    
    # Shadow
    shadow_merry = font_large.render(merry_text, True, (80, 0, 0))
    surface.blit(shadow_merry, (merry_rect.x + 3, merry_rect.y + 3))
    
    # Gold outline
    for offset_x in [-2, -1, 0, 1, 2]:
        for offset_y in [-2, -1, 0, 1, 2]:
            if offset_x != 0 or offset_y != 0:
                outline = font_large.render(merry_text, True, (180, 140, 0))
                surface.blit(outline, (merry_rect.x + offset_x, merry_rect.y + offset_y))
    
    # Main text
    surface.blit(merry_surface, merry_rect)
    
    # Highlight
    highlight = font_large.render(merry_text, True, (255, 200, 200))
    surface.blit(highlight, (merry_rect.x - 1, merry_rect.y - 1))
    
    # Add decorative elements
    # Left snowflake
    snowflake_left_x = merry_rect.left - 40
    snowflake_y = to_screen_y(-485)
    draw_decorative_snowflake(surface, snowflake_left_x, snowflake_y, 15)
    
    # Right snowflake
    snowflake_right_x = merry_rect.right + 40
    draw_decorative_snowflake(surface, snowflake_right_x, snowflake_y, 15)
    
    # Hearts around the text
    heart_positions = [
        (merry_rect.left - 70, to_screen_y(-490)),
        (merry_rect.right + 70, to_screen_y(-490)),
    ]
    
    for hx, hy in heart_positions:
        draw_heart(surface, hx, hy, 12)

def draw_decorative_snowflake(surface, x, y, size):
    """Draw a decorative snowflake"""
    color = (200, 230, 255)
    
    # Main cross
    pygame.draw.line(surface, color, (x - size, y), (x + size, y), 3)
    pygame.draw.line(surface, color, (x, y - size), (x, y + size), 3)
    
    # Diagonal cross
    pygame.draw.line(surface, color, (x - size//1.5, y - size//1.5), (x + size//1.5, y + size//1.5), 2)
    pygame.draw.line(surface, color, (x - size//1.5, y + size//1.5), (x + size//1.5, y - size//1.5), 2)
    
    # Tips
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        tip_x = x + math.cos(rad) * size
        tip_y = y + math.sin(rad) * size
        pygame.draw.circle(surface, (255, 255, 255), (int(tip_x), int(tip_y)), 3)

def draw_heart(surface, x, y, size):
    """Draw a small heart"""
    color = (255, 100, 120)
    
    # Create heart shape using circles and triangle
    pygame.draw.circle(surface, color, (int(x - size//3), int(y - size//3)), size//2)
    pygame.draw.circle(surface, color, (int(x + size//3), int(y - size//3)), size//2)
    
    # Triangle bottom
    points = [
        (x - size//1.5, y - size//4),
        (x + size//1.5, y - size//4),
        (x, y + size)
    ]
    pygame.draw.polygon(surface, color, points)
    
    # Highlight
    pygame.draw.circle(surface, (255, 180, 200), (int(x - size//2), int(y - size//2)), size//4)


def draw_smoke_puff(surface, cx, cy, r, alpha):
    puff = pygame.Surface((r * 4, r * 4), pygame.SRCALPHA)
    pygame.draw.circle(puff, (220, 220, 220, alpha), (r * 2, r * 2), r)
    pygame.draw.circle(puff, (255, 255, 255, alpha // 2), (r * 2 - r//3, r * 2 - r//3), r // 2)
    surface.blit(puff, (cx - r * 2, cy - r * 2))


def draw_cozy_house(surface, x, y, scale=1.0, phase=0.0):
    """Draw a small cozy house with chimney and animated smoke."""
    base_w = int(220 * scale)
    base_h = int(130 * scale)
    roof_h = int(80 * scale)
    sx = to_screen_x(x)
    sy = to_screen_y(y)

    # Base
    house_rect = pygame.Rect(sx - base_w // 2, sy - base_h, base_w, base_h)
    pygame.draw.rect(surface, (165, 120, 90), house_rect)
    pygame.draw.rect(surface, (90, 60, 40), house_rect, 3)

    # Roof
    roof_points = [
        (sx - base_w // 2 - int(10 * scale), sy - base_h),
        (sx, sy - base_h - roof_h),
        (sx + base_w // 2 + int(10 * scale), sy - base_h),
    ]
    pygame.draw.polygon(surface, (120, 50, 40), roof_points)
    pygame.draw.polygon(surface, (200, 90, 70), roof_points, 3)

    # Chimney
    chimney_w = int(28 * scale)
    chimney_h = int(70 * scale)
    chimney_rect = pygame.Rect(sx + base_w // 4, sy - base_h - chimney_h + int(10 * scale), chimney_w, chimney_h)
    pygame.draw.rect(surface, (90, 60, 40), chimney_rect)
    pygame.draw.rect(surface, (60, 40, 30), chimney_rect, 2)

    # Smoke animation
    smoke_base_x = chimney_rect.centerx
    smoke_base_y = chimney_rect.top - int(10 * scale)
    for i in range(4):
        puff_r = int((16 - i * 2) * scale)
        offset_y = int(i * -22 * scale - math.sin(phase * 0.5 + i) * 6 * scale)
        offset_x = int(math.sin(phase * 0.4 + i * 0.8) * 12 * scale)
        draw_smoke_puff(surface, smoke_base_x + offset_x, smoke_base_y + offset_y, max(6, puff_r), 90)

    # Door
    door_w = int(40 * scale)
    door_h = int(70 * scale)
    door_rect = pygame.Rect(sx - door_w // 2, sy - door_h, door_w, door_h)
    pygame.draw.rect(surface, (90, 45, 25), door_rect)
    pygame.draw.rect(surface, (60, 30, 15), door_rect, 2)
    pygame.draw.circle(surface, (245, 190, 50), (door_rect.right - int(10 * scale), door_rect.centery), max(2, int(3 * scale)))

    # Windows with interior scenes (mirror-like glass)
    win_w = int(74 * scale)
    win_h = int(58 * scale)
    upstairs_win = pygame.Rect(sx - base_w // 3 - win_w // 2, sy - base_h + int(10 * scale), win_w, win_h)
    downstairs_win = pygame.Rect(sx + base_w // 3 - win_w // 2, sy - base_h + int(52 * scale), win_w, win_h)

    def draw_window_frame(win_rect):
        # Outer wood frame
        frame_th = max(4, int(6 * scale))
        pygame.draw.rect(surface, (120, 85, 60), win_rect.inflate(frame_th * 2, frame_th * 2), frame_th)
        # Inner recess shadow
        inner = win_rect.inflate(-int(2 * scale), -int(2 * scale))
        shadow = pygame.Surface((inner.width, inner.height), pygame.SRCALPHA)
        pygame.draw.rect(shadow, (0, 0, 0, 60), pygame.Rect(0, 0, inner.width, inner.height))
        surface.blit(shadow, inner.topleft)
        # Sill under window
        sill_h = max(6, int(8 * scale))
        sill_rect = pygame.Rect(win_rect.left - int(6 * scale), win_rect.bottom, win_rect.width + int(12 * scale), sill_h)
        pygame.draw.rect(surface, (140, 100, 70), sill_rect)
        pygame.draw.rect(surface, (90, 60, 40), sill_rect, 2)

    def draw_window_mullions(win_rect):
        # Divide into 2x2 panes
        pane_w = win_rect.width // 2
        pane_h = win_rect.height // 2
        bar_th = max(3, int(4 * scale))
        # Vertical bar
        pygame.draw.rect(surface, (230, 230, 230), (win_rect.left + pane_w - bar_th // 2, win_rect.top, bar_th, win_rect.height))
        # Horizontal bar
        pygame.draw.rect(surface, (230, 230, 230), (win_rect.left, win_rect.top + pane_h - bar_th // 2, win_rect.width, bar_th))

    def draw_curtains(win_rect):
        # Simple drapes partially open
        curtain_w = int(win_rect.width * 0.25)
        curtain_h = win_rect.height
        left = pygame.Rect(win_rect.left, win_rect.top, curtain_w, curtain_h)
        right = pygame.Rect(win_rect.right - curtain_w, win_rect.top, curtain_w, curtain_h)
        # Fold shading
        for rect, base in [(left, (200, 40, 40)), (right, (200, 40, 40))]:
            pygame.draw.rect(surface, base, rect)
            for i in range(5):
                x = rect.left + int((i + 1) * rect.width / 6)
                pygame.draw.line(surface, (160, 20, 20), (x, rect.top), (x - 6, rect.bottom), 2)
        # Tiebacks
        pygame.draw.circle(surface, (245, 190, 50), (left.right, win_rect.centery), max(3, int(4 * scale)))
        pygame.draw.circle(surface, (245, 190, 50), (right.left, win_rect.centery), max(3, int(4 * scale)))

    def glass_reflection(win_rect):
        # Glare overlay only (frame is drawn separately)
        glass = pygame.Surface((win_rect.width, win_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(glass, (250, 230, 160, 40), pygame.Rect(0, 0, win_rect.width, win_rect.height))
        for i in range(0, win_rect.width, 6):
            alpha = max(0, 35 - i // 5)
            pygame.draw.line(glass, (255, 255, 255, alpha), (i, 0), (max(0, i - 14), win_rect.height), 2)
        surface.blit(glass, win_rect.topleft)

    def draw_sleeping_scene(win_rect):
        # Bed
        bed = pygame.Rect(win_rect.left + int(win_rect.width * 0.08), win_rect.bottom - int(win_rect.height * 0.35), int(win_rect.width * 0.84), int(win_rect.height * 0.28))
        pygame.draw.rect(surface, (120, 80, 60), bed)
        pygame.draw.rect(surface, (90, 60, 40), bed, 2)
        # Blanket with gentle rise/fall
        wave = int(3 * math.sin(phase * 0.8))
        blanket = pygame.Rect(bed.left + 4, bed.top - int(win_rect.height * 0.25) + wave, bed.width - 8, int(win_rect.height * 0.26))
        pygame.draw.rect(surface, (200, 30, 30), blanket)
        pygame.draw.rect(surface, (255, 200, 200), blanket, 2)
        # Person silhouette
        head_x = bed.left + int(win_rect.width * 0.2)
        head_y = bed.top - int(win_rect.height * 0.14)
        pygame.draw.circle(surface, (240, 200, 180), (head_x, head_y), int(win_rect.height * 0.09))
        pygame.draw.rect(surface, (240, 200, 180), (head_x - int(win_rect.width * 0.18), head_y, int(win_rect.width * 0.36), int(win_rect.height * 0.08)))
        # Lamp glow
        lamp_center = (win_rect.right - int(win_rect.width * 0.18), win_rect.top + int(win_rect.height * 0.18))
        for r in range(18, 2, -3):
            alpha = int(60 * (r / 18))
            pygame.draw.circle(surface, (255, 240, 180, alpha), lamp_center, r)

    def draw_tree_gifts_scene(win_rect):
        # Floor
        pygame.draw.rect(surface, (160, 120, 90), (win_rect.left, win_rect.bottom - int(win_rect.height * 0.25), win_rect.width, int(win_rect.height * 0.25)))
        # Tree
        tx = win_rect.centerx
        ty = win_rect.bottom - int(win_rect.height * 0.25)
        # simple layered tree inside window
        layer_w = int(win_rect.width * 0.7)
        for i in range(3):
            lw = layer_w - i * int(win_rect.width * 0.2)
            lh = int(win_rect.height * 0.18)
            points = [(tx, ty - (i + 1) * lh), (tx - lw // 2, ty - i * lh), (tx + lw // 2, ty - i * lh)]
            pygame.draw.polygon(surface, (40, 130, 60), points)
            pygame.draw.polygon(surface, (80, 170, 90), points, 2)
        # Trunk
        pygame.draw.rect(surface, (100, 70, 40), (tx - 6, ty - 10, 12, 10))
        # Ornaments
        for _ in range(8):
            ox = random.randint(win_rect.left + 6, win_rect.right - 6)
            oy = random.randint(win_rect.top + 6, ty - 6)
            pygame.draw.circle(surface, random.choice([(255,50,50),(255,215,0),(50,150,255)]), (ox, oy), 3)
        # Gifts
        gift_w = int(win_rect.width * 0.18)
        gift_h = int(win_rect.height * 0.12)
        gifts = [
            (win_rect.left + int(win_rect.width * 0.12), ty - gift_h, (200, 20, 20), (255,215,0)),
            (tx - gift_w // 2, ty - gift_h - 6, (0, 150, 0), (220,20,20)),
            (win_rect.right - int(win_rect.width * 0.3), ty - gift_h + 4, (20, 100, 200), (255,255,255)),
        ]
        for gx, gy, c, rc in gifts:
            pygame.draw.rect(surface, c, (gx, gy, gift_w, gift_h))
            pygame.draw.rect(surface, rc, (gx + gift_w // 2 - 5, gy, 10, gift_h))
            pygame.draw.rect(surface, rc, (gx, gy + gift_h // 2 - 5, gift_w, 10))

    # Draw scenes, curtains, mullions, frame, then glare overlay
    draw_sleeping_scene(upstairs_win)
    draw_tree_gifts_scene(downstairs_win)
    draw_curtains(upstairs_win)
    draw_curtains(downstairs_win)
    draw_window_mullions(upstairs_win)
    draw_window_mullions(downstairs_win)
    draw_window_frame(upstairs_win)
    draw_window_frame(downstairs_win)
    glass_reflection(upstairs_win)
    glass_reflection(downstairs_win)

    # Simple porch steps
    step_height = int(8 * scale)
    for i in range(2):
        pygame.draw.rect(surface, (150, 110, 80), (door_rect.left - int(4 * scale), sy - door_h + door_h + i * step_height, door_w + int(8 * scale), step_height))


def draw_snowman(surface, x, y, scale=1.0, phase=0.0):
    """Draw a friendly snowman."""
    sx = to_screen_x(x)
    sy = to_screen_y(y)
    base_r = int(28 * scale)
    mid_r = int(20 * scale)
    head_r = int(14 * scale)

    # Shadows
    shadow = pygame.Surface((base_r * 4, base_r * 2), pygame.SRCALPHA)
    pygame.draw.ellipse(shadow, (0, 0, 0, 70), (0, 0, base_r * 4, base_r))
    surface.blit(shadow, (sx - base_r * 2, sy - int(base_r * 0.2)))

    # Body
    pygame.draw.circle(surface, SNOW_WHITE, (sx, sy), base_r)
    pygame.draw.circle(surface, SNOW_WHITE, (sx, sy - int(base_r + mid_r * 0.2)), mid_r)
    pygame.draw.circle(surface, SNOW_WHITE, (sx, sy - int(base_r + mid_r + head_r * 0.6)), head_r)

    # Buttons
    for i in range(3):
        pygame.draw.circle(surface, (40, 40, 40), (sx, sy - int(i * 12 * scale)), max(2, int(3 * scale)))

    # Eyes and nose
    eye_y = sy - int(base_r + mid_r + head_r * 0.8)
    pygame.draw.circle(surface, (0, 0, 0), (sx - int(5 * scale), eye_y), max(1, int(2 * scale)))
    pygame.draw.circle(surface, (0, 0, 0), (sx + int(5 * scale), eye_y), max(1, int(2 * scale)))
    pygame.draw.polygon(surface, (255, 140, 0), [
        (sx, eye_y + int(3 * scale)),
        (sx + int(16 * scale), eye_y + int(2 * scale)),
        (sx, eye_y + int(5 * scale))
    ])

    # Smile
    pygame.draw.arc(surface, (0, 0, 0), (sx - int(10 * scale), eye_y + int(6 * scale), int(20 * scale), int(10 * scale)), math.pi * 0.1, math.pi * 0.9, 2)

    # Arms
    arm_y = sy - int(base_r + mid_r * 0.2)
    arm_len = int(38 * scale)
    sway = math.sin(phase * 0.5) * 4 * scale
    pygame.draw.line(surface, (120, 80, 40), (sx - mid_r, arm_y), (sx - mid_r - arm_len, arm_y + int(4 * scale + sway)), int(3 * scale))
    pygame.draw.line(surface, (120, 80, 40), (sx + mid_r, arm_y), (sx + mid_r + arm_len, arm_y + int(-4 * scale - sway)), int(3 * scale))

    # Hat
    brim_w = int(38 * scale)
    pygame.draw.rect(surface, (30, 30, 30), (sx - brim_w // 2, eye_y - int(12 * scale), brim_w, int(5 * scale)))
    pygame.draw.rect(surface, (40, 40, 40), (sx - int(16 * scale), eye_y - int(32 * scale), int(32 * scale), int(20 * scale)))
    pygame.draw.rect(surface, (200, 0, 0), (sx - int(16 * scale), eye_y - int(24 * scale), int(32 * scale), int(6 * scale)))


def draw_reindeer(surface, x, y, scale=1.0, phase=0.0):
    """Draw a stylized reindeer with slight animated leg motion."""
    sx = to_screen_x(x)
    sy = to_screen_y(y)
    
    body_len = int(90 * scale)
    body_ht = int(28 * scale)
    head_size = int(18 * scale)
    leg_phase = math.sin(phase) * 4 * scale
    
    # Body
    pygame.draw.ellipse(surface, REINDEER_BROWN, (sx - body_len//2, sy - body_ht//2, body_len, body_ht))
    pygame.draw.ellipse(surface, REINDEER_LIGHT, (sx - body_len//3, sy - body_ht//3, body_len//2, body_ht//2))
    
    # Legs
    leg_x_offsets = [-25, -10, 10, 25]
    for i, lx in enumerate(leg_x_offsets):
        ly = sy + int(leg_phase if i % 2 == 0 else -leg_phase)
        pygame.draw.line(surface, REINDEER_BROWN, (sx + lx, sy + body_ht//2), (sx + lx, ly + int(28 * scale)), int(4 * scale))
        pygame.draw.line(surface, (50, 30, 20), (sx + lx, ly + int(28 * scale)), (sx + lx + int(6 * scale), ly + int(34 * scale)), int(4 * scale))
    
    # Neck and head
    neck_x = sx + int(body_len//2 - 10 * scale)
    neck_y = sy - int(body_ht//4)
    pygame.draw.line(surface, REINDEER_BROWN, (neck_x, neck_y), (neck_x + int(8 * scale), neck_y - int(18 * scale)), int(6 * scale))
    pygame.draw.circle(surface, REINDEER_BROWN, (neck_x + int(14 * scale), neck_y - int(22 * scale)), head_size)
    pygame.draw.circle(surface, REINDEER_LIGHT, (neck_x + int(8 * scale), neck_y - int(20 * scale)), head_size//2)
    
    # Antlers
    antler_base = (neck_x + int(14 * scale), neck_y - int(22 * scale))
    for offset in [-1, 1]:
        pygame.draw.line(surface, (80, 60, 40), antler_base, (antler_base[0] + int(12 * scale * offset), antler_base[1] - int(18 * scale)), int(3 * scale))
        pygame.draw.line(surface, (80, 60, 40), (antler_base[0] + int(8 * scale * offset), antler_base[1] - int(10 * scale)), (antler_base[0] + int(16 * scale * offset), antler_base[1] - int(4 * scale)), int(3 * scale))
    
    # Eye
    pygame.draw.circle(surface, (0, 0, 0), (neck_x + int(18 * scale), neck_y - int(24 * scale)), max(1, int(2 * scale)))
    
    # Nose (small glow)
    nose_x = neck_x + int(26 * scale)
    nose_y = neck_y - int(18 * scale)
    pygame.draw.circle(surface, (200, 30, 30), (nose_x, nose_y), max(3, int(4 * scale)))
    pygame.draw.circle(surface, (255, 180, 180), (nose_x - int(2 * scale), nose_y - int(2 * scale)), max(1, int(2 * scale)))
    
    # Harness
    pygame.draw.line(surface, LEATHER, (sx + body_len//2 - int(10 * scale), sy - int(6 * scale)), (sx - body_len//2 + int(15 * scale), sy - int(6 * scale)), int(3 * scale))
    pygame.draw.circle(surface, SLEIGH_GOLD, (sx, sy - int(6 * scale)), max(2, int(3 * scale)))


def draw_sleigh(surface, x, y, scale=1.0):
    """Draw Santa's sleigh."""
    sx = to_screen_x(x)
    sy = to_screen_y(y)
    body_w = int(110 * scale)
    body_h = int(45 * scale)
    rail_h = int(18 * scale)
    
    # Rails
    pygame.draw.line(surface, SLEIGH_GOLD, (sx - body_w//2, sy + body_h//2), (sx + body_w//2, sy + body_h//2), int(6 * scale))
    pygame.draw.arc(surface, SLEIGH_GOLD, (sx + body_w//4, sy + body_h//2 - rail_h, body_w//2, rail_h * 2), math.pi, math.pi * 2, int(5 * scale))
    
    # Body base
    pygame.draw.rect(surface, SLEIGH_RED, (sx - body_w//2, sy - body_h//2, body_w, body_h))
    pygame.draw.rect(surface, SLEIGH_GOLD, (sx - body_w//2, sy - body_h//2, body_w, body_h), int(4 * scale))
    
    # Front curve
    pygame.draw.arc(surface, SLEIGH_RED, (sx + body_w//3, sy - body_h//2 - int(10 * scale), body_w//2, body_h), math.pi, math.pi * 2, int(12 * scale))
    pygame.draw.arc(surface, SLEIGH_GOLD, (sx + body_w//3, sy - body_h//2 - int(10 * scale), body_w//2, body_h), math.pi, math.pi * 2, int(4 * scale))
    
    # Seat highlight
    pygame.draw.rect(surface, (255, 230, 200), (sx - body_w//2 + int(10 * scale), sy - body_h//2 + int(10 * scale), body_w - int(20 * scale), int(12 * scale)))
    
    # Gift silhouettes inside sleigh
    pygame.draw.rect(surface, (50, 120, 200), (sx - int(25 * scale), sy - body_h//2 - int(5 * scale), int(20 * scale), int(20 * scale)))
    pygame.draw.rect(surface, (200, 50, 50), (sx, sy - body_h//2 - int(10 * scale), int(18 * scale), int(22 * scale)))
    pygame.draw.line(surface, (255, 255, 255), (sx + int(9 * scale), sy - body_h//2 - int(10 * scale)), (sx + int(9 * scale), sy - body_h//2 + int(12 * scale)), int(3 * scale))
    pygame.draw.line(surface, (255, 255, 255), (sx, sy - body_h//2), (sx + int(18 * scale), sy - body_h//2), int(3 * scale))


def draw_sleigh_team(surface, x, y, scale=1.0, phase=0.0):
    """Draw sleigh with two reindeer and harness ropes."""
    spacing = int(120 * scale)
    reindeer1_pos = (x - spacing, y)
    reindeer2_pos = (x - spacing * 2, y - int(5 * scale))
    
    # Ropes from sleigh to reindeer
    sx = to_screen_x(x)
    sy = to_screen_y(y)
    nose1 = (to_screen_x(reindeer1_pos[0] + 40 * scale), to_screen_y(reindeer1_pos[1] - 10 * scale))
    nose2 = (to_screen_x(reindeer2_pos[0] + 40 * scale), to_screen_y(reindeer2_pos[1] - 10 * scale))
    pygame.draw.line(surface, LEATHER, (sx - int(50 * scale), sy - int(10 * scale)), nose1, int(3 * scale))
    pygame.draw.line(surface, LEATHER, (sx - int(50 * scale), sy - int(14 * scale)), nose2, int(3 * scale))
    
    # Reindeer
    draw_reindeer(surface, *reindeer1_pos, scale=scale, phase=phase)
    draw_reindeer(surface, *reindeer2_pos, scale=scale * 0.95, phase=phase + 0.6)
    
    # Sleigh
    draw_sleigh(surface, x, y, scale=scale)

def draw_santa(surface, x, y, wave_offset=0):
    """Draw Santa Claus waving (x, y in world coordinates)"""
    screen_x = to_screen_x(x)
    screen_y = to_screen_y(y)
    
    # Scale factor
    scale = 1.5
    
    # Santa shadow
    shadow = pygame.Surface((int(80 * scale), int(100 * scale)), pygame.SRCALPHA)
    pygame.draw.ellipse(shadow, (0, 0, 0, 100), (0, int(80 * scale), int(80 * scale), int(20 * scale)))
    surface.blit(shadow, (screen_x - int(40 * scale), screen_y - int(10 * scale)))
    
    # Gift sack
    sack_x = screen_x - int(35 * scale)
    sack_y = screen_y - int(60 * scale)
    sack_points = [
        (sack_x, sack_y),
        (sack_x - int(20 * scale), sack_y - int(15 * scale)),
        (sack_x - int(15 * scale), sack_y - int(40 * scale)),
        (sack_x + int(5 * scale), sack_y - int(45 * scale)),
        (sack_x + int(15 * scale), sack_y - int(35 * scale)),
        (sack_x + int(15 * scale), sack_y - int(10 * scale))
    ]
    pygame.draw.polygon(surface, (139, 90, 60), sack_points)
    pygame.draw.polygon(surface, (100, 65, 40), sack_points, 2)
    
    # Sack tie
    pygame.draw.circle(surface, (200, 180, 100), (sack_x, sack_y - int(42 * scale)), int(8 * scale))
    pygame.draw.line(surface, (200, 180, 100), (sack_x - int(8 * scale), sack_y - int(45 * scale)), 
                    (sack_x + int(8 * scale), sack_y - int(45 * scale)), 3)
    
    # Legs (boots)
    # Left leg
    pygame.draw.rect(surface, (40, 40, 40), 
                    (screen_x - int(15 * scale), screen_y - int(35 * scale), int(12 * scale), int(40 * scale)))
    # Right leg
    pygame.draw.rect(surface, (40, 40, 40), 
                    (screen_x + int(5 * scale), screen_y - int(35 * scale), int(12 * scale), int(40 * scale)))
    
    # Boots
    pygame.draw.ellipse(surface, (20, 20, 20), 
                       (screen_x - int(18 * scale), screen_y - int(5 * scale), int(20 * scale), int(12 * scale)))
    pygame.draw.ellipse(surface, (20, 20, 20), 
                       (screen_x + int(2 * scale), screen_y - int(5 * scale), int(20 * scale), int(12 * scale)))
    
    # Body (red suit)
    body_points = [
        (screen_x - int(25 * scale), screen_y - int(35 * scale)),
        (screen_x - int(28 * scale), screen_y - int(65 * scale)),
        (screen_x - int(20 * scale), screen_y - int(75 * scale)),
        (screen_x + int(20 * scale), screen_y - int(75 * scale)),
        (screen_x + int(28 * scale), screen_y - int(65 * scale)),
        (screen_x + int(25 * scale), screen_y - int(35 * scale))
    ]
    pygame.draw.polygon(surface, (200, 20, 20), body_points)
    pygame.draw.polygon(surface, (160, 15, 15), body_points, 3)
    
    # White fur trim on coat
    pygame.draw.ellipse(surface, (255, 255, 255), 
                       (screen_x - int(22 * scale), screen_y - int(77 * scale), int(44 * scale), int(10 * scale)))
    pygame.draw.ellipse(surface, (255, 255, 255), 
                       (screen_x - int(27 * scale), screen_y - int(38 * scale), int(54 * scale), int(8 * scale)))
    
    # Black belt
    pygame.draw.rect(surface, (30, 30, 30), 
                    (screen_x - int(28 * scale), screen_y - int(55 * scale), int(56 * scale), int(12 * scale)))
    # Gold buckle
    pygame.draw.rect(surface, GOLD, 
                    (screen_x - int(10 * scale), screen_y - int(53 * scale), int(20 * scale), int(8 * scale)))
    pygame.draw.rect(surface, (200, 170, 0), 
                    (screen_x - int(10 * scale), screen_y - int(53 * scale), int(20 * scale), int(8 * scale)), 2)
    pygame.draw.rect(surface, (255, 240, 150), 
                    (screen_x - int(8 * scale), screen_y - int(52 * scale), int(16 * scale), int(6 * scale)), 1)
    
    # Left arm (holding sack)
    pygame.draw.circle(surface, (200, 20, 20), 
                      (screen_x - int(30 * scale), screen_y - int(60 * scale)), int(10 * scale))
    pygame.draw.line(surface, (200, 20, 20), 
                    (screen_x - int(25 * scale), screen_y - int(65 * scale)),
                    (sack_x + int(10 * scale), sack_y - int(40 * scale)), int(8 * scale))
    
    # Left hand (black glove)
    pygame.draw.circle(surface, (40, 40, 40), 
                      (sack_x + int(10 * scale), sack_y - int(40 * scale)), int(8 * scale))
    
    # Right arm (waving) - animated
    wave_angle = math.sin(wave_offset) * 0.4
    arm_end_x = screen_x + int(35 * scale) + int(math.cos(wave_angle) * 15 * scale)
    arm_end_y = screen_y - int(85 * scale) - int(math.sin(wave_angle + 0.5) * 10 * scale)
    
    pygame.draw.circle(surface, (200, 20, 20), 
                      (screen_x + int(25 * scale), screen_y - int(65 * scale)), int(10 * scale))
    pygame.draw.line(surface, (200, 20, 20), 
                    (screen_x + int(25 * scale), screen_y - int(70 * scale)),
                    (arm_end_x, arm_end_y), int(8 * scale))
    
    # Right hand (black glove) - waving
    hand_angle = wave_angle + 0.3
    pygame.draw.circle(surface, (40, 40, 40), (int(arm_end_x), int(arm_end_y)), int(10 * scale))
    
    # Fingers waving
    for i in range(3):
        finger_offset = math.sin(wave_offset + i * 0.3) * 5
        pygame.draw.circle(surface, (40, 40, 40), 
                         (int(arm_end_x + (i - 1) * 5), int(arm_end_y - 8 + finger_offset)), 
                         int(3 * scale))
    
    # Head (peach/skin color)
    head_center_x = screen_x
    head_center_y = screen_y - int(90 * scale)
    pygame.draw.circle(surface, (255, 220, 190), (head_center_x, head_center_y), int(18 * scale))
    
    # Ears
    pygame.draw.circle(surface, (240, 200, 170), 
                      (head_center_x - int(16 * scale), head_center_y), int(6 * scale))
    pygame.draw.circle(surface, (240, 200, 170), 
                      (head_center_x + int(16 * scale), head_center_y), int(6 * scale))
    
    # Santa hat
    hat_points = [
        (head_center_x - int(18 * scale), head_center_y - int(8 * scale)),
        (head_center_x - int(12 * scale), head_center_y - int(30 * scale)),
        (head_center_x + int(5 * scale), head_center_y - int(35 * scale)),
        (head_center_x + int(20 * scale), head_center_y - int(8 * scale))
    ]
    pygame.draw.polygon(surface, (200, 20, 20), hat_points)
    pygame.draw.polygon(surface, (160, 15, 15), hat_points, 2)
    
    # Hat white trim
    pygame.draw.ellipse(surface, (255, 255, 255), 
                       (head_center_x - int(20 * scale), head_center_y - int(12 * scale), 
                        int(40 * scale), int(10 * scale)))
    
    # Hat pom-pom
    pom_x = head_center_x + int(8 * scale)
    pom_y = head_center_y - int(35 * scale)
    pygame.draw.circle(surface, (255, 255, 255), (pom_x, pom_y), int(6 * scale))
    pygame.draw.circle(surface, (240, 240, 240), (pom_x, pom_y), int(6 * scale), 1)
    
    # Beard
    beard_points = [
        (head_center_x - int(16 * scale), head_center_y - int(5 * scale)),
        (head_center_x - int(18 * scale), head_center_y + int(8 * scale)),
        (head_center_x - int(12 * scale), head_center_y + int(15 * scale)),
        (head_center_x, head_center_y + int(18 * scale)),
        (head_center_x + int(12 * scale), head_center_y + int(15 * scale)),
        (head_center_x + int(18 * scale), head_center_y + int(8 * scale)),
        (head_center_x + int(16 * scale), head_center_y - int(5 * scale)),
        (head_center_x + int(10 * scale), head_center_y + int(5 * scale)),
        (head_center_x - int(10 * scale), head_center_y + int(5 * scale))
    ]
    pygame.draw.polygon(surface, (255, 255, 255), beard_points)
    pygame.draw.polygon(surface, (230, 230, 230), beard_points, 2)
    
    # Mustache
    pygame.draw.ellipse(surface, (255, 255, 255), 
                       (head_center_x - int(15 * scale), head_center_y - int(3 * scale), 
                        int(12 * scale), int(8 * scale)))
    pygame.draw.ellipse(surface, (255, 255, 255), 
                       (head_center_x + int(3 * scale), head_center_y - int(3 * scale), 
                        int(12 * scale), int(8 * scale)))
    
    # Nose
    pygame.draw.circle(surface, (255, 180, 160), 
                      (head_center_x, head_center_y - int(2 * scale)), int(5 * scale))
    pygame.draw.circle(surface, (255, 200, 180), 
                      (head_center_x - int(2 * scale), head_center_y - int(3 * scale)), int(2 * scale))
    
    # Eyes (closed/happy)
    pygame.draw.arc(surface, (80, 50, 30), 
                   (head_center_x - int(12 * scale), head_center_y - int(10 * scale), 
                    int(8 * scale), int(6 * scale)), 0, math.pi, 3)
    pygame.draw.arc(surface, (80, 50, 30), 
                   (head_center_x + int(4 * scale), head_center_y - int(10 * scale), 
                    int(8 * scale), int(6 * scale)), 0, math.pi, 3)
    
    # Rosy cheeks
    cheek_surface = pygame.Surface((int(12 * scale), int(12 * scale)), pygame.SRCALPHA)
    pygame.draw.circle(cheek_surface, (255, 150, 150, 80), (int(6 * scale), int(6 * scale)), int(6 * scale))
    surface.blit(cheek_surface, (head_center_x - int(20 * scale), head_center_y + int(2 * scale)))
    surface.blit(cheek_surface, (head_center_x + int(8 * scale), head_center_y + int(2 * scale)))
    
    # Add sparkles around Santa for magic
    random.seed(888)
    for _ in range(8):
        spark_angle = random.uniform(0, math.pi * 2)
        spark_dist = random.uniform(40, 60) * scale
        spark_x = int(screen_x + math.cos(spark_angle) * spark_dist)
        spark_y = int(screen_y - 60 * scale + math.sin(spark_angle) * spark_dist)
        spark_size = random.choice([2, 3])
        
        pygame.draw.circle(surface, (255, 255, 200), (spark_x, spark_y), spark_size)
        pygame.draw.line(surface, (255, 255, 255), (spark_x - spark_size*2, spark_y), 
                        (spark_x + spark_size*2, spark_y), 1)
        pygame.draw.line(surface, (255, 255, 255), (spark_x, spark_y - spark_size*2), 
                        (spark_x, spark_y + spark_size*2), 1)

# Create snow particles
snow_particles = [SnowParticle() for _ in range(700)]

# Start music once
start_music()

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update animation frame
    animation_frame += 0.08
    
    # Draw gradient sky with stars
    draw_gradient_sky(screen)
    
    # Draw snowy ground
    draw_snowy_ground(screen)
    
    # Draw tree shadows (world coordinates)
    draw_tree_shadow(screen, -280, -400, 1.1)
    draw_tree_shadow(screen, 80, -400, 1.3)
    
    # Draw trees (world coordinates)
    draw_realistic_tree(screen, -280, -400, 1.1, 0)
    draw_realistic_tree(screen, 80, -400, 1.3, 100)
    
    # Bring house to foreground (front) on the left side
    draw_cozy_house(screen, -380, -400, 0.95, animation_frame)

    # Sleigh with reindeer — resting on snowy ground at right
    draw_sleigh_team(screen, 260, -370, scale=0.7, phase=animation_frame)

    # Draw Santa Claus waving in the center
    draw_santa(screen, -100, -370, animation_frame)
    
    # Draw presents under trees
    draw_present(screen, -320, -430, 40, 35, (200, 20, 20), GOLD)
    draw_present(screen, -270, -435, 35, 30, GREEN, RED)
    draw_present(screen, -240, -432, 28, 25, (20, 100, 200), (255, 215, 0))
    
    draw_present(screen, 30, -438, 45, 38, (220, 30, 30), (0, 180, 0))
    draw_present(screen, 85, -442, 38, 32, (255, 215, 0), RED)
    draw_present(screen, 130, -440, 32, 28, (150, 0, 200), (255, 255, 100))
    draw_present(screen, 105, -420, 25, 22, (20, 150, 220), (200, 0, 0))

    # Snowman near the right tree
    draw_snowman(screen, 180, -420, 0.9, animation_frame)
    
    # Draw Merry Christmas banner
    draw_merry_christmas_banner(screen)
    
    # Update and draw snow with gentle global wind for uniform motion
    wind_dx = math.sin(animation_frame * 0.25) * 0.06
    for particle in snow_particles:
        particle.update(wind_dx)
        particle.draw(screen)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

if pygame.mixer.get_init():
    pygame.mixer.music.stop()
    pygame.mixer.quit()
pygame.quit()
