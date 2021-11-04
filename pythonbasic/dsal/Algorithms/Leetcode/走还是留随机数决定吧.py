



# import random
#
# for i in range(1, 11):
#     quit = random.randint(1, 11)
#
#     if i == 7:
#         if quit % 2 == 0:
#             print("留下来")
#         else:
#             print("离开吧")

import hashlib

for i in range(1, 11):

    if i == 7:
        s = hashlib.sha256()
        s.update("wy".encode("utf8"))
        quit = s.hexdigest()

        if ord(quit[7]) % 2 == 0:
            print("留下来")
        else:
            print("离开吧")

