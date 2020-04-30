import os,loader
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from matplotlib import pyplot as plt
import csv
from PIL import Image,ImageTk

r=[]
q=[]

def clicked():
    r.append(t1.get())
    q.append(c1.get())

def h():
    messagebox.showinfo('covid-graph','->Add countries with first letter capital\n->For multiple entries use ,(comma) between'+
                        '\n->make sure that no whitespace is used in the entry box')
    
def run():
    d={'new deaths':6,'total deaths':5,'new cases':4,'total cases':3}
    l=[]
    l = r[-1].split(',')
    for h in l:
        y=[]
        with open('data.txt','r') as f:
            read = csv.reader(f)
            k = next(read)
            g=[]
            i=0
            for line in read:
                if line[1]==h :
                    g=line[2].split('-')
                    #g=g.split('-')
                    if int(g[1]) >=1 and int(g[0]) == 2020:
                        y.append(int(line[d[q[-1]]]))
                        i+=1
                #else: continue
            x=range(0,i)
        plt.style.use('seaborn')
        plt.plot(x,y,label = h,marker='.')
    
    plt.xlabel('DAYS FROM JANUARY 2020--->')
    plt.ylabel(q[-1]+'--->')
    #plt.grid()
    plt.legend()
    plt.show()

#load content into the file 'data.txt'
os.system('python loader.py') 

#<GUI>
window = Tk()
window.title('COVID19-GRAPHICAL_INFO')
window.geometry('560x340')

load = Image.open('image.jpg')
render = ImageTk.PhotoImage(load)

img = Label(window,image=render)
img.image = render
img.place(x=0,y=0)

b1 = Button(window,text='help',command = h)
b1.place(x=460,y=20)

#l2 = Label(window, text='multiple countries')
#l2.grid(column=2,row=6)

l1 = Label(window, text='countries:')
l1.place(x=150,y=100)

#l3 = Label(window, text='USE comma for')
#l3.grid(column=1,row=6)

t1 = Entry(window, width=20)
t1.place(x=280,y=100)

l2 = Label(window, text='parameter(per day):')
l2.place(x=150,y=150)

c1 = Combobox(window, width=20)
c1.place(x=300,y=150)
c1['values']=('new deaths','total deaths','new cases','total cases')
c1.current(0)

b1 = Button(window, text='apply',command = clicked) 
b1.place(x=290,y=200)

b2 = Button(window, text='RUN',command = run)
b2.place(x=290,y=225)

window.mainloop()
#</GUI>






