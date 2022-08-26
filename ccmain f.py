from spellchecker import SpellChecker
spell=SpellChecker()
from tkinter import*
from tkinter import messagebox

root=Tk()
root.title('Caesar Cipher')
root.geometry('600x600')
root.resizable(0, 0)
canvas=Canvas(root,width=600,height=600,bg='azure3')
canvas.pack()

l1=Label(root,text='Enter the text',bg='light blue')
canvas.create_window(300,100,window=l1)

l2=Label(root,text='Enter the value of key',bg='lightgreen')
canvas.create_window(300,175,window=l2)


y=StringVar()
digit=StringVar()

e1=Entry(root,width=25,textvariable=y,bd=3)
canvas.create_window(300,125,window=e1)
e1.focus_set()

e2=Entry(root,width=5,bd=3,textvariable=digit)
canvas.create_window(300,200,window=e2)

l3=Label(root,text='Choose operation',bg='pink')
canvas.create_window(300,250,window=l3)

l4 = Label(root)
l5 = Label(root)
l6 = Label(root)
btn1 = Button(root)
btn2 = Button(root)

image3=PhotoImage(file='btnc.png')
image4=PhotoImage(file='btnc.png')
image5=PhotoImage(file='btnc.png')

clrBtn1=Button(root,text='clear',padx=0,pady=1,command=lambda:resetd(l4),image=image4,bd=1)
canvas.create_window(100,300,window=clrBtn1)
clrBtn2=Button(root,text='clear',padx=0,pady=1,command=lambda: resetd(l5),image=image5,bd=1)
canvas.create_window(100,400,window=clrBtn2)

Font_tuple = ("Courier New", 10)
clrBtn1.configure(font= Font_tuple)
clrBtn2.configure(font= Font_tuple)

Font_tuple1 = ("Century Gothic", 12)
l1.configure(font= Font_tuple1)
l2.configure(font= Font_tuple1)
l3.configure(font= Font_tuple1)
Font_tuple3 = ("Century Gothic", 11)



def clear():
    y.set('')

def next_shift (e):
    e2.focus_set()
e1.bind('<Return>',next_shift)
    
    

def copyText(t):
    root.clipboard_clear()
    root.clipboard_append(t)
    root.update()

def resetd(id):
    id.destroy()


def encrypt():
    if e1.get()=='':
        messagebox.showinfo('Warning','Enter the text')
    x=e1.get()
    b=e2.get()
    if b.isdigit()==False:
        messagebox.showinfo('Warning','Enter an integer value for key')
        digit.set('')
    y=int(e2.get())    
    r=''
    for i in x:
        if i.isupper():
            r+=chr((ord(i)-65+y)%26+65)
        elif i.isspace():
            r+=i
        elif i.isdigit() :
            r+=chr((ord(i)-48+y)%10+48)
        else:
            r+=chr(((ord(i)-97+y)%26)+97)
    b2['state']=DISABLED
    global l4, btn1
    l4.destroy()
    l4=Label(root,text=r,bg='yellow')
    canvas.create_window(300,350,window=l4)
    btn1 = Button(root, text = 'copy', padx=0, pady=1, command =copyText(r))
    canvas.create_window(400, 350, window = btn1)
    btn1.configure(font= Font_tuple)
    l4.configure(font= Font_tuple3)
    return r


    
def decrypt() :
    if e1.get() == '' or e2.get() == '':
        return
    x=e1.get()
    y=int(e2.get())
    r=''
    for i in x:
        if i.isupper():
            r+=chr((ord(i)-65-y)%26+65)
        elif i.isspace():
            r+=i
        elif i.isdigit() :
            r+=chr((ord(i)-48-y)%10+48)
        else:
            r+=chr((ord(i)-97-y)%26+97)
    global l5, btn2
    l5.destroy()
    l5=Label(root,text=r,bg='yellow')
    canvas.create_window(300,450,window=l5)
    btn2 = Button(root, text = 'copy', padx=0, pady=1, command =copyText(r))
    canvas.create_window(400, 450, window = btn2)
    btn2.configure(font= Font_tuple)
    l5.configure(font= Font_tuple3)
    return r


def decrypt1():
    l,v,k=[],[],[]
    x=e1.get()
    x.lower()
    x=list(x)
    b=''
    for i in range(1,27):
        for i in range(0,len(x)):
            if ord(x[i])>96 and ord(x[i])<123:
                if ord(x[i])<122:
                    b=chr(ord(x[i])+1)
                    x[i]=b
                else:
                    x[i]='a'
        r=''.join(x)
        l.append(r)
    for i in l:
        i=i.split(' ')
        j=spell.known(i)
        
        v.append(len(j))
    for i in range(0,len(v)):
        if v[i]==max(v):
            k.append(i)
    
    for i in range(0,len(k)):
        global l6
        l6.destroy()
        l6=Label(root,text=l[k[i]],bg='yellow')
        canvas.create_window(300,550,window=l6)
        l6.configure(font= Font_tuple3)
        
    return l[k[i]]
def reset():
    l=[l4,l5,l6]
    btns = [btn1, btn2]
    for i in range(len(l)):
        try:
            l[i].destroy()
        except:
            print("No label: " + l[i])

    for i in range(len(btns)):
        try:
            btns[i].destroy()
        except:
            print("No button: " + btns[i])

    e1.delete(0, END)
    e2.delete(0,END)
    b2['state']=NORMAL
    e1.focus_set()
image=PhotoImage(file='enc.png')
image1=PhotoImage(file='dec.png')
image2=PhotoImage(file='decw3.png')
image3=PhotoImage(file='btnc.png')

c1=Button(root,text='Clear',command=clear,image=image3,bd=1)
b1=Button(root,text='Encryption',command=encrypt,borderwidth=0,image=image)
b2=Button(root,text='Decryption',command=decrypt,image=image1,bd=0)
b3=Button(root,text='Decryption without a key',command=decrypt1,bd=2,image=image2)
b4=Button(root,text='Reset',padx=15,pady=10,command=reset)


canvas.create_window(420,125,window=c1)
canvas.create_window(300,300,window=b1)
canvas.create_window(300,400,window=b2)
canvas.create_window(300,500,window=b3)
canvas.create_window(550,550,window=b4)

Font_tuple2 = ("Century Gothic", 12)
b1.configure(font= Font_tuple2)
b2.configure(font= Font_tuple2)
b3.configure(font= Font_tuple2)
c1.configure(font= Font_tuple)
b4.configure(font= Font_tuple)

root.mainloop()
    
    





