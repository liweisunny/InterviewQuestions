#__author:liwei
#date:2018/5/11

# 单链表
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

# 构造链表
head = None
for count in range(1, 6):
    head = Node(count, head)

# # 遍历链表
# probe = head
# while probe:
#     print(probe)
#     probe = probe.next


# # 将数组原序转换成列表
# arry = [3, 5, 2, 6, 1, 7, 4]
# node = None
# for i in arry[::-1]:
#     node = Node(i, node)
#
# while node:
#     print(node)
#     node = node.next


# 搜索链表某一项
# target_item = 4
# probe = head
# while probe and target_item != probe.data:
#     probe = probe.next
#
# if probe:
#     print('exist')
# else:
#     print('not exist')


# 替换链表某一项
# target_item = 5
# new_item = 8
# probe = head
# while probe and target_item != probe.data:
#     probe = probe.next
# if probe:
#     probe.data = new_item
# else:
#     print('not exist!!')
#
# # 遍历
# while probe:
#     print(probe)
#     probe = probe.next


# 替换第i项

i = 3
probe = head
while i > 1 and probe:
    probe = probe.next
    i -= 1
probe.data = 8

probe = head
# 遍历
while probe:
    print(probe)
    probe = probe.next
