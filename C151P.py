from tkinter import*
root= Tk()
root.title("Sales Application")
root.geometry("800x800")


month=("January","February","March","April","May","June","July","August","September","October","November","December")
profits=(400000,352467,728193,958745,790976,125686,893523,686643,283098,123589,203645,45369015)

l1 = Label(root,text=month)
l1.place(relx=0.5, rely=0.3, anchor=CENTER)

l2 = Label(root,text=profits)
l2.place(relx=0.5, rely=0.4, anchor=CENTER)

l3 = Label(root)
l3.place(relx=0.5, rely=0.6, anchor=CENTER)

l4 = Label(root)
l4.place(relx=0.5, rely=0.8, anchor=CENTER)

def max1():
    mx= max(profits)
    print(mx)

    mxi= profits.index(mx)
    print(mxi)

    mn1= month[mxi]
    print(mn1)
    print("The maxximum sales record of " + str(mx)+ " in the month of "+ mn1)
    l3["text"]= "The maxximum sales record of " + str(mx)+ " in the month of "+ mn1
    
def min1(): 
    mn= min(profits)
    print(mn)

    mni= profits.index(mn)
    print(mni)

    mn2= month[mni]
    print(mn2)
    print("The minimum sales record of " + str(mn)+ " in the month of "+ mn2)
    l4["text"]="The minimum sales record of " + str(mn)+ " in the month of "+ mn2

b1=Button(root,text="Find Maximmum sales", command=max1)
b1.place(relx=0.5, rely=0.5, anchor=CENTER)


b2=Button(root,text="Find Minimum sales", command=min1)
b2.place(relx=0.5, rely=0.7, anchor=CENTER)


root.mainloop()