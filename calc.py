try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# Janela principal
jcalc = tkinter.Tk()
jcalc.title("RPyN Calc")
jcalc.geometry('208x300+100+100')
jcalc.columnconfigure(0, weight=1)
jcalc.rowconfigure(0, weight=1)
jcalc.resizable(False, False)

frmbt = tkinter.Frame(jcalc)
frmbt.grid(row=2, column=0, sticky='new')

# Variaveis
pilha = []

usedPm = tkinter.BooleanVar()
usedPm.set(False)

usedDot = tkinter.BooleanVar()
usedDot.set(False)

disResp = tkinter.StringVar()
disResp.set("")

# Funcoes


def digito(dig):
    disp.insert("end", str(dig))


def pm(sig):
    if not usedPm.get():
        disp.insert(0, str(sig))
        usedPm.set(True)
    else:
        disp.delete(0)
        usedPm.set(False)


def dot(doti):
    if not usedDot.get():
        disp.insert("end", str(doti))
        usedDot.set(True)


def cls():
    disp.delete(0, 'end')
    usedDot.set(False)
    usedPm.set(False)
    pilha.clear()
    disPilha.delete(0, "end")


def clsce():
    if disp.get() != '':
        disp.delete(0, 'end')
        usedDot.set(False)
        usedPm.set(False)
    else:
        pilha.pop()
        mkpilha()


def ent():
    if disp.get() != '':
        pilha.append(disp.get())
        print(pilha)
        disp.delete(0, 'end')
        usedDot.set(False)
        usedPm.set(False)
        mkpilha()


def mkpilha():
    disPilha.delete(0, "end")
    for lista in pilha:
        disPilha.insert(tkinter.END, lista)


def soma():
    ent()
    a = float(pilha[-2]) + float(pilha[-1])
    pilha.pop()
    pilha.pop()
    pilha.append(str(a))
    mkpilha()


def sub():
    ent()
    a = float(pilha[-2]) - float(pilha[-1])
    pilha.pop()
    pilha.pop()
    pilha.append(str(a))
    mkpilha()


def mul():
    ent()
    a = float(pilha[-2]) * float(pilha[-1])
    pilha.pop()
    pilha.pop()
    pilha.append(str(a))
    mkpilha()


def div():
    ent()
    a = float(pilha[-2]) / float(pilha[-1])
    pilha.pop()
    pilha.pop()
    pilha.append(str(a))
    mkpilha()


def per():
    ent()
    a = float(pilha[-1]) / 100
    pilha.pop()
    pilha.append(str(a))
    mkpilha()
# display


disPilha = tkinter.Listbox(jcalc, width=1)
disPilha.grid(row=0, column=0, sticky='nsew', rowspan=2)
disPilha.config(border=0, relief='sunken')


disp = tkinter.Entry(jcalc, width=1, textvariable=disResp)
disp.grid(row=1, column=0, sticky='new')


# Botoes de operacoes
btC = tkinter.Button(frmbt, text="C", width=3, command=lambda: cls())
btCe = tkinter.Button(frmbt, text="CE", width=3, command=lambda: clsce())
btPm = tkinter.Button(frmbt, text="+/-", width=3, command=lambda: pm('-'))
btPc = tkinter.Button(frmbt, text="%", width=3, command=lambda: per())
btsum = tkinter.Button(frmbt, text="+", width=3, command=lambda: soma())
btsub = tkinter.Button(frmbt, text="-", width=3, command=lambda: sub())
btmul = tkinter.Button(frmbt, text="x", width=3, command=lambda: mul())
btdiv = tkinter.Button(frmbt, text="/", width=3, command=lambda: div())
bteval = tkinter.Button(frmbt, text="Ent", width=3, command=lambda: ent())
btdot = tkinter.Button(frmbt, text=".", width=3, command=lambda: dot('.'))

# frmbt.bind('<Return>', ent())
# frmbt.bind('<c>', cls())

# Botoes numericos
bt0 = tkinter.Button(frmbt, text="0", width=3, command=lambda: digito(0))
bt1 = tkinter.Button(frmbt, text="1", width=3, command=lambda: digito(1))
bt2 = tkinter.Button(frmbt, text="2", width=3, command=lambda: digito(2))
bt3 = tkinter.Button(frmbt, text="3", width=3, command=lambda: digito(3))
bt4 = tkinter.Button(frmbt, text="4", width=3, command=lambda: digito(4))
bt5 = tkinter.Button(frmbt, text="5", width=3, command=lambda: digito(5))
bt6 = tkinter.Button(frmbt, text="6", width=3, command=lambda: digito(6))
bt7 = tkinter.Button(frmbt, text="7", width=3, command=lambda: digito(7))
bt8 = tkinter.Button(frmbt, text="8", width=3, command=lambda: digito(8))
bt9 = tkinter.Button(frmbt, text="9", width=3, command=lambda: digito(9))

# Mapa dos botoes
btC.grid(row=2, column=0, sticky='e')
btCe.grid(row=2, column=1, sticky='e')
btPm.grid(row=2, column=2, sticky='e')
btPc.grid(row=2, column=3, sticky='e')

bt7.grid(row=3, column=0, sticky='e')
bt8.grid(row=3, column=1, sticky='e')
bt9.grid(row=3, column=2, sticky='e')
btsum.grid(row=3, column=3, sticky='e')

bt4.grid(row=4, column=0, sticky='e')
bt5.grid(row=4, column=1, sticky='e')
bt6.grid(row=4, column=2, sticky='e')
btsub.grid(row=4, column=3, sticky='e')

bt1.grid(row=5, column=0, sticky='e')
bt2.grid(row=5, column=1, sticky='e')
bt3.grid(row=5, column=2, sticky='e')
btmul.grid(row=5, column=3, sticky='e')

bt0.grid(row=6, column=0, sticky='e')
btdot.grid(row=6, column=1, sticky='e')
bteval.grid(row=6, column=2, sticky='e')
btdiv.grid(row=6, column=3, sticky='e')

jcalc.mainloop()
