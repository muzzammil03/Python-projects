from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)
    #remove from 1st line to end

    
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad ")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

        
def saveFile():
    global file
    if file==None:
        file =asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file =="":
            file=None
        else:
            #save as new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+" - Notepad ")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
            
def quitApp():
    root.destroy()

    
def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by Muzzammil ahmed")






def mainfile():
    root=Tk()
    root.geometry("644x788")
    root.iconbitmap("favicon.ico")
    root.title("Notepad")

#adding text area
    TextArea=Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)

#creating menu bar
    MenuBar=Menu(root)

 #creating file menu
    FileMenu=Menu(MenuBar,tearoff=0)

 #to open new file
    FileMenu.add_command(label="New",command=newFile)

#To open already exisintg file
    FileMenu.add_command(label="Open",command=openFile)

 #To save the current file

    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)

    #Edit Menu start
    EditMenu=Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)

    MenuBar.add_cascade(label="Edit",menu=EditMenu)
 #Edit Menu ends

 


    #help menu start
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
#helop menu end

    root.config(menu=MenuBar)

    #adding scrollbar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()
    
mainfile()




