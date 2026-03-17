"""Consurrency Program in python"""
import threading
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

# Using threading
threads = []
t = threading.Thread(target=taking_order)
o = threading.Thread(target=making_dish)
threads.append(t)
threads.append(o)

for t in threads:
    t.start()

for t in threads:
    t.join()
