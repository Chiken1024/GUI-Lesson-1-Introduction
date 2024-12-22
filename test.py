from tkinter import *

window = Tk()
window.title("Enter Information")
window.geometry("384x256")
window.config(background = "#222244")


header = Label(window, text = "Enter your information:").place(x = 16, y = 16)

name = Label(window, text = "Name:").place(x = 16, y = 48)
age = Label(window, text = "Age:").place(x = 16, y = 80)
hobbies = Label(window, text = "Hobbies:").place(x = 16, y = 112)
birthDate = Label(window, text = "Birth Date:").place(x = 16, y = 144)
country = Label(window, text = "Country:").place(x = 16, y = 176)

inputName = Entry(window, width = 12).place(x = 96, y = 48)
inputAge = Entry(window, width = 12).place(x = 96, y = 80)
inputHobbies = Entry(window, width = 12).place(x = 96, y = 112)
inputBirthDate = Entry(window, width = 12).place(x = 96, y = 144)
inputCountry = Entry(window, width = 12).place(x = 96, y = 176)

submit = Button(window, text = "Submit").place(x = 16, y = 208)


window.mainloop()