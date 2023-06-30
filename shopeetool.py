import subprocess
import time
from tkinter import *
from tkinter import ttk
import psutil
import random
import tkinter as tk
from tkinter import messagebox
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
    global numberofview, linklist, wait_time, lenlinklist, number_of_tab
    number_of_tab = int(e4.get())
    wait_time = int(e3.get())
    numberofview = int(e1.get())
    linklist_txt = str(e2.get())
    linklist = linklist_txt.split(",")
    lenlinklist = len(linklist)
    #linklist_output = [link.split() for link in linklist_output]
    #print ("Đã nhận tham số")
    #print (linklist)

#open từng link
def open_main():
    j=0
    # subwindow = tk.Toplevel(parent)  # Create a new Toplevel window
    # subwindow.title("Progress")  # Set the title of the subwindow
    # subwindow.geometry("200x100")  # Set the size of the subwindow
    # # Create a label for the loading message
    

    for i in range (numberofview):
        new_link_list = linklist
        for x in range (number_of_tab):
            random_link = random.choice(new_link_list)
            new_link_list = [x for x in linklist if x != random_link]
            open_new_window(random_link)
        j=j+1

        progress_bar['value']=(j*100//numberofview)
        pVal = str(j*100//numberofview) + "%"
        
        if j < numberofview:
            progress_label = Label(parent, text=pVal)

        if j == numberofview:
            progress_label = Label(parent, text="DONE!")
        progress_label.place(x=250, y=210)            
        parent.update_idletasks()    

        #print("lan thu: ",j)
        time.sleep(wait_time)
        close_all_chrome_windows()
        time.sleep(random.randint(25,100))

#    progress_bar.stop()
#close all chrome windows đã bật
def close_all_chrome_windows():
    chrome_processes = [proc for proc in psutil.process_iter() if proc.name() == "chrome.exe"]
    
    for proc in chrome_processes:
        try:
            proc.kill()
        except psutil.NoSuchProcess:
            pass
    # for proc in psutil.process_iter(['pid', 'name']):
    #     if proc.info['name'] == 'chrome.exe':
    #         proc.kill()


if __name__ == "__main__":
    parent = Tk()
    parent.geometry('300x300')

    #Number of view
    view = Label(parent, text = "Số view").place(x = 30, y = 50)
    e1 = Entry(parent)
    e1.place(x = 100, y = 50)
    
    #list of link
    link = Label(parent, text = "Link List").place(x = 30, y = 90)
    e2 = Entry(parent)
    e2.place(x = 100, y = 90)

    #wait time
    wait_time = Label(parent, text = "wait time").place(x = 30, y = 130)
    e3 = Entry(parent)
    e3.place(x = 100, y = 130)
    
    number_of_tab = Label(parent, text = "tab/list").place(x = 30, y = 170)
    e4 = Entry(parent)
    e4.place(x = 100, y = 170)

    apply_button = ttk.Button(parent, text='Apply', command=apply_info).grid(row = 4, column = 0)
    run_button = ttk.Button(parent, text='run', command=open_main).grid(row=4, column=1)
    #kill_button = ttk.Button(parent, text='close all', command=close_all_chrome_windows).grid(row=4, column=2)
    loading_label = Label(parent, text="Progress")
    loading_label.place(x = 30, y = 210)

    # Create a progress bar
    progress_bar = ttk.Progressbar(parent, mode="determinate", length=125)
    progress_bar.place(x = 100, y = 210)

    parent.mainloop()





# # open new window with files  
#     file_path = "links.txt"  # Path to the text file containing links

#     with open(file_path, "r") as file:
#         links = file.readlines()
#         links = [link.strip() for link in links]  # Remove newline characters and whitespace
#     print (links)
#     for link in links:
#         open_new_window(link)
