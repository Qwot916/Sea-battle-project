from tkinter import *
import random
field = []
q = input()
q = int(q, base=10)
click_number = 0
a = 0
b = 0
shots = input()
shots = int(shots, base=10)
def boom():
     global a, b, shots
     a = steel.get()
     b = run.get()
     guess_row = b-1
     guess_col = a-1
     if shots<=0:
          gyro['text'] = "you are out of shots"
     elif guess_row == ship_row and guess_col == ship_col:
          gyro['text'] = "win"
          sbr['text'] = shots-1
          field[guess_row][guess_col] = "W"
          tusk.delete('1.0', END)
          tusk.insert(1.0, field)
     else:
          gyro['text'] = "miss"
          field[guess_row][guess_col] = "X"
          sbr['text'] = shots-1
          tusk.delete('1.0', END)
          tusk.insert(1.0, field)
     shots = shots-1
def button_clicked():
     global click_number
     gyro['text'] = base[click_number]
     click_number = click_number+1
for x in range(q):
     field.append(["0"] * q)
def random_row(field):
     return random.randint(0, len(field) - 1)
def random_col(field):
     return random.randint(0, len(field[0]) - 1)
ship_row = random_row(field)
ship_col = random_col(field)
print(ship_col + 1, ship_row + 1)
root = Tk()
root.configure(bg='blue')
root.title("THE morskoy boi")
root.geometry('800x600+600+100')
root.grab_set
gyro = Button()
gyro.configure(bg='red', fg='yellow', text='click', command=boom, width=15, height=3)
gyro.place(relx=0.5, x=-40, rely=0)
zepp = Label(text="Shots left:", fg='blue')
zepp.place(relx=0.5, rely=0.1)
steel = Scale(orient=HORIZONTAL, length=300, from_=1, to=q, tickinterval=1, resolution=1)
steel.place(relx=0.5, rely=0.2, x=-150)
run = Scale(orient=VERTICAL, length=300, from_=1, to=q, tickinterval=1, resolution=1)
run.pack(side='left')
tusk = Text(root, bd=2, height=q, width=2*q+2)
tusk.insert(1.0, field)
tusk.place(relx=0.5, rely=0.5, x=-8*q-8, y=-8*q)
sbr = Label(text=shots)
sbr.place(relx=0.6, rely=0.1)
root.mainloop()
