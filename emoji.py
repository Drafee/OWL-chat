from tkinter import *


class Top:
    def __init__(self):
        self.window = Tk()
        self.window.title("Emoji")
        self.window.geometry("150x250")
        self.window.resizable(0, 0)
        self.add_command = None

        self.hint = Label(self.window, text="Select then add", width=14, height=2)
        self.list = Listbox(self.window, width=12)
        self.button = Button(self.window, text="Click to add")

        self.list.insert(END, "(︶︹︺)", "(ﾉ´д｀)", '(･_-｡ )', 'ˋ(′～‵”)ˊ', "(　TロT)σ ", "( T﹏T )", "(; ´_ゝ`)", "(,,Ծ‸Ծ,,)",
                         "(ಥ_ಥ)", "( ꈨຶ ˙̫̮ ꈨຶ )", "(;´༎ຶД༎ຶ`)", "(＞人＜)", "(°̥̥̥̥̥̥̥̥-°̥̥̥̥̥̥̥̥ )", "థ౪థ", "இдஇ",
                         "p(´⌒｀｡q)", "( ´•︵•` )", "(´-ι_-｀)",
                         "(┳◇┳)", "( >﹏<。)～", "( ̤இॕ⌓இॕ ̤)", "°(ಗдಗ。)°", "(´இ皿இ｀)", "(´；ω；｀) ｡：ﾟ", "(｡ﾉω＼｡)ﾟ･｡",
                         "(;*△*;)", "( ཀ͝ ∧ ཀ͝ )")

        self.button.bind("<Button-1>", lambda *e: self.add_command())

        self.hint.grid(row=0, column=1)
        self.list.grid(row=1, column=1)
        self.button.grid(row=2, column=1)

    def open(self):
        self.window.mainloop()

    def close(self):
        self.window.destroy()


if __name__ == '__main__':
    emo = Top()
    emo.open()
