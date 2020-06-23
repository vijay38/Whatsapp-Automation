from tkinter import *
from tkinter import filedialog
root=Tk()
root.title("WA Bulk SMS")
root.configure(background="snow",height=500,width=800)

canvas1=Canvas(root,bg="cyan")
canvas1.place(relwidth=1,relheight=0.2)

head_text=Label(canvas1,text="WA BULK SMS",font="impact 60 bold",fg="green",bg="cyan")
head_text.pack()



Message=Label(root,text="Paste your message:",font="Courier 16 bold",bg="snow")
Message.place(relx=0.02,rely=0.6)

messagebox=Entry(root,font="Helvetica 16")
messagebox.insert(0,"Type Here...")
messagebox.place(relx=0.02,rely=0.65,relwidth=0.9,relheight=0.2)
    
root.mainloop()
