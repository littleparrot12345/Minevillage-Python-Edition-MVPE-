VER="1.1.2.16"
from tkinter import *
from time import sleep
from os import getcwd,path
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
mx=0
my=0
cwd=getcwd()
bt={"grass":["/.minevillage/mvt/gbtc.png"]}
canves=None
gm=[]
class Block():
    t="grass"
    sel=False
    x=0
    y=0
    ci=0
    cim=1
    def tick(self):
        global mx,my
        if(mx>=self.x and mx<=self.x+16 and my>=self.y and my<=self.y+16):
            self.sel=True
        else:
            self.sel=False
        self.ci+=1
        self.ci%=self.cim
    def draw(self):
        canves.create_image(self.x,self.y,image=bt[self.t][self.ci],anchor=NW)
def mp(event):
    global mx,my
    mx,my=event.widget.winfo_pointerxy()
def Tick():
    #something
    return
def li(s):
    for i in range(len(bt[s])):
        img_path=cwd+bt[s][i]
        bt[s][i]=PhotoImage(file=img_path)
tk=Tk()
tk.iconbitmap(cwd+"/.minevillage/icons/icon.ico")
tk.title("Minevillage "+VER)
canves=Canvas(tk,width=1024,height=576,highlightthickness=0)
canves.pack()
tk.update()
tk.bind("<Motion>",mp)
for i in ["grass"]:
    li(i)
for i in range(0,1024,16):
    gm.append([])
    xb=i//16
    for j in range(0,576,16):
        tmp=Block()
        tmp.x=i
        tmp.y=j
        tmp.draw()
        gm[xb].append(tmp)
for row in gm:
    for block in row:
        block.draw()
while True:
    sleep(1/20)
    for row in gm:
        for block in row:
            block.tick()
    Tick()
    tk.update_idletasks()
    tk.update()
