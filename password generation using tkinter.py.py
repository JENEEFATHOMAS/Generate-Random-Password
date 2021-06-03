from tkinter import *                                   #import libraries
from random import *


root=Tk()                                                         #initialize window
root.title('Generate random password')
root.geometry("500x600")


def gen_pass():                                                     # function to generate password
    gen_entry.delete(0,END)                                #clear the entry box
    pass_len=int(my_entry.get())                         #get password length

    password=[]                                                       #initialize empty string
    for i in range(pass_len):                                  #loop till the length
        password += chr(randint(33,126))
    gen_entry.insert(0,password)                          #return the random password

def copy_pass():                                                    #function to copy
    root.clipboard_clear()                                       #clear the clipboard
    root.clipboard_append(gen_entry.get())          #copy

    
label= LabelFrame(root, text="Enter number of Characters")            #create label frame
label.pack(pady=20)

my_entry = Entry(label, font=("Arial"))                                                #create input entry box
my_entry.insert(0,'Password length')                                                     #optional
my_entry.pack(padx=20, pady=20)

gen_entry= Entry(root,font=("Arial"))                                                #create output entry box
gen_entry.pack(pady=20)

frame=Frame(root, bg="black", bd=2)                                                 # create frame for buttons
frame.pack(pady=10)

button=Button(frame,text="Generate Password",command=gen_pass)  # create generate button
button.grid(row=0,column=0,padx=20)

copy_button=Button(frame,text="Copy to Clipboard",command=copy_pass)   #create copy button
copy_button.grid(row=0, column=1,padx=20)

#root.mainloop()
