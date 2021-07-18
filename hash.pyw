import random
from tkinter import *
from tkinter import messagebox

## ROOT

root = Tk()

root.config(width="640", height="480")
root.title("Generate Hash")
root.resizable(False, False)

# FRAME

container = Frame(root, height="480", width="640")
container.config(background="lightyellow", padx=280, pady=120)
container.pack()

### OPTIONS

string = ""
amountInt = 0

justLowerCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
justUpperCharacters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
justNumbersCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
justSymbolsCharacters = ["@", "%", "#", "!", "&", "$", "?", '"', "'", "°", "¬", "|", "/", "(", ")", "=", "¨", "´", "*", "+", "~", "[", "]", "{", "}", "^", "`", "-", "_", ".", ":", ";", ",", "<", ">"]

lowerChech = IntVar()
upperChech = IntVar()
numberChech = IntVar()
symbolChech = IntVar()

completList = []

# AMOUNT

lowerText = Label(container, text="AMOUNT OF CHARACTERS", bg="lightblue", fg="#fff", font=("Georgia", 16), justify="left")
lowerText.grid(row=0, column=0, pady=12, padx=8)
amountCharacters = Entry(container, width=4, justify="center", font=("Georgia", 18))
amountCharacters.insert(END, 16)
amountCharacters.grid(row=0, column=1, pady=12, padx=8)

def amount():
    global string
    global completList

    if(lowerChech.get() == 0 and upperChech.get() == 0 and numberChech.get() == 0 and symbolChech.get() == 0):
        messagebox.showerror("ERROR", "You have select at least one option.")

    if lowerChech.get() == 1 and upperChech.get() == 0 and numberChech.get() == 0 and symbolChech.get() == 0:
        completList.extend(justLowerCharacters)
    elif lowerChech.get() == 0 and upperChech.get() == 1 and numberChech.get() == 0 and symbolChech.get() == 0:
        completList.extend(justUpperCharacters)
    elif lowerChech.get() == 0 and upperChech.get() == 0 and numberChech.get() == 1 and symbolChech.get() == 0:
        completList.extend(justNumbersCharacters)
    elif lowerChech.get() == 0 and upperChech.get() == 0 and numberChech.get() == 0 and symbolChech.get() == 1:
        completList.extend(justSymbolsCharacters)
    elif lowerChech.get() == 1 and upperChech.get() == 1 and numberChech.get() == 0 and symbolChech.get() == 0:
        completList.extend(justLowerCharacters)
        completList.extend(justUpperCharacters)
    elif lowerChech.get() == 0 and upperChech.get() == 0 and numberChech.get() == 1 and symbolChech.get() == 1:
        completList.extend(justNumbersCharacters)
        completList.extend(justSymbolsCharacters)
    elif lowerChech.get() == 1 and upperChech.get() == 0 and numberChech.get() == 1 and symbolChech.get() == 0:
        completList.extend(justLowerCharacters)
        completList.extend(justNumbersCharacters)
    elif lowerChech.get() == 0 and upperChech.get() == 1 and numberChech.get() == 0 and symbolChech.get() == 1:
        completList.extend(justUpperCharacters)
        completList.extend(justSymbolsCharacters)
    elif lowerChech.get() == 1 and upperChech.get() == 0 and numberChech.get() == 0 and symbolChech.get() == 1:
        completList.extend(justLowerCharacters)
        completList.extend(justSymbolsCharacters)
    elif lowerChech.get() == 0 and upperChech.get() == 1 and numberChech.get() == 1 and symbolChech.get() == 0:
        completList.extend(justUpperCharacters)
        completList.extend(justNumbersCharacters)
    elif lowerChech.get() == 1 and upperChech.get() == 1 and numberChech.get() == 1 and symbolChech.get() == 0:
        completList.extend(justLowerCharacters)
        completList.extend(justUpperCharacters)
        completList.extend(justNumbersCharacters)
    elif lowerChech.get() == 0 and upperChech.get() == 1 and numberChech.get() == 1 and symbolChech.get() == 1:
        completList.extend(justUpperCharacters)
        completList.extend(justNumbersCharacters)
        completList.extend(justSymbolsCharacters)
    elif lowerChech.get() == 1 and upperChech.get() == 0 and numberChech.get() == 1 and symbolChech.get() == 1:
        completList.extend(justLowerCharacters)
        completList.extend(justNumbersCharacters)
        completList.extend(justSymbolsCharacters)
    elif lowerChech.get() == 1 and upperChech.get() == 1 and numberChech.get() == 0 and symbolChech.get() == 1:
        completList.extend(justLowerCharacters)
        completList.extend(justUpperCharacters)
        completList.extend(justSymbolsCharacters)
    elif lowerChech.get() == 1 and upperChech.get() == 1 and numberChech.get() == 1 and symbolChech.get() == 1:
        completList.extend(justLowerCharacters)
        completList.extend(justUpperCharacters)
        completList.extend(justNumbersCharacters)
        completList.extend(justSymbolsCharacters)

    print(completList)

    hash.delete(0, END)
    amountInt = int(amountCharacters.get())

    if amountInt < 1 or amountInt > 99:
        messagebox.showerror("ERROR", "You min amount of charactes is 1 and the max is 99.")
    else: 
        random.shuffle(completList)

        while amountInt > 0:
            string+=completList[6]
            random.shuffle(completList)
            amountInt-=1

        hash.insert(0, string)
        string = ""
        completList = []

# LABELS

lowerText = Label(container, text="INCLUDE LOWERS CHARACTERS", bg="lightblue", fg="#fff", font=("Georgia", 16), justify="left")
lowerText.grid(row=1, column=0, pady=12, padx=8)
checkLower = Checkbutton(container, bg="lightyellow", border="0", variable=lowerChech, onvalue=1, offvalue=0)
checkLower.grid(row=1, column=1)

upperText = Label(container, text="INCLUDE UPPERS CHARACTERS", bg="lightblue", fg="#fff", font=("Georgia", 16), justify="left")
upperText.grid(row=2, column=0, pady=12, padx=8)
checkUpper = Checkbutton(container, bg="lightyellow", border="0", variable=upperChech, onvalue=1, offvalue=0)
checkUpper.grid(row=2, column=1)

numberText = Label(container, text="INCLUDE NUMBERS CHARACTERS", bg="lightblue", fg="#fff", font=("Georgia", 16), justify="left")
numberText.grid(row=3, column=0, pady=12, padx=8)
checkNumber = Checkbutton(container, bg="lightyellow", border="0", variable=numberChech, onvalue=1, offvalue=0)
checkNumber.grid(row=3, column=1)

symbolText = Label(container, text="INCLUDE SYMBOLS CHARACTERS", bg="lightblue", fg="#fff", font=("Georgia", 16), justify="left")
symbolText.grid(row=4, column=0, pady=12, padx=8)
checkSymbol = Checkbutton(container, bg="lightyellow", border="0", variable=symbolChech, onvalue=1, offvalue=0)
checkSymbol.grid(row=4, column=1)

button = Button(container, text="GENERATE", padx=8, pady=4, width=10, bg="yellowgreen", fg="#fff", font=("Georgia", 16), cursor="pirate", border="0")
button.config(command=lambda:amount())
button.grid(row=5, columnspan=2)

### PROGRAMING ###

hash = Entry(container, width=40, justify="center", fg="red", font=("Georgia", 18))
hash.grid(row=6, columnspan=2, pady=12, padx=8)

root.mainloop()


    






