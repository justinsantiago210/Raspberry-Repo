# Write your code here :-)
# imports as usual
import psutil #Util to get System Diag and Web Statistics
from time import sleep
from time import time
import colorama
from colorama import Fore, Style #import color to make code results change color
from tkinter import * #import Tkinter for GUI App

#Global Variables
path = '/'


def cpu_cores():
    cpu_cores = psutil.cpu_count()
    return cpu_cores

#interval 0 gets CPU that same instance, change to 1 so it can  tell u load after initial calling
def cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1,percpu=False)
    return cpu_usage

def gigabytes_avail():
    bytes_avail = psutil.disk_usage(path).free
    gigabytes_avail = bytes_avail / 1024 / 1024 /1024
    gigabytes_avail = int(gigabytes_avail)
    return gigabytes_avail

#Memory function to return RAM Values
def memory():
    #'memory.x' returns the stat, use virtual_memory to use function otherwise use '.' in terminal
    memory = psutil.virtual_memory()
    # Divide from Bytes ->KB -> MB
    available = round(memory.available/1024.0/1024.0,1)
    total = round(memory.total/1024.0/1024.0,1)
    return str(available) + "MB free / " + str(total) + "MB total (" + str(memory.percent) + "%)"


#Tkinter Variables
diagwindow = Tk()
btn = Button(diagwindow, text = "This is a button widget", fg = 'blue')
lbl = Label(diagwindow, text = "Diskspace Available:", fg = 'black')
btn.place(x = 80, y = 100)
lbl.place(x = 80, y = 50)


#CPU CounterVariables for whileLoop
cpu_temp_list = [0, 0, 0, 0, 0]
iterations_count = 0
time_b4_warning = 5 #5 seconds
cooldown_time = 10 # in seconds
cooldown_end = None
too_hot_temp = 15

def cpu_cores():
    cpu_cores = psutil.cpu_count()
    return cpu_cores


print("Diskspace Available:", gigabytes_avail(),"/32GB")
print("Number of CPU Cores:", cpu_cores())
print("Systemwide CPU Usage as of now:",cpu_usage(),"/100%" )
print("RAM Usage:", memory())

#Build Tkinter Window
diagwindow.title("RPi System Diag")
diagwindow.geometry("300x200+10+20")
diagwindow.mainloop()


#print CPULoad per 1second
# cpu_usage runs indefinitly | cooldown_end always None unlesswarning happens, then it goes up until time() > cooldown_end then it resets to None
#while True:
#    cpu_usage = psutil.cpu_percent(interval=1,percpu=False)
#    print("CPU:",cpu_usage,"%")
#    if cooldown_end:
#        if time() > cooldown_end:
#            cooldown_end = None
#    else:
#        #cpu_usage = psutil.cpu_percent(interval=1,percpu=False)
#        #print("CPU:",cpu_usage,"%")
#        cpu_temp_list.append(cpu_usage)
#        cpu_temp_list = cpu_temp_list[-time_b4_warning::]
#        if all([x > too_hot_temp for x in cpu_temp_list]):
#            print("last 5 iterations have been over15%")
#            cooldown_end = time()+cooldown_time
#    sleep(1)