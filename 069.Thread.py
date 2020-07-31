import threading


#
# Create a Thread
#

def Task():
    print("I'm the Thread \"%s\"" % threading.current_thread().name)

if __name__ == "__main__":
    print("I'm the Thread \"%s\"" % threading.current_thread().name)

    print("\"ChildThread\" will be start")
    t = threading.Thread(target=Task, name="ChildThread")
    t.start()
    t.join()
    print("\"ChildThread\" finished")


#
# MultiThreading can cause conflicts in variable writing
#

n = 0

def Changer(number):
    global n
    for i in range(number):
        n = n + 1
    for i in range(number):
        n = n - 1


t1 = threading.Thread(target=Changer, args=(100000,))
t2 = threading.Thread(target=Changer, args=(300000,))
t1.start()
t2.start()
t1.join()
t2.join()
print(n)  # Result : -64236


#
# Use threading.Lock() to Protect the Thread
#

n = 0
lock = threading.Lock()

def ChangerWithLock(number):
    lock.acquire()
    global n
    for i in range(number):
        n = n + 1
    for i in range(number):
        n = n - 1
    lock.release()


t1 = threading.Thread(target=ChangerWithLock, args=(100000,))
t2 = threading.Thread(target=ChangerWithLock, args=(300000,))
t1.start()
t2.start()
t1.join()
t2.join()
print(n)  # Result : 0

