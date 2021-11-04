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



# 假设链表为 1 2 3 1→2→3→∅，我们想要把它改成 1 2 3∅←1←2←3。
#
# 在遍历链表时，将当前节点的 \textit{next}next 指针改为指向前一个节点。由于节点没有引用其前一个节点，因此必须事先存储其前一个节点。在更改引用之前，还需要存储后一个节点。最后返回新的头引用。


# 头节点没有前一个节点 设为None
pre = None
# 设当前节点为cur
cur = root
# 设下一个节点为nex
nex = root

# 当当前节点不为空
while cur:
    nex = cur.next
    cur.next = pre
    pre = cur
    cur = nex

while pre:
    print(pre.val)
    pre = pre.next
# print(pre)

while cur:
    print(cur.val)
    cur = cur.next
# print(cur)

while nex:
    print(nex.val)
    nex = nex.next