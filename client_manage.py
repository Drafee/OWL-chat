# This python file is to manage the logged in clients
def get_clients():
    f = open("active_list.txt", "r")
    ACTIVE_CLIENT = f.read().strip("\n").strip(",").split(",")
    return ACTIVE_CLIENT

def up_date_clients(new_list):
    f = open("active_list.txt", "w")
    new = ""
    for item in new_list:
        new += item + ","
    f.write(new)
    f.close()




def add_client(new_name):
    ACTIVE_CLIENT = get_clients()
    if new_name not in ACTIVE_CLIENT:
        ACTIVE_CLIENT.append(new_name)
        up_date_clients(ACTIVE_CLIENT)

def remove_client(name):
    ACTIVE_CLIENT = get_clients()
    if name in ACTIVE_CLIENT:
        ACTIVE_CLIENT.remove(name)
        up_date_clients(ACTIVE_CLIENT)
