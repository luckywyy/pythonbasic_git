
import threading
import random

BUFFER_SIZE = 10
buffer = [[]] * 10
counter = 0
in_ = 0
out_ = 0
item = 0

def productor():
    global in_, buffer, counter, item
    while 1:
        while counter == BUFFER_SIZE:
            print("productor wait...\n")
        item = random.randint(1, 1000)
        buffer[in_].append(item)
        print("product {}\n".format(item))
        print("product counter {}\n".format(counter))
        in_ = (in_+1) % BUFFER_SIZE

        counter += 1

def customer():
    global out_, buffer, counter, item
    while 1:
        while counter == 0:
            print("customer wait...\n")

        item = buffer[out_].pop()
        print("custom {}\n".format(item))
        print("custom counter {}\n".format(counter))
        out_ = (out_+1) % BUFFER_SIZE

        counter -= 1


productorThread = threading.Thread(target=productor)
customerThread = threading.Thread(target=customer)

productorThread.start()
customerThread.start()


