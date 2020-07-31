from multiprocessing import Pool
import os, time, random

def SubTask(name):
    print("Start Running Task %s (PID %s)" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Finished Running Task %s (%.2f seconds)" % (name, end - start))

if __name__ == "__main__":
    p = Pool(3)

    for i in range(1, 6):
        p.apply_async(SubTask, args=(i,))
    p.close()  # Finished Adding Process
    p.join()   # Wait until Process Finished
    print("All Sub Processes Finished")

    # Result :
    # Start Running Task 1 (PID 18028)
    # Start Running Task 2 (PID 1232)
    # Start Running Task 3 (PID 6180)
    # Finished Running Task 1 (0.31 seconds)
    # Start Running Task 4 (PID 18028)
    # Finished Running Task 4 (0.77 seconds)
    # Start Running Task 5 (PID 18028)
    # Finished Running Task 5 (0.27 seconds)
    # Finished Running Task 2 (2.20 seconds)
    # Finished Running Task 3 (2.39 seconds)
    # All Sub Processes Finished
