from tkinter import *
from tkinter import ttk

def Adam():
    adamscreen = Toplevel(main)
    adamscreen.title("Adam Mitchell")
    adamscreen.geometry("500x500")
    
    
   
    def editadamhw1():
        entryhw1a.grid(row= 1, column=1)
        
    def updatehw1():
        try:
            int(entryhw1a.get())
            if int(entryhw1a.get()) > 100:
               Label(tab1,text='Invalid').grid(row=1,column=7)
            elif int(entryhw1a.get()) <0:
                Label(tab1,text='Invalid').grid(row=1,column=7)
            else:
                global array1
                array1 = ["90\n","90\n","90\n","90\n"]
          
                myfile= open("Adam_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryhw1a.get() + "\n"

                array1[3] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("Adam_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryhw1a.grid_forget()
                adamscreen.destroy()
                Adam()
        except ValueError:
            Label(tab1,text="Invalid").grid(row=1,column=7)
            
    def editadamhw2():
        entryhw2a.grid(row= 2, column=1)
            
    def updatehw2():
        try:
            int(entryhw2a.get())
            if int(entryhw2a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=2,column=7)
            elif int(entryhw2a.get()) <0:
                Label(tab1,text='Invalid').grid(row=2,column=7)
            else:
                global array1
                array1 = ["90\n","90\n","90\n","90\n"]
                myfile= open("Adam_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryhw2a.get() + "\n"

                array1[2] =str(shownew)
                
                array1str= [str(int) for int in array1]

                myfile = open("Adam_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryhw2a.grid_forget()
                adamscreen.destroy()
                Adam()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=2,column=7)
    def editadamt1():
        entryt1a.grid(row= 3, column=1)
        
    def updatet1():
        try:
            int(entryt1a.get())
            if int(entryt1a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=3,column=7)
            elif int(entryt1a.get()) <0:
                Label(tab1,text='Invalid').grid(row=3,column=7)
            else:
                global array1
                array1 = ["90\n","90\n","90\n","90\n"]
          
                myfile= open("Adam_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryt1a.get() + "\n"

                array1[1] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("Adam_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryt1a.grid_forget()
                adamscreen.destroy()
                Adam()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=3,column=7)
            
    def editadamt2():
        entryt2a.grid(row= 4, column=1)
        
    def updatet2():
        try:
            int(entryt2a.get())
            if int(entryt2a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=4,column=7)
            elif int(entryt2a.get()) <0:
               Label(tab1,text='Invalid').grid(row=4,column=7)
            else:
                global array1
                array1 = ["90\n","90\n","90\n","90\n"]
          
                myfile= open("Adam_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryt2a.get() + "\n"

                array1[0] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("Adam_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryt2a.grid_forget()
                adamscreen.destroy()
                Adam()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=4,column=7)
        
        
    f= open("Adam_CSET4250.txt", "r")
    global array1
    array1=[]    
    file = f.readline()
    files= file.rstrip("\n")

    while file != '':
        q=0
        grade=int(file)
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

    total= 100
    newarray1 = [int(i)/total for i in array1]
    hw1grade = IntVar(value=newarray1[0]*100)
    hw2grade = IntVar(value=newarray1[1]*100)
    test1grade = IntVar(value=newarray1[2]*100)
    test2grade = IntVar(value=newarray1[3]*100)

    hwtotal = IntVar(value=hw1grade.get() + hw2grade.get())
    testtotal = IntVar(value=test1grade.get() + test2grade.get())
    totalhw=IntVar(value=ahwtotal.get() * 2)
    totaltest= IntVar(value=ahwtotal.get() * 2)
    totalpoints= IntVar(value=ahwtotal.get() * 4)

    hwgrade = IntVar( value= (hwtotal.get() / totalhw.get()) * 100)
    testgrade = IntVar( value= (testtotal.get() / totaltest.get()) * 100)
    totalgrade = IntVar( value= ((hwtotal.get()+testtotal.get()) / totalpoints.get()) * 100)
    hwandtest= IntVar( value=hwtotal.get()+testtotal.get())
    

    
#get hw1 letter grade
    if hw1grade.get() >=90:
        hw1letter=StringVar(value= 'A')
    elif hw1grade.get() >= 80:
        hw1letter= StringVar(value='B')
    elif hw1grade.get() >= 70:
        hw1letter= StringVar(value='C')
    elif hw1grade.get() >= 60:
        hw1letter= StringVar(value='D')
    else:
        hw1letter= StringVar(value='F')
# get hw2 letter grade
    if hw2grade.get() >=90:
        hw2letter=StringVar(value= 'A')
    elif hw2grade.get() >= 80:
        hw2letter= StringVar(value='B')
    elif hw2grade.get() >= 70:
        hw2letter= StringVar(value='C')
    elif hw2grade.get() >= 60:
        hw2letter= StringVar(value='D')
    else:
        hw2letter= StringVar(value='F')
# get test1 letter grade     
    if test1grade.get() >=90:
       test1letter=StringVar(value= 'A')
    elif test1grade.get() >= 80:
        test1letter= StringVar(value='B')
    elif test1grade.get() >= 70:
        test2letter= StringVar(value='C')
    elif test1grade.get() >= 60:
        test1letter= StringVar(value='D')
    else:
        test1letter= StringVar(value='F')
 # get test 2 letter grade        
    if test2grade.get() >=90:
        test2letter=StringVar(value= 'A')
    elif test2grade.get() >= 80:
        test2letter= StringVar(value='B')
    elif test2grade.get() >= 70:
        test2letter= StringVar(value='C')
    elif test2grade.get() >= 60:
        test2letter= StringVar(value='D')
    else:
        test2letter= StringVar(value='F')
# total hw letter grade 
    if hwgrade.get() >=90:
        hwgradeletter=StringVar(value= 'A')
    elif hwgrade.get() >= 80:
        hwgradeletter= StringVar(value='B')
    elif hwgrade.get() >= 70:
        hwgradeletter= StringVar(value='C')
    elif hwgrade.get() >= 60:
        hwgradeletter= StringVar(value='D')
    else:
        hwgradeletter= StringVar(value='F')

    #total test letter grade
    if testgrade.get() >=90:
        testgradeletter=StringVar(value= 'A')
    elif testgrade.get() >= 80:
        testgradeletter= StringVar(value='B')
    elif testgrade.get() >= 70:
        testgradeletter= StringVar(value='C')
    elif testgrade.get() >= 60:
        testgradeletter= StringVar(value='D')
    else:
        testgradeletter= StringVar(value='F')

        #overall letter grade
    if totalgrade.get() >=90:
        totalgradeletter=StringVar(value= 'A')
    elif totalgrade.get() >= 80:
        totalgradeletter= StringVar(value='B')
    elif totalgrade.get() >= 70:
        totalgradeletter= StringVar(value='C')
    elif totalgrade.get() >= 60:
        totalgradeletter= StringVar(value='D')
    else:
        totalgradeletter= StringVar(value='F')
   
   
    
    
    Label(tab1,text= "Assignment").grid(row=0,column=0)
    Label(tab1,text= "Points").grid(row=0,column=1)
    Label(tab1,text='Total Points').grid(row=0,column=2)
    Label(tab1,text='Grade(%)').grid(row=0,column=3)
    Label(tab1,text= 'Letter Grade').grid(row=0,column=4)
    

#HW1 

    Label(tab1,text= "Homework 1").grid(row=1,column=0)
    Label(tab1,textvariable= hw1adam).grid(row=1,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=1,column=2)
    Label(tab1,textvariable= hw1grade).grid(row=1,column=3)
    Label(tab1, textvariable=hw1letter).grid(row=1,column=4)
    Button(tab1,text='Edit Score', command= editadamhw1).grid(row=1,column=5)
    Button(tab1,text= 'Update', command= updatehw1).grid(row=1,column=6)
    entryhw1a= Entry(tab1,width='3')
   
#Hw2
    Label(tab1,text= "Homework 2").grid(row=2,column=0)
    Label(tab1,textvariable= hw2adam).grid(row=2,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=2,column=2)
    Label(tab1,textvariable= hw2grade).grid(row=2,column=3)
    Label(tab1, textvariable= hw2letter).grid(row=2,column=4)
    Button(tab1,text='Edit Score', command= editadamhw2).grid(row=2,column=5)
    Button(tab1,text= 'Update', command= updatehw2).grid(row=2,column=6)
    entryhw2a= Entry(tab1,width='3')
#test 1
    Label(tab1,text= "Test 1").grid(row=3,column=0)
    Label(tab1,textvariable= test1adam).grid(row=3,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=3,column=2)
    Label(tab1,textvariable= test1grade).grid(row=3,column=3)
    Label(tab1, textvariable= test1letter).grid(row=3,column=4)
    Button(tab1,text='Edit Score', command= editadamt1).grid(row=3,column=5)
    Button(tab1,text= 'Update', command= updatet1).grid(row=3,column=6)
    entryt1a= Entry(tab1,width='3')
# test 2
    Label(tab1,text= "Test 2").grid(row=4,column=0)
    Label(tab1,textvariable= test2adam).grid(row=4,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=4,column=2)
    Label(tab1,textvariable= test2grade).grid(row=4,column=3)
    Label(tab1, textvariable=test2letter).grid(row=4,column=4)
    Button(tab1,text='Edit Score', command= editadamt2).grid(row=4,column=5)
    Button(tab1,text= 'Update', command= updatet2).grid(row=4,column=6)
    entryt2a= Entry(tab1,width='3')

    Label(tab1, text= "").grid(row=5,column=0)

#overall grades for cset4250
    #HW grade
    Label(tab1, text= "Homework grade").grid(row=6,column=0)
    Label(tab1, textvariable = hwtotal ).grid(row=6,column = 1)
    Label(tab1, textvariable = totalhw).grid(row=6,column = 2)
    Label(tab1, textvariable = hwgrade ).grid(row=6,column = 3)
    Label(tab1, textvariable = hwgradeletter).grid(row=6,column = 4)
    #Test grade 

    Label(tab1, text= "Test grade").grid(row=7,column=0)
    Label(tab1, textvariable = testtotal).grid(row=7,column=1)
    Label(tab1, textvariable = totaltest).grid(row=7,column=2)
    Label(tab1, textvariable=testgrade ).grid(row=7,column = 3)
    Label(tab1, textvariable= testgradeletter  ).grid(row=7,column = 4)

    #overall grade

    Label(tab1, text= "Overall grade").grid(row=8,column=0)
    Label(tab1, textvariable= hwandtest ).grid(row=8,column=1)
    Label(tab1, textvariable=totalpoints).grid(row=8,column=2)
    Label(tab1, textvariable = totalgrade ).grid(row=8,column = 3)
    Label(tab1, textvariable= totalgradeletter ).grid(row=8,column = 4)

    
################################################################################CSET 4850 #################################################################

    

    
 #########################JOHN############################################################   

def John():
    johns= Toplevel(main)
    johns.title("John Smith")
    johns.geometry("500x500")


    def editjohnhw1():
       entryhw1a.grid(row= 1, column=1)
        
    def updatehw1():
        try:
            int(entryhw1a.get())
            if int(entryhw1a.get()) > 100:
               Label(tab1,text='Invalid').grid(row=1,column=7)
            elif int(entryhw1a.get()) <0:
                Label(tab1,text='Invalid').grid(row=1,column=7)
            else:
                global array1
                array1 = ["90\n","70\n","76\n","81\n"]
          
                myfile= open("John_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryhw1a.get() + "\n"

                array1[3] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("John_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryhw1a.grid_forget()
                johns.destroy()
                John()
        except ValueError:
            Label(tab1,text="Invalid").grid(row=1,column=7)
            
    def editjohnhw2():
        entryhw2a.grid(row= 2, column=1)
            
    def updatehw2():
        try:
            int(entryhw2a.get())
            if int(entryhw2a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=2,column=7)
            elif int(entryhw2a.get()) <0:
                Label(tab1,text='Invalid').grid(row=2,column=7)
            else:
                global array1
                array1 = ["90\n","70\n","76\n","81\n"]
                myfile= open("John_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryhw2a.get() + "\n"

                array1[2] =str(shownew)
                
                array1str= [str(int) for int in array1]

                myfile = open("John_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryhw2a.grid_forget()
                johns.destroy()
                John()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=2,column=7)
    def editjohnt1():
        entryt1a.grid(row= 3, column=1)
        
    def updatet1():
        try:
            int(entryt1a.get())
            if int(entryt1a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=3,column=7)
            elif int(entryt1a.get()) <0:
                Label(tab1,text='Invalid').grid(row=3,column=7)
            else:
                global array1
                array1 = ["90\n","70\n","76\n","81\n"]
          
                myfile= open("John_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryt1a.get() + "\n"

                array1[1] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("John_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryt1a.grid_forget()
                johns.destroy()
                John()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=3,column=7)
            
    def editjohnt2():
        entryt2a.grid(row= 4, column=1)
        
    def updatet2():
        try:
            int(entryt2a.get())
            if int(entryt2a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=4,column=7)
            elif int(entryt2a.get()) <0:
               Label(tab1,text='Invalid').grid(row=4,column=7)
            else:
                global array1
                array1 = ["90\n","70\n","76\n","81\n"]
          
                myfile= open("John_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryt2a.get() + "\n"

                array1[0] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("John_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryt2a.grid_forget()
                johns.destroy()
                John()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=4,column=7)
        
        
    f= open("John_CSET4250.txt", "r")
    global array1
    array1=[]    
    file = f.readline()
    files= file.rstrip("\n")

    while file != '':
        q=0
        grade=int(file)
        array1.insert(q,grade)
        file = f.readline()
        files= file.rstrip("\n")
        q=q+1
        
    hw1john= IntVar(value=array1[0])
    hw2john= IntVar(value=array1[1])
    test1john= IntVar(value=array1[2])
    test2john= IntVar(value=array1[3])

    f.close()
    
    


    tabControl = ttk.Notebook(johns)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text ='CSET 4250')
    tabControl.add(tab2, text ='CSET 4850')
    tabControl.pack(expand = 1, fill ="both")


    ahwtotal= IntVar(value=100)

    total= 100
    newarray1 = [int(i)/total for i in array1]
    hw1grade = IntVar(value=newarray1[0]*100)
    hw2grade = IntVar(value=newarray1[1]*100)
    test1grade = IntVar(value=newarray1[2]*100)
    test2grade = IntVar(value=newarray1[3]*100)

    hwtotal = IntVar(value=hw1grade.get() + hw2grade.get())
    testtotal = IntVar(value=test1grade.get() + test2grade.get())
    totalhw=IntVar(value=ahwtotal.get() * 2)
    totaltest= IntVar(value=ahwtotal.get() * 2)
    totalpoints= IntVar(value=ahwtotal.get() * 4)

    hwgrade = IntVar( value= (hwtotal.get() / totalhw.get()) * 100)
    testgrade = IntVar( value= (testtotal.get() / totaltest.get()) * 100)
    totalgrade = IntVar( value= ((hwtotal.get()+testtotal.get()) / totalpoints.get()) * 100)
    hwandtest= IntVar( value=hwtotal.get()+testtotal.get())
    

    
#get hw1 letter grade
    if hw1grade.get() >=90:
        hw1letter=StringVar(value= 'A')
    elif hw1grade.get() >= 80:
        hw1letter= StringVar(value='B')
    elif hw1grade.get() >= 70:
        hw1letter= StringVar(value='C')
    elif hw1grade.get() >= 60:
        hw1letter= StringVar(value='D')
    else:
        hw1letter= StringVar(value='F')
# get hw2 letter grade
    if hw2grade.get() >=90:
        hw2letter=StringVar(value= 'A')
    elif hw2grade.get() >= 80:
        hw2letter= StringVar(value='B')
    elif hw2grade.get() >= 70:
        hw2letter= StringVar(value='C')
    elif hw2grade.get() >= 60:
        hw2letter= StringVar(value='D')
    else:
        hw2letter= StringVar(value='F')
# get test1 letter grade     
    if test1grade.get() >=90:
        test1letter = StringVar(value= 'A')
    elif test1grade.get() >= 80:
        test1letter= StringVar(value='B')
    elif test1grade.get() >= 70:
        test1letter= StringVar(value='C')
    elif test1grade.get() >= 60:
        test1letter= StringVar(value='D')
    else:
        test1letter= StringVar(value='F')
 # get test 2 letter grade        
    if test2grade.get() >=90:
        test2letter=StringVar(value= 'A')
    elif test2grade.get() >= 80:
        test2letter= StringVar(value='B')
    elif test2grade.get() >= 70:
        test2letter= StringVar(value='C')
    elif test2grade.get() >= 60:
        test2letter= StringVar(value='D')
    else:
        test2letter= StringVar(value='F')
# total hw letter grade 
    if hwgrade.get() >=90:
        hwgradeletter=StringVar(value= 'A')
    elif hwgrade.get() >= 80:
        hwgradeletter= StringVar(value='B')
    elif hwgrade.get() >= 70:
        hwgradeletter= StringVar(value='C')
    elif hwgrade.get() >= 60:
        hwgradeletter= StringVar(value='D')
    else:
        hwgradeletter= StringVar(value='F')

    #total test letter grade
    if testgrade.get() >=90:
        testgradeletter=StringVar(value= 'A')
    elif testgrade.get() >= 80:
        testgradeletter= StringVar(value='B')
    elif testgrade.get() >= 70:
        testgradeletter= StringVar(value='C')
    elif testgrade.get() >= 60:
        testgradeletter= StringVar(value='D')
    else:
        testgradeletter= StringVar(value='F')

        #overall letter grade
    if totalgrade.get() >=90:
        totalgradeletter=StringVar(value= 'A')
    elif totalgrade.get() >= 80:
        totalgradeletter= StringVar(value='B')
    elif totalgrade.get() >= 70:
        totalgradeletter= StringVar(value='C')
    elif totalgrade.get() >= 60:
        totalgradeletter= StringVar(value='D')
    else:
        totalgradeletter= StringVar(value='F')
   
   
    
    
    Label(tab1,text= "Assignment").grid(row=0,column=0)
    Label(tab1,text= "Points").grid(row=0,column=1)
    Label(tab1,text='Total Points').grid(row=0,column=2)
    Label(tab1,text='Grade(%)').grid(row=0,column=3)
    Label(tab1,text= 'Letter Grade').grid(row=0,column=4)
    

#HW1 

    Label(tab1,text= "Homework 1").grid(row=1,column=0)
    Label(tab1,textvariable= hw1john).grid(row=1,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=1,column=2)
    Label(tab1,textvariable= hw1grade).grid(row=1,column=3)
    Label(tab1, textvariable=hw1letter).grid(row=1,column=4)
    Button(tab1,text='Edit Score', command= editjohnhw1).grid(row=1,column=5)
    Button(tab1,text= 'Update', command= updatehw1).grid(row=1,column=6)
    entryhw1a= Entry(tab1,width='3')
   
#Hw2
    Label(tab1,text= "Homework 2").grid(row=2,column=0)
    Label(tab1,textvariable= hw2john).grid(row=2,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=2,column=2)
    Label(tab1,textvariable= hw2grade).grid(row=2,column=3)
    Label(tab1, textvariable= hw2letter).grid(row=2,column=4)
    Button(tab1,text='Edit Score', command= editjohnhw2).grid(row=2,column=5)
    Button(tab1,text= 'Update', command= updatehw2).grid(row=2,column=6)
    entryhw2a= Entry(tab1,width='3')
#test 1
    Label(tab1,text= "Test 1").grid(row=3,column=0)
    Label(tab1,textvariable= test1john).grid(row=3,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=3,column=2)
    Label(tab1,textvariable= test1grade).grid(row=3,column=3)
    Label(tab1, textvariable= test1letter).grid(row=3,column=4)
    Button(tab1,text='Edit Score', command= editjohnt1).grid(row=3,column=5)
    Button(tab1,text= 'Update', command= updatet1).grid(row=3,column=6)
    entryt1a= Entry(tab1,width='3')
# test 2
    Label(tab1,text= "Test 2").grid(row=4,column=0)
    Label(tab1,textvariable= test2john).grid(row=4,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=4,column=2)
    Label(tab1,textvariable= test2grade).grid(row=4,column=3)
    Label(tab1, textvariable=test2letter).grid(row=4,column=4)
    Button(tab1,text='Edit Score', command= editjohnt2).grid(row=4,column=5)
    Button(tab1,text= 'Update', command= updatet2).grid(row=4,column=6)
    entryt2a= Entry(tab1,width='3')

    Label(tab1, text= "").grid(row=5,column=0)

#overall grades for cset4250
    #HW grade
    Label(tab1, text= "Homework grade").grid(row=6,column=0)
    Label(tab1, textvariable = hwtotal ).grid(row=6,column = 1)
    Label(tab1, textvariable = totalhw).grid(row=6,column = 2)
    Label(tab1, textvariable = hwgrade ).grid(row=6,column = 3)
    Label(tab1, textvariable = hwgradeletter).grid(row=6,column = 4)
    #Test grade 

    Label(tab1, text= "Test grade").grid(row=7,column=0)
    Label(tab1, textvariable = testtotal).grid(row=7,column=1)
    Label(tab1, textvariable = totaltest).grid(row=7,column=2)
    Label(tab1, textvariable=testgrade ).grid(row=7,column = 3)
    Label(tab1, textvariable= testgradeletter  ).grid(row=7,column = 4)

    #overall grade

    Label(tab1, text= "Overall grade").grid(row=8,column=0)
    Label(tab1, textvariable= hwandtest ).grid(row=8,column=1)
    Label(tab1, textvariable=totalpoints).grid(row=8,column=2)
    Label(tab1, textvariable = totalgrade ).grid(row=8,column = 3)
    Label(tab1, textvariable= totalgradeletter ).grid(row=8,column = 4)

######################################SCOTT############################################
def Scott():
    scotts= Toplevel(main)
    scotts.title("Scott Brahaney")
    scotts.geometry("500x500")

    def editjohnhw1():
       entryhw1a.grid(row= 1, column=1)
        
    def updatehw1():
        try:
            int(entryhw1a.get())
            if int(entryhw1a.get()) > 100:
               Label(tab1,text='Invalid').grid(row=1,column=7)
            elif int(entryhw1a.get()) <0:
                Label(tab1,text='Invalid').grid(row=1,column=7)
            else:
                global array1
                array1 = ["100\n","100\n","100\n","100\n"]
          
                myfile= open("Scott_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryhw1a.get() + "\n"

                array1[3] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("Scott_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryhw1a.grid_forget()
                scotts.destroy()
                Scott()
        except ValueError:
            Label(tab1,text="Invalid").grid(row=1,column=7)
            
    def editjohnhw2():
        entryhw2a.grid(row= 2, column=1)
            
    def updatehw2():
        try:
            int(entryhw2a.get())
            if int(entryhw2a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=2,column=7)
            elif int(entryhw2a.get()) <0:
                Label(tab1,text='Invalid').grid(row=2,column=7)
            else:
                global array1
                array1 = ["100\n","100\n","100\n","100\n"]
                myfile= open("Scott_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryhw2a.get() + "\n"

                array1[2] =str(shownew)
                
                array1str= [str(int) for int in array1]

                myfile = open("Scott_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryhw2a.grid_forget()
                scotts.destroy()
                Scott()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=2,column=7)
    def editjohnt1():
        entryt1a.grid(row= 3, column=1)
        
    def updatet1():
        try:
            int(entryt1a.get())
            if int(entryt1a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=3,column=7)
            elif int(entryt1a.get()) <0:
                Label(tab1,text='Invalid').grid(row=3,column=7)
            else:
                global array1
                array1 = ["100\n","100\n","100\n","100\n"]
          
                myfile= open("Scott_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryt1a.get() + "\n"

                array1[1] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("Scott_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryt1a.grid_forget()
                scotts.destroy()
                Scott()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=3,column=7)
            
    def editjohnt2():
        entryt2a.grid(row= 4, column=1)
        
    def updatet2():
        try:
            int(entryt2a.get())
            if int(entryt2a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=4,column=7)
            elif int(entryt2a.get()) <0:
               Label(tab1,text='Invalid').grid(row=4,column=7)
            else:
                global array1
                array1 = ["100\n","100\n","100\n","100\n"]
          
                myfile= open("Scott_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryt2a.get() + "\n"

                array1[0] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("Scott_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryt2a.grid_forget()
                scotts.destroy()
                Scott()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=4,column=7)
        
        
    f= open("Scott_CSET4250.txt", "r")
    global array1
    array1=[]    
    file = f.readline()
    files= file.rstrip("\n")

    while file != '':
        q=0
        grade=int(file)
        array1.insert(q,grade)
        file = f.readline()
        files= file.rstrip("\n")
        q=q+1
        
    hw1john= IntVar(value=array1[0])
    hw2john= IntVar(value=array1[1])
    test1john= IntVar(value=array1[2])
    test2john= IntVar(value=array1[3])

    f.close()
    
    


    tabControl = ttk.Notebook(scotts)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text ='CSET 4250')
    tabControl.add(tab2, text ='CSET 4850')
    tabControl.pack(expand = 1, fill ="both")


    ahwtotal= IntVar(value=100)

    total= 100
    newarray1 = [int(i)/total for i in array1]
    hw1grade = IntVar(value=newarray1[0]*100)
    hw2grade = IntVar(value=newarray1[1]*100)
    test1grade = IntVar(value=newarray1[2]*100)
    test2grade = IntVar(value=newarray1[3]*100)

    hwtotal = IntVar(value=hw1grade.get() + hw2grade.get())
    testtotal = IntVar(value=test1grade.get() + test2grade.get())
    totalhw=IntVar(value=ahwtotal.get() * 2)
    totaltest= IntVar(value=ahwtotal.get() * 2)
    totalpoints= IntVar(value=ahwtotal.get() * 4)

    hwgrade = IntVar( value= (hwtotal.get() / totalhw.get()) * 100)
    testgrade = IntVar( value= (testtotal.get() / totaltest.get()) * 100)
    totalgrade = IntVar( value= ((hwtotal.get()+testtotal.get()) / totalpoints.get()) * 100)
    hwandtest= IntVar( value=hwtotal.get()+testtotal.get())
    

    
#get hw1 letter grade
    if hw1grade.get() >=90:
        hw1letter=StringVar(value= 'A')
    elif hw1grade.get() >= 80:
        hw1letter= StringVar(value='B')
    elif hw1grade.get() >= 70:
        hw1letter= StringVar(value='C')
    elif hw1grade.get() >= 60:
        hw1letter= StringVar(value='D')
    else:
        hw1letter= StringVar(value='F')
# get hw2 letter grade
    if hw2grade.get() >=90:
        hw2letter=StringVar(value= 'A')
    elif hw2grade.get() >= 80:
        hw2letter= StringVar(value='B')
    elif hw2grade.get() >= 70:
        hw2letter= StringVar(value='C')
    elif hw2grade.get() >= 60:
        hw2letter= StringVar(value='D')
    else:
        hw2letter= StringVar(value='F')
# get test1 letter grade     
    if test1grade.get() >=90:
        test1letter = StringVar(value= 'A')
    elif test1grade.get() >= 80:
        test1letter= StringVar(value='B')
    elif test1grade.get() >= 70:
        test1letter= StringVar(value='C')
    elif test1grade.get() >= 60:
        test1letter= StringVar(value='D')
    else:
        test1letter= StringVar(value='F')
 # get test 2 letter grade        
    if test2grade.get() >=90:
        test2letter=StringVar(value= 'A')
    elif test2grade.get() >= 80:
        test2letter= StringVar(value='B')
    elif test2grade.get() >= 70:
        test2letter= StringVar(value='C')
    elif test2grade.get() >= 60:
        test2letter= StringVar(value='D')
    else:
        test2letter= StringVar(value='F')
# total hw letter grade 
    if hwgrade.get() >=90:
        hwgradeletter=StringVar(value= 'A')
    elif hwgrade.get() >= 80:
        hwgradeletter= StringVar(value='B')
    elif hwgrade.get() >= 70:
        hwgradeletter= StringVar(value='C')
    elif hwgrade.get() >= 60:
        hwgradeletter= StringVar(value='D')
    else:
        hwgradeletter= StringVar(value='F')

    #total test letter grade
    if testgrade.get() >=90:
        testgradeletter=StringVar(value= 'A')
    elif testgrade.get() >= 80:
        testgradeletter= StringVar(value='B')
    elif testgrade.get() >= 70:
        testgradeletter= StringVar(value='C')
    elif testgrade.get() >= 60:
        testgradeletter= StringVar(value='D')
    else:
        testgradeletter= StringVar(value='F')

        #overall letter grade
    if totalgrade.get() >=90:
        totalgradeletter=StringVar(value= 'A')
    elif totalgrade.get() >= 80:
        totalgradeletter= StringVar(value='B')
    elif totalgrade.get() >= 70:
        totalgradeletter= StringVar(value='C')
    elif totalgrade.get() >= 60:
        totalgradeletter= StringVar(value='D')
    else:
        totalgradeletter= StringVar(value='F')
   
   
    
    
    Label(tab1,text= "Assignment").grid(row=0,column=0)
    Label(tab1,text= "Points").grid(row=0,column=1)
    Label(tab1,text='Total Points').grid(row=0,column=2)
    Label(tab1,text='Grade(%)').grid(row=0,column=3)
    Label(tab1,text= 'Letter Grade').grid(row=0,column=4)
    

#HW1 

    Label(tab1,text= "Homework 1").grid(row=1,column=0)
    Label(tab1,textvariable= hw1john).grid(row=1,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=1,column=2)
    Label(tab1,textvariable= hw1grade).grid(row=1,column=3)
    Label(tab1, textvariable=hw1letter).grid(row=1,column=4)
    Button(tab1,text='Edit Score', command= editjohnhw1).grid(row=1,column=5)
    Button(tab1,text= 'Update', command= updatehw1).grid(row=1,column=6)
    entryhw1a= Entry(tab1,width='3')
   
#Hw2
    Label(tab1,text= "Homework 2").grid(row=2,column=0)
    Label(tab1,textvariable= hw2john).grid(row=2,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=2,column=2)
    Label(tab1,textvariable= hw2grade).grid(row=2,column=3)
    Label(tab1, textvariable= hw2letter).grid(row=2,column=4)
    Button(tab1,text='Edit Score', command= editjohnhw2).grid(row=2,column=5)
    Button(tab1,text= 'Update', command= updatehw2).grid(row=2,column=6)
    entryhw2a= Entry(tab1,width='3')
#test 1
    Label(tab1,text= "Test 1").grid(row=3,column=0)
    Label(tab1,textvariable= test1john).grid(row=3,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=3,column=2)
    Label(tab1,textvariable= test1grade).grid(row=3,column=3)
    Label(tab1, textvariable= test1letter).grid(row=3,column=4)
    Button(tab1,text='Edit Score', command= editjohnt1).grid(row=3,column=5)
    Button(tab1,text= 'Update', command= updatet1).grid(row=3,column=6)
    entryt1a= Entry(tab1,width='3')
# test 2
    Label(tab1,text= "Test 2").grid(row=4,column=0)
    Label(tab1,textvariable= test2john).grid(row=4,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=4,column=2)
    Label(tab1,textvariable= test2grade).grid(row=4,column=3)
    Label(tab1, textvariable=test2letter).grid(row=4,column=4)
    Button(tab1,text='Edit Score', command= editjohnt2).grid(row=4,column=5)
    Button(tab1,text= 'Update', command= updatet2).grid(row=4,column=6)
    entryt2a= Entry(tab1,width='3')

    Label(tab1, text= "").grid(row=5,column=0)

#overall grades for cset4250
    #HW grade
    Label(tab1, text= "Homework grade").grid(row=6,column=0)
    Label(tab1, textvariable = hwtotal ).grid(row=6,column = 1)
    Label(tab1, textvariable = totalhw).grid(row=6,column = 2)
    Label(tab1, textvariable = hwgrade ).grid(row=6,column = 3)
    Label(tab1, textvariable = hwgradeletter).grid(row=6,column = 4)
    #Test grade 

    Label(tab1, text= "Test grade").grid(row=7,column=0)
    Label(tab1, textvariable = testtotal).grid(row=7,column=1)
    Label(tab1, textvariable = totaltest).grid(row=7,column=2)
    Label(tab1, textvariable=testgrade ).grid(row=7,column = 3)
    Label(tab1, textvariable= testgradeletter  ).grid(row=7,column = 4)

    #overall grade

    Label(tab1, text= "Overall grade").grid(row=8,column=0)
    Label(tab1, textvariable= hwandtest ).grid(row=8,column=1)
    Label(tab1, textvariable=totalpoints).grid(row=8,column=2)
    Label(tab1, textvariable = totalgrade ).grid(row=8,column = 3)
    Label(tab1, textvariable= totalgradeletter ).grid(row=8,column = 4)
#########################################SUSAN############################################
def Susan():
    susans= Toplevel(main)
    susans.title("Susan Higgins")
    susans.geometry("500x500")

    def editjohnhw1():
       entryhw1a.grid(row= 1, column=1)
        
    def updatehw1():
        try:
            int(entryhw1a.get())
            if int(entryhw1a.get()) > 100:
               Label(tab1,text='Invalid').grid(row=1,column=7)
            elif int(entryhw1a.get()) <0:
                Label(tab1,text='Invalid').grid(row=1,column=7)
            else:
                global array1
                array1 = ["99\n","81\n","91\n","100\n"]
          
                myfile= open("Susan_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryhw1a.get() + "\n"

                array1[3] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("Susan_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryhw1a.grid_forget()
                susans.destroy()
                Susan()
        except ValueError:
            Label(tab1,text="Invalid").grid(row=1,column=7)
            
    def editjohnhw2():
        entryhw2a.grid(row= 2, column=1)
            
    def updatehw2():
        try:
            int(entryhw2a.get())
            if int(entryhw2a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=2,column=7)
            elif int(entryhw2a.get()) <0:
                Label(tab1,text='Invalid').grid(row=2,column=7)
            else:
                global array1
                array1 = ["99\n","81\n","91\n","100\n"]
                myfile= open("Susan_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryhw2a.get() + "\n"

                array1[2] =str(shownew)
                
                array1str= [str(int) for int in array1]

                myfile = open("Susan_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryhw2a.grid_forget()
                susans.destroy()
                Susan()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=2,column=7)
    def editjohnt1():
        entryt1a.grid(row= 3, column=1)
        
    def updatet1():
        try:
            int(entryt1a.get())
            if int(entryt1a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=3,column=7)
            elif int(entryt1a.get()) <0:
                Label(tab1,text='Invalid').grid(row=3,column=7)
            else:
                global array1
                array1 = ["99\n","81\n","91\n","100\n"]
          
                myfile= open("Susan_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryt1a.get() + "\n"

                array1[1] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("Susan_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryt1a.grid_forget()
                susans.destroy()
                Susan()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=3,column=7)
            
    def editjohnt2():
        entryt2a.grid(row= 4, column=1)
        
    def updatet2():
        try:
            int(entryt2a.get())
            if int(entryt2a.get()) > 100:
                Label(tab1,text='Invalid').grid(row=4,column=7)
            elif int(entryt2a.get()) <0:
               Label(tab1,text='Invalid').grid(row=4,column=7)
            else:
                global array1
                array1 = ["99\n","81\n","91\n","100\n"]
          
                myfile= open("Susan_CSET4250.txt")
                list1= myfile.readlines()

                shownew= entryt2a.get() + "\n"

                array1[0] =str(shownew)
            
                array1str= [str(int) for int in array1]

                myfile = open("Susan_CSET4250.txt" , "w")
                newfile=''.join(array1str)
    
                myfile.write(newfile)
                myfile.close()
        
                entryt2a.grid_forget()
                susans.destroy()
                Susan()
        except ValueError:
            Label(tab1,text='Invalid').grid(row=4,column=7)
        
        
    f= open("Susan_CSET4250.txt", "r")
    global array1
    array1=[]    
    file = f.readline()
    files= file.rstrip("\n")

    while file != '':
        q=0
        grade=int(file)
        array1.insert(q,grade)
        file = f.readline()
        files= file.rstrip("\n")
        q=q+1
        
    hw1john= IntVar(value=array1[0])
    hw2john= IntVar(value=array1[1])
    test1john= IntVar(value=array1[2])
    test2john= IntVar(value=array1[3])

    f.close()
    
    


    tabControl = ttk.Notebook(susans)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text ='CSET 4250')
    tabControl.add(tab2, text ='CSET 4850')
    tabControl.pack(expand = 1, fill ="both")


    ahwtotal= IntVar(value=100)

    total= 100
    newarray1 = [int(i)/total for i in array1]
    hw1grade = IntVar(value=newarray1[0]*100)
    hw2grade = IntVar(value=newarray1[1]*100)
    test1grade = IntVar(value=newarray1[2]*100)
    test2grade = IntVar(value=newarray1[3]*100)

    hwtotal = IntVar(value=hw1grade.get() + hw2grade.get())
    testtotal = IntVar(value=test1grade.get() + test2grade.get())
    totalhw=IntVar(value=ahwtotal.get() * 2)
    totaltest= IntVar(value=ahwtotal.get() * 2)
    totalpoints= IntVar(value=ahwtotal.get() * 4)

    hwgrade = IntVar( value= (hwtotal.get() / totalhw.get()) * 100)
    testgrade = IntVar( value= (testtotal.get() / totaltest.get()) * 100)
    totalgrade = IntVar( value= ((hwtotal.get()+testtotal.get()) / totalpoints.get()) * 100)
    hwandtest= IntVar( value=hwtotal.get()+testtotal.get())
    

    
#get hw1 letter grade
    if hw1grade.get() >=90:
        hw1letter=StringVar(value= 'A')
    elif hw1grade.get() >= 80:
        hw1letter= StringVar(value='B')
    elif hw1grade.get() >= 70:
        hw1letter= StringVar(value='C')
    elif hw1grade.get() >= 60:
        hw1letter= StringVar(value='D')
    else:
        hw1letter= StringVar(value='F')
# get hw2 letter grade
    if hw2grade.get() >=90:
        hw2letter=StringVar(value= 'A')
    elif hw2grade.get() >= 80:
        hw2letter= StringVar(value='B')
    elif hw2grade.get() >= 70:
        hw2letter= StringVar(value='C')
    elif hw2grade.get() >= 60:
        hw2letter= StringVar(value='D')
    else:
        hw2letter= StringVar(value='F')
# get test1 letter grade     
    if test1grade.get() >=90:
        test1letter = StringVar(value= 'A')
    elif test1grade.get() >= 80:
        test1letter= StringVar(value='B')
    elif test1grade.get() >= 70:
        test1letter= StringVar(value='C')
    elif test1grade.get() >= 60:
        test1letter= StringVar(value='D')
    else:
        test1letter= StringVar(value='F')
 # get test 2 letter grade        
    if test2grade.get() >=90:
        test2letter=StringVar(value= 'A')
    elif test2grade.get() >= 80:
        test2letter= StringVar(value='B')
    elif test2grade.get() >= 70:
        test2letter= StringVar(value='C')
    elif test2grade.get() >= 60:
        test2letter= StringVar(value='D')
    else:
        test2letter= StringVar(value='F')
# total hw letter grade 
    if hwgrade.get() >=90:
        hwgradeletter=StringVar(value= 'A')
    elif hwgrade.get() >= 80:
        hwgradeletter= StringVar(value='B')
    elif hwgrade.get() >= 70:
        hwgradeletter= StringVar(value='C')
    elif hwgrade.get() >= 60:
        hwgradeletter= StringVar(value='D')
    else:
        hwgradeletter= StringVar(value='F')

    #total test letter grade
    if testgrade.get() >=90:
        testgradeletter=StringVar(value= 'A')
    elif testgrade.get() >= 80:
        testgradeletter= StringVar(value='B')
    elif testgrade.get() >= 70:
        testgradeletter= StringVar(value='C')
    elif testgrade.get() >= 60:
        testgradeletter= StringVar(value='D')
    else:
        testgradeletter= StringVar(value='F')

        #overall letter grade
    if totalgrade.get() >=90:
        totalgradeletter=StringVar(value= 'A')
    elif totalgrade.get() >= 80:
        totalgradeletter= StringVar(value='B')
    elif totalgrade.get() >= 70:
        totalgradeletter= StringVar(value='C')
    elif totalgrade.get() >= 60:
        totalgradeletter= StringVar(value='D')
    else:
        totalgradeletter= StringVar(value='F')
   
   
    
    
    Label(tab1,text= "Assignment").grid(row=0,column=0)
    Label(tab1,text= "Points").grid(row=0,column=1)
    Label(tab1,text='Total Points').grid(row=0,column=2)
    Label(tab1,text='Grade(%)').grid(row=0,column=3)
    Label(tab1,text= 'Letter Grade').grid(row=0,column=4)
    

#HW1 

    Label(tab1,text= "Homework 1").grid(row=1,column=0)
    Label(tab1,textvariable= hw1john).grid(row=1,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=1,column=2)
    Label(tab1,textvariable= hw1grade).grid(row=1,column=3)
    Label(tab1, textvariable=hw1letter).grid(row=1,column=4)
    Button(tab1,text='Edit Score', command= editjohnhw1).grid(row=1,column=5)
    Button(tab1,text= 'Update', command= updatehw1).grid(row=1,column=6)
    entryhw1a= Entry(tab1,width='3')
   
#Hw2
    Label(tab1,text= "Homework 2").grid(row=2,column=0)
    Label(tab1,textvariable= hw2john).grid(row=2,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=2,column=2)
    Label(tab1,textvariable= hw2grade).grid(row=2,column=3)
    Label(tab1, textvariable= hw2letter).grid(row=2,column=4)
    Button(tab1,text='Edit Score', command= editjohnhw2).grid(row=2,column=5)
    Button(tab1,text= 'Update', command= updatehw2).grid(row=2,column=6)
    entryhw2a= Entry(tab1,width='3')
#test 1
    Label(tab1,text= "Test 1").grid(row=3,column=0)
    Label(tab1,textvariable= test1john).grid(row=3,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=3,column=2)
    Label(tab1,textvariable= test1grade).grid(row=3,column=3)
    Label(tab1, textvariable= test1letter).grid(row=3,column=4)
    Button(tab1,text='Edit Score', command= editjohnt1).grid(row=3,column=5)
    Button(tab1,text= 'Update', command= updatet1).grid(row=3,column=6)
    entryt1a= Entry(tab1,width='3')
# test 2
    Label(tab1,text= "Test 2").grid(row=4,column=0)
    Label(tab1,textvariable= test2john).grid(row=4,column=1)
    Label(tab1,textvariable= ahwtotal).grid(row=4,column=2)
    Label(tab1,textvariable= test2grade).grid(row=4,column=3)
    Label(tab1, textvariable=test2letter).grid(row=4,column=4)
    Button(tab1,text='Edit Score', command= editjohnt2).grid(row=4,column=5)
    Button(tab1,text= 'Update', command= updatet2).grid(row=4,column=6)
    entryt2a= Entry(tab1,width='3')

    Label(tab1, text= "").grid(row=5,column=0)

#overall grades for cset4250
    #HW grade
    Label(tab1, text= "Homework grade").grid(row=6,column=0)
    Label(tab1, textvariable = hwtotal ).grid(row=6,column = 1)
    Label(tab1, textvariable = totalhw).grid(row=6,column = 2)
    Label(tab1, textvariable = hwgrade ).grid(row=6,column = 3)
    Label(tab1, textvariable = hwgradeletter).grid(row=6,column = 4)
    #Test grade 

    Label(tab1, text= "Test grade").grid(row=7,column=0)
    Label(tab1, textvariable = testtotal).grid(row=7,column=1)
    Label(tab1, textvariable = totaltest).grid(row=7,column=2)
    Label(tab1, textvariable=testgrade ).grid(row=7,column = 3)
    Label(tab1, textvariable= testgradeletter  ).grid(row=7,column = 4)

    #overall grade

    Label(tab1, text= "Overall grade").grid(row=8,column=0)
    Label(tab1, textvariable= hwandtest ).grid(row=8,column=1)
    Label(tab1, textvariable=totalpoints).grid(row=8,column=2)
    Label(tab1, textvariable = totalgrade ).grid(row=8,column = 3)
    Label(tab1, textvariable= totalgradeletter ).grid(row=8,column = 4)

    

    

    

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
        
    
