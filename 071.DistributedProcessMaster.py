import queue
import random
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager

#
# Create Origin Queues and Return Functions
#

TaskQueue = queue.Queue()
ResultQueue = queue.Queue()

def GetTaskQueue():
    return TaskQueue

def GetResultQueue():
    return ResultQueue


#
# Create QueueManager for Network Transferring
#

class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    # Offer Freeze Support for Pickling the Queues
    freeze_support()

    # Register 2 Functions to Network Manager
    QueueManager.register("GetTaskQueue", callable=GetTaskQueue)
    QueueManager.register("GetResultQueue", callable=GetResultQueue)

    # Start the Network Manager
    manager = QueueManager(address=("127.0.0.1", 5000), authkey=b"abc")
    manager.start()

    # Get Queues after Network Manager's Processing
    Task = manager.GetTaskQueue()
    Result = manager.GetResultQueue()

    # Put Task to Network Manager
    for i in range(10):
        thingToPut = random.randint(1000, 10000)
        print("%d time putting : %d" % (i, thingToPut))
        Task.put(thingToPut)

    print('Try get results...')

    # Get Result from Network Manager
    for i in range(10):
        print("%d time getting : %d" % (i, Result.get(timeout=10)))

    manager.shutdown()
    print('Master exit.')
