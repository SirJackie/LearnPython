import queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

if __name__ == "__main__":
    QueueManager.register("GetTaskQueue")
    QueueManager.register("GetResultQueue")

    manager = QueueManager(address=("127.0.0.1", 5000), authkey=b"abc")
    manager.start()

    Task = manager.GetTaskQueue()
    Result = manager.GetResultQueue()

    while True:
        try:
            work = Task.get(timeout=10)
            Result.put(work)
        except queue.Empty:
            print("Worker finished all the works")
            break

    manager.shutdown()
