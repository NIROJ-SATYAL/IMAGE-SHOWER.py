from tkinter import *
from PIL import ImageTk
from PIL import Image
root=Tk()
root.title("satyal powershell")#naming 
#root.geometry("1000x2000")#give apropriate size
img = PhotoImage(file='A.png')#added small image or logo on top of the corner
root.tk.call('wm', 'iconphoto', root._w, img)
img1=ImageTk.PhotoImage(Image.open("photo1.jpg"))#added image on gui using tkinter
img2=ImageTk.PhotoImage(Image.open("photo2.jpg"))#added image on gui using tkinter
img3=ImageTk.PhotoImage(Image.open("photo5.jpg"))#added image on gui using tkinter
img4=ImageTk.PhotoImage(Image.open("photo6.jpg"))#added image on gui using tkinter
img5=ImageTk.PhotoImage(Image.open("photo7.jpg"))#added image on gui using tkinter
nature=[img1,img2,img3,img4,img5]#list of image
label=Label(image=img1)
label.grid(row=0,column=0,columnspan=3)
status=Label(root,text="1 0f" + str(len(nature)),relief=SUNKEN,bd=2,anchor=E)
def forward(number):#function call from forward button from line num 46
    global l#initiliaze global variable (i.e access from every where)
    
    global f#initiliaze global variable (i.e access from every where)
    global b#initiliaze global variable (i.e access from every where)
    label.grid_forget()#delete current label
    l=Label(image=nature[number-1])
    f=Button(root,text=">>",command=lambda:forward(number+1))#update button when forward button is clicked by user
    b=Button(root,text="<<",command=lambda:back(number-1))#update button when backward button is clicked by user
    

    if number == 5:
        f=Button(root,text=">>",state=DISABLED)#Condition to disabled forward button when image is in last index
    f.grid(row=1,column=2)#"showing on window"
    b.grid(row=1,column=0)#"showing on window"
    l.grid(row=0,column=0,columnspan=3)#"showing on window"
    #UPDATE STATUS LABEL 
    status=Label(root,text="image" + str(number) + "of"  + str(len(nature)),relief=SUNKEN,bd=2,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
def back(number):#function call from back button from line num 45
    global l#initiliaze global variable (i.e access from every where)
    global f#initiliaze global variable (i.e access from every where)
    global b#initiliaze global variable (i.e access from every where)
    label.grid_forget()#delete the current label
    l=Label(image=nature[number-1])
    
    f=Button(root,text=">>",command=lambda:forward(number+1))#update button when forward button is clicked by user
    b=Button(root,text="<<",command=lambda:back(number-1))#update button when backward button is clicked by user
    
    if number == 1:
        b=Button(root,text="<<",state=DISABLED)#same as line number 27
    f.grid(row=1,column=2)#"showing on window"
    b.grid(row=1,column=0)#"showing on window"
    l.grid(row=0,column=0,columnspan=3)#"showing on window"
    #UPDATE STATUS LABEL    
    status=Label(root,text="image" + str(number) + "of"  +str(len(nature)),relief=SUNKEN,bd=2,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
button_back=Button(root,text="<<",command=back,state=DISABLED)#create a button for backward
button_forward=Button(root,text=">>",command=lambda:forward(2))#create a button for forward
button_exit=Button(root,text="EXIT",command=root.quit)#create a button for exit
button_back.grid(row=1,column=0)#"showing on window"
button_exit.grid(row=1,column=1)#"showing on window"
button_forward.grid(row=1,column=2)#"showing on window"
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
root.mainloop()
