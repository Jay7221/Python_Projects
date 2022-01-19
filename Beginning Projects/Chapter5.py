#! python3
# Chapter5


import random
import timeit

def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        elif item > a_list[midpoint]:
            first = midpoint + 1
    return found

def binary_search2(a_list, item):
    if len(a_list) == 0:
        return False

    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            return binary_search(a_list[:midpoint], item)
        elif item > a_list[midpoint]:
            return binary_search(a_list[midpoint + 1:], item)
def binary_search3(a_list, item):
    return binary_search4(a_list, item, 0, len(a_list) - 1)

def binary_search4(a_list, item, start, end):
    mid = (start + end) // 2
    if start< 0 or end<0:
        return False
    if a_list[mid] == item:
        return True
    elif a_list[mid] > item:
        return binary_search4(a_list, item, start, mid - 1)
    elif a_list[mid] <  item:
        return binary_search4(a_list, item, mid + 1, end)
    return False
    
def hash1(a_string, table_size):
    sum = 0
    for pos in range(len(a_string)):
        sum += ord(a_string[pos])* (pos + 1)
    return sum % table_size

def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]

def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        pass_num -= 1

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
            a_list[pos_of_max], a_list[fill_slot] = a_list[fill_slot], a_list[pos_of_max]

def insert_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1
        a_list[position] = current_value

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        #print('After increments of size', sublist_count, 'The list is', a_list)
        sublist_count //= 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position -= gap
        a_list[position] = current_value

def merge_sort(a_list):
    #print('Splitting', a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(right_half)
        merge_sort(left_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
    #print('Merging', a_list)

def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):
    '''if len(a_list) < 2:
        insertion_sort(a_list)
        return first
    pivot_list =[ a_list[first], a_list[(first + last) // 2], a_list[last]]
    pivot_list.remove(max(pivot_list))
    pivot_list.remove(min(pivot_list))
    pivot_value = pivot_list.pop()'''

    pivot_value = first

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark += 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]

    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    return right_mark
            
                

def data(n = 1000):
        a = list()
        for i in range(n):
            a.append(random.randint(1, 1000))
        return a
    
def benchmark_test(n):
    
    bubble = timeit.Timer('bubble_sort(data())', 'from __main__ import bubble_sort, data')
    short_bubble = timeit.Timer('short_bubble_sort(data())', 'from __main__ import short_bubble_sort, data')
    selection = timeit.Timer('selection_sort(data())', 'from __main__ import selection_sort, data')
    insert = timeit.Timer('insert_sort(data())', 'from __main__ import insert_sort, data')
    shell = timeit.Timer('shell_sort(data())', 'from __main__ import shell_sort, data')
    merge = timeit.Timer('merge_sort(data())', 'from __main__ import merge_sort, data')
    quick = timeit.Timer('quick_sort(data())', 'from __main__ import quick_sort, data')

    print('Time required for bubble_sort is %s'%bubble.timeit(10))
    print('Time required for short_bubble is %s'%short_bubble.timeit(10))
    print('Time required for selection is %s'%selection.timeit(10))
    print('Time required for insert is %s'%insert.timeit(10))
    print('Time required for shell is %s'%shell.timeit(10))
    print('Time required for merge is %s'%merge.timeit(10))
    print('Time required for quick is %s'%quick.timeit(10))

if __name__ == '__main__':
    benchmark_test(500)
