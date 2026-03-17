"""Paralalizm Program in python"""
import multiprocessing
import time

def taking_order():
    """Simple func that taking order"""
    for i in range(4):
        print(f"Taking order: {i}")
        time.sleep(1)

def making_dish():
    """Simple func that making dish"""
    for i in range(4):
        print(f"Serving Order: {i}")
        time.sleep(2)

if __name__ == "__main__":
    processes = []

    t = multiprocessing.Process(target=taking_order)
    o = multiprocessing.Process(target=making_dish)

    processes.append(t)
    processes.append(o)

    for p in processes:
        p.start()

    for p in processes:
        p.join()
