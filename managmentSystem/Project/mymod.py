from PyPDF2 import PdfFileReader
from pandas import DataFrame,read_csv
from tkinter import Label,Frame,Button,Toplevel,PhotoImage,Entry,BOTH,DISABLED,X
from pandastable import Table
from matplotlib.pyplot import bar,xlabel,ylabel,title,show

def Formaldate(date):
        date = str(date)
        c = date[1]
        
        if(date.isalpha()==True) | (date == None):
            return None
        else:
            if (c.isdigit() == False) :
                date = "0"+date[:]
                date = date[0:2]+'/'+date[3:]
                
            else :
                date = date[:2]+'/'+date[3:]

            c = date[4]

            if (c.isdigit()== False) :
                date = date[:3]+'0'+ date[3:]
                date = date[:5]+'/'+ date[6:]
            else :
                date = date[:5]+'/'+date[6:]
            
            return date
def DateCal(date):
    
    day = date[:2]
    month = date[3:5]
    year = date[8:]
    day = int(day)
    month= int(month)
    year=int(year)
    daynum = 0
    daynum = day + (month-1)*31 + year*373
    return daynum


def isfolat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

def WeeklyDF(path):
    def hour_per_week(df):
        def hoursCalc(In,Out):
    
            SI=In[:2]
            SO=Out[:2]
            if In[3:]=="":
                DI='00'
            else:
                DI=In[3:]
            if Out[3:]=="":
                DO='00'
            else:
                DO=Out[3:]

            MinI = 60*int(SI) + int(DI)
            MinO = 60*int(SO) + int(DO)
            daily=MinO-MinI
            daily=daily/60
            return daily
        i=0
        Total_Work=0
        for j in range(6):
            i+=1
            
            if (df.loc[i-1,'in'] and df.loc[i-1,'out'])!= None:
                Total_Work+=hoursCalc(df.loc[i-1,'in'],df.loc[i-1,'out'])
        return Total_Work
    def workingDays(df):
        i=0
        wd = []
        for j in range(6):   
            i+=1
            
            
            if (df.loc[i-1,"Date"])!= None:
                
                day=df.loc[i-1,"Date"]
                wd.append(day)
            
        return wd
    def Adress(df):
        i=0
        adrs = []
        for j in range(6):   
            i+=1
            
            
            if (df.loc[i-1,"Date"])!= None:
                
                day=df.loc[i-1,"Adress"]
                adrs.append(day)
            
        return adrs

    pdfobject=open('Project/pdfs/'+path+'.pdf','rb')
    pdf= PdfFileReader(pdfobject)
    boxes=pdf.getFormTextFields()
    worksheet = {
        
        'days'    : [1,2,3,4,5,6,7],
        'in'      : [boxes['Text Box 1'],boxes['Text Box 1_7'],boxes['Text Box 1_13'],boxes['Text Box 1_19'],boxes['Text Box 1_25'],boxes['Text Box 1_31'],boxes['Text Box 1_37']],
        'out'     : [boxes['Text Box 1_2'],boxes['Text Box 1_8'],boxes['Text Box 1_14'],boxes['Text Box 1_20'],boxes['Text Box 1_26'],boxes['Text Box 1_32'],boxes['Text Box 1_38']],
        'JobDis'  : [boxes['Text Box 1_3'],boxes['Text Box 1_9'],boxes['Text Box 1_15'],boxes['Text Box 1_21'],boxes['Text Box 1_27'],boxes['Text Box 1_33'],boxes['Text Box 1_39']],
        'WDYD'    : [boxes['Text Box 1_4'],boxes['Text Box 1_10'],boxes['Text Box 1_16'],boxes['Text Box 1_22'],boxes['Text Box 1_28'],boxes['Text Box 1_34'],boxes['Text Box 1_40']],
        'Adress'  : [boxes['Text Box 1_5'],boxes['Text Box 1_11'],boxes['Text Box 1_17'],boxes['Text Box 1_23'],boxes['Text Box 1_29'],boxes['Text Box 1_35'],boxes['Text Box 1_41']],
        'Date'   : [boxes['Text Box 1_6'],boxes['Text Box 1_12'],boxes['Text Box 1_18'],boxes['Text Box 1_24'],boxes['Text Box 1_30'],boxes['Text Box 1_36'],boxes['Text Box 1_42']],
    }
    Name = str(boxes['Text Box 2'])
    payableamount = boxes['Text Box 3_2']
    check_number= boxes['Text Box 3_3']
    day1 = boxes['Text Box 1_6']
    day2 = boxes['Text Box 1_12']
    day3 = boxes['Text Box 1_18']
    day4 = boxes['Text Box 1_24']
    day5 = boxes['Text Box 1_30']
    day6 = boxes['Text Box 1_36']
    day7 = boxes['Text Box 1_42']
    day1 = Formaldate(day1)
    day2 = Formaldate(day2)
    day3 = Formaldate(day3)
    day4 = Formaldate(day4)
    day5 = Formaldate(day5)
    day6 = Formaldate(day6)
    day7 = Formaldate(day7)
    name = Name.lower()

    weeks_df = DataFrame(worksheet)
    total_work=hour_per_week(weeks_df)
    WorkingDays= workingDays(weeks_df)
    adress = Adress(weeks_df)
    #[name,total_work,payableamount,check_number,WorkingDays]
    sum_info ={
        "Name" : name,
        "Total Work" : total_work,
        "Payable Amount" : payableamount,
        "Check Number": check_number,
        "Working Days": [WorkingDays],
        "Client Adresses":[adress],
        "day1": day1,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "day7": day7
    }
    weekly_inf = DataFrame(sum_info)
    return weekly_inf

def readButton(pathbox):
    path = pathbox.get()

    root1= Toplevel()
    root1.title('Weekly Data')
    root1.iconbitmap('Project/bgs/icon2.ico')
    fr = Frame(root1)
    fr.pack(fill=X,side='top')
    data = WeeklyDF(path)
    pt = Table(fr,dataframe=data)
    pt.show()

    def savepaymentperH():
        global a
        a=data['Payable Amount']=float(payEnt.get())*float(data['Total Work'])
        totlab.config(text=a)
    def savepayment():
        global a
        a=data['Payable Amount']=float(payEnt.get())
        totlab.config(text=a)

    fr2 = Frame(root1)
    fr2.pack(fill=BOTH)
    paylab = Label(fr2,text="Payment : ")
    paylab.grid(row=0,column=0,pady=10,padx=10)
    payEnt = Entry(fr2,width=10)
    payEnt.grid(row=0,column=1,pady=10,padx=10)
    
    DpHbutt = Button(fr2,text='Dollar Per Hour',command=savepaymentperH)
    DpHbutt.grid(row=0,column=2,pady=10,padx=10)
    payButt = Button(fr2,text='Direct Total',command=savepayment)
    payButt.grid(row=0,column=3,pady=10,padx=10)
    totlab = Label(fr2,text="Total Payment")
    totlab.grid(row=0,column=4,pady=10,padx=10)
    saveButton = Button(fr2,background='black',fg='white',borderwidth=1,width=20,text='Save',command=lambda:savingDf(data))
    saveButton.grid(row=1,column=4,padx=10,pady=10)
    
    def savingDf(Weekly_inf):
        def conform():
            Weekly_inf.to_csv('Project\csvs\employees.csv',sep = ",", mode='a', index=False, header=False)
            saveButton.config(state=DISABLED)
            root2.destroy()

        
        root2=Toplevel()
        root2.resizable(False,False)
        root2.iconbitmap('Project/bgs/icon2.ico')
        butt1 = Button(root2,background='black',fg='white',borderwidth=1,width=7,text="Save",command=conform)
        butt1.grid(row=0,column=0,padx=20,pady=50)
        butt2 = Button(root2,background='black',fg='white',borderwidth=1,width=7,text="Exit",command=root2.destroy)
        butt2.grid(row=0,column=1,padx=20,pady=50)

def on_entry_click(entry):
    global firstclick
    firstclick=True
    def click(entry):
        """function that gets called whenever entry1 is clicked"""        
        global firstclick

        if firstclick: # if this is the first time they clicked it
            firstclick = False
            entry.delete(0, "end") # delete all the text in the entry
    click(entry)

def SearchName(SearchNameEntry):
    def emp_history(tosearch):

        ts = str(tosearch)
        ts = ts.lower()
        df = read_csv('Project\csvs\employees.csv')
        filt = df["Name"]==ts
        return(df[filt])
    

    name=SearchNameEntry.get()
    hist = emp_history(name)
    if hist.empty==False:
        hist['Payable Amount']=hist['Payable Amount'].astype(float)
        hist['Total Houres']=hist['Total Houres'].astype(float)
        def total_payment():
            
            cs = hist['Payable Amount'].sum()
            tpLab = Label(fr2,text=cs).grid(row=0,column=1,padx=10,pady=15)

        def avpay():
            d =  hist['Payable Amount'].sum()
            h = hist['Total Houres'].sum()
            dph = d/h
            dphlab = Label(fr2,text=dph).grid(row=1,column=1,padx=10,pady=15)
            return

        root1= Toplevel()
        root1.iconbitmap('Project/bgs/icon2.ico')
        root1.title('Employee Data')
        fr = Frame(root1)

        fr.pack(fill=X,side='top')
        pt = Table(fr,dataframe=hist)
        pt.show()
        fr2= Frame(root1)
        fr2.pack(fill=BOTH)
        tpButt = Button(fr2,background='black',fg='white',borderwidth=1,width=20,text="Total Payment :",command=total_payment)
        tpButt.grid(row=0,column=0,padx=20,pady=15)
        avButt = Button(fr2,background='black',fg='white',borderwidth=1,width=20,text="Average $/h : ",command=avpay)
        avButt.grid(row=1,column=0,padx=20,pady=15)
    else:
        return

def SearchDate(SearchDateEntry):
    def Date_info(tosearch):
        ts = str(tosearch)
        ts = Formaldate(ts)
        df = read_csv('Project\csvs\employees.csv')
        filt = (df['day1']==ts) | (df['day2']==ts) | (df['day3']==ts) | (df['day4']==ts) | (df['day5']==ts) | (df['day6']==ts) | (df['day7']==ts) 
        return(df[filt])
    date=SearchDateEntry.get()
    hist=Date_info(date)
    root1 = Toplevel()
    root1.title('Date Data')
    root1.iconbitmap('Project/bgs/icon2.ico')
    pt = Table(root1,dataframe=hist)
    pt.show()
    return

def DailyCapitalData():
    def Calculate():
        
        
        Date = Dateinp.get()
        Date = Formaldate(Date)

        empCost = empCostinp.get()
        toolCost = toolCostinp.get()
        otherCost = (otherCostinp.get())
        RA = (RAinp.get())
        ssn = DateCal(Date)

        if (isfolat(empCost)==True) & (isfolat(toolCost)==True) & (isfolat(otherCost)== True) & (isfolat(RA) == True):
            empCost = float(empCost)
            toolCost = float(toolCost)
            otherCost = float(otherCost)
            RA = float(RA)


            totalcost = empCost+toolCost+otherCost
            netEarn = RA-totalcost
            Info ={
                "Date" : [Date],
                "Employee Expence" : [empCost],
                "Tool Expence" : [toolCost],
                "Other Expence" : [otherCost],
                "Recived Amount": [RA],
                "Net Earn" : [netEarn],
                'SSN' : [ssn]
            }

            
            


            lb1['text']="Total Expence : "+str(totalcost)
            

            lb2['text']="Total Earn :      "+str(netEarn)
            
            calbut.config(state=DISABLED)

            return Info
        else:
            return

    def save():
        Info = Calculate()
        netE = ent1.get()

        if (isfolat(netE)==True):
            Info["Net Earn"] = netE
            dailyDF = DataFrame(Info)
            dailyDF.to_csv('Project\csvs\DailyDF.csv',sep = ",", mode='a', index=False, header=False)
            savebut.config(state=DISABLED)
        else :
            dailyDF= DataFrame(Info)
            dailyDF.to_csv('Project\csvs\DailyDF.csv',sep = ",", mode='a', index=False, header=False)
            savebut.config(state=DISABLED)


    root1 = Toplevel()
    root1.geometry("500x500")
    root1.iconbitmap('Project/bgs/icon2.ico')
    root1.title('Daily Form')
    
    global bg1
    bg1 = PhotoImage(file='Project/bgs/bg4.png')
    bglab1 = Label(root1,image=bg1)
    bglab1.place(x=0,y=0,relheight=1,relwidth=1)

    Dateinp= Entry(root1,width=25)
    Dateinp.insert(0, 'Date : ')
    Dateinp.bind('<FocusIn>',lambda event:on_entry_click(Dateinp))
    Dateinp.grid(row=0,column=0,padx=10,pady=10)

    
    
    empCostinp = Entry(root1,width=25)
    empCostinp.insert(0, 'Employee Expence :')
    empCostinp.bind('<FocusIn>',lambda event:on_entry_click(empCostinp))
    empCostinp.grid(row=1,column=0,padx=10,pady=10)

    toolCostinp = Entry(root1,width=25)
    toolCostinp.insert(0, 'Tool Expence : ')
    toolCostinp.bind('<FocusIn>',lambda event:on_entry_click(toolCostinp))
    toolCostinp.grid(row=2,column=0,padx=10,pady=10)

    otherCostinp = Entry(root1,width=25)
    otherCostinp.insert(0, 'Other Expence : ')
    otherCostinp.bind('<FocusIn>',lambda event:on_entry_click(otherCostinp))
    otherCostinp.grid(row=3,column=0,padx=10,pady=10)

    RAinp = Entry(root1,width=25)
    RAinp.insert(0, 'Colected Amount : ')
    RAinp.bind('<FocusIn>',lambda event:on_entry_click(RAinp))
    RAinp.grid(row=4,column=0,padx=10,pady=10)

    calbut = Button(root1,background='black',fg='white',borderwidth=1,width=20,text='Show Calculation',command=Calculate)
    calbut.grid(row=4,column=1,padx=10,pady=10)

    lb1 = Label(root1,text="Total Expence : ")
    lb1.grid(row=5,column=0,padx=10,pady=10)
    lb2 = Label(root1,text="Total Earn    : ")
    lb2.grid(row=6,column=0,padx=10,pady=10)

    ent1 = Entry(root1,width=20)
    ent1.insert(0, 'Net Earn (Manual): ')
    ent1.bind('<FocusIn>',lambda event:on_entry_click(ent1))
    ent1.grid(row=7,column=0,padx=10,pady=10)

    savebut = Button(root1,background='black',fg='white',borderwidth=1,width=20,text='Save',command=save)
    savebut.grid(row=8,column=1,padx=10,pady=10)

def mgDateSearch(entry):
    def search(date):
        df = read_csv('Project\csvs\DailyDF.csv')
        filt = df['Date']== date
        return df[filt]
    date = entry.get()
    date = Formaldate(date)
    hist = search(date)
    if hist.empty==False:
        root1 = Toplevel()
        root1.iconbitmap('Project/bgs/icon2.ico')
        root1.title(date+' Info')
        pt = Table(root1,dataframe=hist)
        pt.show()
    else:
        print('Not working')
        return

def mgDataBetweenTwoDate(Date1Entry,Date2Entry):

    def plotBar():
        left = [1, 2, 3, 4, 5,6]
        ee = df['Employee Expence'].sum()
        te = df['Tool Expence'].sum()
        oe = df['Other Expence'].sum()
        ra = df['Recived Amount'].sum()
        ne = df['Net Earn'].sum()
        totex = ee+te+oe
        height = [ee,te,oe,totex,ra,ne]

        tick_label = ['Emp. Ex.', 'Tool Ex.', 'Other Ex.','Tot. Ex.', 'Rec. Amount', 'Net Earn']
        bar(left, height, tick_label = tick_label,width = 0.8, color = ['red', 'green'])
        xlabel('')
        ylabel('$')
        title('Earn/Expence Bar')
        show()
        return


    date1 = Date1Entry.get()
    date2 = Date2Entry.get()
    date1 = Formaldate(date1)
    date2 = Formaldate(date2)
    ssn1=DateCal(date1)
    ssn2=DateCal(date2)
    df = read_csv('Project/csvs/DailyDF.csv')
    filt = (df['SSN']>=ssn1) & (df['SSN']<=ssn2)
    df = df[filt]
    df = df.sort_values(by='SSN',ascending=True)

    if(df.empty==False):
        root1 = Toplevel()
        root1.iconbitmap('Project/bgs/icon2.ico')
        root1.geometry('700x350')
        root1.resizable(False,False)
        fr1=Frame(root1)
        fr1.pack(fill='x')
        pt = Table(fr1,dataframe=df)
        fr2=Frame(root1)
        fr2.pack(side='left')
        plotButt = Button(fr2,background='black',fg='white',borderwidth=1,width=20,text='Plot Bar',command=plotBar)
        plotButt.grid(column=0,row=1,padx=10,pady=10)
        pt.show()
    else:
        print('Not working')
        return
        