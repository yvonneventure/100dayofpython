from tkinter import *   #import all the CONSTANTS and Classes
from tkinter import messagebox   #messagebox is not a Class, just a module, that's why we have to import again
import random
import pyperclip  #copy to clipboard
import json

#---------------Password Generator ---------#

#Password Generator Project from Day 5
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwordletters=[random.choice(letters) for _ in range(random.randint(8, 10))]
    passwordnum=[random.choice(numbers) for _ in range(random.randint(2, 4))]
    passwordsymbol=[random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = passwordletters+passwordsymbol+passwordnum
    #random.shuffle(password_list)

    newpass = "".join(password_list)
    password.insert(0,newpass)
    pyperclip.copy(newpass)



#-------------------- Save Password -------------#
def save():
    web= website.get()
    name=username.get()
    pw = password.get()
    new_data ={
        web:{
        "email":name,
        "password": pw,
        }
    }

    if len(web)==0 or len(pw)==0:

        messagebox.showinfo(title="Oops",message="please don't leave any fields empty!")
    else:
        try:
            f=open("data.json",mode="r")

        except FileNotFoundError:
            pass
        else:
            with open("data.json", mode="r") as data:
                #read old data
                content=json.load(data)
                #update old data with new data added to the dictionary
                content.update(new_data)
        finally:
        #save the updated data
            with open("data.json",mode="w") as data:
                json.dump(new_data,data,indent=4)
                delete()
def search():

    try:
        # read old data
        with open("data.json", mode="r") as data:
            content = json.load(data)
    except FileNotFoundError:
        f=open("data.json", mode="w")
        messagebox.showinfo(title="alert", message="No data file exists")
        f.close()
    else:
        web=website.get()
        if web in content:
            messagebox.showinfo(title=f"{website.get()}",message=f"Email: {content[web]['email']}\n Passoword : {content[web]['password']}")
        else:
            messagebox.showinfo(title="alert",message="website doesn't exist")
def delete():
    website.delete(0,END)
    username.delete(0,END)
    password.delete(0,END)

#-------------------- UI Set Up------------------#

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)   # position of the image
canvas.grid(column=1,row=0)

#Create labels:
web_label=Label(text="Website: ")
user_label = Label(text="Email/Username: ")
pass_label = Label(text="Password: ")
web_label.grid(column=0,row=1)
user_label.grid(column=0,row=2)
pass_label.grid(column=0,row=3)


#create entries for website, email/user name and password
website = Entry(width =17)
username = Entry(width =35)
password = Entry(width =17)
website.grid(column=1,row=1)
website.focus()   #put a cursor in the entry box
username.grid(column=1,row=2,columnspan=2)
username.insert(END, string="Your email")
password.grid(column=1,row=3)

#create buttons
gen_pass = Button(text="Generate Password",width =14,command=generate_password)
search_button=Button(text="Search", width =14,command=search)
add_button =Button(text="Add",width=34, command=save)
gen_pass.grid(column=2,row=3)
search_button.grid(column=2,row=1)
add_button.grid(column=1,row=4,columnspan=2)






window.mainloop()