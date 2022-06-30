import tkinter as tk
import tkinter.ttk as ttk

# Create main window, set title, geometry = 200x400

# Set main label with title 'Registration Form'

# Add a 'frame' after the label

# In the frame add label with title 'Full name' as grid(row = 0, column = 0)

# In the frame add entry at grid (row = 0, column = 1, columnspan = 3)

def processSubmitButton():
    print("runingprocessSubmitButton")
    tk.messagebox.showinfo(title='Successful', message='Form is being submitted successfully.')


mainWindowTitle = "Registraton Form Application"
mainWindowLabel = "Registraton Form"

mainWindow = tk.Tk()
mainWindow.title(mainWindowTitle)
mainWindow.geometry('500x200')
#mainWindow.configure (bg= 'White')


title= tk.Label(mainWindow, text=mainWindowLabel, justify=tk.LEFT)
title.pack()


mainFormFrame = tk.Frame(mainWindow)


formFullNameTitle = tk.Label(mainFormFrame, text= "Full Name", justify=tk.LEFT)
formFullNameTitle.grid(row=0, column=0)

formFullNameEntry = tk.Entry(mainFormFrame, text="Enter your full name here ->", justify=tk.LEFT)
formFullNameEntry.grid(row=0, column=1, columnspan=7, padx=30)

formEmailTitle = tk.Label(mainFormFrame, text= "Email", justify=tk.LEFT)
formEmailTitle.grid(row=1, column=0)

formEmailEntry = tk.Entry(mainFormFrame, text="Enter your Email here ->", justify=tk.LEFT)
formEmailEntry.grid(row=1, column=1, columnspan=7, padx=30)

formgendertitle= tk.Label(mainFormFrame, text= "Gender", justify=tk.LEFT)
formgendertitle.grid(row=2, column=0)

formGenderVar = tk.IntVar()
formGenderRadioMale = tk.Radiobutton(mainFormFrame,text="Male",variable= formGenderVar, value=1, padx=30).grid(row=2, column=1)
formGenderRadioFemale = tk.Radiobutton(mainFormFrame,text="Female",variable= formGenderVar, value=2, padx = 30).grid(row=2, column=2)

formCountryTitle= tk.Label(mainFormFrame, text= "Country", justify=tk.LEFT)
formCountryTitle.grid(row=3, column=0)



formCountryVar = tk.StringVar()
formCountryCombobox=ttk.Combobox(mainFormFrame, text= "Country", textvariable=formCountryVar)
formCountryCombobox['value']=["Karachi","Lahore","Islamabad","Peshawer","Kalam","Swat"]
formCountryCombobox.grid(row=3, column=1, columnspan=2)
formCountryCombobox.current(0)

formprogramtitle= tk.Label(mainFormFrame, text= "programming Language", justify=tk.LEFT)
formgendertitle.grid(row=2, column=0)

formProgramingPythonVar = tk.IntVar()
formProgramingJavaVar = tk.IntVar()
formProgramCheck = tk.Checkbutton(mainFormFrame,text="Python",variable= formProgramingPythonVar, padx= 30).grid(row=4, column=1)
formProgramCheck = tk.Checkbutton(mainFormFrame,text="Java",variable= formProgramingJavaVar, padx = 30).grid(row=4, column=2)

formProgramTitle= tk.Label(mainFormFrame, text= "Programming Language ", justify=tk.LEFT)
formProgramTitle.grid(row=4, column=0)


formSubmitTitle = tk.Label(mainFormFrame, text= "Submit", justify=tk.LEFT)
formSubmitTitle.grid(row=5, column=0)

formSubmitButton = tk.Button(mainFormFrame, text="Submit", justify=tk.LEFT, bg="red", command= processSubmitButton)
formSubmitButton.grid(row=5, column= 0)



# --------------------------------------
mainFormFrame.pack(fill=tk.X)
mainWindow.mainloop()