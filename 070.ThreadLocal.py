import threading

ThreadLocal = threading.local()

def PrintingService():
    print("Your name is %s. (in %s)" %
          (ThreadLocal.name, threading.current_thread().name))

def ThreadModel(name):
    ThreadLocal.name = name
    PrintingService()

if __name__ == "__main__":
    t1 = threading.Thread(target=ThreadModel, args=("Alice",), name="Thread-1")
    t2 = threading.Thread(target=ThreadModel, args=("Bob",), name="Thread-2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # Result :
    # Your name is Alice. (in Thread-1)
    # Your name is Bob. (in Thread-2)
