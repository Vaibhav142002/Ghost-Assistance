from tkinter import *

def open_win():
      root = Tk()

      root.geometry('630x700+450+30')
      root.title('Credits')
      root.resizable(FALSE,FALSE)
      # img=PhotoImage(file='ic_n.png')
      # root.iconphoto(False,img)
 
      data_s='''
                                          GHOST INC.

      Developers :-

                  Mr.Yash Hasabe
                  Mr.Harshad Powar
                  Mr.Vishal Madekar
                  Mr.Rohit Nikam
                  Mr.Vaibhav Ukande

      Under Guidence :- Prof. S. M. Rane (B.E.CSE)

                       THANK YOU FOR CHOOSING US
      '''



      fr = LabelFrame(
            root,text="Team Mates - ",
            font=('Despairs',15,'bold'),
            highlightthickness=3,
              bd=4
      )
      fr.pack(fill=BOTH,expand=YES)

      txt = Message(
            fr,
            bg='black',
            fg='white',
      )

      def go(counter=1):
            txt.config(text=data_s[:counter])
            if counter < len(data_s):
                  root.after(20, lambda: go(counter+1))

      txt.config(font=('teko',18,''),justify=LEFT,aspect=300)
      txt.pack(fill=BOTH,expand=YES)

      b = Button(fr,text='Credits',command=go,bg='black',fg='white') 
      b.config(font=('dispence',13))
      b.pack(fill=X,expand=NO)

      b = Button(fr,text='Back to ghost',command=root.destroy,bg='black',fg='red') 
      b.config(font=('dispence',13,'italic'))
      b.pack(fill=X,expand=NO)

      mainloop()

if __name__ == "__main__":
      open_win()
