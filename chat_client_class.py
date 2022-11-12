import time
import socket
import select
import sys
import json
import random
from chat_utils import *
import client_state_machine as csm
import main_interface
import client_manage
import tkinter.messagebox as mbox

import threading


class Client:
    def __init__(self, args):
        self.peer = ''
        self.console_input = []
        self.state = S_OFFLINE
        self.system_msg = ''
        self.local_msg = ''
        self.peer_msg = ''
        self.args = args

        self.window = main_interface.Top()
        self.window.send_btn_cb = self.on_send_btn_click
        self.window.quit_btn_cb = self.quit
        self.window.func_connect_command = self.on_connect_btn_click
        self.window.disc_btn_cb = self.on_disconnect_bt_click
        self.window.search_btn_cb = self.on_search_bt_click

        self.name = None

    def quit(self):
        self.sm.disconnect()
        mysend(self.sm.s, json.dumps({"action": "exchange", "from": "[" + self.sm.me + "]", "message": "bye"}))
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        self.window.close()
        client_manage.remove_client(self.name)

    def get_name(self):
        return self.name

    def init_chat(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        svr = SERVER if self.args.d == None else (self.args.d, CHAT_PORT)
        self.socket.connect(svr)
        self.sm = csm.ClientSM(self.socket)
        # reading_thread = threading.Thread(target=self.read_input)
        # reading_thread.daemon = True
        # reading_thread.start()

    def shutdown_chat(self):
        return

    def send(self, msg):
        mysend(self.socket, msg)

    def recv(self):
        return myrecv(self.socket)

    def get_msgs(self):
        read, write, error = select.select([self.socket], [], [], 0)
        my_msg = ''
        peer_msg = []
        # peer_code = M_UNDEF    for json data, peer_code is redundant
        if len(self.console_input) > 0:
            my_msg = self.console_input.pop(0)
        if self.socket in read:
            peer_msg = self.recv()
        return my_msg, peer_msg

    def output(self):
        if len(self.system_msg) > 0:
            self.window.receive.configure(state=main_interface.NORMAL)
            self.window.receive.insert(main_interface.END, self.system_msg + "\n")
            self.system_msg = ''
            self.window.receive.see(main_interface.END)
            self.window.receive.configure(state=main_interface.DISABLED)

    def on_send_btn_click(self):
        if self.window.textbox.get(1.0, main_interface.END).strip(" ") != "":
            self.window.receive.configure(state=main_interface.NORMAL)
            text_itself = self.window.textbox.get(1.0, main_interface.END)
            self.window.receive.insert(main_interface.END, "[" + self.name + "]" + text_itself.strip("\n") + "\n")
            self.console_input.append(text_itself.strip("\n"))
            self.window.textbox.delete(1.0, main_interface.END)
            self.window.receive.see(main_interface.END)
            self.window.receive.configure(state=main_interface.DISABLED)
            return "break"

    def on_connect_btn_click(self):
        if self.sm.state != S_CHATTING:
            i = self.window.client_list.curselection()[0]
            target = self.window.client_list.get(i)
            self.console_input.append("c" + target)

    def on_disconnect_bt_click(self):
        self.sm.disconnect()
        self.sm.state = S_LOGGEDIN
        self.sm.peer = ''
        self.state = S_LOGGEDIN
        mysend(self.sm.s, json.dumps({"action": "exchange", "from": "[" + self.sm.me + "]", "message": "bye"}))

    def on_search_bt_click(self):
        if self.state == S_CHATTING or self.state == S_CONNECTED or self.peer != "" or self.sm.peer != "":
            mbox.showerror("Error", "You can't search history when you are chatting.")
        else:
            self.window.receive.configure(state=main_interface.NORMAL)
            self.window.receive.delete(1.0, main_interface.END)
            term = self.window.search_entry.get()
            self.console_input.append("?" + term.strip(" "))
            self.window.search_term.set("")
            self.window.receive.see(main_interface.END)

    def login(self):
        # my_msg, peer_msg = self.get_msgs()
        # if len(my_msg) > 0:
        # self.name = my_msg
        msg = json.dumps({"action": "login", "name": self.name})
        self.window.greeting_label.configure(text=(random.choice(["Have a nice day, ", "Enjoy your day, ",
                                                                  "Today is your day to relax, ", "Have a good time, "]) + self.name))
        self.send(msg)
        response = json.loads(self.recv())
        if response["status"] == 'ok':
            self.state = S_LOGGEDIN
            self.sm.set_state(S_LOGGEDIN)
            self.sm.set_myname(self.name)
            self.print_instructions()
            return (True)
        elif response["status"] == 'duplicate':
            self.system_msg += 'Duplicate username, try again'
            return False
        # else:  # fix: dup is only one of the reasons
        # return (False)

    # def read_input(self):
    # while True:
    # text = sys.stdin.readline()[:-1]
    # self.console_input.append(text) # no need for lock, append is thread safe

    def print_instructions(self):
        self.system_msg += menu

    def get_name_list(self):
        current = "".join(sorted(list(self.window.client_list.get(0, self.window.client_list.size() + 1))))
        standard = "".join(sorted(client_manage.get_clients()))
        if current != standard:
            self.window.client_list.delete(0, main_interface.END)
            for item in client_manage.get_clients():
                self.window.client_list.insert(main_interface.END, item)

    def run_chat(self):
        self.init_chat()
        self.output()

        sub_proc_thread = threading.Thread(target=self.sub_proc)
        sub_proc_thread.daemon = True
        sub_proc_thread.start()

        self.window.open()



    def sub_proc(self):
        while self.login() != True:
            self.output()
        self.system_msg += 'Welcome to OWLs, ' + self.get_name() + '!\n'
        self.output()
        self.window.c_interface.title(self.name + " - OWLs")
        while self.sm.get_state() != S_OFFLINE:
            if self.sm.get_state() == S_CHATTING:
                self.window.textbox.configure(state=main_interface.NORMAL)
            else:
                self.window.textbox.configure(state=main_interface.DISABLED)
            self.proc()
            self.output()
            self.get_name_list()
            time.sleep(CHAT_WAIT)
        self.quit()

    # ==============================================================================
    # main processing loop
    # ==============================================================================
    def proc(self):
        my_msg, peer_msg = self.get_msgs()
        self.system_msg += self.sm.proc(my_msg, peer_msg)
