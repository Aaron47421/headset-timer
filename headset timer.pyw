import time
from tkinter import *
import pystray
import PIL.Image
import threading

global exiting
exiting = False

DIM = [300,300]
MID = [DIM[0]/2,DIM[1]/2]
def create_message(time):
    root = Tk()
    root.attributes('-topmost', True)
    root.geometry(f"{DIM[0]}x{DIM[1]}")
    root.configure(bg="black")
    root.title(f"headset timer [{time}]")
    root.update()
    text = Label(root, text="move your headset!", font=("Arial", 20), fg="white", bg="black")
    text.place(x=MID[0]-120,y=MID[1]-25)
    root.mainloop()

def exfun(icon, item):
    if str(item) == "exit":
        global exiting
        exiting = True
        icon.stop()
        exit()

def main():
    total = "25m"

    try:
        with open("timer.txt", "r") as f:
            total = f.readlines()[3]

    except:
        pass

    print(total)

    tim = int(total[:-1])
    typ = total[-1:]
    while 1:
        if exiting:
            break

        if typ == "m":
            time.sleep(tim * 60)
            create_message(total)
            
        elif typ == "s":
            time.sleep(tim)
            create_message(total)

        elif typ == "h":
            time.sleep((tim * 60) * 60)
            create_message(total)

t1 = threading.Thread(target=main)

if __name__ == "__main__":
    icon = PIL.Image.open("icon.png")
    icon = pystray.Icon("headset timer", icon, menu=pystray.Menu(
        pystray.MenuItem("exit", exfun)
    ))

    t1.start()
    icon.run()