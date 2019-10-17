from tkinter import *


def convert():
    celsius = float(c1.get())
    e2['text'] = f'{273.15+celsius:.2f}ºK'
    e3['text'] = f'{1.8*celsius+32:.2f}ºF'
    farenheit = float(f1.get())
    e4['text'] = f'{(farenheit-32)/1.8:.2f}ºC'
    e5['text'] = f'{((farenheit-32)/1.8)+273.15:.2f}ºK'
    kelvin = float(k1.get())
    e6['text'] = f'{kelvin-273.15:.2f}ºC'
    e7['text'] = f'{(kelvin-273.15)*1.8+32:.2f}ºF'


def ajuda():
    top = Toplevel()
    top.geometry('200x65')
    top.title('?')
    top.wm_iconbitmap('conversor_icon.ico')
    top.resizable(False, False)
    Label(top, text='Conversor de temperaturas', justify='center').place(x=25, y=0)
    Label(top, text='Por: Wesley Dias', justify='center').place(x=25, y=20)
    Label(top, text='Github: WeDias', justify='center').place(x=25, y=40)
    top.grab_set()


janela = Tk()
janela.title('Conversor V0.1')
janela.geometry('298x105')
janela.wm_iconbitmap('conversor_icon.ico')
janela.resizable(False, False)
Label(janela, text='ºC').place(x=65, y=0)
c1 = Entry(janela, width=10, justify='right')
c1.place(x=0, y=0)
c1.insert(0, 0)
e2 = Label(janela, width=15)
e2.place(x=100, y=0)
e3 = Label(janela, width=15)
e3.place(x=200, y=0)
Label(janela, text='ºF').place(x=65, y=30)
f1 = Entry(janela, width=10, justify='right')
f1.place(x=0, y=30)
f1.insert(0, 0)
e4 = Label(janela, width=15)
e4.place(x=100, y=30)
e5 = Label(janela, width=15)
e5.place(x=200, y=30)
Label(janela, text='ºK').place(x=65, y=60)
k1 = Entry(janela, width=10, justify='right')
k1.place(x=0, y=60)
k1.insert(0, 0)
e6 = Label(janela, width=15)
e6.place(x=100, y=60)
e7 = Label(janela, width=15)
e7.place(x=200, y=60)
btajuda = Button(text='?', width=10, command=ajuda).place(x=0, y=81)
bt = Button(janela, width=30, text='Converter', command=convert)
bt.place(x=80, y=80)
convert()
janela.mainloop()
