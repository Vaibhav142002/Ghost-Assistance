from tkinter import *

def new_GUI():
      
    root = Tk()
    root.geometry('630x680+450+40')
    root.title('Commands')
    root.resizable(FALSE,FALSE)
    root.attributes('-alpha',1)
    # root.wm_attributes('-transparentcolor','red')

    cmds="""                 

    1)Search Google keyword
        example: search google python or search google AI assistant
                
    2)Search Wikipedia keyword
        example: search Wikipedia python or search Wikipedia AI

    3)Open any app

    4)Speech to text
            ask to type and speak what do you want!

    5)Google maps keyword
        example: google map kolhapur

    6)Open Code-> To open Microsoft Visual Code

    7)Open C or D Drive -> To Open C or D Drive 

    8)Play music-> To play Music

    9)Play video-> To play Video

    10)Search Youtube keyword
        example: search youtube python or search youtube AI assistant

    11)Open google-> To open google on browser

    12)Open Youtube-> To open youtube on browser

    13)Go Offline/Nothing/Bye-> To close Application

    14)Shutdown-> To shutdown the Operating System 

    15)Opne a file

    """

    # img1=PhotoImage(file="cms.png",master=root)
    # l1 = Label(root,image=img1)
    # l1.place(x=3,y=3)
    hpframe=LabelFrame(
        root,
        bd=3,
        text="Commands:- ",
        font=('Despairs',13,'bold'),
        highlightthickness=3)
    # hpframe.creat_image(0,0,image=img1,anchor="nw")
    hpframe.pack(fill=BOTH)

    hpmsg=Message(
        hpframe,
        text=cmds,
        background='#111111',
        fg='white'
        )

    hpmsg.config(font=('larabiefont rg',10,''),justify="left")
    hpmsg.pack(fill=BOTH)


    exitbtn = Button(
        root, 
        text='BACK TO GHOST!', 
        font=('Dispence', 13, 'italic'), 
        bg='black', 
        fg='red',
        borderwidth=5,
        command=root.destroy).pack(fill='x', expand='yes')
    
    # root.attributes('-transarentcolor', 'red')
    root.mainloop()

if __name__ == "__main__":
      new_GUI()
