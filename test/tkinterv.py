from tkinter import *

win = Tk() # instantiate an instance of a window
win.geometry("800x800") # GUi dimensions
win.title("sun samurai") # title of my game

Icon = PhotoImage(file='img/idle/tanjiro_idle0.png') # displays the image from file path to the gui icon on the left of the screen

win.iconphoto(True, Icon)


class gameplay():
    def __init__(self,root):
        self.root = root
        self.img = PhotoImage(file='img/bg/start.png')
        self.img2 = PhotoImage(file='img/bg/start.png')
        
        
    
        self.background = PhotoImage(file='img/bg/background.png')
        self.bg = Label(root, image= self.background)
        self.bg.place(x= 0, y= 0, relwidth= 1, relheight= 1)
        def STARTGAME():
           print("start game")
          # this is so that i can hide the main menu
           win.withdraw()
           self.transition()
        self.starts = Button(root, text='START')
        self.starts.config(command=STARTGAME)
        self.starts.config(font=('Ink Free', 30, 'bold'))
        self.starts.config(image=self.img)
        self.starts.config(compound="center")
        def ENDGAME():
            print("end game")
            win.quit()
        self.quit = Button(root,text='QUIT')
        self.quit.config(command=ENDGAME)
        self.quit.config(font=('Ink Free', 30, 'bold'))
        self.quit.config(image=self.img2)
        self.quit.config(compound="center") 
    

    
    
    # function for actually drawing the button on the GUI   
    def draw_buttons(self):
        self.starts.place(x= 250, y= 300)
        self.quit.place(x= 250, y= 490)  
        
    #a function for editing the the text onto the button
    
    #a function for giving the buttons some colour
    def button_colour(self):
        self.starts.config(bg='green')
        self.quit.config(bg='red')
    
    def transition(self,):
        transition = levels(self.root)
        transition.screen()

class levels:
    def __init__(self,root):
        self.root = root
        self.lvl_win = Toplevel(self.root)
        self.lvl_win.geometry("800x800")
        self.lvl_win.title("Levels")
        self.lvl_win.config(bg='black')
    
    def screen(self):
        Llable = Label(self.lvl_win, text="LEVEL 1")
        Llable.config(font=('Ink Free', 30, 'bold'))
        Llable.place(x= 250, y=300)        
        


main = gameplay(win)
main.draw_buttons()
main.transition()

lvls = levels(win)
lvls.screen()


win.mainloop() # this piece of code is responsible for displaying win on the computer
