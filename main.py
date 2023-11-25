VER="1.0.3.1"
from tkinter import *
from time import sleep
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
def Tick():
    #something
    return
tk=Tk() 
tk.title("Minevillage "+VER)
grass_block_top_img=PhotoImage("/.minevillage/textures/block")
#canves=Canves
while True:
    sleep(1/20)
    Tick()
    tk.update_idletasks()
    tk.update()
