import pygame
from pygame import mixer  # Import the mixer module for sound effects
from random import randint
pygame.init()  # Initialize all pygame modules

# Set up screen dimensions
scrn_width = 800  # Width of the display
scrn_height = int(scrn_width * 0.8)  # Height calculated based on width

# Create the display window
screen = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption('sun slayers')  # Set the window title

# Set the framerate
clock = pygame.time.Clock()  # Create a clock object to manage the game's frame rate
FPS = 60  # Desired frames per second

# Background music setup
mixer.music.load('if.wav')  # Load the background music file
mixer.music.play(-1)  # Play the music indefinitely
mixer.music.pause()
# My constant Game variables
current_level = 1
gravity = 0.5  # Gravity value for character movement
scroll_limit = 200  # Limit for scrolling background
rows = 16  # Number of rows in the game grid
cols = 150  # Number of columns in the game grid
screen_scroll = 0  # Variable for background scrolling
bg_scroll = 0  # Variable for controlling background scroll speed
p_positon = [400,300] # the players initial position
camera = [0,0] #this will be used to track the background and the player together
# Player action variables
move_lft = False  # Movement flags for left and right
move_rgt = False
rgt_clck = False  # Right mouse button flag
lft_clck = False  # Left mouse button flag
e = False  # Flag for action e
z = False  # Flag for action z
x = False  # Flag for action x

#game states:
main_menu = True

# Load background image and scale it
bg = pygame.image.load('img/bg/background.png')  # Load background image
scle = pygame.transform.scale(bg, (800, 640))  # Scale background image to fit screen
pos = 0  # Position for background scrolling


red =(225,0,0)
blue = (0,0, 220)
white = (225,225,225)
message_colour = white


class mainplayer(pygame.sprite.Sprite):
    def __init__(self, idle, run, punch, swrdjab, slash, ultimate, water, x, y, scale, speed, Enemy):
        pygame.sprite.Sprite.__init__(self)  # Initialize the parent Sprite class
        # Initialize character type attributes
        self.alive = True
        self.health = 100 #limit of health points
        self.start_health = 100 # the starting health
        self.score = 0
        self.idle = idle
        self.run = run
        self.punch = punch
        self.swrdjab = swrdjab
        self.slash = slash
        self.ultimate = ultimate
        self.char_type_water = water
        self.speed = speed  # Set the character's speed
        self.direction = 1  # Direction the character is facing
        self.jump = False
        self.air = True
        self.velocitY = 0
        self.flip = False  # Flip attribute for character sprite
        self.anim_list = []  # List to hold different animations
        self.frame_index = 0  # Current frame index for animation
        self.action = 0  # Current action of the character
        self.update_time = pygame.time.get_ticks()  # Initialize the update time
        self.Enemy = Enemy
        # Load idle animation
        templst = []  # Temporary list for animation frames
        for i in range(2):
            sprites = pygame.image.load(f'img/idle/{self.idle}{i}.png')  # Load idle sprites
            sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))  # Scale the sprite
            pygame.Surface.convert_alpha(sprites)  # Convert surface for transparency
            templst.append(sprites)  # Add sprite to the temporary list
        self.anim_list.append(templst)  # Add idle animation list to the main animation list
        
        # Load run animation
        templst = []  # Reset temporary list
        for i in range(6):
            sprites = pygame.image.load(f'img/run/{self.run}{i}.png')  # Load run sprites
            sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))  # Scale the sprite
            templst.append(sprites)  # Add sprite to the temporary list
        self.anim_list.append(templst)  # Add run animation list to the main animation list
        
        # Load punch animation
        templst = []  # Reset temporary list
        for i in range(2):
            sprites = pygame.image.load(f'img/punch/{self.punch}{i}.png')  # Load punch sprites
            sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))  # Scale the sprite
            templst.append(sprites)  # Add sprite to the temporary list
        self.anim_list.append(templst)  # Add punch animation list to the main animation list
        
        # Load sword jab animation
        templst = []  # Reset temporary list
        for i in range(2):
            sprites = pygame.image.load(f'img/swrdjab/{self.swrdjab}{i}.png')  # Load sword jab sprites
            sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))  # Scale the sprite
            templst.append(sprites)  # Add sprite to the temporary list
        self.anim_list.append(templst)  # Add sword jab animation list to the main animation list
        
        # Load slash animation
        templst = []  # Reset temporary list
        for i in range(6):
            sprites = pygame.image.load(f'img/slash/{self.slash}{i}.png')  # Load slash sprites
            sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))  # Scale the sprite
            templst.append(sprites)  # Add sprite to the temporary list
        self.anim_list.append(templst)  # Add slash animation list to the main animation list
        
        # Load ultimate animation
        templst = []  # Reset temporary list
        for i in range(7):
            sprites = pygame.image.load(f'img/ultimate/{self.ultimate}{i}.png')  # Load ultimate sprites
            sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))  # Scale the sprite
            templst.append(sprites)  # Add sprite to the temporary list
        self.anim_list.append(templst)  # Add ultimate animation list to the main animation list
        
        # Load water animation
        templst = []  # Reset temporary list
        for i in range(9):
            sprites = pygame.image.load(f'img/water/{self.char_type_water}{i}.png')  # Load water sprites
            sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))  # Scale the sprite
            templst.append(sprites)  # Add sprite to the temporary list
        self.anim_list.append(templst)  # Add water animation list to the main animation list
        
        # Initialize sprite and rectangle for collision detection
        self.sprites = self.anim_list[self.action][self.frame_index]  # Set the initial sprite
        self.rect = self.sprites.get_rect()  # Create a rectangle around the sprite for positioning
        self.pp = self.rect.center = (x, y)  # Set the rectangle's center position

    def move(self, move_rgt, move_lft):
        dx = 0
        dy = 0

        if move_lft:
            dx = -self.speed
            self.flip = True
        if move_rgt:
            dx = self.speed
            self.flip = False

        if self.jump and not self.air:
            self.velocitY = -15
            self.jump = False
            self.air = True

        self.velocitY += gravity
        dy += self.velocitY

        if self.rect.bottom + dy > scrn_height - 50:
            dy = scrn_height - 50 - self.rect.bottom
            self.air = False

        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        anim_cldwn = 120
        self.image = self.anim_list[self.action][self.frame_index]

        if pygame.time.get_ticks() - self.update_time > anim_cldwn:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.anim_list[self.action]):
            self.frame_index = 0

    def updte_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def healthbar(self, x, y):
        bar_width = 200
        current_health = max(0, self.health)
        fill_width = (current_health / self.start_health) * bar_width

        pygame.draw.rect(screen, (255, 0, 0), (x, y, bar_width, 20))
        pygame.draw.rect(screen, (0, 255, 0), (x, y, fill_width, 20))

    def draw(self):
        screen.blit(pygame.transform.flip(self.sprites, self.flip, False), self.rect)


# Player Instance
player = mainplayer('tanjiro_idle', 'tanjiro_run', 'tanjiro_punch', 'tanjiro_slash', 'tanjiro_s', 'tanjiro_ultimate', 'tanjiro_water', 400, 300, 3, 5, None)

run = True
move_lft = False
move_rgt = False
e = False
z = False
x = False

while run:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    player.draw()
    player.healthbar(50, 50)
    player.update_animation()
    player.move(move_rgt, move_lft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_lft = True
                player.updte_action(1)
            if event.key == pygame.K_d:
                move_rgt = True
                player.updte_action(1)
            if event.key == pygame.K_w:
                player.jump = True
            if event.key == pygame.K_e:
                e = True
                player.updte_action(2)
            if event.key == pygame.K_z:
                z = True
                player.updte_action(5)
            if event.key == pygame.K_x:
                x = True
                player.updte_action(6)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_lft = False
            if event.key == pygame.K_d:
                move_rgt = False
            if event.key in [pygame.K_e, pygame.K_z, pygame.K_x]:
                player.updte_action(0)

    pygame.display.update()

pygame.quit()