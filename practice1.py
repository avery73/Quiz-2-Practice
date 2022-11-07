# Identify and update the code below to accomplish the following tasks:

# 1) Rearrange the widgets in the window so that it looks like the picture provided and add any necessary widgets. ✅
#    Fix the frame size ✅
# 2) Change the title of the dialog box from 'Quiz II' to 'Breakfast Diner Delivery App Order' ✅
# 3) Change the default option for the radio button to Pancakes (when the programs starts up) ✅
# 4) Fix the buttons (not currently working) ✅
# 5) Add a label and input box (to the top frame) where the user can enter in the address of the delivery ✅
# 6) The review order button should then display the address, total cost of the food, 
#    as well as a random delivery time between 20 and 100 minutes 

import tkinter
import tkinter.messagebox
import random

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.geometry('350x300')
        self.main_window.title("Breakfast Dinner Delivery App")

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #address
        self.address = tkinter.Label(self.top_frame,text="Delivery Address:")
        self.address_entry = tkinter.Entry(self.top_frame)
        self.address.pack(side="left")
        self.address_entry.pack(side="left")
        
        #entrees - RADIO BUTTONS
        self.var = tkinter.IntVar()
        self.var.set(1)
     
        self.entree_label = tkinter.Label(self.mid_frame,text='Select an entree', font=('',20))

        self.entree1 = tkinter.Radiobutton(self.mid_frame,text='Pancakes ($8)',variable=self.var,value=8)
        self.entree2 = tkinter.Radiobutton(self.mid_frame,text='Waffle ($9)',variable=self.var,value=9)
        self.entree3 = tkinter.Radiobutton(self.mid_frame,text='English Breakfast ($5)',variable=self.var,value=5)

        self.entree1.select()

        self.entree_label.pack()
        self.entree1.pack()
        self.entree2.pack()
        self.entree3.pack()

        #sides - CHECK BUTTONS
        self.side_label = tkinter.Label(self.mid_frame,text='Select your sides',font=('',20))

        self.sidevar1 = tkinter.IntVar()
        self.sidevar2 = tkinter.IntVar()
        self.sidevar3 = tkinter.IntVar()

        self.sidevar1.set(0)
        self.sidevar2.set(0)
        self.sidevar3.set(0)

        self.side1 = tkinter.Checkbutton(self.mid_frame,text='Hashbrowns ($1.50)',variable=self.sidevar1)
        self.side2 = tkinter.Checkbutton(self.mid_frame,text='Sausage ($2.20)',variable=self.sidevar2)
        self.side3 = tkinter.Checkbutton(self.mid_frame,text='Bacon ($2.25)',variable=self.sidevar3)

        self.side_label.pack()
        self.side1.pack()
        self.side2.pack()
        self.side3.pack()

        #buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='Review Order', command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
       
        tkinter.mainloop()

    #function
    def calculate(self):
            # Display the message in an info dialog box.
        try:
            price = float(self.var.get())
            if float(self.sidevar1.get()) == 1:
                price += 1.5
            if float(self.sidevar2.get()) == 1:
                price += 2.2
            if float(self.sidevar3.get()) == 1:
                price += 2.25
            tkinter.messagebox.showinfo(title="Delivery Time",message=f"Delivery Address: {self.address_entry.get()} \n Cost: {price} \n\n Your food will arrive in approximately {random.randint(20,100)} minutes",icon="info")
        except:
            pass

my_gui = MyGUI()