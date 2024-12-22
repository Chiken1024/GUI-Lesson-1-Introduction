from tkinter import *

window = Tk()
window.title("Login Window")
window.geometry("384x256")
window.config(background = "#442222")


username = Label(window, text = "Username:").place(x = 16, y = 16)
password = Label(window, text = "Password:").place(x = 16, y = 48)

usernameInput = Entry(window, width = 16).place(x = 96, y = 16)
passwordInput = Entry(window, width = 16).place(x = 96, y = 48)

submit = Button(window, text = "Submit").place(x = 16, y = 80)


window.mainloop()