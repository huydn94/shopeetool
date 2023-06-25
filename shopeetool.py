import subprocess
import time
from tkinter import *
from tkinter import ttk
import psutil

#open new window
def open_new_window(url):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to Chrome executable

    # Command to open a new guest tab
    command = [chrome_path, "--new-window", "--guest", url]

    # Execute the command
    subprocess.Popen(command)
    #time.sleep(10)


#apply tham số
def apply_info():
    global numberofview, linklist, wait_time
    wait_time = int(e3.get())
    numberofview = int(e1.get())
    linklist_txt = str(e2.get())
    linklist = linklist_txt.split(",")
    #linklist_output = [link.split() for link in linklist_output]
    print (numberofview)
    print (linklist)

#open từng link
def open_main():
    print(numberofview)
    for i in range (numberofview):
        for link in linklist:
            open_new_window(link)
        time.sleep(wait_time)
        close_all_chrome_windows()
        time.sleep(30)

#close all chrome windows đã bật
def close_all_chrome_windows():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'chrome.exe':
            proc.kill()


if __name__ == "__main__":
    parent = Tk()
    parent.geometry('300x300')

    #Number of view
    view = Label(parent, text = "Số view").place(x = 30, y = 50)
    e1 = Entry(parent)
    e1.place(x = 80, y = 50)
    
    #list of link
    link = Label(parent, text = "Link List").place(x = 30, y = 90)
    e2 = Entry(parent)
    e2.place(x = 80, y = 90)

    #wait time
    wait_time = Label(parent, text = "wait time").place(x = 30, y = 130)
    e3 = Entry(parent)
    e3.place(x = 80, y = 130)
    
    apply_button = ttk.Button(parent, text='Apply', command=apply_info).grid(row = 4, column = 0)
    run_button = ttk.Button(parent, text='run', command=open_main).grid(row=4, column=1)
    #kill_button = ttk.Button(parent, text='close all', command=close_all_chrome_windows).grid(row=4, column=2)
    parent.mainloop()





# # open new window with files  
#     file_path = "links.txt"  # Path to the text file containing links

#     with open(file_path, "r") as file:
#         links = file.readlines()
#         links = [link.strip() for link in links]  # Remove newline characters and whitespace
#     print (links)
#     for link in links:
#         open_new_window(link)
