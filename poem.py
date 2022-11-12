from tkinter import *
import random
import indexer
import tkinter.font as tkFont


class Top:
    def __init__(self):
        self.poem = Tk()
        self.poem.geometry("500x700")
        self.poem.title("Poem Reader")
        self.poem.resizable(0, 0)
        self.color = ["#23238E",
                      "#32CD99",
                      "#545454",
                      "#D8BFD8",
                      "#6B4226",
                      "#2F2F4F",
                      "#6B238E",
                      "#CDB53B",
                      "#D19275",
                      "#70DBDB",
                      "#8F8FBD",
                      "#3299CC",
                      "#CDCDCD",
                      "#7093DB"]


        self.p = StringVar()

        self.sb = Scrollbar(self.poem, orient=VERTICAL)
        self.output = Text(self.poem,
                           font=('Times', 22, 'bold italic'),
                           height=23,
                           width=44, xscrollcommand=self.sb.set)
        self.sb.pack(side=RIGHT)

        self.output.place(x = 2, y = 1)
        self.sb.config(command=self.output.xview)



        self.reminder = Label(self.poem,
                              text="Please enter a number of the poem:",
                              height=2,
                              width=30,
                              bg = 'white',
                              font=('Times', 20, 'bold italic'))
        self.reminder.place(x = 2, y = 630)

        self.p = StringVar()
        self.entry = Entry(self.poem, textvariable=self.p, width=8, bg='#87CEFA')
        self.entry.place(x=300, y=642)
        #self.entry.bind('<Return>', self.search_poem)

        self.decide = Button(self.poem, text="Read", fg="black", width=10, height=2,
                             command=self.search_poem)
        #self.decide.bind('<Button-1>' ,self.search_poem)
        self.decide.place(x= 400, y=640)

    def search_poem(self):
        self.output.configure(state=NORMAL)
        self.output.delete(1.0, END)

        sonnets = indexer.PIndex("AllSonnets.txt")
        if self.entry.get().isdigit():
            num = int(self.entry.get())
            if not (num <= 108 and num >= 1):
                out = "Please enter a number between 1 and 108"
            else:
                self.output.configure(fg=random.choice(self.color))
                poem = sonnets.get_poem(num)
                self.p.set("")
                out = "\n\n\n"
                for line in poem:
                    out += line + "\n"
        else:
            out = "Please enter a number between 1 and 108"

        self.output.insert(END, out)
        self.p.set("")
        self.entry.delete(0, END)
        self.output.configure(state=DISABLED)


        
    def open(self):
        self.poem.mainloop()

    def close(self):
        self.poem.destroy()


if __name__ == '__main__':
    main = Top()
    main.open()
