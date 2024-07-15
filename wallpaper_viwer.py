from tkinter import *
from PIL import ImageTk,Image
import os

def rotate_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter= counter+1


counter=1
root=Tk()
root.title("Image Viwer")

root.geometry('380x480')
root.configure(background='black')

file = os.listdir('wallpaper')

img_array=[]
for item in file:
    img=Image.open(os.path.join('wallpaper',item))
    resized_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label=Label(root,image=img_array[0])
img_label.pack(pady=(15,10))

email_label=Label(root,text='Click "Next" for another image',fg='#fffaf0',bg='black')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',14))


next_btn=Button(root,text='Next',bg='white',fg='black', width=18,height=1, command=rotate_img)
next_btn.pack()
next_btn.config(font=('bardana',14,'bold'))

root.mainloop()
