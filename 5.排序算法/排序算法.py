#__author:liwei
#date:2018/4/24

import random


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


# 选择排序
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


# 堆排序
def heap_sort(lst):
    length = len(lst)
    # 初始化堆
    i = length // 2
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


# 冒泡排序
def bubble_sort(lst):

    i = 0
    while i < len(lst):

        j = 0  # 每一轮的比较都是从列表的第一项开始

        while j < len(lst) - 1:

            if lst[j] > lst[j + 1]:  # 前一项大于后一项交换元素（降序排列）

                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # swap element

            j += 1

        i += 1


# 快速排序
def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)


def quick_sort_helper(lst, low, high):
    if low >= high:
        return
    # three_standard_value(lst, low, high)
    middle_index = partition(lst, low, high)
    quick_sort_helper(lst, low, middle_index - 1)
    quick_sort_helper(lst, middle_index + 1, high)


def three_standard_value(lst, low, high):

    ''' 三数取中确定基准元，将确定好的基准元与第一个数交换'''
    mid = (high + low) // 2

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


# 插入排序
def insert_sort(lst):
    i = 1
    while i < len(lst):
        j = i-1
        insert_item = lst[i]
        while j >= 0 and lst[j] > insert_item:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = insert_item # j+1 为当前带插入的位置，因为在找到带插入位置后会经过 j-=1。
        i += 1


# 希尔排序
def shell_sort(lst):
    n = len(lst)
    gap = n // 2  # 初始步长
    while gap > 0:

        # 开始插入排序
        i = gap  # 直接插入排序的起始元素是第二个元素，希尔排序的起始元素是索引为当前步长的那个元素
        while i <= n - gap:  # 循环

            j = i - gap
            insert_item = lst[i]

            while j >= 0 and lst[j] > insert_item:
                lst[j + gap] = lst[j]
                j -= gap

            lst[j + gap] = insert_item
            i += 1

        gap //= 2


# 归并排序
def mergeSortHelper(lyst, copyBuffer, low, high):
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle + 1, high)
        merge(lyst, copyBuffer, low, middle, high)


def merge(lyst, copyBuffer, low, middle, high):
    i1 = low
    i2 = middle + 1
    for i in range(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        else:
            copyBuffer[i] = lyst[i2]
            i2 += 1
    for i in range(low, high + 1):
        lyst[i] = copyBuffer[i]


def mergeSort(lyst):
    count = len(lyst)
    copyBuffer = [0 for i in range(0, count)]
    mergeSortHelper(lyst, copyBuffer, 0, count-1)


# 归并排序2
def merge2(lyst, left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def mergeSort2(lyst):
    if len(lyst) <= 1:
        return lyst
    mid_index = len(lyst)//2
    left = mergeSort2(lyst[:mid_index])  # 递归拆解的过程
    right = mergeSort2(lyst[mid_index:])
    return merge2(lyst, left, right)  # 合并的过程


def main(size=6, sort=quickSort2):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size+1))
    print(lyst)
    sort(lyst)
    print(lyst)

if __name__ == '__main__':
    main()