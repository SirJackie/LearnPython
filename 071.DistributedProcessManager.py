import queue
import random
from multiprocessing.managers import BaseManager
import multiprocessing

TaskQueue = queue.Queue()
ResultQueue = queue.Queue()


def TaskQueueReturner():
    return TaskQueue


def ResultQueueReturner():
    return ResultQueue


class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    multiprocessing.freeze_support()

    QueueManager.register("get_task_queue", callable=TaskQueueReturner)
    QueueManager.register("get_result_queue", callable=ResultQueueReturner)

    manager = QueueManager(address=("127.0.0.1", 5000), authkey=b"abc")
    manager.start()

    Task = manager.get_task_queue()
    Result = manager.get_result_queue()

    for i in range(10):
        thingToPut = random.randint(1000, 10000)
        Task.put(thingToPut)
        print("%d time putting : %d" % (i, thingToPut))

    # for i in range(10):
    #     print("%d time getting : %d" % (i, Result.get(timeout=10)))
    #
    # manager.shutdown()
    print('Try get results...')
    for i in range(10):
        r = Result.get(timeout=10)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')
