from tkinter import *

root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w_s = (w / 2) - 150
h_s = (h / 2) - 150
root.geometry(f'300x300+{int(w_s)}+{int(h_s)}')
x = 1

def change():
    global x
    root.title(f'{x} Clicks')
    if x % 2 == 0:
        btn.config(text='CLICK')
    else:
        btn.config(text='CLICKED')
    x += 1

btn = Button(text='CLICK', font=(None, 40), command=change, bg='Lime', relief='groove', width=8, height=2)
btn.pack(pady=30)

root.mainloop()

