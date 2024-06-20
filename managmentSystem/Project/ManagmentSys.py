import mymod
from tkinter import Tk,Label,Button,PhotoImage,Entry


root = Tk()

root.title("Managment System")
root.iconbitmap('Project/bgs/icon2.ico')
root.geometry("800x800")
root.resizable(False,False)

#------------------------------ROW 0-----------------------------------------------

bg = PhotoImage(file='Project/bgs/bg3.png')
bglab = Label(root,image=bg)
bglab.place(x=0,y=0,relheight=1,relwidth=1)
emplab = Label(root,text="Employees Info",font=("Courier", 12),fg='black',background='lightgray')
emplab.grid(row=0,column=0,padx=10,pady=10)

#-----------------------------ROW 1------------------------------------------------

pathbox = Entry(root,width=45)
pathbox.insert(0,"Enter PDF's Name")
pathbox.bind('<FocusIn>',lambda event: mymod.on_entry_click(pathbox))
pathbox.grid(row=1,column=0,columnspan=3,padx=20,pady=10)



readButton = Button(root,text="Read PDF",background='black',fg='white',borderwidth=1,width=20,command=lambda:mymod.readButton(pathbox))
readButton.grid(row=1,column=4,padx=10,pady=10,columnspan=10)

SearchNameEntry = Entry(root,width=45)
SearchNameEntry.insert(0, 'Enter Name for Search')
SearchNameEntry.bind('<FocusIn>',lambda event:mymod.on_entry_click(SearchNameEntry))
SearchNameEntry.grid(row=2,column=0,columnspan=3,padx=20,pady=10)

SearchNameButt = Button(root,text="Search This Name",background='black',fg='white',borderwidth=1,width=20,command=lambda:mymod.SearchName(SearchNameEntry))
SearchNameButt.grid(row=2,column=4,padx=10,pady=10)

#--------------------------------ROW 3----------------------------------------------
SearchDateEntry = Entry(root,width=45)
SearchDateEntry.insert(0, 'Enter Date for Search')
SearchDateEntry.bind('<FocusIn>',lambda event:mymod.on_entry_click(SearchDateEntry))
SearchDateEntry.grid(row=3,column=0,columnspan=3,padx=20,pady=10)

SearchDateButt = Button(root,text="Seach this date",background='black',fg='white',borderwidth=1,width=20,command=lambda:mymod.SearchDate(SearchDateEntry))
SearchDateButt.grid(row=3,column=4,padx=10,pady=10)


mglab = Label(root,text='Mangagment Info',font=("Courier", 12),fg='black',background='lightgray')
mglab.grid(row=4,column=0,pady=40)


mgSearchDateEntry = Entry(root,width=45)
mgSearchDateEntry.insert(0, 'Enter Date for Search')
mgSearchDateEntry.bind('<FocusIn>',lambda event:mymod.on_entry_click(mgSearchDateEntry))
mgSearchDateEntry.grid(row=5,column=0,columnspan=3,padx=20,pady=10)

mgSearchDateButt = Button(root,text="Seach this date",background='black',fg='white',borderwidth=1,width=20,command=lambda:mymod.mgDateSearch(mgSearchDateEntry))
mgSearchDateButt.grid(row=5,column=4,padx=10,pady=10)

mg1DateEntry = Entry(root,width=45)
mg1DateEntry.insert(0, 'Enter Initial Date for Search')
mg1DateEntry.bind('<FocusIn>',lambda event:mymod.on_entry_click(mg1DateEntry))
mg1DateEntry.grid(row=6,column=0,columnspan=3,padx=20,pady=10)

mg2DateEntry = Entry(root,width=45)
mg2DateEntry.insert(0, 'Enter Final Date for Search')
mg2DateEntry.bind('<FocusIn>',lambda event:mymod.on_entry_click(mg2DateEntry))
mg2DateEntry.grid(row=7,column=0,columnspan=3,padx=20,pady=10)

dailyDatabutt = Button(root,text="Search Data Between",background='black',fg='white',borderwidth=1,width=20,command=lambda:mymod.mgDataBetweenTwoDate(mg1DateEntry,mg2DateEntry))
dailyDatabutt.grid(row=7,column=4,padx=10,pady=10)


dailyDatabutt = Button(root,text="Filling Daily Form",background='black',fg='white',borderwidth=1,width=20,command=mymod.DailyCapitalData)
dailyDatabutt.grid(row=8,column=4,padx=10,pady=10)

root.mainloop()