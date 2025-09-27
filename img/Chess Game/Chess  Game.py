import pygame 
import os
print(os.getcwd())
cwd = os.getcwd()
pygame.init()
logged_in = True 
surface = pygame.display.set_mode((1000,800)) # creating surface for the game to be displayed on
pygame.display.set_caption('Chess') 
background_colour = (50,80,130)
white = (255,255,255)
light_blue = (150,160, 230)
red = (200,100,100)
green = (100,200,100)
height = surface.get_height()
width = surface.get_width()
font = pygame.font.Font('freesansbold.ttf', 32) 
playtext = font.render('Play', True, light_blue, white)
tutorialtext = font.render('Tutorial', True, light_blue, white)
optionstext = font.render('Options', True, light_blue, white)
quittext = font.render('Quit', True, light_blue, white)
playtextsurface = playtext.get_rect()
selected = [None,0,0] # list which will be updated to contain the last piece the user has clicked, alongside the coordinates of that piece

black_pawn_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\black-pawn.png")
black_pawn_image = pygame.transform.scale(black_pawn_image, (100, 100))

white_pawn_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\white-pawn.png")
white_pawn_image = pygame.transform.scale(white_pawn_image, (100, 100))

# Knights
black_knight_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\black-knight.png")
black_knight_image = pygame.transform.scale(black_knight_image, (100, 100))

white_knight_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\white-knight.png")
white_knight_image = pygame.transform.scale(white_knight_image, (100, 100))

# Bishops
black_bishop_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\black-bishop.png")
black_bishop_image = pygame.transform.scale(black_bishop_image, (100, 100))

white_bishop_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\white-bishop.png")
white_bishop_image = pygame.transform.scale(white_bishop_image, (100, 100))

# Rooks
black_rook_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\black-rook.png")
black_rook_image = pygame.transform.scale(black_rook_image, (100, 100))

white_rook_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\white-rook.png")
white_rook_image = pygame.transform.scale(white_rook_image, (100, 100))

# Queens
black_queen_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\black-queen.png")
black_queen_image = pygame.transform.scale(black_queen_image, (100, 100))

white_queen_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\white-queen.png")
white_queen_image = pygame.transform.scale(white_queen_image, (100, 100))

# Kings
black_king_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\black-king.png")
black_king_image = pygame.transform.scale(black_king_image, (100, 100))

white_king_image = pygame.image.load(cwd+r"\OneDrive - Red Kite Learning Trust\Saved Games\Chess Game\white-king.png")
white_king_image = pygame.transform.scale(white_king_image, (100, 100))


class Board(): # board class will contain each piece and functions associated with the playing of the game
    def __init__(self):
        self.active = False
        self.turn = "white"
        self.turn_number = 0
    def change_turn(self):
        if self.turn == "white":
            self.turn_number +=1
            return "black"
        if self.turn == "black":
            self.turn_number +=1
            return "white"
    def try_combinations(self):
        allmoves = []
        for pieces in chess_pieces[board.turn]:
            for piece in chess_pieces[board.turn][pieces]:
                for column in range(8):
                    for row in range(8):
                        if piece.determine_move([piece,piece.posx,piece.posy],column,row, self.board):
                            allmoves.append([piece, column, row])
                            #print([piece, row, column])
        return allmoves
    def test_board(self,piece,column,row):
        newboard = self.board
        newboard = piece.determine_move([piece,piece.posx,piece.posy],column,row,newboard)[1]
        return newboard
    def try_check(self,newboard,checking):
        if board.turn == "black":
            if checking.determine_move([checking, checking.posx,checking.posy], chess_pieces["white"]["king"][0].posx, chess_pieces["white"]["king"][0].posy, newboard) != None:
                if checking.determine_move([checking, checking.posx,checking.posy], chess_pieces["white"]["king"][0].posx, chess_pieces["white"]["king"][0].posy, newboard) == True:
                    return True
        if board.turn == "white":
            if checking.determine_move([checking, checking.posx,checking.posy], chess_pieces["black"]["king"][0].posx, chess_pieces["black"]["king"][0].posy, newboard) != None:
                if checking.determine_move([checking, checking.posx,checking.posy], chess_pieces["black"]["king"][0].posx, chess_pieces["black"]["king"][0].posy, newboard) == True:
                    return True


    def setup_board(self, chess_pieces): # this subroutine will take self, and the dictionary containing each piece that will be used in the game. 
    #It will be used whenever the user wants to start a new game.
        self.board = [[None]*8]*8 # creating the 2d array of 8x8
        self.board[1] = [ #board is "upside down", (white should be on the bottom), howver, since the coordinates of pygame are reversed i have decided to reverse the array as well to save time.
    chess_pieces["black"]["pawns"][0], 
    chess_pieces["black"]["pawns"][1], 
    chess_pieces["black"]["pawns"][2], 
    chess_pieces["black"]["pawns"][3], 
    chess_pieces["black"]["pawns"][4], 
    chess_pieces["black"]["pawns"][5], 
    chess_pieces["black"]["pawns"][6], 
    chess_pieces["black"]["pawns"][7]
]  
        self.board[6] = [
    chess_pieces["white"]["pawns"][0], 
    chess_pieces["white"]["pawns"][1], 
    chess_pieces["white"]["pawns"][2], 
    chess_pieces["white"]["pawns"][3], 
    chess_pieces["white"]["pawns"][4], 
    chess_pieces["white"]["pawns"][5], 
    chess_pieces["white"]["pawns"][6], 
    chess_pieces["white"]["pawns"][7]
]  
        self.board[0] = [
    chess_pieces["black"]["rooks"][0], 
    chess_pieces["black"]["knights"][0], 
    chess_pieces["black"]["bishops"][0], 
    chess_pieces["black"]["queen"][0], 
    chess_pieces["black"]["king"][0], 
    chess_pieces["black"]["bishops"][1], 
    chess_pieces["black"]["knights"][1], 
    chess_pieces["black"]["rooks"][1]
]  

        self.board[7] = [
    chess_pieces["white"]["rooks"][0], 
    chess_pieces["white"]["knights"][0], 
    chess_pieces["white"]["bishops"][0], 
    chess_pieces["white"]["queen"][0], 
    chess_pieces["white"]["king"][0], 
    chess_pieces["white"]["bishops"][1], 
    chess_pieces["white"]["knights"][1], 
    chess_pieces["white"]["rooks"][1]
] 

        self.board[2] = [None, None, None, None, None, None, None, None] # whilst these sections of the array are already each None, they have to be individually assigned as None,
        self.board[3] = [None, None, None, None, None, None, None, None] # this is because pieces would not be able to move into these empty spaces correctly, instead they would
        self.board[4] = [None, None, None, None, None, None, None, None] # ocupy each available space with value None 
        self.board[5] = [None, None, None, None, None, None, None, None]
    def start_game(self): # attribute of the board class created with a method to change it from one to the other, which the game loop uses to test if the board should be displayed
        if self.active == False:
            self.active = True
        else:
            self.active = False
    def show_board(self): # method which will draw the board when self.active is true
        for column in range(8):
            for row in range(8):
                if (column + row)%2 == 0:
                    pygame.draw.rect(surface,light_blue,[100+100*column,100*row,100,100])
                if self.board[row][column] != None: # since None has no attribute .type, it must first be checked that the selection is not None, so that .type can determine the type
                    if self.board[row][column].type == "Pawn":
                        if self.board[row][column].colour == "black":
                            surface.blit(black_pawn_image,(100+100*column,100*row,20,20))
                        else:
                            surface.blit(white_pawn_image,(100+100*column,100*row,20,20))
                    elif self.board[row][column].type == "King":
                        if self.board[row][column].colour == "black":
                            surface.blit(black_king_image,(100+100*column,100*row,20,20))                           
                        else:
                            surface.blit(white_king_image,(100+100*column,100*row,20,20))
                    elif self.board[row][column].type == "Bishop":
                        if self.board[row][column].colour == "black":
                            surface.blit(black_bishop_image,(100+100*column,100*row,20,20))
                        else:
                            surface.blit(white_bishop_image,(100+100*column,100*row,20,20))
                    elif self.board[row][column].type == "Knight":
                        if self.board[row][column].colour == "black":
                            surface.blit(black_knight_image,(100+100*column,100*row,20,20))
                        else:
                            surface.blit(white_knight_image,(100+100*column,100*row,20,20))
                    elif self.board[row][column].type == "Queen":
                        if self.board[row][column].colour == "black":
                            surface.blit(black_queen_image,(100+100*column,100*row,20,20))
                        else:
                            surface.blit(white_queen_image,(100+100*column,100*row,20,20))
                    elif self.board[row][column].type == "Rook":
                        if self.board[row][column].colour == "black":
                            surface.blit(black_rook_image,(100+100*column,100*row,20,20))
                        else:
                            surface.blit(white_rook_image,(100+100*column,100*row,20,20))
    def button_check(self,x,y): # this method is used to update the selected list
        if x >=0 and x <= 7:
            #print(self.board[y][x])
            return [self.board[y][x], x, y]
        else: return [None,0,0]
    #def move(self, selected):
        #pass

class Piece(): # piece class used as a class from which each different piece inherits 
    def __init__(self, colour,x,y): 
        self.colour = colour # "black" or "white"
        self.turns = 0
        self.checking = False
        self.posx = x
        self.posy = y 
    def move(self,selected, x, y, newboard): # parameters of selected and x,y are given so that we have the piece clicked previously, and the square that has been clicked most recently
        #print(selected[1],selected[2])
        if (selected[1],selected[2]) == (x,y):# makes sure the piece cannot capture itself
            return
        if selected[0] != None:
            #print(selected[0].colour)
            if selected[0].colour == board.turn: # checking if it is right players turn
                if newboard[y][x] != None:
                    if newboard[y][x].colour == board.turn: # stopping code if the piece tries to capture own teammates
                        return
                newboard[y][x] = selected[0] # moving piece object to clicked square
                newboard[selected[2]][selected[1]] = None # removing the piece from the square it was just on
                self.turns+=1
                self.posx = x
                self.posy = y
                return [True, newboard]

class Pawn(Piece): # each piece inherits from the piece class, and will contain their own move set.
    def __init__(self, colour,x,y):
        super().__init__(colour,x,y)
        self.type = "Pawn"
    def determine_move(self,selected, x, y, newboard): # check whether a move is legal before using move method
        if self.turns < 1: # pawns can move further on the first turn for each player
            if board.turn == "white":
                if x == selected[1]:
                    if y == selected[2]-1 or y == selected[2]-2: # pawn can move 1 or 2 spaces forwards here
                        if newboard[y][x] == None:
                            return True
                if x == selected[1]+1 or x == selected[1]-1: 
                    if selected[2] == y +1:
                        if newboard[y][x] != None:
                            if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                                return True
            elif board.turn == "black":
                if x == selected[1]:
                    if y == selected[2]+1 or y == selected[2]+2:
                        if newboard[y][x] == None:
                            return True
                if x == selected[1]+1 or x == selected[1]-1:
                    if selected[2] == y -1:
                        if newboard[y][x] != None:
                            if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                                return True
        else:
            if board.turn == "white":
                if x == selected[1]: #when the pawn moves vertically forwards
                    if y == selected[2]-1: #1 space
                        if newboard[y][x] == None: # pawn can only move if there is no piece in its way when going forward
                            return True # using move function
                if x == selected[1]+1 or x == selected[1]-1: # pawns can move diagonally. These are the columns either side of pawn being checked
                    if selected[2] == y +1: # can only move 1 space
                        if newboard[y][x] != None: # can only move diagonally when capturing
                            if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                                return True
            if board.turn == "black":
                if x == selected[1]:
                    if y == selected[2]+1:
                        if newboard[y][x] == None:
                            return True
                if x == selected[1]+1 or x == selected[1]-1:
                    if selected[2] == y -1:
                        if newboard[y][x] != None:
                            if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                                return True


class Bishop(Piece):
    def __init__(self, colour,x,y):
        super().__init__(colour,x,y)
        self.type = "Bishop"
    def determine_move(self,selected, x, y, newboard):
        for i in range(1, 8): #each move must be checked in a specific order because the bishop can be blocked by other pieces getting in its way
            if selected[1]+i >7: # prevent the code from searching an element of the board array which does not exist
                break
            if selected[2]+i >7:
                break
            if selected[1]+i == x and selected[2]+i == y:
                if newboard[y][x] != None:
                    if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                        return True
                else:
                    return True
            if newboard[selected[2]+i][selected[1]+i] != None:
                break
        for i in range(1, 8): 
            if selected[1]-i <0: 
                break
            if selected[2]+i >7:
                break
            if selected[1]-i == x and selected[2]+i == y:
                if newboard[y][x] != None:
                    if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                        return True
                else:
                    return True
            if newboard[selected[2]+i][selected[1]-i] != None:
                break
        for i in range(1, 8): 
            if selected[1]+i >7: 
                break
            if selected[2]-i <0:
                break
            if selected[1]+i == x and selected[2]-i == y:
                if newboard[y][x] != None:
                    if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                        return True
                else:
                    return True
            if newboard[selected[2]-i][selected[1]+i] != None:
                break
        for i in range(1, 8): 
            if selected[1]-i <0: 
                break
            if selected[2]-i <0:
                break
            if selected[1]-i == x and selected[2]-i == y:
                if newboard[y][x] != None:
                    if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                        return True
                else:
                    return True
            if newboard[selected[2]-i][selected[1]-i] != None:
                break
            
            
class King(Piece):
    def __init__(self, colour, pos1,pos2):
        super().__init__(colour,pos1,pos2)
        self.type = "King"
        self.in_check = False
    def determine_move(self,selected, x, y, newboard):
        if abs(selected[1]-x) <2: # king can move -1,0, or 1 in x coord
            if abs(selected[2]-y) <2: #same for y
                if newboard[y][x] != None:
                    if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                        return True
                else:
                    return True
        if newboard[y][x] != None:
            if newboard[y][x].type == "Rook" and newboard[y][x].colour == board.turn and newboard[y][x].turns == 0 and self.turns == 0 and x == 7 and y == 7: # castling move
                if newboard[7][5] == None and newboard[7][6] == None: # check if pieces are in the way
                    print("hello")
                    self.move(selected,6,7)
                    newboard[7][5] = board[7][7] # position has to be changed this way because the move function will add to the turn counter and the rook moving would not be allowed
                    newboard[7][7] = None      
                    return False          


class Queen(Piece):
    def __init__(self, colour,x,y):
        super().__init__(colour,x,y)
        self.type = "Queen"
    def determine_move(self, selected, x, y, newboard):
        if selected[1] == x:
            for i in range(1,8):
                if selected[2]+i >7:
                    break
                if selected[1] == x and selected[2]+i == y:
                    if newboard[y][x] != None:
                        if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                            return True
                    else:
                        return True 
                if newboard[selected[2]+i][selected[1]] != None:
                    break
            for i in range(1,8):
                if selected[2]-i < 0:
                    break
                if selected[1] == x and selected[2]-i == y:
                    if newboard[y][x] != None:
                        if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                            return True
                    else:
                        return True
                if newboard[selected[2]-i][selected[1]] != None:
                    break
        if selected[2] == y:
            for i in range(1,8): 
                if selected[1]+i >7:
                    break
                if selected[1]+i == x and selected[2] == y:
                    if newboard[y][x] != None:
                        if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                            return True
                    else:
                        return True
                if newboard[selected[2]][selected[1]+i] != None:
                    break
            for i in range(1,8):
                if selected[1]-i < 0:
                    break
                if selected[1]-i == x and selected[2] == y:
                    if newboard[y][x] != None:
                        if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                            return True
                    else:
                        return True 
                if newboard[selected[2]][selected[1]-i] != None:
                    break
        for i in range(1, 8): 
            if selected[1]+i >7: 
                break
            if selected[2]+i >7:
                break
            if selected[1]+i == x and selected[2]+i == y:
                if newboard[y][x] != None:
                    if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                        return True
                else:
                    return True
            if newboard[selected[2]+i][selected[1]+i] != None:
                break
        for i in range(1, 8): 
            if selected[1]-i <0: 
                break
            if selected[2]+i >7:
                break
            if selected[1]-i == x and selected[2]+i == y:
                if newboard[y][x] != None:
                    if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                        return True
                else:
                    return True
            if newboard[selected[2]+i][selected[1]-i] != None:
                break
        for i in range(1, 8): 
            if selected[1]+i >7: 
                break
            if selected[2]-i <0:
                break
            if selected[1]+i == x and selected[2]-i == y:
                if newboard[y][x] != None:
                    if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                        return True
                else:
                    return True
            if newboard[selected[2]-i][selected[1]+i] != None:
                break
        for i in range(1, 8): 
            if selected[1]-i <0: 
                break
            if selected[2]-i <0:
                break
            if selected[1]-i == x and selected[2]-i == y:
                if newboard[y][x] != None:
                    if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                        return True
                else:
                    return True
            if newboard[selected[2]-i][selected[1]-i] != None:
                break

class Rook(Piece):
    def __init__(self, colour,x,y):
        super().__init__(colour,x,y)
        self.type = "Rook"
    def determine_move(self,selected, x, y, newboard):
        if selected[1] == x:
            for i in range(1,8):
                if selected[2]+i >7:
                    break
                if selected[1] == x and selected[2]+i == y:
                    if newboard[y][x] != None:
                        if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                            return True
                    else:
                        return True
                if newboard[selected[2]+i][selected[1]] != None:
                    break
            for i in range(1,8):
                if selected[2]-i < 0:
                    break
                if selected[1] == x and selected[2]-i == y:
                    if newboard[y][x] != None:
                        if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                            return True
                    else:
                        return True
                if newboard[selected[2]-i][selected[1]] != None:
                    break
        if selected[2] == y:
            for i in range(1,8): 
                if selected[1]+i >7:
                    break
                if selected[1]+i == x and selected[2] == y:
                    if newboard[y][x] != None:
                        if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                            return True
                    else:
                        return True
                if newboard[selected[2]][selected[1]+i] != None:
                    break
            for i in range(1,8):
                if selected[1]-i < 0:
                    break
                if selected[1]-i == x and selected[2] == y:
                    if newboard[y][x] != None:
                        if newboard[y][x].colour != board.turn and [x,y] != [selected[0],selected[1]]:
                            return True
                    else:
                        return True 
                if newboard[selected[2]][selected[1]-i] != None:
                    break

class Knight(Piece):
    def __init__(self, colour,x,y):
        super().__init__(colour,x,y)
        self.type = "Knight"
    def determine_move(self,selected, x, y, newboard):
        if abs(selected[1] - x) == 1: # using absoloute value function so i have to write less rather than have to write for cases of +1 and -1 difference 
            if abs(selected[2]-y) == 2:
                return True
        if abs(selected[1] - x) == 2: 
            if abs(selected[2]-y) == 1:
                return True

class EmptyPiece(Piece):
    def __init__(self, colour):
        super().__init__(colour)
class Menu():
    def __init__(self):
        self.active = False
    def open_menu(self):
        self.active = True
    def show_menu(self):
         for i in range(4):
            pygame.draw.rect(surface,white,[100+i*210,40,170,720]) 
            playtextsurface.center = (185, 400) 
            surface.blit(playtext, playtextsurface)
            playtextsurface.center = (370, 400) 
            surface.blit(tutorialtext, playtextsurface)
            playtextsurface.center = (575, 400) 
            surface.blit(optionstext, playtextsurface)
            playtextsurface.center = (810, 400) 
            surface.blit(quittext, playtextsurface)
    def button_check(self, mousex, mousey):
        if mousey > 40 and mousey < 760:
            if mousex > 100 and mousex < 270:
                self.active = False
                board.active = True
            if mousex > 310 and mousex < 480:
                pass
                #print("tutorial")
            if mousex > 520 and mousex < 690:
                pass
                #print ("options")
            if mousex > 730 and mousex < 900:
                 global Running
                 Running = False
class Login():
    def __init__(self):
        self.logged_in = False
    def signed_in(self):
        self.logged_in = True
menu = Menu()
menu.open_menu()
login = Login()
login.signed_in()
board = Board() #objects created
chess_pieces = { # dictionary containing each piece which will be created at the start of the game
    "white": {
        "pawns": [Pawn("white",i,6) for i in range(8)], 
        "rooks": [Rook("white",7*i,7) for i in range(2)],
        "knights": [Knight("white", 5*i + 1, 7) for i in range(2)], # 5*i because of a gap of 5
        "bishops": [Bishop("white", 3*i +2,7) for i in range(2)],
        "queen": [Queen("white", 3, 7)],
        "king": [King("white", 4,7)],
    },
    "black": {
        "pawns": [Pawn("black", i, 1) for i in range(8)],
        "rooks": [Rook("black",7*i,0) for i in range(2)],
        "knights": [Knight("black", 5*i+1,0) for i in range(2)],
        "bishops": [Bishop("black", 3*i + 2,0) for i in range(2)],
        "queen": [Queen("black", 3,0)],
        "king": [King("black",4,0)],
    }
}
#print(chess_pieces["black"]["pawns"][0])
board.setup_board(chess_pieces) # dictionary is passed into the setup board method
Running = True
while Running:
    mouse = pygame.mouse.get_pos() 
    mousex = mouse[0]
    mousey = mouse[1] # these are given to variables immediately for convenience
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            Running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if menu.active == True:
                menu.button_check(mousex, mousey)
            if board.active == True:
                if selected[0] != None: # making sure we dont use a method on None which will cause a syntax error
                    if chess_pieces["black"]["king"][0].in_check == True:                        
                        print(board.try_combinations())                        
                    if chess_pieces["white"]["king"][0].in_check == True:                        
                        print(board.try_combinations())                        
                    if selected[0].determine_move(selected,(mousex-100)//100,mousey//100, board.board) == True:
                        if selected[0].move(selected,(mousex-100)//100,mousey//100, board.board)[0] == True:
                            if board.try_check(board.board,selected[0]) == True:
                                if board.turn == "white":
                                    chess_pieces["black"]["king"][0].in_check = True
                                    checking = selected[0]
                                if board.turn == "black":
                                    chess_pieces["white"]["king"][0].in_check = True
                                    checking = selected[0]

                        board.turn = board.change_turn()
                selected = board.button_check((mousex-100)//100, mousey//100)           
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                selected[0] = None
    surface.fill(background_colour)    
    if login.signed_in == False: # selection used to determine which phase the program is in.
        #print("sign")
        pass
    elif menu.active == True:
        menu.show_menu()
    elif board.active == True:
        board.show_board()
    
    pygame.display.update()
 