import threading, time

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        f.read()

# Single thread
start = time.time()
read("file.txt")
read("file1.txt")
print("Single thread:", time.time() - start)

# Two threads
start = time.time()
t1 = threading.Thread(target=read, args=("file.txt",))
t2 = threading.Thread(target=read, args=("file1.txt",))
t1.start(); t2.start()
t1.join(); t2.join()
print("Two threads:", time.time() - start)

