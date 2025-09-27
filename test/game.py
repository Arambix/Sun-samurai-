import pygame
from pygame import mixer  # Import the mixer module for sound effects
from random import randint
pygame.init()  # Initialize all pygame modules

# Set up screen dimensions
scrn_width = 800  # Width of the display
scrn_height = int(scrn_width * 0.8)  # Height calculated based on width

# Create the display window
screen = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption('sun samurai')  # Set the window title

# Set the framerate
clock = pygame.time.Clock()  # Create a clock object to manage the game's frame rate
FPS = 60  # Desired frames per second


red =(225,0,0)
blue = (0,0, 220)
white = (225,225,225)
message_colour = white



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
# instance
main = mainmenu(screen)

run = True  # Main game loop flag
while run:
    clock.tick(FPS)  # Control the frame rate
    # game state implemented
    if mainmenu == True:
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
    for event in pygame.event.get():  # Handle events
        
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()  # Update the display

pygame.quit()  # Quit the game
