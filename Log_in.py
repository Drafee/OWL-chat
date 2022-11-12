from tkinter import *
import tkinter.messagebox as mbox
import tkinter.font as font
import Reg
import chat_cmdl_client
import client_manage


class Top:
    def __init__(self):
        self.theme = "#FFFFFF"
        self.topic = "#FFFFFF"

        self.keep = False

        self.log_command = None

        self.log_window = Tk()
        self.log_window.title("OWLs - Log in")
        self.log_window.resizable(0, 0)
        self.log_window.geometry("500x380")
        self.log_window.configure(background=self.theme)

        self.titleft = font.Font(family='Marker Felt Thin', size=40, weight=font.BOLD)
        self.emptyfont0 = font.Font(size=25)
        self.emptyfont1 = font.Font(size=20)
        self.IPfont = font.Font(family="Gill Sans", size=20, weight=font.BOLD)

        self.empty0 = Label(self.log_window, text="          ", font=self.emptyfont1, bg=self.theme)
        self.empty1 = Label(self.log_window, text="          ", font=self.emptyfont0, bg=self.theme)
        self.empty2 = Label(self.log_window, text="          ", font=self.emptyfont0, bg=self.theme)
        self.empty3 = Label(self.log_window, text="          ", height=1, bg=self.theme)

        self.Title = Label(self.log_window, text="OWLs", font=self.titleft, fg="purple", bg=self.theme)
        self.frame = Frame(self.log_window, bg=self.theme)

        self.ID = Label(self.frame, text="ID:", height=2, font=self.IPfont, bg=self.theme)
        self.Password = Label(self.frame, text="Password:", height=2, font=self.IPfont, bg=self.theme)
        self.id = StringVar()
        self.ID_entry = Entry(self.frame, textvariable=self.id, bg=self.topic)

        self.p = StringVar()
        self.Password_entry = Entry(self.frame, textvariable=self.p, bg=self.topic)
        self.Password_entry["show"] = "*"
        self.Password_entry.bind("<Return>", self.validinfo)

        self.Login = Button(self.log_window, text="Log in", fg="red", width=10, height=2, command=self.validinfo, bg=self.topic)
        # self.Login.bind("<Button-1>", lambda *e: self.log_command())
        self.Login.bind("<Button-1>", self.validinfo)
        self.Register = Button(self.log_window, text="Resgister", fg="blue", width=10, height=2, command=self.reg, bg=self.topic)

        self.empty0.pack(side=TOP)
        self.Title.pack(side=TOP)
        self.empty1.pack(side=TOP)
        self.ID.grid(row=5, column=0, sticky=E)
        self.Password.grid(row=6, column=0, sticky=E)
        self.ID_entry.grid(row=5, column=1)
        self.Password_entry.grid(row=6, column=1)

        self.frame.pack(side=TOP)
        self.empty2.pack()
        self.Login.pack()
        self.empty3.pack()
        self.Register.pack()

    def reg(self):
        reg_window = Reg.Top()
        reg_window.open()

    def open(self):
        self.log_window.mainloop()

    def close(self):
        self.log_window.destroy()

    def validinfo(self, event):
        f = open("accountinfo.txt", "r")
        c = f.readlines()
        ac_dict = {}
        for item in c:
            if item != "" and item != "\n":
                item_list = item.strip("\n").split(",")
                ac_dict[str(item_list[0])] = [str(item_list[1]), str(item_list[2])]
        f.close()

        id_text = self.id.get()
        p_text = self.p.get()
        if id_text not in ac_dict.keys():
            mbox.showerror("Error", "No Such ID")
            return False
        else:
            if ac_dict[id_text][0] == p_text:
                if ac_dict[id_text][1] in client_manage.get_clients():
                    mbox.showerror("Error", "Duplicate Log-in Request")
                else:
                    mbox.showinfo("welcome", "Welcome, " + ac_dict[id_text][1])
                    self.close()
                    out_name = ac_dict[id_text][1]
                    client_manage.add_client(out_name)
                    chat_cmdl_client.main(out_name)

                return True
            else:
                mbox.showerror("Error", "Wrong Password")
                self.p.set("")
                return False

    def open(self):
        self.log_window.mainloop()

    def close(self):
        self.log_window.destroy()


if __name__ == '__main__':
    main = Top()
    main.open()
