from tkinter import *
import csv
#global variable
#global choice

#interfata principala
app=Tk()
app.title("Gestiune facultate")
app.geometry('200x50')

#adaugare obiecte in inventar
def adauga():
    f=open("gestiune.csv","r")
    r=csv.reader(f)
    line=next(r)
    for i in r:
        for j in i:
            if j==adaug_label.get():
                f.close()
                f = open("gestiune.csv", "w")
                w=csv.writer(f)
                print(j)

#interfata adaugare
def interfata_adaugare():
    global adaug_label
    app_adaugare=Tk()
    app_adaugare.title("Adauga un obiect in gestiune")
    app_adaugare.geometry("1000x500")
    adaug_buton=Button(app_adaugare, text='Adauga obiect', command=adauga)
    adaug_buton.place(x=10, y=10)
    adaug_label=Entry(app_adaugare)
    adaug_label.place(x=150, y=15)

#interfata stergere
def interfata_stergere():
    app_stergere=Tk()
    app_stergere.title("Sterge un obiect din gestiune")
    app_stergere.geometry("1000x500")
    sterge_buton=Button(app, text='Sterge obiect', command=printeaza)
    sterge_buton.place(x=10, y=50)

#functie de alegere a optiunii
def alegere(choice):
    choice=variable.get()
    if choice=='Adauga in gestiune':
        interfata_adaugare()
    else:
        interfata_stergere()

#functie de test
def printeaza():
    print("da")

'''def interface():
    adaug_label=Label(app,text='Introduceti ')
    adaug_entry=Entry(app)
    adaug_label.place(x=10,y=10)
'''

def interface():
    global variable
    variable = StringVar()
    variable.set("Selecteaza o optiune")  # default value
    optiuni=["Selecteaza o optiune", "Adauga in gestiune", "Sterge din gestiune"]
    option_menu = OptionMenu(app, variable, *optiuni, command=alegere)
    option_menu.pack()

def build():
    interface()
    app.mainloop()

if __name__=='__main__':
    build()