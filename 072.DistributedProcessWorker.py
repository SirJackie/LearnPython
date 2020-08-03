import queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

if __name__ == "__main__":
    QueueManager.register("get_task_queue")
    QueueManager.register("get_result_queue")

    manager = QueueManager(address=("127.0.0.1", 5000), authkey=b"abc")
    manager.connect()

    Task = manager.get_task_queue()
    Result = manager.get_result_queue()

    for i in range(10):
        work = Task.get(timeout=10)
        Result.put(work)

    print("Worker finished all the work")
