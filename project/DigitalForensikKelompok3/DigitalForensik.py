#!/usr/bin/env python
# coding: utf-8

# In[32]:


import tkinter as tk


# In[33]:


import os


# In[34]:


from tkinter import  *


# In[35]:


import tkinter.messagebox


# In[36]:


from tkinter import PhotoImage


# In[37]:


from tkinter import filedialog


# In[38]:


window=Tk()
window.geometry("810x520")
window.config(bg="#FBE9C1")
photo = PhotoImage(file="asset/model.png")
seriall = PhotoImage(file="asset/serial.png")
pilih_folder = PhotoImage(file="asset/folder.png")
os_vir = PhotoImage(file="asset/os_vitsion.png")
manufaktur = PhotoImage(file="asset/Manufaktur.png")
exitbutton = PhotoImage (file ="asset/exit.png")
aboutt= PhotoImage (file ="asset/about.png")
backupbutton = PhotoImage (file ="asset/backup.png")
backupcamera = PhotoImage (file ="asset/backup_camera.png")
backup_devicee = PhotoImage (file ="asset/backup_device.png")
backup_storagee = PhotoImage (file ="asset/backup_storage.png")
backup_systemm = PhotoImage (file ="asset/backup_system.png")
ikonbutton = PhotoImage (file ="asset/ikon.png")
photo2 = PhotoImage(file="asset/button.png")
window.title("software digital forensik kelompok 3")


# In[39]:


# setting switch state:
btnState = False


# In[40]:


# setting switch function:

class FolderSelect(Frame):
    def __init__(self, parent=None, folderDescription="", **kw):
        Frame.__init__(self, master=parent, **kw)
        self.folderPath = StringVar()
        self.lblName = Label(self, text=folderDescription, bg="#FBE9C1")
        self.lblName.grid(pady=1, column=1)
        self.entPath = Entry(self, textvariable=self.folderPath, width=43, font=("arial", 13))
        self.entPath.grid(row=0, column=1)
        self.btnFind = tk.Button(self, text="Browse Folder", border=0, bg="#FBE9C1", image=pilih_folder,
                                 command=self.setFolderPath, width=120)
        self.btnFind.grid(row=0, column=5)

    def setFolderPath(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)

    @property
    def folder_path(self):
        return self.folderPath.get()


# In[41]:


# setting switch function:
def switch():
    global btnState
    if btnState:
        btn.config(image=offImg, bg="#FBE9C1", activebackground="#FBE9C1")
        window.config(bg="#FBE9C1")
        txt.config(text="Dark Mode: OFF", bg="#FBE9C1")

        btnState = False


    else:
        btn.config(image=onImg, bg="#2B2B2B", activebackground="#2B2B2B")
        window.config(bg="#2B2B2B")
        txt.config(text="Dark Mode: ON", bg="#2B2B2B")
        btnState = True


# In[42]:


deviceManufaktur = os.popen('adb shell getprop ro.product.manufacturer').read()
def Manufaktur():
    if deviceSerial == '':
        label2 = tkinter.Label(window, bg="#FBE9C1", text="Tidak ada device")
        label2.place(x=230,y=150)
    else:
        label2 = tkinter.Label(window, bg="#FBE9C1", text=(deviceManufaktur))
        label2.place(x=230,y=150)


# In[43]:


deviceSerial = os.popen('adb shell getprop ro.serialno').read()
def serial():
    if deviceSerial == '':
        label2 = tkinter.Label(window, bg="#FBE9C1", text="Tidak ada device")
        label2.place(x=230,y=200)
    else:
        label2 = tkinter.Label(window, bg="#FBE9C1", text=(deviceSerial))
        label2.place(x=230,y=200)


# In[44]:


deviceName = os.popen('adb shell getprop ro.product.model').read()
def model1():
    if deviceName == '':
        label2 = tkinter.Label(window, bg="#FBE9C1", text="Tidak ada device")
        label2.place(x=630,y=150)
    else:
        label2 = tkinter.Label(window, bg="#FBE9C1", text=(deviceName))
        label2.place(x=630,y=150)


# In[45]:


deviceNameOs = os.popen('adb shell getprop ro.build.version.sdk').read()
def osvir():
    if deviceName == '':
        label2 = tkinter.Label(window, bg="#FBE9C1", text="Tidak ada device")
        label2.place(x=630,y=200)
    else:
        label2 = tkinter.Label(window, bg="#FBE9C1", text=(deviceNameOs))
        label2.place(x=630, y=200)


# In[46]:


def ikon():
    window.destroy()


# In[47]:


def logo():
    window.destroy()


# In[48]:


def exit1():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        window.destroy()
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')


# In[49]:


def about():
    tkinter.messagebox.showinfo('Team Info', 'Kelompok 3')


# In[50]:


def backup():
    folder1 = directory1Select.folder_path.replace("/","\\")
    MsgBox = tk.messagebox.askquestion('Backup Data', 'Are you sure you want to Backup Data',
                                       icon='warning')
    if MsgBox == 'yes':
        os.system("adb backup -apk -shared -all -nosystem -f \"" + folder1 + "\\backup.ab\"")
        os.system("ab-decrypt \"" + folder1 + "\\backup.ab\" \"" + folder1 + "\\backup.tar\"")
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')


# In[51]:


def camera():
    folder1 = directory1Select.folder_path.replace("/","\\")
    MsgBox = tk.messagebox.askquestion('Backup Data', 'Are you sure you want to Backup Data',
                                       icon='warning')
    if MsgBox == 'yes':
        os.system("adb pull /sdcard/DCIM " + folder1)
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')


# In[52]:


def backup_device():
    folder1 = directory1Select.folder_path.replace("/","\\")
    MsgBox = tk.messagebox.askquestion('Backup Data', 'Are you sure you want to Backup Data',
                                       icon='warning')
    if MsgBox == 'yes':
        os.system("adb backup -all -f \"" + folder1 + "\\backup.ab\"")
        os.system("ab-decrypt \"" + folder1 + "\\backup.ab\" \"" + folder1 + "\\backup.tar\"")
#         os.system("ab-decrypt C:\Backups\\backup.ab C:\Backups\\backup.tar")
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')


# In[53]:


def backup_storage():
    folder1 = directory1Select.folder_path.replace("/","\\")
    MsgBox = tk.messagebox.askquestion('Backup Data', 'Are you sure you want to Backup Data',
                                       icon='warning')
    if MsgBox == 'yes':
        os.system("adb backup -noapk -shared -nosystem -f \"" + folder1 + "\\backup.ab\"")
        os.system("ab-decrypt \"" + folder1 + "\\backup.ab\" \"" + folder1 + "\\backup.tar\"")
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')


# In[54]:


def backup_system():
    folder1 = directory1Select.folder_path.replace("/","\\")
    MsgBox = tk.messagebox.askquestion('Backup Data', 'Are you sure you want to Backup Data',
                                       icon='warning')
    if MsgBox == 'yes':
        os.system("adb backup -apk -shared -all -system -f \"" + folder1 + "\\backup.ab\"")
        os.system("ab-decrypt \"" + folder1 + "\\backup.ab\" \"" + folder1 + "\\backup.tar\"")
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')


# In[55]:


labell=Label(window, text="SOFTWARE DIGITAL FORENSIK",fg='blue',relief="solid", bg='yellow', font =("arial", 16, "bold")).pack()
button1=Button(window,bg="#FBE9C1", image=manufaktur ,border =0, text="Manufaktur", fg='blue', command = Manufaktur)
button3=Button(window,bg="#FBE9C1", image=seriall,border =0,text="Serial",command = serial)
button2=Button(window,bg="#FBE9C1",image=photo ,border =0, text="Model", command = model1)
button4=Button(window,bg="#FBE9C1",image=backupbutton ,border =0, text="backuptanpa sistem", command = backup)
button5=Button(window,bg="#FBE9C1",image=backup_devicee ,border =0, text="backup_devicee", command = backup_device)
button6=Button(window,bg="#FBE9C1",image=backup_storagee ,border =0, text="backup_storagee", command = backup_storage)
button7=Button(window,bg="#FBE9C1",image=backup_systemm ,border =0, text="backup_systemm", command = backup_system)
button8=Button(window,bg="#FBE9C1",image= os_vir ,border =0, text="backup_systemm", command = osvir)
button9=Button(window,bg="#FBE9C1",image=backupcamera ,border =0, text="backup_systemm", command = camera)


# In[56]:


b2=Button(window,text="Quit",border=0, image = exitbutton, command = exit1) #button Exit
b3=Button(window,text="About",border=0,bg="#FBE9C1",image =aboutt, command = about) #button About
b4=Button(window,border=0,bg="#FBE9C1",image = ikonbutton, command = about) #button About


# In[57]:


folderPath = StringVar()

directory1Select = FolderSelect(window, "Select Folder 1")
directory1Select.place(x=50, y=250)


# In[58]:


# loading the switch images:
onImg = PhotoImage(file="asset/switch-on.png")
offImg = PhotoImage(file="asset/switch-off.png")


# In[59]:


# Night mode label:
txt = tk.Label(window, text="Dark Mode: OFF", font="FixedSys 17", bg="#FBE9C1", fg="green")
txt.place(relx=0.8, rely=0.1, anchor="center")


# In[60]:


# switch widget:
btn = tk.Button(window, text="OFF", borderwidth=0, command=switch, bg="#FBE9C1", activebackground="#FBE9C1")
btn.place(relx=0.8, rely=0.2, anchor="center")
btn.config(image=offImg)


# In[61]:


button9.place(x=250, y=350)
button7.place(x=450, y=400)
button6.place(x=450, y=300)
button5.place(x=50, y=400)
button4.place(x=50, y=300)
button3.place (x=50,y=200)
button2.place (x=450,y=150)
button8.place (x=450,y=200)
button1.place(x=50,y=150)
# button10.place(x=250, y=350)
b2.place(x=550,y=460)
b3.place(x=650, y=460)
b4.place(x=50, y=40)


# In[ ]:


window.mainloop()

