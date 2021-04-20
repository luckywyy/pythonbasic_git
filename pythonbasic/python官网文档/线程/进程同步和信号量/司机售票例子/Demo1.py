
import threading


def driver():
    while True:
        print("启动\n")
        print("出发\n")
        print("停车\n")

def conductor():
    while True:
        print("关门\n")
        print("售票\n")
        print("开门\n")


driverThread = threading.Thread(target=driver)
conductorThread = threading.Thread(target=conductor)


driverThread.start()
conductorThread.start()
