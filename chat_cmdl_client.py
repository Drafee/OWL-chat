from chat_client_class import *
import Log_in
import tkinter.messagebox as mbox




def main(out_name):
    import argparse
    parser = argparse.ArgumentParser(description='chat client argument')
    parser.add_argument('-d', type=str, default=None, help='server IP addr')
    args = parser.parse_args()
    client = Client(args)
    client.name = out_name
    client.run_chat()



