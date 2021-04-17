

import time
import datetime

# 获取当前时间，返回当前时间字符串
def getNowDateTime():
    now_datatime = datetime.datetime.now()
    now_time_str = "现在是北京时间{}年{}月{}日{}时{}分{}秒".format(
        now_datatime.year, now_datatime.month, now_datatime.day,
        now_datatime.hour, now_datatime.minute, now_datatime.second
    )
    return now_time_str

