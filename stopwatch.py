from time import sleep as wait; import threading, time
hours = 0
minutes = 0
seconds = 0
def count(hours, minutes, seconds):
    while True:
        wait(1)
        seconds = (seconds + 1)
        wait(60)
        minutes = (minutes + 1)
        wait(3600)
        hours = (hours + 1)
def printcount(hours, minutes, seconds):
    while True:
        full = str(hours)+str(':'+ str(minutes)+':'+ str(seconds)+' have passed sice opening'); print(full)
        print(full)
if __name__ == "__main__":
    thread1=threading.Thread(target=count)
    thread2=threading.Thread(target=printcount)
    thread1.start()
    thread2.start()