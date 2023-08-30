from tkinter import *
from tkinter import messagebox


#Defining Function for BMI

def calculate_bmi():
    weight = float(entry.get())
    height = float(entry1.get())
    bmi = round(weight / height ** 2)
    if bmi < 18.5:
        messagebox.showinfo(title="Title", message= f"your bmi is {bmi}, You are under weight")
    elif bmi < 25:
        messagebox.showinfo(title="Title", message= f"Your bmi is {bmi}, You have a normal weight")
    elif bmi < 30:
        messagebox.showinfo(title="Title", message=f"Your bmi is {bmi}, you are overweight ")
    elif bmi < 35:
        messagebox.showinfo(title="Title", message=f"your bmi is {bmi}, you are obese")
    else:
        messagebox.showinfo(title="Title", message=f"your bmi is {bmi}, You are severely obese ")


windows = Tk()
windows.title("Welcome to the Body Mass Index")
windows.minsize(width=150, height=150)
windows.config(padx=70, pady=70)
windows.config(bg="gray")


canva = Canvas(height=200, width=200)
img = PhotoImage(file="bmi.png")
canva.create_image(100, 100, image=img)
canva.grid(column=0, row=0, columnspan=2)

label = Label(text="Weight")
label.grid(column=0, row=1)

label1 = Label(text="Height")
label1.grid(column=0, row=2)

entry = Entry(width=20)
entry.focus()
entry.grid(column=1, row=1)
print(entry)

entry1 = Entry(width=20)
entry1.grid(column=1, row=2)
print(entry1)

button = Button(text="Check", command=calculate_bmi)
button.grid(row=4, column=1)


mainloop()