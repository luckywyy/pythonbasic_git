
# 反转链表这个题做法还是挺多的，一般有迭代 递归

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 1->2->3->4->5->NULL 反转以root为根节点的链表
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)

# while root:
#     print(root.val)
#     root = root.next

stack = []
head = root
while head:
    stack.append(head.val)
    head = head.next

head = root
while stack:
    root.val = stack.pop()
    root = root.next


while head:
    print(head.val)
    head = head.next
