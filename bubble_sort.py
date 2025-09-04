def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        # 最后 i 个元素已经排好，不需要再比较
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 示例
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", data)
    bubbleSort(data)
    print("排序后:", data)
