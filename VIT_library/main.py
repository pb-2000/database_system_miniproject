from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from admin import admin  
from ViewBooks import *

def open_window(user_type):
    if user_type == "admin":
        admin()  
    # elif user_type == "student":
        
# root = Tk()
# Create a login screen
def login_screen():
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Take n greater than 0.25 and less than 5
    same=True
    n=0.25

    # Adding a background image
    background_image =Image.open("lib2.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
        
    # background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to\nVIT Library", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Admin",bg='black', fg='white', command=admin)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    vertical_space = 0.18    
    btn2 = Button(root,text="Student",bg='black', fg='white', command=View)
    # btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1, anchor='n', pady=vertical_space)
    btn2.place(relx=0.28, rely=0.4 + vertical_space, relwidth=0.45, relheight=0.1)

    root.mainloop()

login_screen()  # Call the login screen function

# root.mainloop()
