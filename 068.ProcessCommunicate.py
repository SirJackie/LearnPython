from multiprocessing import Process, Queue
import os

def WriteTask(q):
    print("Process to write : %s" % os.getpid())
    for ch in "ABC":
        print("Write %s into Queue" % ch)
        q.put(ch)

def ReadTask(q):
    print("Process to read : %s" % os.getpid())
    while True:
        ch = q.get(True)
        print("Read %s from Queue" % ch)

if __name__ == "__main__":

    # Create a Queue
    Queue1 = Queue()

    # Create Writing and Reading Process
    ProcessToWrite = Process(target=WriteTask, args=(Queue1,))
    ProcessToRead = Process(target=ReadTask, args=(Queue1,))

    # Start two Processes
    ProcessToWrite.start()
    ProcessToRead.start()

    # Wait the Processes Finish
    ProcessToWrite.join()      # Wait until Writing Process is finished
    ProcessToRead.terminate()  # Force the Reading Process to stop

    # Result :
    # Process to write : 13436
    # Write A into Queue
    # Write B into Queue
    # Write C into Queue
    # Process to read : 9096
    # Read A from Queue
    # Read B from Queue
    # Read C from Queue
