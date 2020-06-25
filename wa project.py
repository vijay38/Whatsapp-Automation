from tkinter import *
from tkinter import filedialog
import webbrowser
import time
import pyautogui as gui
import csv
from tkinter import messagebox
from io import BytesIO
import win32clipboard
import PIL
from PIL import Image
import urllib.parse

global path
global success
global numentry
global imagepath
global image_success
global message


imagepath=""
path=""
root=Tk()
root.title("WA Bulk SMS")
root.configure(background="snow",height=500,width=800)

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def selectimage():
    global imagepath
    global image_success
    root.imagename=filedialog.askopenfilename(initialdir="d:",title="select a file"
                                             ,filetype=(("JPEG Files","*.jpg"),("PNG files","*.png")))
    imagepath=root.imagename
    image_success=Label(root,text="Image received",fg="red",bg="snow",font="times 14")
    image_success.place(relx=0.72,rely=0.76)
    
def selectfile():
    global path
    global success
    root.filename=filedialog.askopenfilename(initialdir="d:",title="select a file"
                                             ,filetype=(("CSV Files","*.csv"),("all files","*.*")))
    path=root.filename
    success=Label(root,text="File has been received",fg="red",bg="snow",font="times 14")
    success.place(relx=0.47,rely=0.54)
def submitt():
    global path
    global imagepath
    global numentry
    global success
    global image_success
    global message
    numbers=[]
    if path!="":
        success.place_forget()
        with open(path,'rt') as f:
          data = csv.reader(f)
          for row in data:
              for ele in row:
                  if len(ele)>5:
                      if ele[0]=="+" or ele.isnumeric():
                          q=ele.strip()
                          q=q.rstrip()
                          numbers.append(q)
    else:
        st=numentry.get()
        if st=="" or st=="Enter Numbers with their country code...":
            messagebox.showerror("No data?","Please Upload a file or type numbers")
        else:
            numbers=[i.strip().rstrip() for i in st.split(",")]
    msg=message.get()
    if msg=="" and imagepath=="":
        messagebox.showerror("No data?","Please type or attach a msg")
    else:
        msg=urllib.parse.quote(msg)
        c=1
        if imagepath=="":
            for i in numbers:
                if c==1:
                    webbrowser.open("https://web.whatsapp.com")
                    time.sleep(12)
                    gui.keyDown('ctrl')
                    gui.press('w')
                    gui.keyUp('ctrl')
                    time.sleep(8)
                    c+=1 
                url="https://web.whatsapp.com/send?phone={}&text={}&source&data&app_absent".format(i,msg)
                webbrowser.open(url)
                time.sleep(12)
                gui.press('enter')
                time.sleep(2)
                gui.keyDown('ctrl')
                gui.press('w')
                gui.keyUp('ctrl')
                time.sleep(8)
        else:
            image_success.place_forget()
            filepath = imagepath
            try:
                image = Image.open(filepath)
                output = BytesIO()
                image.convert("RGB").save(output, "BMP")
                data = output.getvalue()[14:]
                output.close()
                send_to_clipboard(win32clipboard.CF_DIB, data)
            except Exception:
                messagebox.showerror("sorry","Not suitable attachment")
                return
            
            for i in numbers:
                if c==1:
                    webbrowser.open("https://web.whatsapp.com")
                    time.sleep(12)
                    gui.keyDown('ctrl')
                    gui.press('w')
                    gui.keyUp('ctrl')
                    time.sleep(8)
                    c+=1
                url="https://web.whatsapp.com/send?phone={}&text={}&source&data&app_absent".format(i,msg)
                webbrowser.open(url)
                time.sleep(12)
                gui.keyDown('ctrl')
                gui.press('v')
                gui.keyUp('ctrl')
                time.sleep(2)
                gui.press('enter')
                time.sleep(2)
                gui.keyDown('ctrl')
                gui.press('w')
                gui.keyUp('ctrl')
                time.sleep(8)
                
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

Message_label=Label(root,text="Paste your message:",font="Courier 16 bold",bg="snow")
Message_label.place(relx=0.02,rely=0.6)

attachment_label=Label(root,text="Add an image:",font="Courier 16 bold",bg="snow")
attachment_label.place(relx=0.65,rely=0.6)

select_image=Button(root,text="select an attachment",command=selectimage)
select_image.place(relx=0.65,rely=0.7,relwidth=0.3)

message=Entry(root,font="Helvetica 16")
message.insert(0,"Type Here...")
message.place(relx=0.02,rely=0.65,relwidth=0.6,relheight=0.2)

submit=Button(root,text="Submit",font="impact 20 bold",fg="white",bg="green",command=submitt)
submit.place(relx=0.3,rely=0.87,relwidth=0.4)
    
root.mainloop()
