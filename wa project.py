from tkinter import *
from tkinter import filedialog
import webbrowser
import time
import pyautogui as gui
import csv

global path
global success
global numentry
path=""
root=Tk()
root.title("WA Bulk SMS")
root.configure(background="snow",height=500,width=800)

def selectfile():
    global path
    root.filename=filedialog.askopenfilename(initialdir="d:",title="select a file"
                                             ,filetype=(("CSV Files","*.csv"),("all files","*.*")))
    path=root.filename
    success=Label(root,text="File has been received",fg="red",bg="snow",font="times 14")
    success.place(relx=0.47,rely=0.54)
def submitt():
    global path
    global numentry
    numbers=[]
    if path!="":
        with open(path,'rt') as f:
          data = csv.reader(f)
          for row in data:
              for ele in row:
                  if len(ele)>5:
                      if ele[0]=="+" or ele.isnumeric():
                          numbers.append(ele)
    else:
        st=numentry.get()
        if st=="" or st=="Enter Numbers with their country code...":
            pass
        else:
            numbers=st.split(",")
    '''for i in numbers:
        url="https://web.whatsapp.com/send?phone={}&text={}&source&data&app_absent".format(i,msg)
        webbrowser.open(url)
        time.sleep(12)
        gui.press('enter')
        time.sleep(2)
        gui.keyDown('ctrl')
        gui.press('w')
        gui.keyUp('ctrl')
        time.sleep(8)'''
canvas1=Canvas(root,bg="cyan")
canvas1.place(relwidth=1,relheight=0.2)

head_text=Label(canvas1,text="WA BULK SMS",font="impact 60 bold",fg="green",bg="cyan")
head_text.pack()

number=Label(root,text="Enter (,)seperated numbers",font="Courier 16 bold",bg="snow")
number.place(relx=0.02,rely=0.22)

numentry=Entry(root,font="Helvetica 12")
numentry.insert(0,"Enter Numbers with their country code...")
numentry.place(relx=0.02,rely=0.30,relwidth=0.9,relheight=0.15)

insert_label=Label(root,text="or insert .csv file",bg="snow",font="Courier 14 bold")
insert_label.place(relx=0.02,rely=0.48)

select=Button(root,text="select a file",command=selectfile)
select.place(relx=0.05,rely=0.54,relwidth=0.4)

Message=Label(root,text="Paste your message:",font="Courier 16 bold",bg="snow")
Message.place(relx=0.02,rely=0.6)

messagebox=Entry(root,font="Helvetica 16")
messagebox.insert(0,"Type Here...")
messagebox.place(relx=0.02,rely=0.65,relwidth=0.9,relheight=0.2)

submit=Button(root,text="Submit",font="impact 20 bold",fg="white",bg="green",command=submitt)
submit.place(relx=0.3,rely=0.85,relwidth=0.4)
    
root.mainloop()
