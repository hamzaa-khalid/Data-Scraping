from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

def opening_form():
    mf = Tk()
    mf.geometry('1010x600+250+100')
    mf.title('Welcome')
    mf.resizable(0, 0)
    photo = PhotoImage(file="mainpage.png")
    label = Label(mf,image=photo)
    label.pack()

    btn_nextform = Button(mf, text="Proceed",bg='#143628', fg='#e3c322', width=19, font=('Open Sans', 25, 'bold'),command=mainMenu)
    btn_nextform.place(x=315, y=328)
    mf.mainloop()

def mainMenu():
    ef = Toplevel()
    ef.geometry('1010x600+250+100')
    ef.title('Main Menu')
    ef.resizable(0, 0)

    pht = PhotoImage(file="mainmenu.png")
    label = Label(ef, image=pht)
    label.pack()

    btn_scraping = Button(ef,text="Data Scraping",bg='#143628', fg='#e3c322', relief='flat', width=19, font=('Open Sans', 25, 'bold'), command=openScreen)
    btn_scraping.place(x=305, y=229)
    btn_addconnects = Button(ef, text="Adding Connects",bg='#143628', fg='#e3c322', relief='flat', width=19, font=('Open Sans', 25, 'bold'), command=inputpage)
    btn_addconnects.place(x=305, y=335)
    btn_info = Button(ef, text="i", bg='#143628', fg='#e3c322', relief='flat', width=3, font=('Arial', 25, 'bold'), command=infopage)
    btn_info.place(x=930, y=525)

    mainloop()

def infopage():
    ef = Toplevel()
    ef.geometry('1010x600+250+100')
    ef.title('Contact Information')
    ef.resizable(0, 0)

    pht = PhotoImage(file="info.png")
    label = Label(ef, image=pht)
    label.pack()

    mainloop()

def inputpage():
    ef = Toplevel()
    ef.geometry('1010x600+250+100')
    ef.title('Contact Information')
    ef.resizable(0, 0)

    pht = PhotoImage(file="input.png")
    label = Label(ef, image=pht)
    label.pack()
    
    global username
    username = StringVar()
    username_txt = Entry(ef, textvar=username,bg='#143628', fg='#e3c322', relief='flat', width=24, font=('Open Sans', 25, 'bold'))
    username_txt.place(x=322, y=206)
    
    global password
    password = StringVar()
    password_txt = Entry(ef, textvar=password,bg='#143628', fg='#e3c322', show = '*', relief='flat', width=24, font=('Open Sans', 25, 'bold'))
    password_txt.place(x=322, y=319)
    
    btn_addconnects = Button(ef, text="Add Connects",bg='#143628', fg='#e3c322', relief='flat', width=15, font=('Open Sans', 25, 'bold'), command=None)
    btn_addconnects.place(x=382, y=422)

    mainloop()

path = None
txtarea = None
lst = []
def openScreen():
    global path
    global txtarea
    ws = Tk()
    ws.title("Open Txt File Containing Links To Scrape")
    ws.geometry("400x450+550+220")
    ws['bg']='#143628'

    txtarea = Text(ws, width=40, height=20)
    txtarea.pack(pady=20)
    path = Entry(ws)
    path.pack(side=LEFT, expand=True, fill=X, padx=20)

    Button(
        ws, 
        text="Open File", 
        command=openFile
        ).pack(side=RIGHT, expand=True, fill=X, padx=20)


    ws.mainloop()
    
    
def openFile():
    global path
    global txtarea
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/User/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    path.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.readlines()
    for i in data:
        lst.append(i)
        txtarea.insert(END, i)
    tf.close()
    messagebox.showinfo('Note','Your Data Will Be Extracted Soon and saved in the downloads directory.')
#     newdf = darazScript(lst) Function of daraz script (replaced by md scraping)
#     newdf.to_csv('DarazSample.csv') saving datafraem to csv
    exit()

# ===============================================
# Main Form
opening_form()





    
