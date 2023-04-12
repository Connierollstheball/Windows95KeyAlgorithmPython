import os
import tkinter
from tkinter import messagebox

print('Product Key Format: xxx-xxxxxxx')
productkey = input('Insert your Windows 95 product key --> ')

if len(productkey) != 11:
   print('X')

prodkeyfirst = int(productkey[0:3])
dashcheck = productkey[3]
prodkeysecond = productkey[4:11]

if prodkeyfirst != 333 and prodkeyfirst != 444 and prodkeyfirst != 555 and prodkeyfirst != 666 and prodkeyfirst != 777 and prodkeyfirst != 888 and prodkeyfirst != 999:
    print('V')
    if dashcheck == '-':
        print('V')
        valueone = int(prodkeysecond[0])
        valuetwo = int(prodkeysecond[1])
        valuethree = int(prodkeysecond[2])
        valuefour = int(prodkeysecond[3])
        valuefive = int(prodkeysecond[4])
        valuesix = int(prodkeysecond[5])
        valueseven = int(prodkeysecond[6])
        if valueone != 9 and valuetwo != 9 and valuethree != 9 and valuefour != 9 and valuefive != 9 and valuesix != 9 and valueseven != 9:
            print('V')
            sumvalue = valueone + valuetwo + valuethree + valuefour + valuefive + valuesix + valueseven
            if sumvalue % 7 == 0:
                print('---------------------')
                print('product key valid')
                tkinter.messagebox.showinfo("Windows 95 Product Key Algorithm", "The Key you introduced is valid and would work on a Windows 95 Setup.")
                exit()
            else:
                print('X')
                tkinter.messagebox.showerror("Windows 95 Product Key Algorithm", "The Key you introduced is invalid. Please try again.")
                exit()
        else:
            print('X')
            tkinter.messagebox.showerror("Windows 95 Product Key Algorithm", "The Key you introduced is invalid. Please try again.")
            exit()
    else:
        print('X')
        tkinter.messagebox.showerror("Windows 95 Product Key Algorithm", "The Key you introduced is invalid. Please try again.")
        exit()
else:
    print('X')
    tkinter.messagebox.showerror("Windows 95 Product Key Algorithm", "The Key you introduced is invalid. Please try again.")
    exit()
