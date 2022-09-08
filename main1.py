from tkinter import *

root = Tk()
root.title("Encryption")

root.geometry("500x500")
root.configure(background = "snow")

enter_word = Entry(root)
enter_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label = Label(root, text = "Name in Ascii : ", bg = "light yellow", fg = "black")
label2 = Label(root, text = "Encrypted Name : ", bg = "light yellow", fg = "black")

def asciiConverter():
    input_word = str(enter_word.get())
    
    for letter in input_word:
        label["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2["text"] += str(chr(encrypted))
        
btn = Button(root, text = "Show Name In Ascii", command = asciiConverter, bg = 'gold', fg = 'black')
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()