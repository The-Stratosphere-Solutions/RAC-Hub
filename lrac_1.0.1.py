import socket
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import time
import threading

messages_window = None
messages_window_messages_text = None
send_window = None
send_window_message_entry = None
send_window_name_entry = None
global_address = None
global_port = None

def get_messages(address, port):
    client = socket.socket()
    client.connect((address, port))
    client.send("1\n".encode())
    answer_length = int(client.recv(10))
    client.close()
    client = socket.socket()
    client.connect((address, port))
    client.send("2\n".encode())
    messages = client.recv(answer_length).decode()
    return messages

def send_message(address, port, message):
    client = socket.socket()
    client.connect((address, port))
    client.send(("0" + message + "\n").encode())
    client.close()

def send_message_global():
    global send_window_message_entry
    global send_window_name_entry
    global global_address
    global global_port

    name = send_window_name_entry.get()
    message = send_window_message_entry.get()

    if name == "":
        messagebox.showerror(title="lRAC", message="Name must be typed!")
        send_window_name_entry.focus_set()
        return
    elif message == "":
        messagebox.showerror(title="lRAC", message="Message must be typed!")
        send_window_message_entry.focus_set()
        return

    send_message(global_address, global_port, "<" + name + "> " + message)

    send_window_message_entry.delete(0, "end")
    send_window_message_entry.focus_set()

def check_address_port(address, port_string):
    try:
        client = socket.socket()
        client.connect((address, int(port_string)))
        client.close()
        return True
    except:
        return False

def update_messages(address, port, sleep_time):
    global messages_window_messages_text
    while True:
        messages = get_messages(address, port)
        messages_window_messages_text.config(state="normal")
        messages_window_messages_text.delete("1.0", "end")
        messages_window_messages_text.insert("1.0", messages)
        messages_window_messages_text.config(state="disabled")
        messages_window_messages_text.see("end")
        time.sleep(sleep_time)

def destroy_messages_window_and_send_window():
    messages_window.destroy()
    send_window.destroy()

def show_messages_window_and_send_window():
    global messages_window
    global messages_window_messages_text
    global send_window
    global send_window_message_entry
    global send_window_name_entry
    global global_address
    global global_port

    address_port = address_port_question_entry.get()

    address = ""
    port = ""
    write_address = True
    for i in address_port:
        if i != ':':
            if write_address:
                address += i
            else:
                port += i
        else:
            write_address = False

    if address_port_question_entry.get() == "" or check_address_port(address, port) == False:
        messagebox.showerror(title="lRAC", message="Enter correct address:port!")
        address_port_question_entry.focus_set()
        return

    port = int(port)

    global_address = address
    global_port = port

    address_port_question_window.destroy()
    messages_window = Tk()
    messages_window.title("lRAC") 
    messages_window.geometry("640x480")
    messages_window.wm_geometry("+%d+%d" % (0, 0))

    messages_window_messages_text = ScrolledText()
    messages_window_messages_text.config(state="disabled")
    messages_window_messages_text.place(x=0, y=0, relwidth=1.0, relheight=1.0)

    update_messages_thread = threading.Thread(target=update_messages, args=(address, port, 1,), daemon=True)
    update_messages_thread.start()

    send_window = Toplevel(messages_window)
    send_window.title("lRAC")
    send_window.resizable(width=False, height=False)
    send_window.wm_geometry("+%d+%d" % (0, 0))

    send_window_lrac_label = Label(send_window, text="lRAC")
    send_window_lrac_label.pack()

    send_window_name_label = Label(send_window, text="Name")
    send_window_name_label.pack()

    send_window_name_entry = Entry(send_window)
    send_window_name_entry.pack()

    send_window_message_label = Label(send_window, text="Message")
    send_window_message_label.pack()

    send_window_message_entry = Entry(send_window)
    send_window_message_entry.pack()

    send_window_send_button = Button(send_window, text="Send", command=send_message_global)
    send_window_send_button.pack(fill="x")

    send_window_name_entry.focus_set()

    messages_window.protocol("WM_DELETE_WINDOW", destroy_messages_window_and_send_window)
    send_window.protocol("WM_DELETE_WINDOW", destroy_messages_window_and_send_window)

    messages_window.mainloop()
    send_window.mainloop()

address_port_question_window = Tk()
address_port_question_window.title("lRAC") 
address_port_question_window.resizable(width=False, height=False)
address_port_question_window.wm_geometry("+%d+%d" % (0, 0))

address_port_question_lrac_label = Label(address_port_question_window, text="lRAC")
address_port_question_lrac_label.pack()

address_port_question_label = Label(address_port_question_window, text="Address:port of server")
address_port_question_label.pack()

address_port_question_entry = Entry(address_port_question_window)
address_port_question_entry.pack()

address_port_question_button = Button(address_port_question_window, text="Connect", command=show_messages_window_and_send_window)
address_port_question_button.pack(fill="x")

address_port_question_entry.focus_set()

address_port_question_window.mainloop()
