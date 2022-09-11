from tkinter import *
#global variable
#global choice

#interfata principala
app=Tk()
app.title("Gestiune facultate")
app.geometry('1000x500')

#interfata adaugare
def interfata_adaugare():
    app_adaugare=Tk()
    app_adaugare.title("Adauga un obiect in gestiune")
    app_adaugare.geometry("1000x500")

#interfata stergere
def interfata_stergere():
    app_stergere=Tk()
    app_stergere.title("Sterge un obiect din gestiune")
    app_stergere.geometry("1000x500")

#functie de test
def printeaza(choice):
    choice=variable.get()
    if choice=='Adauga in gestiune':
        interfata_adaugare()
    else:
        interfata_stergere()

'''def interface():
    adaug_buton=Button(app, text='Adauga obiect', command=printeaza)
    sterge_buton=Button(app, text='Sterge obiect', command=printeaza)
    adaug_label=Label(app,text='Introduceti ')
    adaug_entry=Entry(app)
    #adaug_bbuton.place(x=10,y=10)
    #sterge_buton.place(x=10,y=50)
    adaug_label.place(x=10,y=10)
'''

def interface():
    global variable
    variable = StringVar()
    variable.set("Selecteaza o optiune")  # default value
    optiuni=["Selecteaza o optiune", "Adauga in gestiune", "Sterge din gestiune"]
    option_menu = OptionMenu(app, variable, *optiuni, command=printeaza)
    option_menu.pack()

def build():
    interface()
    app.mainloop()

if __name__=='__main__':
    build()