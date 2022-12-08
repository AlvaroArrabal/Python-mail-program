from tkinter import *


optionList = ["PUSCH","RSSI","Sin MIMO Rank2","MIMO Rank2 Bajo","Sin MIMO Rank4","MIMO Rank4 Bajo","CA PCELL",
              "CA SCELL","SRVCC","Sin tráfico 5G"]
buttonsList = ["Write","Save","Clean"]

# Initiating the app
app = Tk()

# Windows configuration
app.geometry("900x600+0+0")
app.resizable(0,0)
app.title("Mail generator")
app.config(bg="white")

# App TOP
topPanel = Frame(app,bd=2,relief=FLAT)
topPanel.pack(side=TOP)

title_name = Label(topPanel,text="XXX\t\t\t",fg="black",font=("Dosis",22,"bold"),bg="SlateBlue",width=25) 
title_name.grid(row=0,column=0)

title_name_2 = Label(topPanel,text="Mail Generator  ",fg="black",font=("Dosis",22,"bold"),bg="SlateBlue",width=25) 
title_name_2.grid(row=0,column=1)

# Left Panel
leftPanel = Frame(app,bd=2,relief=FLAT)
leftPanel.pack(side=LEFT)

optionsPanel = LabelFrame(leftPanel,text="Options", font=("Dosis",19,"bold"),bd=1,relief=FLAT,fg="black")
optionsPanel.pack(side=LEFT)

# Right Panel
rightPanel = Frame(app,bd=2,relief=FLAT)
rightPanel.pack(side=RIGHT)

# Mail Panel
mailPanel = Frame(rightPanel,bd=2,relief=FLAT,bg="black")
mailPanel.pack()

# Buttons Panel
buttonsPanel = Frame(rightPanel,bd =1,relief=FLAT,bg="black")
buttonsPanel.pack()


# Option Panel Configuration
optionsVariables= []
optionsBox = []
optionsText = []

cont = 0

for option in optionList:
    # Check Buttons
    optionsVariables.append("")
    optionsVariables[cont] = IntVar()
    option = Checkbutton(optionsPanel,text=option,font=("Arial",15,"bold"),onvalue=1,offvalue=0, variable=optionsVariables[cont])
    option.grid(row=cont, column=0, sticky=W)  
    
    # Option Box 
    optionsBox.append("")
    optionsText.append("")
    optionsText[cont] =StringVar()
    optionsText[cont].set("0")
    optionsBox[cont] = Entry(optionsPanel,font=("Arial",15,"bold"),bd=1,width=15,state=DISABLED,textvariable=optionsText[cont])
    optionsBox[cont].grid(row=cont,column=1)

    cont +=1

# Mail Panel Configuration
mailText = Text(mailPanel,font=("Arial",12),fg="black",bd=1,width=56,height=27)
mailText.grid(row=0,column=0)

# Buttons Panel Configuration
buttonsAux = []
columns = 0

for button in buttonsList:
    button = Button(buttonsPanel,text=button,font=("Arial",13,"bold"),fg="black",bg="Gray",bd=2,width=16)
    buttonsAux.append(button)
    button.grid(row=0,column=columns)
    columns += 1


app.mainloop()