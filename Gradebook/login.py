from tkinter import *
from tkinter import ttk
def Adam():
    adamscreen = Toplevel(main)
    adamscreen.title("Adam Mitchell")
    adamscreen.geometry("410x350")
    
    f= open("Adam_CSET4250.txt", "r")
    global array1
    array1= []
    file = f.readline()
    files= file.rstrip("\n")

    while files != '':
        q=0
        grade=int(files)
        array1.insert(q,grade)
        file = f.readline()
        files= file.rstrip("\n")
        q=q+1
        
    hw1adam= IntVar(value=array1[0])
    hw2adam= IntVar(value=array1[1])
    test1adam= IntVar(value=array1[2])
    test2adam= IntVar(value=array1[3])

    f.close()


    tabControl = ttk.Notebook(adamscreen)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text ='CSET 4250')
    tabControl.add(tab2, text ='CSET 4850')
    tabControl.pack(expand = 1, fill ="both")


    ahwtotal= IntVar(value=100)
    
  
    Label(tab1,text= "Assignment").grid(row=0,column=0)
    Label(tab1,text= "Grade").grid(row=0,column=1)
    Label(tab1,text='Total Points').grid(row=0,column=2)
    Label(tab1,text='Grade').grid(row=0,column=3)
    Label(tab1,text= 'Letter Grade').grid(row=0,column=4)
    

#HW1 

    Label(tab1,text= "Homework 1").grid(row=1,column=0)
    Label(tab1,textvariable= hw1adam).grid(row=1,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=1,column=2)
    Label(tab1,textvariable= hw1adam).grid(row=1,column=3)
    Label(tab1, text='A').grid(row=1,column=4)
#Hw2
    Label(tab1,text= "Homework 2").grid(row=2,column=0)
    Label(tab1,textvariable= hw2adam).grid(row=2,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=2,column=2)
    Label(tab1,textvariable= hw2adam).grid(row=2,column=3)
    Label(tab1, text='A').grid(row=2,column=4)
#test 1
    Label(tab1,text= "Test 1").grid(row=3,column=0)
    Label(tab1,textvariable= test1adam).grid(row=3,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=3,column=2)
    Label(tab1,textvariable= test1adam).grid(row=3,column=3)
    Label(tab1, text='A').grid(row=3,column=4)
# test 2
    Label(tab1,text= "Test 2").grid(row=4,column=0)
    Label(tab1,textvariable= test2adam).grid(row=4,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=4,column=2)
    Label(tab1,textvariable= test2adam).grid(row=4,column=3)
    Label(tab1, text='A').grid(row=4,column=4)

    Label(tab1, text= "").grid(row=5,column=0)

    Label(tab1, text= "Homework grade").grid(row=6,column=0)
    Label(tab1, text = "Get the grade" ).grid(row=6,column = 3)
    Label(tab1, text = "Lettergrade" ).grid(row=6,column = 4)

    Label(tab1, text= "Test grade").grid(row=7,column=0)
    Label(tab1, text = "Get the grade" ).grid(row=7,column = 3)
    Label(tab1, text = "Lettergrade" ).grid(row=7,column = 4)

    Label(tab1, text= "Overall grade").grid(row=8,column=0)
    Label(tab1, text = "Get the grade" ).grid(row=8,column = 3)
    Label(tab1, text = "Lettergrade" ).grid(row=8,column = 4)


    
    

def John():
    johns= Toplevel(main)
    johns.title("John Smith")
    johns.geometry("410x350")

    Jhwtotal= IntVar(value=100)
    Jhw1grade= IntVar(value=66)

    Label(johns,text= "Class").grid(row=0,column=0)
    Label(johns,text= "Assignment").grid(row=0,column=1)
    Label(johns,text= "Grade").grid(row=0,column=2)
    Label(johns,text='Total Points').grid(row=0,column=3)
    Label(johns,text='Grade').grid(row=0,column=4)
 
    Label(johns,text= 'Letter Grade').grid(row=0,column=5)
    


    Label(johns,text= "CSET 4250").grid(row=1,column=0)
    Label(johns,text= "CSET 4850").grid(row=2,column=0)
    Label(johns,text= "Homework 1").grid(row=1,column=1)
    Label(johns,textvariable= Jhw1grade).grid(row=1,column=2)
    Label(johns,textvariable= Jhwtotal).grid(row=1,column=3)
 
    Label(johns,textvariable= Jhw1grade, text='%').grid(row=1,column=5)


def Scott():
    scotts= Toplevel(main)
    scotts.title("Scott Brahaney")
    scotts.geometry("410x350")

    Shwtotal= IntVar(value=100)
    Shw1grade= IntVar(value=99)

    Label(scotts,text= "Class").grid(row=0,column=0)
    Label(scotts,text= "Assignment").grid(row=0,column=1)
    Label(scotts,text= "Grade").grid(row=0,column=2)
    Label(scotts,text='Total Points').grid(row=0,column=3)
    Label(scotts,text='Grade').grid(row=0,column=4)
 
    Label(scotts,text= 'Letter Grade').grid(row=0,column=5)
    


    Label(scotts,text= "CSET 4250").grid(row=1,column=0)
    Label(scotts,text= "CSET 4850").grid(row=2,column=0)
    Label(scotts,text= "Homework 1").grid(row=1,column=1)
    Label(scotts,textvariable= Shw1grade).grid(row=1,column=2)
    Label(scotts,textvariable= Shwtotal).grid(row=1,column=3)
 
    Label(scotts,textvariable= Shw1grade, text='%').grid(row=1,column=5)

def Susan():
    susans= Toplevel(main)
    susans.title("Susan Higgins")
    susans.geometry("410x350")

    Suhwtotal= IntVar(value=100)
    Suhw1grade= IntVar(value=75)

    Label(susans,text= "Class").grid(row=0,column=0)
    Label(susans,text= "Assignment").grid(row=0,column=1)
    Label(susans,text= "Grade").grid(row=0,column=2)
    Label(susans,text='Total Points').grid(row=0,column=3)
    Label(susans,text='Grade').grid(row=0,column=4)
 
    Label(susans,text= 'Letter Grade').grid(row=0,column=5)
    


    Label(susans,text= "CSET 4250").grid(row=1,column=0)
    Label(susans,text= "CSET 4850").grid(row=2,column=0)
    Label(susans,text= "Homework 1").grid(row=1,column=1)
    Label(susans,textvariable= Suhw1grade).grid(row=1,column=2)
    Label(susans,textvariable= Suhwtotal).grid(row=1,column=3)
 
    Label(susans,textvariable= Suhw1grade, text='%').grid(row=1,column=5)

    

    

    

def Students():
    global main
    main = Tk()
    main.geometry("600x600")
    main.title("Student Selector")

    Label(text="Select the student whose gradebook you would like to view: ", font = "Verdana 10 bold").pack()
    Button(text = "Adam Mitchell" , height ="2" , width = "20" , command = Adam).pack()
    Label(text="").pack()
    Button(text = "John Smith" , height ="2" , width = "20" , command = John).pack()
    Label(text="").pack()
    Button(text = "Scott Brahaney" , height ="2" , width = "20" , command = Scott).pack()
    Label(text="").pack()
    Button(text = "Susan Higgins" , height ="2" , width = "20" , command = Susan).pack()


    main.mainloop()

Students()
        
    
