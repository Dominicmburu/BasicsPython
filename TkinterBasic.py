from tkinter import *

root = Tk()
root.title("Hello World")
root.geometry("400x400")

def clicked():
    my_label.config(text="You clicked me")

def entry():
    my_label.config(text=my_input.get())

## LABELS
my_label = Label(root, text="Hello World", fg="green", bg="white", font=("Helvtica", 32), relief="ridge", state="disabled", height=5, width=10, padx=1, pady=2)
my_label.grid(column=0, row=0, sticky=W, columnspan=2)

## BUTTON
my_button = Button(root, text="Click me", command=entry)
my_button.grid(column=0, row=1, sticky=W)

## Entry
my_input = Entry(root, width=30, font=("Aria", 20))
my_input.grid(column=1, row=1, pady=20)

## ICONS






root.mainloop()




