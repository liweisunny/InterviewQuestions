#__author:liwei
#date:2018/5/19




def bubble_sort(lst):

    i = 0
    while i < len(lst):

        swapped = False
        j = 0  # 每一轮的比较都是从列表的第一项开始

        while j < len(lst)-1:

            if lst[j] > lst[j+1]:   # 前一项大于后一项交换元素（降序排列）

                lst[j], lst[j+1] = lst[j+1], lst[j]  # swap element
                swapped = True

            j += 1

        if not swapped:
            return

        i += 1


def select_sort(lst):
    i = 0
    while i < len(lst)-1:

        j = i+1
        min_index = i

        while j < len(lst):
            if lst[min_index] > lst[j]:
                min_index = j
            j += 1

        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]

        i += 1


def quick_sort(lst):

    if len(lst) <= 1:
        return lst
    middle_index = len(lst)//2
    middle_value = lst[middle_index]

    left = [i for i in lst if i < middle_value]

    right = [i for i in lst if i > middle_value]

    return quick_sort(left) + [middle_value] * lst.count(middle_value) + quick_sort(right)


def quick_sort2(lst):
    quick_sort_helper(lst, 0, len(lst)-1)


def quick_sort_helper(lst, low, high):
    if low >= high:
        return
    # three_standard_value(lst, low, high)
    middle_index = partition(lst, low, high)
    quick_sort_helper(lst, low, middle_index-1)
    quick_sort_helper(lst, middle_index+1, high)


def three_standard_value(lst, low, high):

    ''' 三数取中确定基准元，将确定好的基准元与第一个数交换'''
    mid = (high + low)//2

    if lst[mid] > lst[high]:
        lst[mid], lst[high] = lst[high], lst[mid]

    if lst[low] > lst[high]:
        lst[low], lst[high] = lst[high], lst[low]

    if lst[mid] > lst[low]:
        lst[mid], lst[low] = lst[low], lst[mid]


def partition(lst, low, high):
    key = lst[low]  # 取第一个数为基准值
    while low < high:
        while low < high and lst[high] >= key:  # 从列表右边开始把小于基准值的元素放到
            high -= 1
        lst[low] = lst[high]
        while low < high and lst[low] <= key:
            low += 1
        lst[high] = lst[low]
    lst[low] = key
    return low


def insert_sort(lst):

    i = 1
    while i < len(lst):

        j = i-1
        insert_item = lst[i]

        while j >= 0 and lst[j] > insert_item:
            lst[j+1] = lst[j]
            j -= 1

        lst[j+1] = insert_item  # j+1 为当前带插入的位置，因为在找到带插入位置后会经过 j-=1。

        i += 1


def shell_sort(lst):
    n = len(lst)
    gap = n//2  # 初始步长
    while gap > 0:

        # 开始插入排序
        i = gap  # 直接插入排序的起始元素是第二个元素，希尔排序的起始元素是索引为当前步长的那个元素
        while i <= n-gap:  # 循环

            j = i - gap
            insert_item = lst[i]

            while j >= 0 and lst[j] > insert_item:
                lst[j+gap] = lst[j]
                j -= gap

            lst[j+gap] = insert_item
            i += 1

        gap //= 2


def heap_sort(lst):
    length = len(lst)
    # 初始化堆
    i = length//2
    while i >= 0:
        init_heap(lst, i, length)
        i -= 1

    # 执行堆排序过程
    j = length - 1
    while j > 0:
        lst[j], lst[0] = lst[0], lst[j]
        # 筛选 R[0] 结点，得到i-1个结点的堆
        init_heap(lst, 0, j)
        j -= 1


def init_heap(lst, parent, length):
    temp = lst[parent]  # 保存当前父节点
    child = 2 * parent + 1  # 先获得左孩子
    while child < length:

        if child + 1 < length and lst[child] < lst[child + 1]:  # 如果有右孩子结点，并且右孩子结点的值大于左孩子结点，则选取右孩子结点
            child += 1

        if temp >= lst[child]:  # 如果父结点的值已经大于孩子结点的值，则直接结束
            break

        lst[parent] = lst[child]  # 把孩子结点的值赋给父结点

        parent = child  # 选取孩子结点的左孩子结点, 继续向下筛选
        child = 2 * child + 1
    lst[parent] = temp

lst = [3, 2, 4, 5, 1, 4, 7]
heap_sort(lst)
print(lst)  # [1, 2, 3, 4, 4, 5, 7]


# def insertSort(relist):
#     len_ = len(relist)
#     for i in range(1,len_):
#         for j in range(i):
#             if relist[i] < relist[j]:
#                 relist.insert(j,relist[i])  # 首先碰到第一个比自己大的数字，赶紧刹车，停在那，所以选择insert
#                 relist.pop(i+1)  # 因为前面的insert操作，所以后面位数+1，这个位置的数已经insert到前面去了，所以pop弹出
#                 break
#     return relist
#
# print(insertSort([1,5,2,6,9,3]))