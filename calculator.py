from tkinter import *

#set the settings of the window
window=Tk()
window.geometry('310x360') #set size
window.title('Calculator') #set title
window.config(background='coral') #set background

def quit() :
    window.destroy()
    exit()

#adding the exit buttom
exit=Button(window ,padx=78,pady=14,bd=4,bg="white",command=quit,text="Quit",font=("times",16,'bold')).place(x=50,y=300)


#adding a number or a sign to the screen(click operand)
def click (nbr) :
    global nbr_on_screen
    nbr_on_screen = nbr_on_screen + str(nbr)
    entry.set(nbr_on_screen)


#clearing the screen
def clear() :
    global nbr_on_screen
    nbr_on_screen = ""
    entry.set(nbr_on_screen)


#answering the operand :
def equal():
     global nbr_on_screen
     try:
         nbr_on_screen=str(eval(nbr_on_screen))
         entry.set(nbr_on_screen)
     except : 
         nbr_on_screen = ""
         entry.set(nbr_on_screen)
         tkinter.messagebox.showerror("Error", "You\'ve made a false entry")


#set the screen
nbr_on_screen = ''
#set and show the screen :
entry=StringVar()
screen=Entry(window, font=("times",12,'bold'), textvariable=entry, width=30, bd=5, bg='white').place(x=50,y=15)


#set and show buttons of numbers :
#set and show nbr 1
button1=Button(window ,padx=14,pady=14,bd=4,bg='white',command=lambda:click(1),text="1",font=("times",16,'bold')).place(x=10,y=60) 

#set and show nbr 2
button2=Button(window ,padx=14,pady=14,bd=4,bg='white',command=lambda:click(2),text="2",font=("times",16,'bold')).place(x=70,y=60)

#set and show nbr 3
button3=Button(window ,padx=14,pady=14,bd=4,bg='white',command=lambda:click(3),text="3",font=("times",16,'bold')).place(x=130,y=60)

#set and show nbr 4
button4=Button(window ,padx=14,pady=14,bd=4,bg='white',command=lambda:click(4),text="4",font=("times",16,'bold')).place(x=10,y=120) 

#set and show nbr 5
button5=Button(window ,padx=14,pady=14,bd=4,bg='white',command=lambda:click(5),text="5",font=("times",16,'bold')).place(x=70,y=120)

#set and show nbr 6
button6=Button(window ,padx=14,pady=14,bd=4,bg='white',command=lambda:click(6),text="6",font=("times",16,'bold')).place(x=130,y=120)

#set and show nbr 7
button7=Button(window ,padx=14,pady=14,bd=4,bg='white',command=lambda:click(7),text="7",font=("times",16,'bold')).place(x=10,y=180) 

#set and show nbr 8
button8=Button(window ,padx=14,pady=14,bd=4,bg='white',command=lambda:click(8),text="8",font=("times",16,'bold')).place(x=70,y=180)

#set and show nbr 9
button9=Button(window ,padx=14,pady=14,bd=4,bg='white',command=lambda:click(9),text="9",font=("times",16,'bold')).place(x=130,y=180)

#set and show nbr 0
button0=Button(window ,padx=44,pady=14,bd=4,bg='white',command=lambda:click(0),text="0",font=("times",16,'bold')).place(x=10,y=240)


#set and show . :
button_dote=Button(window ,padx=16,pady=14,bd=4,bg='white',command=lambda:click("."),text=".",font=("times",16,'bold')).place(x=130,y=240)


#set and show buttons of signs :
#set and show +
button_plus=Button(window ,padx=14,pady=14,bd=4,bg='white',command=lambda:click('+'),text="+",font=("times",16,'bold')).place(x=190,y=60) 

#set and show 
button_moins=Button(window ,padx=14,pady=14,bd=4,bg='white',command=lambda:click('-'),text="-",font=("times",16,'bold')).place(x=250,y=60) 

#set and show *
button_multiplication=Button(window ,padx=15,pady=14,bd=4,bg='white',command=lambda:click('*'),text="X",font=("times",16,'bold')).place(x=190,y=120) 

#set and show /
button_diviser=Button(window ,padx=15,pady=14,bd=4,bg='white',command=lambda:click('/'),text="/",font=("times",16,'bold')).place(x=250,y=120) 


#set button for clear :
button_clear=Button(window ,padx=14,pady=44,bd=4,bg='white',command=clear,text="ce",font=("times",16,'bold')).place(x=190,y=180) 


#set button for clear :
button_equal=Button(window ,padx=14,pady=44,bd=4,bg='white',command=equal,text="=",font=("times",16,'bold')).place(x=250,y=180) 

def main() :
    #show the window :
    window.mainloop()

if __name__ == '__main__':
    main()