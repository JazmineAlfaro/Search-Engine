from tkinter import *
from tkinter.ttk import *
from main2 import fun



root= Tk()



root.title("Buscador de libros")

root.geometry("500x350")





def submit():
	t = StringVar()
	t = my_box.get()
	res = fun(t)
	my_label.config(text=res)

my_box = Entry(root)

my_box.pack(pady=20)



my_label = Label(root,text="")

my_label.pack(pady=20)

my_button = Button(root, text="Subir", command=submit)

my_button.pack(pady=20)


root.mainloop()

