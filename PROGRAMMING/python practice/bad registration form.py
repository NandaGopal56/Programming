from tkinter import *

window=Tk()
window.title('registration')
window['bg']='gray30'

def login():
    username_login=username_entry.get()
    password_login=password_entry.get()

    if username_login in username:
        i=username.index(username_login)
        if password_login==password[i]:
            print('sign up successfull')
        else:
            print('wrong credentials')


def sign_up():

    global username
    global password

    username=[]
    password=[]

    username .append( username_entry.get())
    print(username)
    password.append(password_entry.get())
    print(password)


username_entry=Entry(window,bg='white')
username_entry.pack()

password_entry=Entry(window,bg='white')
password_entry.pack()



login_button=Button(window,bg='blue',text='login',command=lambda :login())
login_button.pack()
sign_up_button=Button(window,bg='blue',text='sing up',command=lambda :sign_up())
sign_up_button.pack()

window.mainloop()