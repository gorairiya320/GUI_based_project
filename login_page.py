from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
    email=email_input.get()
    password=password_input.get()
    
    if email=='riya@gmail.com'and password=='1234':
        messagebox.showinfo('login','login successfully')
    else:
        messagebox.showerror('Error','login failed')


root=Tk()
root.title('Login Form')
root.geometry('350x500')

root.configure(background='#728fce')


img=(Image.open('robo.jpg'))
resized_img=img.resize((100,100))
img= ImageTk.PhotoImage(resized_img)


img_label=Label(root,image=img)
img_label.pack(pady=(10,10))

text_Label=Label(root,text='Robotics club',fg='#fffaf0',bg='#728fce')
text_Label.pack()
text_Label.config(font=('bakery',24,'bold'))

email_label=Label(root,text='Enter your mail here',fg='#fffaf0',bg='#728fce')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',14))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))



password_label=Label(root,text='Enter your password here',fg='#fffaf0',bg='#728fce')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',14))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn=Button(root,text='login here',bg='#fffaf0',fg='black',width=18,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',8,'bold'))


root.mainloop()