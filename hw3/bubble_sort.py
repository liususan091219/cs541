#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HW3: Bubble Sort Implementation
冒泡排序算法实现

Author: CS541 Course
Date: October 2025
"""


def bubble_sort(arr):
    """
    冒泡排序算法
    
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    
    参数:
        arr (list): 需要排序的列表
    
    返回:
        list: 排序后的列表（原地排序）
    
    示例:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
        # 标记是否发生交换，用于优化
        swapped = False
        
        # 最后 i 个元素已经排好序了
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果没有发生交换，说明已经排序完成
        if not swapped:
            break
    
    return arr


def bubble_sort_descending(arr):
    """
    冒泡排序算法（降序）
    
    参数:
        arr (list): 需要排序的列表
    
    返回:
        list: 降序排序后的列表
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            # 降序：如果当前元素小于下一个元素，则交换
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


def bubble_sort_with_stats(arr):
    """
    带统计信息的冒泡排序
    
    返回排序结果和统计信息（比较次数、交换次数）
    """
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        
        if not swapped:
            break
    
    return arr, comparisons, swaps


def main():
    """
    主函数：测试冒泡排序算法
    """
    print("=" * 50)
    print("HW3: 冒泡排序算法测试")
    print("=" * 50)
    
    # 测试用例 1: 普通数组
    test_array_1 = [64, 34, 25, 12, 22, 11, 90]
    print("\n测试 1 - 普通数组:")
    print(f"原始数组: {test_array_1}")
    sorted_array_1 = bubble_sort(test_array_1.copy())
    print(f"排序后数组: {sorted_array_1}")
    
    # 测试用例 2: 空数组
    test_array_2 = []
    print("\n测试 2 - 空数组:")
    print(f"原始数组: {test_array_2}")
    sorted_array_2 = bubble_sort(test_array_2.copy())
    print(f"排序后数组: {sorted_array_2}")
    
    # 测试用例 3: 单个元素
    test_array_3 = [42]
    print("\n测试 3 - 单个元素:")
    print(f"原始数组: {test_array_3}")
    sorted_array_3 = bubble_sort(test_array_3.copy())
    print(f"排序后数组: {sorted_array_3}")
    
    # 测试用例 4: 已排序数组
    test_array_4 = [1, 2, 3, 4, 5]
    print("\n测试 4 - 已排序数组:")
    print(f"原始数组: {test_array_4}")
    sorted_array_4 = bubble_sort(test_array_4.copy())
    print(f"排序后数组: {sorted_array_4}")
    
    # 测试用例 5: 逆序数组
    test_array_5 = [5, 4, 3, 2, 1]
    print("\n测试 5 - 逆序数组:")
    print(f"原始数组: {test_array_5}")
    sorted_array_5 = bubble_sort(test_array_5.copy())
    print(f"排序后数组: {sorted_array_5}")
    
    # 测试用例 6: 包含重复元素
    test_array_6 = [3, 7, 3, 1, 7, 2]
    print("\n测试 6 - 包含重复元素:")
    print(f"原始数组: {test_array_6}")
    sorted_array_6 = bubble_sort(test_array_6.copy())
    print(f"排序后数组: {sorted_array_6}")
    
    # 测试用例 7: 降序排序
    test_array_7 = [64, 34, 25, 12, 22, 11, 90]
    print("\n测试 7 - 降序排序:")
    print(f"原始数组: {test_array_7}")
    sorted_array_7 = bubble_sort_descending(test_array_7.copy())
    print(f"排序后数组: {sorted_array_7}")
    
    # 测试用例 8: 带统计信息
    test_array_8 = [64, 34, 25, 12, 22, 11, 90]
    print("\n测试 8 - 带统计信息:")
    print(f"原始数组: {test_array_8}")
    sorted_array_8, comps, swaps = bubble_sort_with_stats(test_array_8.copy())
    print(f"排序后数组: {sorted_array_8}")
    print(f"比较次数: {comps}")
    print(f"交换次数: {swaps}")
    
    print("\n" + "=" * 50)
    print("所有测试完成！")
    print("=" * 50)


if __name__ == "__main__":
    main()
