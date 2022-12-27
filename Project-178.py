from tkinter import *
import random

root = Tk()
root.title("Color Randomizing game")
root.geometry("500x400")
root.config(bg="white")

namelabel= Label(root,font=("comic sans ms",40),bg="white")
namelabel.place(relx=0.5,rely=0.3,anchor=CENTER)

class Game():
    def __init__(self):
        self.__score = 0
    
    def updateGame(self):
        self.text=["BLACK","PINK","BLUE","GREEN","YELLOW","ORANGE","RED","PURPLE"]
        self.random_number_for_text = random.randint(0,7)
        self.color=["BLACK","PINK","BLUE","GREEN","YELLOW","ORANGE","RED","PURPLE"]
        self.random_number_for_color = random.randint(0,7)
        namelabel["text"]=self.text[self.random_number_for_text]
        namelabel["fg"]=self.color[self.random_number_for_color]
        
obj=Game()
btn=Button(root,text="start",fg="green",padx=7,pady=1,font=("comic sans ms",22),command=obj.updateGame)
btn.place(relx=0.65,rely=0.65,anchor=CENTER)
root.mainloop()

