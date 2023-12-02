VER="1.1.1.7"
from tkinter import *
from time import sleep
from os import getcwd
data={}
def data_save():
    global data
    sf=open("data.mvpes","wb")
    pickle.dump(data,sf)
    sf.close()
def data_load():
    global data
    lf=open("data.mvpes","rb")
    data=pickle.load(lf)
    lf.close()
mx=None
my=None
cwd=getcwd()
bt={"grass":["\.minevillage\mvt\gbtc.png"]}
class block():
    t="grass"
    sel=False
    x=None
    y=None
    ci=0
    cim=0
    def Tick():
        if(mx>=x and mx<=x+16 and my>=x and my<=y+16):
            self.sel=True
        else:
            self.sel=False
        self.ci+=1
        self.ci%=self.cim
        
def print_pos(event):
    global mx,my
    mx,my=event.widget.winfo_pointerxy()
def Tick():
    #something
    return
def li(s):
    for i in range(len(bt[s])):
        bt[s][i]=PhotoImage(cwd+bt[s][i])
tk=Tk() 
tk.title("Minevillage "+VER)
canves=Canvas(tk,width=1024,height=576,highlightthickness=0)
canves.pack()
tk.update()
tk.bind("<Motion>",print_pos)
while True:
    sleep(1/20)
    Tick()
    tk.update_idletasks()
    tk.update()
