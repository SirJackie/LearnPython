from multiprocessing.managers import BaseManager

#
# Create QueueManager for Network Transferring
#

class QueueManager(BaseManager):
    pass

if __name__ == "__main__":
    # Get 2 Functions From Network Manager
    QueueManager.register("GetTaskQueue")
    QueueManager.register("GetResultQueue")

    # Connect the Network Manager to the Master Process
    manager = QueueManager(address=("127.0.0.1", 5000), authkey=b"abc")
    manager.connect()

    # Get 2 Queues
    Task = manager.GetTaskQueue()
    Result = manager.GetResultQueue()

    # Calculate the Task and send the Result
    for i in range(10):
        thingToCalc = Task.get(timeout=10)
        print("%d time calculating : %d * %d = %d"
              % (i, thingToCalc, thingToCalc, thingToCalc ** 2))
        Result.put(thingToCalc ** 2)

    print("Worker exit.")
