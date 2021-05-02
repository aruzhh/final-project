from tkinter import *
import csv

filename = 'weather.csv'
f_open = open(filename)
read = csv.reader(f_open, delimiter=',')
data = list(read)
del(data[0])
city = []
date = []
var = []
tem = []
step = 0
for x in range(0, len(data)):
    date.append(data[x][1])
    city.append(data[x][0])

root = Tk()
root.geometry('500x500')
root.title('WEATHER')


def start():
    if ent.get() in city:
        tem_day_label.grid(row=2, column=0)
        tem_night_label.grid(row=3, column=0)
        start_label.grid(row=0, column=1)
        button1.grid(row=1, column=0)
        listbox1.grid(row=0, column=0)
        tem_night_label2.grid(row=3, column=1)
        tem_day_label2.grid(row=2, column=1)
        ent.grid_forget()
        button2.grid_forget()
        for index, y in enumerate(city):
            if ent.get() == y:
                var.append(date[index])
                tem.append(data[index])
                var2 = StringVar(value=var)
                listbox1.config(listvariable=var2)
    else:
        pass

def forecast():
    index = listbox1.curselection()[0]
    tem_day_label2.config(text=tem[index][2])
    tem_night_label2.config(text=tem[index][3])

tem_day_label = Label(root, text='Day Temperature:')
tem_night_label = Label(root, text='Night Temperature:')
start_label = Label(root, text='<-- Choose date')

listbox1 = Listbox(root, listvariable='', width=30)
button1 = Button(root, text='forecast', command=forecast)
button2 = Button(root, text='start', command=start)
button2.grid(row=1, column=0)


ent = Entry(root, width=49)
ent.grid(row=0, column=0)