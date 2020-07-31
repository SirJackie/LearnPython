from multiprocessing import Process
import os

def TaskToRun(name):
    print("Run Child Process \"%s\" (PID %s)" % (name, os.getpid()))

if __name__ == "__main__":  # Very Important, witch can prevent recursive
    print("I'm Parent Process (PID %s)" % os.getpid())

    # Create a Process
    p = Process(target=TaskToRun, args=("test",))

    # Run the Process
    print("Child Process will start")
    p.start()  # Start a Sub Process
    p.join()   # Wait until Sub Process Finished
    print("Child Process finished")

    # Result :
    # I'm Parent Process (PID 13304)
    # Child Process will start
    # Run Child Process "test"(PID 792)
    # Child Process finished
