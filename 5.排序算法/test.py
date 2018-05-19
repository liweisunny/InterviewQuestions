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



lst = [3, 2, 4, 5, 1, 4]
quick_sort2(lst)
print(lst)  # [1, 2, 3, 4, 4, 5]