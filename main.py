import pygame
from pygame import mixer # this is for the music and sound effects
pygame.init()

scrn_width = 1000 # this is how wide the display screen will be
scrn_height = 740 # this is how tall the display screen will be

screen = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption('sun samurai') # the name of display
#bg music
mixer.music.load('if.wav') # the background music
mixer.music.play(1)
# Set the framerate
clock = pygame.time.Clock()
FPS = 360
x = 200
y = 200
scale = 3
# Player movement
move_lft = False
move_rgt = False
rgt_clck = False
lft_clck = False
e = False
z = False
x = False


def bg():
    screen.fill((200, 50, 0))

class Chars(pygame.sprite.Sprite):
    def __init__(self, char_type, img_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.img_type = img_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.anim_list = []
        self.frame_index = 0
        self.action = 0  # Start with idle
        self.time_udpate = pygame.time.get_ticks()

        self.rectangle = pygame.Rect(x, y, 50, 50)  # Default size; adjust as needed
        self.load_animations(scale)

    def load_animations(self, scale):
        # Create a list of animations: index 0 for idle, 1 for run
        self.anim_list = [
            [],  # Idle animations
            []   # Run animations
        ]

        # Load idle animations
        for i in range(2):  # Assuming idle images are char_type0.png and char_type1.png
            img = pygame.image.load(f'img/{self.img_type}/{self.char_type}{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
            self.anim_list[0].append(img)

        # Load run animations
        for i in range(6):  # Assuming run images are char_type2.png to char_type7.png
            img = pygame.image.load(f'img/{self.img_type}/{self.char_type}{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
            self.anim_list[1].append(img)
    
    def move(self, move_rgt, move_lft):
        # I have made dx and dy because d meansaaaaa change in so if there is a change in x reset it to 0
        dx = 0
        dy = 0

        if move_lft:
           dx = -self.speed
           self.flip = True
           self.direction = -1      
        if move_rgt:
            dx = self.speed
            self.flip = False
            self.direction = 1
        # Updating rectangle
        self.rectangle.x += dx
        self.rectangle.y += dy
    

    def update_movement(self):
        movement_cooldown = 100
        self.sprites = self.anim_list[self.action][self.frame_index]

        if pygame.time.get_ticks() - self.time_udpate > movement_cooldown:
            self.time_udpate = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.anim_list[self.action]):
            self.frame_index = 0

    def updte_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.time_udpate = pygame.time.get_ticks()

    def print(self, screen):
        screen.blit(pygame.transform.flip(self.sprites, self.flip, False), self.rectangle)



main = Chars('tanjiro_run','run',200,300,3,2) # in this code 'main' is the instance variable 


#to keep my game running I need to use a while loop
running = True
while running:
    
    
    bg()   
    main.update_movement()
    main.print(screen)
    main.move(move_rgt,move_lft)
    pygame.display.update()
    
    
    
    for event in pygame.event.get(): #  this is going to give me a record of what i do and it will register it like click the mouse button
        if event.type == pygame.QUIT:
            running = False
     

        # When the keys are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_lft = True
            if event.key == pygame.K_d:
                move_rgt = True
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_e:
                e = True
            if event.key == pygame.K_z:
                z = True
            if event.key == pygame.K_x:
                x = True

        # Button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_lft = False
            if event.key == pygame.K_d:
                move_rgt = False
            if event.key == pygame.K_e:
                e = False
            if event.key == pygame.K_z:
                z = False
            if event.key == pygame.K_x:
                x = False

        # Mouse button press
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                lft_clck = True
            if event.button == 3:
                rgt_clck = True

        # Mouse button release
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                lft_clck = False
            if event.button == 3:
                rgt_clck = False

    #Update action
        if e:
          main.updte_action(2)
        elif z:
           main.updte_action(5)
        elif x:
           main.updte_action(6)
        elif lft_clck:
           main.updte_action(3)
        elif rgt_clck:
           main.updte_action(4)
        elif move_rgt or move_lft:
           main.updte_action(1)
        else:
           main.updte_action(0)
    #screen_scroll = player.move(move_rgt, move_lft)
    #print(screen_scroll)
    pygame.display.update()


    
pygame.quit()