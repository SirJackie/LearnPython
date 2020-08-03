import queue
import random
import time
import os
from multiprocessing.managers import BaseManager
import multiprocessing

TaskQueue = queue.Queue()
ResultQueue = queue.Queue()

def TaskQueueReturner():
    global TaskQueue
    return TaskQueue

def ResultQueueReturner():
    global TaskQueue
    return ResultQueue

class QueueManager(BaseManager):
    pass

if __name__ == "__main__":
    # multiprocessing.freeze_support()

    QueueManager.register("GetTaskQueue", callable=TaskQueueReturner)
    QueueManager.register("GetResultQueue", callable=TaskQueueReturner)

    manager = QueueManager(address=("127.0.0.1", 5000), authkey=b"abc")
    manager.start()

    Task = manager.GetTaskQueue()
    Result = manager.GetResultQueue()

    for i in range(10):
        thingToPut = random.randint(1000, 10000)
        Task.put(thingToPut)
        print("%d time putting : %d" % (i, thingToPut))

    print("Finished putting the works, Press any key to get the result")
    os.system("pause")

    for i in range(10):
        print("%d time getting : %d" % (i, Result.get(timeout=10)))

    manager.shutdown()