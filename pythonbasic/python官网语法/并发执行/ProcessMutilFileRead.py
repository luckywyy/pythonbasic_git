from multiprocessing import Process


def fr1():
    with open(file='./multiprocessingProcess.py', mode='r', encoding='utf-8') as f:

        print(f.read())

def fr2():
    with open(file='./multiprocessingProcess2.py', mode='r', encoding='utf-8') as f:

        print(f.read())


if __name__ == '__main__':

    p1 = Process(target=fr1)
    p2 = Process(target=fr2)

    p1.start()
    p2.start()

