import random
from tkinter import *
import tkinter.messagebox as mbox
import tkinter.font as font
import Log_in
import time
import poem
import interface_24
import emoji



class Top:
    def __init__(self):
        self.send_btn_cb = None
        self.quit_btn_cb = None
        self.func_connect_command = None
        self.disc_btn_cb = None
        self.search_btn_cb = None





        self.theme = ["#C0D9D9", "#9BB0B5", "#E8E3CE"][0]

        self.c_interface = Tk()
        self.c_interface.geometry("700x600")
        self.c_interface.configure(background=self.theme)
        self.c_interface.title("OWLs")
        self.c_interface.resizable(0, 0)

        # Set font
        self.button_text_font = font.Font(family='Marker Felt Thin', size=15)
        self.titleft = font.Font(family='Marker Felt Thin', size=38, weight=font.BOLD)

        # Display the time synchronously
        self.time_var = StringVar()
        self.time = Label(self.c_interface, textvariable=self.time_var, font=("Arial", 20), fg="Black", width=16,
                          height=2, bg=self.theme)

        # Set button

        self.title = Label(self.c_interface, text="OWLs", font=self.titleft, fg="#6666FF", width=7, height=1,
                           bg=self.theme)
        self.poem = Button(self.c_interface, text="Poem", font=self.button_text_font, fg="black", width=14, height=2,
                           command=self.poem_window, bg="#70DB93")
        self.game = Button(self.c_interface, font=self.button_text_font, text="Game: 24 Points", fg="black",
                           width=14, height=2, command=self.window_24, bg="#70DB93")
        self.connect = Label(self.c_interface, font=self.button_text_font,
                             text="Start Chatting!\n[Select one and Connect]", fg="black",
                             width=18, height=3, bg=self.theme)
        self.connect_command = Button(self.c_interface, text="Connect", font=self.button_text_font, fg="black",
                                      width=10, height=1, activebackground="#70DB93")
        self.connect_command.bind("<Button-1>", lambda *e: self.func_connect_command())
        self.blank = Label(self.c_interface, font=self.button_text_font, text="\n\n", width=16, height=2, bg=self.theme)

        self.quit = Button(self.c_interface, text="Quit", font=self.button_text_font, fg="black", width=14, height=2,
                           bg="#70DB93")

        self.quit.bind("<Button-1>", lambda *e: self.quit_btn_cb())
        self.client_list = Listbox(self.c_interface, width=12, bg="#FFFFFF")

        self.empty1 = Label(self.c_interface, font=self.button_text_font, text="", width=16, height=1, bg=self.theme)
        self.empty2 = Label(self.c_interface, font=self.button_text_font, text="", width=16, height=1, bg=self.theme)
        self.empty3 = Label(self.c_interface, font=self.button_text_font, text="", width=16, height=1, bg=self.theme)

        # Place the buttons
        self.time.grid(row=1, column=1)
        self.title.grid(row=2, column=1)
        self.connect.grid(row=3, column=1)
        self.client_list.grid(row=4, column=1)
        self.empty1.grid(row=5, column=1)
        self.connect_command.grid(row=6, column=1)
        self.blank.grid(row=7, column=1)
        self.poem.grid(row=8, column=1)
        self.empty2.grid(row=9, column=1)
        self.game.grid(row=10, column=1)
        self.empty3.grid(row=11, column=1)
        self.quit.grid(row=12, column=1)

        self.chat_frame = Frame(self.c_interface, bg=self.theme, highlightbackground="#70DBDB", highlightcolor="#70DBDB",
                                height=590, width=490)
        self.chat_frame.place(x=200, y=5)

        self.textbox = Text(self.chat_frame,
                            width=46,
                            height=7,
                            font=('Athelas', 18),
                            bg='#FFFFFF',
                            highlightcolor='black',
                            bd=1)

        self.textbox.place(x=10, y=370)
        self.textbox.bind('<Return>', lambda *e: self.send_btn_cb())

        # send button
        self.sendb = Button(self.chat_frame, text="Send", font=self.button_text_font, fg="black", width=9, height=2)
        self.sendb.bind("<Button-1>", lambda *e: self.send_btn_cb())

        self.disc_bt = Button(self.chat_frame, text="Disconnect", font=self.button_text_font, fg="black", width=9,
                              height=2)
        self.disc_bt.bind("<Button-1>", lambda *e: self.disc_btn_cb())

        self.emoji_button = Button(self.chat_frame, text="emoji", font=self.button_text_font, fg="black", width=9,
                                   height=2, command=self.emoji_call)


        self.search_bt = Button(self.chat_frame, text="Search", font=self.button_text_font, fg="black", width=6,
                                height=1)
        self.search_bt.bind("<Button-1>", lambda *e: self.search_btn_cb())

        self.search_term = StringVar()
        self.search_entry = Entry(self.chat_frame, textvariable=self.search_term, width=10)

        self.greeting_label = Label(self.chat_frame, text="", bg=self.theme, width=24, height=2,
                                    font=("Marker Felt Thin", 20))
        #Bradley Hand

        self.sendb.place(x=375, y=535)
        self.disc_bt.place(x=10, y=535)
        self.search_bt.place(x=410, y=15)
        self.search_entry.place(x=300, y=12)
        self.search_entry.bind("<Return>", lambda *e: self.search_btn_cb())
        self.emoji_button.place(x=270, y=535)
        self.greeting_label.place(x=0, y=0)

        self.receive = Text(self.chat_frame,
                            width=46,
                            height=15,
                            font=('Athelas', 18),
                            bg='#FFFFFF')

        self.receive.place(x=10, y=45)

    # Basic methods
    def open(self):
        self.showtime()
        self.c_interface.mainloop()

    def close(self):
        self.c_interface.destroy()

    def showtime(self):
        self.time_var.set(time.strftime('%H:%M:%S'))
        self.time.after(1000, self.showtime)

    def poem_window(self):
        main = poem.Top()
        main.open()

    def window_24(self):
        tf = interface_24.Top()
        tf.open()





    def emoji_call(self):
        emoji_window = emoji.Top()

        def on_click_add():
            i = emoji_window.list.curselection()[0]
            insert_emoji = emoji_window.list.get(i)
            self.textbox.insert(END, insert_emoji)
            emoji_window.close()

        emoji_window.add_command = on_click_add
        emoji_window.open()




if __name__ == '__main__':
    main = Top()
    main.open()
