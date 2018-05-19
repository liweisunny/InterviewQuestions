#__author:liwei
#date:2018/3/2


# 二分查找
def binary_search(lst, item):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low+high)/2
        guess = lst[mid]
        if guess > item:
            high = mid-1
        elif guess < item:
            low = mid+1
        else:
            return mid
    return None
my_list = [1, 3, 5, 7,  9]
print(binary_search(my_list, 3))



#合并两个有序列表

def _recursion_merge_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)


def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])

#
# 循环算法
# 思路：
#
# 定义一个新的空列表
#
# 比较两个列表的首个元素
#
# 小的就插入到新列表里
#
# 把已经插入新列表的元素从旧列表删除
#
# 直到两个旧列表有一个为空
#
# 再把旧列表加到新列表后面
#
def loop_merge_sort(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp


a = [1, 2, 3, 7]
b = [3, 4, 5]


def merge_sorted_list(a, b):
    c = []
    while a and b:
        if a[0] >= b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
    while a:
        c.append(a.pop(0))
    while b:
        c.append(b.pop(0))
    return c
print(merge_sorted_list(a,b))

