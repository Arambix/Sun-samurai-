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

# Function to draw the background
def draw_bg():
    screen.fill(red)
    screen.blit(scle, (0,0))

#game state initilaized
class mainmenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

        
        
        


        pos = 0
    comic_sans = pygame.font.SysFont("comic sans MS", 30)
    def drawmsge(self, msge, comic_sans,message_colour, x,y): # this will display the message on the main menu screen so like play now
        img = comic_sans.render(msge, True, message_colour)
        img_rect = img.get_rect(topleft=(x, y))
        return img, img_rect
    

    def playbutton(self):
        white = (225,225,225)
        img,img_rectangle = self.drawmsge("  PLAY   ", self.comic_sans, white, 350,300)
        play_rectangle = img_rectangle.inflate(20, 30)# this is used to create a bigger rectangle than the orginal rectangle so
        pygame.draw.rect(self.screen, (0, 0, 0), play_rectangle, 2)
        screen.blit(img, img_rectangle)
        
        return play_rectangle
    def quitbutton(self):
        white = (225,225,225)
        img,img_rectangle = self.drawmsge("  QUIT  ", self.comic_sans, white, 350,400)
        quit_rectangle = img_rectangle.inflate(20, 30)# this is used to create a bigger rectangle than the orginal rectangle so
        pygame.draw.rect(self.screen, (0, 0, 0), quit_rectangle, 2)
        screen.blit(img, img_rectangle)
        return quit_rectangle
    
    def collision(self):
        play_rectangle = self.playbutton()
        quit_rectangle = self.quitbutton()
        mouse_pos = pygame.mouse.get_pos()
        self.play_collision = play_rectangle.collidepoint(mouse_pos)
        if self.play_collision == True:
            pygame.draw.rect(self.screen, (0, 0, 0, 100), play_rectangle)
        quit_rectangle = quit_rectangle.collidepoint(mouse_pos)
        if quit_rectangle == True:
            pygame.draw.rect(self.screen, (0, 0, 0, 100), quit_rectangle)

class levels:
    def __init__(self, screen):
        self.screen = screen
        self.menu = main_menu
    
    def faded_text(self, duration ,msge, comic_sans,message_colour, x,y):
        fade_surface = pygame.Surface((scrn_width, scrn_height))
        fade_surface.fill((0,0,0)) #filling the screen with black
        text = comic_sans.render(msge, True, message_colour)
     # this is used for how long the screen will be black for 
        start = pygame.time.get_ticks()
        end = 0
        
        while end < duration:
            end = pygame.time.get_ticks() - start
            transparent = min(255, int((end/duration) *255))
            fade_surface.set_alpha(transparent)
            self.screen.blit(fade_surface, (0,0))
            self.screen.blit(text, (x,y))
            pygame.display.update()
            pygame.time.wait(10)
            
              

# Character class definition
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
        dx = 0  # Change in x position
        dy = 0  # Change in y position

        # Check for left movement
        if move_lft:
            dx = -self.speed  # Move left
            self.flip = True  # Flip the sprite for left movement
            self.direction = -1  # Update direction
        # Check for right movement
        if move_rgt:
            dx = self.speed  # Move right
            self.flip = False  # No flip for right movement
            self.direction = 1  # Update direction
        
        if self.jump == True and self.air == False:
            self.velocitY = -15
            self.jump = False 
           
        
        #adding gravity so my player doesnt just fly off the screen
        self.velocitY += gravity
        if self.velocitY > 10:
            self.velocitY
        dy += self.velocitY

        if self.rect.bottom + dy > 550:
            dy = 550 - self.rect.bottom 
            self.air = False
            
        
        # Update rectangle position based on movement
        self.rect.x += dx
        self.rect.y += dy
        global screen_scroll
        #camera tracker
        #if  self.pp :
            #if self.rect.right > scrn_width - scroll_limit or self.rect.left < scrn_width + scroll_limit:
                #self.rect.x -= dx
                #screen_scroll = -dx

        return screen_scroll
    def update_animation(self):
        # Update animation based on action
        anim_cldwn = 120  # Default animation cooldown
        if self.action == 2:  # Punch action
            anim_cldwn = 10  # Faster cooldown for punch
        elif self.action == 3:  # Sword jab action
            anim_cldwn = 10  # Faster cooldown for sword jab
        elif self.action == 5:  # Ultimate action
            anim_cldwn = 100  # Slower cooldown for ultimate
        elif self.action == 4:  # Slash action
            anim_cldwn = 100  # Faster cooldown for slash
        
        # Update current sprite depending on the action and frame index
        self.sprites = self.anim_list[self.action][self.frame_index]  # Get the current sprite
        # Check if it's time to update the frame
        if pygame.time.get_ticks() - self.update_time > anim_cldwn:
            self.update_time = pygame.time.get_ticks()  # Reset the update time
            self.frame_index += 1  # Move to the next frame
        
        # Reset frame index if it exceeds the number of frames for the current action
        if self.frame_index >= len(self.anim_list[self.action]):
            self.frame_index = 1  # Reset to the second frame to loop the animation
    
    def updte_action(self, new_action):
        # Change action if it's different from the current one
        if new_action != self.action:
            self.action = new_action  # Update to new action
            self.frame_index = 0  # Reset frame index to the first frame
            self.update_time = pygame.time.get_ticks()  # Reset update time
    
    def collision(self, enemy):
        # Check collision with platforms
        if self.rect.colliderect(enemy.rect):
            if self.action in [2,4,5,6]:
                skeleton.updte_action(3)
                skeleton1.updte_action(3)

                enemy_group.remove(skeleton,skeleton1)  # This code indicates which animations cause a collision effect on the enemy so I have just added the attack animations from the main player to the enemy so it dies
                print('enemy is dead')
    def collectcol(self, collectables):
            if self.rect.colliderect(collectables.rect):
                if self.action:
                    self.health = 100 # if the player collides with this their health will go to to 100 no matter what health they are currently at 
                    print('there is a collision for power ups')
                    collectables_group.remove(firepower)
            
         
    def damages(self, enemy):
        # deal damaage to the enemy
        if  self.rect.colliderect(enemy.rect) :
            if self.action in [2,4,5,6]:
                skeleton.health -= 10 
                
                print('enemy is damaged')
                if skeleton.health <= 0:
                    self.score = 10
                    skeleton.updte_action(3)
                    enemy_group.remove(skeleton)
                skeleton1.health -= 10 
               
                print('enemy is damaged')
                if skeleton1.health <= 0:
                    self.score = 10
                    skeleton1.updte_action(3)
                    enemy_group.remove(skeleton1)
        # deal damage to the player 
        if self.rect.colliderect(enemy.rect):
            if self.action in [1,2,4,5,6]:
                self.health -= 1
                print('player is damaged')
                

    def healthbar(self, x,y, current_health):
         bar_width = 200 # size 
         bar_height = 20 # size
         current_health = max(0, self.health )
         fill_width = (current_health/self.start_health)* bar_width #shows the aftermath of getting hit by the enemy
         bar_dim = pygame.Rect(x,y, bar_width, bar_height)
         fill_bar_colour = pygame.Rect(x,y, fill_width, bar_height)
         # displaying the bar and its colour
         pygame.draw.rect(screen, (255,0,0), bar_dim) #starting health
         pygame.draw.rect(screen, (0,255,0), fill_bar_colour) # once hit shows red
         # drawing the health text to indicate what they start with and their current
         font = pygame.font.Font(None, 25)
         htext = font.render(f'HEALTH: {current_health}', True, (255,255,255))
         screen.blit(htext, (x, y - 20)) #  displays text above the health bar 
    def scoreboard(self, x,y):
        # display the score
        font = pygame.font.Font(None, 25)
        score_text = font.render(f'SCORE: {self.score}', True, (255,255,255))
        screen.blit(score_text,(x,y - 20))
        

    def draw(self):
        # Draw the current sprite on the screen
        screen.blit(pygame.transform.flip(self.sprites, self.flip, False), self.rect)  # Flip sprite if needed
    
#enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, idle, walk, attack, dead, x, y, scale ,speed, steps_limit=50):
        pygame.sprite.Sprite.__init__(self)  
        self.Ealive = True
        self.health = 50 
        self.walk = walk #constructor for calling images from their paths
        self.idle = idle
        self.attack = attack
        self.speed = speed
        self.step_lim = steps_limit # this is the maximum amount of steps the enemy can take before flipping 
        self.step_counter = 0 # this is used for counting how many steps the enemy takes before it flips
        self.dead = dead
        self.direction = 1 
        self.flip = False
        self.anim_list = []
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        # Load idle animation
        #idle
        templst = []  # Temporary list for animation frames
        for i in range(1):
            sprites = pygame.image.load(f'img/sidle/{self.idle}{i}.png')  # Load idle sprites
            sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))  # Scale the sprite
            pygame.Surface.convert_alpha(sprites)  # Convert surface for transparency
            templst.append(sprites)  # Add sprite to the temporary list
        self.anim_list.append(templst)  # Add idle animation list to the main animation list
        
        # Load walk animation
        #walk
        templst = []  # Temporary list for animation frames
        for i in range(8):
            sprites = pygame.image.load(f'img/walk/{self.walk}{i}.png')  # Load idle sprites
            sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))  # Scale the sprite
            pygame.Surface.convert_alpha(sprites)  # Convert surface for transparency
            templst.append(sprites)  # Add sprite to the temporary list
        self.anim_list.append(templst)  # Add idle animation list to the main animation list
         # Load idle animation
        #attack
        templst = []  # Temporary list for animation frames
        for i in range(6):
            sprites = pygame.image.load(f'img/sattack/{self.attack}{i}.png')  # Load idle sprites
            sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))  # Scale the sprite
            pygame.Surface.convert_alpha(sprites)  # Convert surface for transparency
            templst.append(sprites)  # Add sprite to the temporary list
        self.anim_list.append(templst)  # Add idle animation list to the main animation list
        
        templst = []  # Temporary list for animation frames
        for i in range(3):
            sprites = pygame.image.load(f'img/Dead/{self.dead}{i}.png')  # Load dead sprites
            sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))  # Scale the sprite
            pygame.Surface.convert_alpha(sprites)  # Convert surface for transparency
            templst.append(sprites)  # Add sprite to the temporary list
        self.anim_list.append(templst)  # Add idle animation list to the main animation list
        
        
        # Initialize sprite and rectangle for collision detection
        self.image = self.anim_list[self.action][self.frame_index]  # Set the initial sprite
        self.rect = self.image.get_rect()  # Create a rectangle around the sprite for positioning
        self.rect.center = (x, y)  # Set the rectangle's center position
        
    def update_animation(self):
        # Set animation cooldown
        anim_cldwn = 100
        # Update current sprite
        self.sprites = self.anim_list[self.action][self.frame_index]
        # Check if it's time to update the frame
        if pygame.time.get_ticks() - self.update_time > anim_cldwn:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # Reset frame index if it exceeds the number of frames
        if self.frame_index >= len(self.anim_list[self.action]):
            if self.action == 3:  # If the action is "dead," stop at the last frame
                self.frame_index = len(self.anim_list[self.action]) - 1
            else:
                self.frame_index = 0  # Reset for looping animations
        self.image = self.anim_list[self.action][self.frame_index]
    def updte_action(self, new_action):
        # Change action if it's different from the current one
        if new_action != self.action:
            self.action = new_action  # Update to new action
            self.frame_index = 0  # Reset frame index to the first frame
            self.update_time = pygame.time.get_ticks()  # Reset update time

    
    def move(self):
        self.rect.x += self.speed * self.direction
        self.step_counter += 1
        
        if self.step_counter >= self.step_lim:
            self.direction *= -1
            self.flip = not self.flip
            self.step_counter = 0 # reset counter
        
           
    def ai(self,player):
        if self.Ealive:
            distance_from_player = abs(self.rect.x - player.rect.x)
            attack_range = 100
            if distance_from_player < attack_range:
                self.updte_action(2)  # Change action to attack
                print("enemy has attacked")
            else:
                if self.rect.centerx < player.rect.centerx:
                    self.direction = 1
                else:
                    self.direction = -1
                self.move()
                self.updte_action(1)
    
    

    def update(self, player):
        self.update_animation()
        self.ai(player) 

    def draw(self):
        # Draw the current sprite on the screen
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)  # Flip sprite if needed

class collectables(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(f'img/collectables/{image}')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def load_image(self,):    
        
        image = pygame.transform.scale(self.image,(50,50))
        screen.blit(image, (self.rect.x, self.rect.y))
# instance


skeleton = Enemy('sidle','sw', 'sa','Dead',550, 450, 2, 2)
skeleton1 = Enemy('sidle','sw', 'sa','Dead',650, 450, 2, 2)
skeleton2 = Enemy('sidle','sw', 'sa', 'Dead', 50, 350, 2, 2)
player = mainplayer('tanjiro_idle', 'tanjiro_run', 'tanjiro_punch', 'tanjiro_slash', 'tanjiro_s', 'tanjiro_ultimate', 'tanjiro_water', 100, 200, 3, 5, skeleton)
firepower = collectables(400,400,"fp.png")
main = mainmenu(screen)
level1 = levels(screen)
gameover = levels(screen)
enemy_group = pygame.sprite.Group()#this is a group to hold all the enemies
enemy_group.add(skeleton,skeleton1)
collectables_group = pygame.sprite.Group()
collectables_group.add(firepower)

run = True  # Main game loop flag
while run:
    clock.tick(FPS)  # Control the frame rate
    # game state implemented
    if main_menu == True:
        screen.fill(blue)
        #draw the main menu buttons
        play_rect= main.playbutton()
        quit_rect= main.quitbutton()
        #the positions of the mouse
        mouse_position = pygame.mouse.get_pos()
        #making this variable for calling it quicker
        # making my variables
        pcol = play_rect.collidepoint(mouse_position)
        pressplay = pygame.mouse.get_pressed()[0]
        qcol = quit_rect.collidepoint(mouse_position)
        pressquit = pygame.mouse.get_pressed()[0]
        if pcol:
            pygame.draw.rect(screen,(0,0,0, 100), play_rect)
            if pressplay == True:
                main_menu = False
            if not main_menu:
               
               level1.faded_text(2500, "Level 1", pygame.font.SysFont("comic sans", 30), (200, 200, 200), 350, 300)
            
              

        if qcol:
            pygame.draw.rect(screen,(0,0,0, 100), quit_rect)
            if pressquit == True:
                run = False
        
       

    else:


        
        draw_bg()   
        
        
        
        for enemy in enemy_group:
            skeleton.update(player)    
            skeleton.draw()
            skeleton1.update(player)
            skeleton1.draw()
                
            


        
        
        
        #tanjiro instance
        player.draw()  # Draw the player character
        player.healthbar(50,50,1000)
        player.scoreboard(500,50)
        player.update_animation()  # Update the player's animation
        player.damages(skeleton1)
        player.damages(skeleton)
        player.collectcol(firepower)
        screen_scroll = player.move(move_rgt, move_lft)  # Move the player based on input
        firepower.load_image()
        
        if player.health == 0:
            gameover.faded_text(900, "game over", pygame.font.SysFont("comic sans", 30), (200, 200, 200), 350, 300)
            
            
            
        
        if len(enemy_group) ==  0: # if enemies have been removed then switch to next level
            if current_level ==1:
                current_level = 2
                level1.faded_text(900,"Level 2", pygame.font.SysFont('comic sans', 36), (200,200,200), 350, 300)
                player.health = 100
                # Add new enemies for Level 2
                skeleton = Enemy('sidle', 'sw', 'sa', 'Dead', 600, 350, 2, 2)
                new_enemy2 = Enemy('sidle', 'sw', 'sa', 'Dead', 300, 350, 2, 2)
                enemy_group.add(skeleton, skeleton1)

                player.damages(skeleton)
                player.damages(skeleton1)
                
        

    for event in pygame.event.get():  # Handle events
        
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pcol == (mouse_position):
                    main_menu = False
        
                    

                
       
                    
        
        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Move left
                move_lft = True
                print("player is moving left a")
            if event.key == pygame.K_d:  # Move right
                move_rgt = True
                print("player is moving right")
            if event.key == pygame.K_w and player.alive: 
                player.jump = True 
                print("player is jumping")
            if event.key == pygame.K_ESCAPE:  # Exit game
                run = False
                print("player has left the game")
            if event.key == pygame.K_e:  # Action punch
                e = True
                print("player has used punch")
            if event.key == pygame.K_z:  # Action z
                z = True
                print("player has used a special move")
            if event.key == pygame.K_x:  # Action x
                x = True
                print("player has used another special move")
        
        
        # Handle key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and player.alive:  # Stop moving left
                move_lft = False
            if event.key == pygame.K_d and player.alive:  # Stop moving right
                move_rgt = False
            if event.key == pygame.K_e and player.alive:  # Stop action e
                e = False
            if event.key == pygame.K_z and player.alive:  # Stop action z
                z = False
            if event.key == pygame.K_x and player.alive:  # Stop action x
                x = False

        # Handle mouse button presses
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button pressed
                lft_clck = True
            if event.button == 3:  # Right mouse button pressed
                rgt_clck = True
                print("player has use a slash")

        # Handle mouse button releases
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button released
                lft_clck = False
            if event.button == 3:  # Right mouse button released
                rgt_clck = False
    if player.alive:
        # Update player action based on inputs
        if player.air:
            player.updte_action(1) #jumping 
        if e:  # If action e is active
            player.updte_action(2)
        elif z:  # If action z is active
            player.updte_action(5)
        elif x:  # If action x is active
            player.updte_action(6)
        elif lft_clck:  # If left mouse button is clicked
            player.updte_action(3)
        elif rgt_clck:  # If right mouse button is clicked
            player.updte_action(4)
        elif move_lft or move_rgt:  # If moving left or right
            player.updte_action(1)
        else:  # If no movement or action, set to idle
            player.updte_action(0)
        
        print(screen_scroll)
    pygame.display.update()  # Update the display

pygame.quit()  # Quit the game
