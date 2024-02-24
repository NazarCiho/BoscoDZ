from tkinter import *
from tkinter import messagebox
import random, time
root=Tk()
root.geometry('400x300+600+300')
root.title('Вгадай число')
def random_chuslo():
    poc=ent_poc.get()
    kin=ent_kin.get()
    if poc.isdigit() and kin.isdigit():
        poc = int(poc)
        kin = int(kin)
        if poc<kin:
            chuslo=random.randint(int(poc), int(kin))
            ent_vgadai=Entry(font=(None, 10),relief='solid')
            ent_vgadai.place(x=180,y=120)
            lab_vgadai = Label(text=f'Вгадайте число:', font=(None, 10))
            lab_vgadai.place(x=1, y=120)
            but_perevirka=Button(text='Перевірити',font=(None, 10), relief='solid',bg='mediumpurple', command=lambda: perevirka(chuslo, ent_vgadai,lab_vgadai, but_perevirka))
            but_perevirka.place(x=145,y=150)
        else:
            messagebox.showwarning('ERROR','Початкова меже не є меншою ніж кінцева!')
    else:
        messagebox.showerror('ERROR','Ви ввели не ціле число!')
    return ent_vgadai, lab_vgadai, but_perevirka
x=0
def perevirka(chuslo, ent_vgadai,lab_vgadai, but_perevirka):
    global lab_win, x
    x += 1
    if x<=5:
        root.title(f'Спроба {x}')
        user_num = ent_vgadai.get()
        if user_num.isdigit():
            if int(user_num) == chuslo:
                lab_win['text']='Ви вгадали число!'
                lab_win['bg'] = 'lime'
                lab_win.place(x=80, y=200)
                restart(ent_vgadai,lab_vgadai, but_perevirka)
            elif int(user_num)<chuslo:
                lab_win['text']='Згенероване число є більше!'
                lab_win['bg'] = 'yellow'
                lab_win.place(x=80, y=200)
            elif int(user_num)>chuslo:
                lab_win['text']='Згенероване число є менше!'
                lab_win['bg'] = 'cyan'
                lab_win.place(x=80, y=200)
        else:
            messagebox.showinfo('ERROR', 'Ви ввели не ціле число!')
    else:
        restart(ent_vgadai,lab_vgadai, but_perevirka)
lab_win = Label(text='', font=(None, 10),relief='solid', width=30, height=3,bg='lime')
lab_win.place_forget()
but_generation=Button(text='Згенерувати число', command=random_chuslo, font=(None,10),relief='solid',bg='orange')
but_generation.place(x=125,y=80)
ent_poc=Entry(font=(None, 10),relief='solid')
ent_poc.place(x=180,y=3)
lab_poc=Label(text='Введіть початкову межу: ',font=(None, 10))
lab_poc.place(x=1,y=1)
lab_kin=Label(text='Введіть кінцеву межу: ',font=(None, 10))
lab_kin.place(x=1,y=50)
ent_kin=Entry(font=(None, 10),relief='solid')
ent_kin.place(x=180,y=53)
def restart(ent_vgadai, lab_vgadai, but_perevirka):
    res = messagebox.askquestion('ПЕРЕЗАПУСК', 'Ви бажаєте розпочати гру заново?')
    if res == 'yes':
        global x
        root.title('Вгадай число')
        ent_poc.delete(0, 'end')
        ent_kin.delete(0, 'end')
        lab_win.place_forget()
        ent_vgadai.place_forget()
        lab_vgadai.place_forget()
        but_perevirka.place_forget()
        x = 0
    else:
        root.destroy()
root.mainloop()


