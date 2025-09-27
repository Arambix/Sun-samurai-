import pygame
from pygame import mixer
pygame.init()

scrn_width = 1000
scrn_height = 740

screen = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption('sun slayers')
#bg music
mixer.music.load('if.wav')
mixer.music.play(-1)
# Set the framerate
clock = pygame.time.Clock()
FPS = 360

# Game variables
gforce = 0.75
scroll_limit = 200
rows = 16
cols = 150
screen_scroll = 0
bg_scroll = 0j

# Player movement
move_lft = False
move_rgt = False
rgt_clck = False
lft_clck = False
e = False
z = False
x = False

bg = pygame.image.load('img/bg/background.png')
scle = pygame.transform.scale(bg, (800, 640))
pos = 0

def draw_bg():
    global pos
    screen.fill((0, 0, 0))
    screen.blit(scle, (pos, 0))
    screen.blit(scle, (scle.get_width() + pos, 0))
    pos -= 5
    
    if pos > scrn_width:
        pos = 0

class Tanjiro(pygame.sprite.Sprite):
    def __init__(self, char_type_idle, char_type_run, char_type_punch, char_type_swrdjab, char_type_slash, char_type_ultimate, char_type_water, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_types = {'idle': char_type_idle,'run': char_type_run,'punch': char_type_punch,'swrdjab': char_type_swrdjab,'slash': char_type_slash,'ultimate': char_type_ultimate,'water': char_type_water}
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.anim_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # List of actions and their frame counts
        actions = [('idle', 2), ('run', 6), ('punch', 2), ('swrdjab', 2), ('slash', 6), ('ultimate', 7), ('water', 9)]

        # Load animations for each action
        for action, frames in actions:
            templst = []
            char_type = self.char_types[action]
            for i in range(frames):
                file_path = f'img/{action}/{char_type}{i}.png'
               
                sprites = pygame.image.load(file_path)
                sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))
                pygame.Surface.convert_alpha(sprites)
                templst.append(sprites)   
                
            self.anim_list.append(templst)
        
        self.sprites = self.anim_list[self.action][self.frame_index]
        self.rect = self.sprites.get_rect()
        self.rect.center = (x, y)
    
    def move(self, move_rgt, move_lft):
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
        self.rect.x += dx
        self.rect.y += dy

        #update scroll
        if self.char_types == 'tanjiro':
            if self.rect.right > scrn_width - scroll_limit or self.rect.left < scroll_limit:
                self.rect.x -= dx
                screen_scroll = -dx
            return screen_scroll

    def update_animation(self):
        # Update animation
        anim_cldwn = 120
        if self.action == 2:
             anim_cldwn = 10
        elif self.action == 3:
            anim_cldwn = 10
        elif self.action == 5:  # Ultimate
        # Slow down the last 3 frames
         if self.frame_index >= len(self.anim_list[self.action]) - 3:
            anim_cldwn = 200  # Slower cooldown for the last 3 frames
         else:
            anim_cldwn = 10  # Normal cooldown for the rest of the frames
        elif self.action == 4:
            anim_cldwn = 10
        
        # Update image depending on current frame 
        self.sprites = self.anim_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > anim_cldwn:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.anim_list[self.action]):
           self.frame_index = 1
       
    def updte_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.sprites, self.flip, False), self.rect)

#spawning the enmies 
class enemy(pygame.sprite.Sprite):
    def __init__(self, char_type_idle, char_type_walk, x, y, scale, speed):
        self.char_types = {'idle': char_type_idle, 'walk': char_type_walk}
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.anim_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # List of actions and their frame counts
        actions = [('idle', 2), ('walk', 8)]

        # Load animations for each action
        for action, frames in actions:
            templst = []
            char_type = self.char_types[action]
            for i in range(frames):
                file_path = f'img/{action}/{char_type}{i}.png'
                sprites = pygame.image.load(file_path)
                sprites = pygame.transform.scale(sprites, (sprites.get_width() * scale, sprites.get_height() * scale))
                pygame.Surface.convert_alpha(sprites)
                templst.append(sprites)

            self.anim_list.append(templst)

        self.sprites = self.anim_list[self.action][self.frame_index]
        self.rect = self.sprites.get_rect()
        self.rect.center = (x, y)
    
    def update_animation(self):
        # Update animation
        anim_cldwn = 120
        if self.action == 2:
             anim_cldwn = 10
        elif self.action == 3:
            anim_cldwn = 10
        elif self.action == 5:  # Ultimate
        # Slow down the last 3 frames
         if self.frame_index >= len(self.anim_list[self.action]) - 3:
            anim_cldwn = 200  # Slower cooldown for the last 3 frames
         else:
            anim_cldwn = 10  # Normal cooldown for the rest of the frames
        elif self.action == 4:
            anim_cldwn = 10
        
        # Update image depending on current frame 
        self.sprites = self.anim_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > anim_cldwn:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.anim_list[self.action]):
           self.frame_index = 1
    
    def updte_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    

        def draw(self):
            screen.blit(pygame.transform.flip(self.sprites, self.flip, False), self.rect)

        
       
        




player = Tanjiro('tanjiro_idle', 'tanjiro_run', 'tanjiro_punch', 'tanjiro_slash', 'tanjiro_s', 'tanjiro_ultimate', 'tanjiro_water', 550, 500, 3, 5)

run = True
while run:
    clock.tick(FPS)
    draw_bg()
    player.draw()
    player.update_animation()
    player.move(move_rgt, move_lft)
    

    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            run = False

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

    # Update action
    if e:
        player.updte_action(2)
    elif z:
        player.updte_action(5)
    elif x:
        player.updte_action(6)
    elif lft_clck:
        player.updte_action(3)
    elif rgt_clck:
        player.updte_action(4)
    elif move_rgt or move_lft:
        player.updte_action(1)
    else:
        player.updte_action(0)
    screen_scroll = player.move(move_rgt, move_lft)
    print(screen_scroll)

    pygame.display.update()

pygame.quit()
