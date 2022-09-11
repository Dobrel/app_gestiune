from tkinter import *
#global variable

#interfata principala
app=Tk()
app.title("Gestiune facultate")
app.geometry('1000x500')

#interfata adaugare
def interfata_adaugare():
    app_aduagare=Tk()
    app_aduagare.title("Adauga un obiect in gestiune")
    app_aduagare.geometry("1000x500")

#interfata stergere

#functie de test
def printeaza(choice):
    choice=variable.get()
    return choice

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
    #select_buton=Button(app,text="Alege",command=printeaza).pack(side=TOP)

def build():
    interface()
    app.mainloop()

if __name__=='__main__':
    build()