from tkinter import*
import time
from PIL import ImageTk , Image




window = Tk()
window.geometry("560x420")
window.title("Coffee Simulator")



Title = Label(window,text='COFFEE SIMULATOR - SPD',font=('Lucida Console',20,'bold','italic'))
Title.place(x=90,y=0)

base = ImageTk.PhotoImage(Image.open("G:\Python\AI School\Empty.png"))

wmc = ImageTk.PhotoImage(Image.open("G:\Python\AI School\mwc.png"))
boiling = ImageTk.PhotoImage(Image.open("G:\Python\AI School\Boil1.png"))
srved = ImageTk.PhotoImage(Image.open("G:\Python\AI School\Srvd.png"))

machine = Label(window,image=base)
machine.place(x=160,y=80)

def add_ingre():
        time.sleep(1)
        machine.configure(image=wmc)
        machine.image = wmc

def Boil():
        time.sleep(1.5)
        machine.configure(image=boiling)
        machine.image = boiling

def Serve():
        time.sleep(1)
        machine.configure(image=srved)
        machine.image = base
        machine.place(x=130,y=80)
        
btnc = Button(window,text='Add Water, Milk and Coffee ',font=('Helevetica',10,'bold'),command= add_ingre )
btnc.place(x=190,y=360)

boil = Button(window,text='Boil',font=('Helevetica',10,'bold'),command= Boil)
boil.place(x=190,y=390)

serve = Button(window,text='Serve',font=('Helevetica',10,'bold'),command=Serve )
serve.place(x=340,y=390)

window.mainloop()