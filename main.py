from tkinter import *

app=Tk()
app.title("Gestiune facultate")
app.geometry('1000x500')

#functie de test
def printeaza():
    print('da')

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
    variable = StringVar(app)
    variable.set("Selecteaza o optiune")  # default value
    w = OptionMenu(app, variable, "Selecteaza o optiune", "Adauga in gestiune", "Sterge din gestiune")
    w.pack()

def build():
    interface()
    app.mainloop()

if __name__=='__main__':
    build()