# This file serves as an appendix to the "log_in"

from tkinter import *
import tkinter.messagebox as mbox
import tkinter.font as font
from tkinter import Tk
import random


class Top:
    def __init__(self):
        self.reg_window = Tk()
        self.reg_window.resizable(0, 0)
        self.reg_window.title("Register")

        self.nick = Label(self.reg_window, text="Nickname:")

        self.nick_v = StringVar()
        self.nick_entry = Entry(self.reg_window, textvariable=self.nick_v)

        self.p1 = Label(self.reg_window, text="Password:")

        self.p1_v = StringVar()
        self.p1_entry = Entry(self.reg_window, textvariable=self.p1_v)
        self.p1_entry["show"] = "*"

        self.p2 = Label(self.reg_window, text="Comfirmed Password:")

        self.p2_v = StringVar()
        self.p2_entry = Entry(self.reg_window, textvariable=self.p2_v)
        self.p2_entry["show"] = "*"

        self.cancel = Button(self.reg_window, text="Cancel", command=self.close)
        self.register = Button(self.reg_window, text="Register", command=self.register_func)

        self.nick.grid(row=0, column=0, sticky=E)
        self.nick_entry.grid(row=0, column=1)
        self.p1.grid(row=1, column=0, sticky=E)
        self.p1_entry.grid(row=1, column=1)
        self.p2.grid(row=2, column=0, sticky=E)
        self.p2_entry.grid(row=2, column=1)
        self.cancel.grid(row=3, column=0)
        self.register.grid(row=3, column=1)

    def close(self):
        self.reg_window.destroy()

    def open(self):
        self.reg_window.mainloop()

    def register_func(self):
        nickname = self.nick_entry.get()
        password = self.p1_entry.get()

        if nickname == "" or password == "":
            mbox.showinfo("Error", "Please complete the form!")
            return False

        if self.p1_entry.get() != self.p2_entry.get():
            mbox.showinfo("Error", "The passwords do not match:")
            return False

        f = open("accountinfo.txt", "r")
        pure_content = f.read()
        f.close()
        f = open("accountinfo.txt", "r")
        c = f.readlines()
        ac_dict = {}
        for item in c:
            if item != "" and item != "\n":
                item_list = item.strip("\n").split(",")
                ac_dict[str(item_list[0])] = [str(item_list[1]), str(item_list[2])]
        f.close()

        for key in ac_dict.keys():
            if nickname == str(ac_dict[key][1]):
                mbox.showerror("Error", "Your nickname is registered in advance, Please use a new one")
                return False

        while True:
            account_num = random.randint(10000, 1000000000)
            if str(account_num) not in ac_dict.keys():
                ac_dict[str(account_num)] = [password, nickname]
                pure_content += str(account_num) + "," + password + "," + nickname + "\n"
                f = open("accountinfo.txt", "w")
                f.write(pure_content)
                f.close()
                mbox.showinfo("Success", "Thank you for registration!\nYour ID is " + str(account_num))
                self.close()
                break
        return True


if __name__ == "__main__":
    main_window = Top()
    main_window.open()
