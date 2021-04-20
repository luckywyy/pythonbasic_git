
# 信号量解决生产消费问题


# 假设生产者提供水资源，每次打一桶水到盆里，盆里共可装10桶水
# 消费者使用桶从盆里打水出来用，只有一个桶，只能倒水或打水
#
import time

empty_plate = 10
full_water = 0
mutex = 1

def P(n, m):
    n -= 1
    if n < 0:
        time.sleep()

def producer():
    pass


time.sleep()
