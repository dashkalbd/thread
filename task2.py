import threading
import time


def process_order(order_id, total):
    print(f"Processing of order {order_id} ({total} UAH) has started")
    time.sleep(2)
    print(f"Processing of order {order_id} ({total} UAH) has finished")


orders = [
    {"id": 101, "total": 1500},
    {"id": 102, "total": 320},
    {"id": 103, "total": 7800},
    {"id": 104, "total": 450},
    {"id": 105, "total": 2100}
]

threads = []

for order in orders:
    thread = threading.Thread(target=process_order, args=(order["id"], order["total"]))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All orders processed. System finished work.")