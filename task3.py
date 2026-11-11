import threading

balance = 1000
lock = threading.Lock()


def deposit(amount):
    global balance
    with lock:
        balance = balance + amount
        print(f"Deposit +{amount}, balance: {balance}")


def withdraw(amount):
    global balance
    with lock:
        if amount > balance:
            print(f"Withdraw -{amount} refused, not enough money (balance: {balance})")
        else:
            balance = balance - amount
            print(f"Withdraw -{amount}, balance: {balance}")


operations = [
    (deposit, 500),
    (withdraw, 200),
    (deposit, 300),
    (withdraw, 400),
    (withdraw, 100),
    (withdraw, 5000)
]

threads = []

for operation, amount in operations:
    thread = threading.Thread(target=operation, args=(amount,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = 1000 + 500 - 200 + 300 - 400 - 100
print(f"Final balance: {balance}")
print(f"Expected balance: {expected}")

if balance == expected:
    print("Balance is correct")
else:
    print("Balance is wrong")