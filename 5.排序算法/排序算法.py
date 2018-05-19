#__author:liwei
#date:2018/4/24

import random

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


# 选择排序
def selectSort(lyst):
    i = 0
    while i < len(lyst)-1:
        min_index = i
        j = i+1
        while j < len(lyst):
            if lyst[j] < lyst[min_index]:
                min_index = j
            j += 1
        if min_index != i:
            swap(lyst, min_index, i)
        i += 1


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


# 插入排序
def insertionSort(lyst):
    i = 1
    count = 0
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i-1
        while j >= 0:
            count += 1
            if itemToInsert < lyst[j]:
                lyst[j+1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j+1] = itemToInsert
        i += 1
    print(count)


# 快速排序1
def quickSort(lyst):
    if len(lyst) <= 1:
        return lyst
    middleIndx = len(lyst)//2
    middleValue = lyst[middleIndx]

    left = [i for i in lyst if middleValue > i]
    right = [i for i in lyst if middleValue < i]

    return quickSort(left) + [middleValue] * lyst.count(middleValue) + quickSort(right)


# 快速排序2
def quickSort2(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)


def quicksortHelper(lyst, left, right):
    if left < right:
        pivot_location = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivot_location - 1)
        quicksortHelper(lyst, pivot_location + 1, right)




def partition(lyst, left, right):
    middle = (left + right)//2  # left + (right-left)/2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    boundry = left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundry)
            boundry += 1
    swap(lyst, right, boundry)
    return boundry


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