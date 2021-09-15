
import time



def decorate(func):

    def warpper():
        startTime = time.time()

        func()

        endTime = time.time()

        print('endTime-startTime: ', endTime-startTime)

    return warpper


@decorate
def ok():
    time.sleep(1)
    print('ok')

ok()