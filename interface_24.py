from tkinter import *
import tkinter.font as tkFont
import point24
import random


class Top():
    def __init__(self):
        self.p24 = Tk()
        self.p24.geometry("400x300")
        self.p24.title('24 point')


        f = open('intro.txt','r')
        intro=f.read().strip()
        f.close()
        
        self.intro = Text(self.p24,
                          height=10,
                          width=36,
                          font=('symbol', 20))
        self.intro.insert('1.2', intro)
        self.intro.configure(state=DISABLED)
        
        self.intro.place(x = 10, y = 8)


        self.show = Text(self.p24,
                         height=1,
                         width=10,
                         bg = 'pink',
                         font=('symbol', 20))

        self.show.configure(state=DISABLED)
        
        self.show.place(x = 136, y = 175)

        self.solution = Text(self.p24,
                         height=1,
                         width=20,
                         bg = 'pink',
                         font=('symbol', 20))

        self.solution.configure(state=DISABLED)
        
        self.solution.place(x = 100, y = 265)


        self.generate = Button(self.p24, text="Generate", fg="black", width=10, height=2,
                               command=self.get_numbers,
                               font=('symbol', 16))
        self.generate.place(x= 145, y=125)


        self.solve = Button(self.p24, text="Solutions", fg="black", width=10, height=2,
                            command=self.get_s,
                            font=('symbol', 16))
        self.solve.place(x= 145, y=215)




    def random_4(self):
        numbers = []
        for i in range(4):
            numbers.append(random.randint(1,10))
        return numbers
            

    def get_numbers(self):
        global numbers
        numbers = self.random_4()
        while point24.dian(numbers)=='':
            numbers = self.random_4()

        self.show.configure(state=NORMAL)
        self.show.delete(1.0, END)
        show_numbers = ''
        for item in numbers:
            show_numbers+=str(item)+','
        self.show.insert('1.0', '  '+ show_numbers[:-1])

        self.show.configure(state=DISABLED)

        self.solution.configure(state=NORMAL)
        self.solution.delete(1.0, END)
        self.solution.configure(state=DISABLED)
        
            
    
    def get_s(self):

        try:
            self.solution.configure(state=NORMAL)
            solution = point24.dian(numbers)
            self.solution.insert('1.0', '  '+solution)
            self.solution.configure(state=DISABLED)

            self.solution.configure(state=DISABLED)
        except NameError:
            self.solution.configure(state=NORMAL)
            self.solution.insert('1.0', 'Click the Generate')
            self.solution.configure(state=DISABLED)
            
            
        



    def open(self):
        self.p24.mainloop()

    def close(self):
        self.p24.destroy()





if __name__ == '__main__':
    main = Top()
    main.open()
