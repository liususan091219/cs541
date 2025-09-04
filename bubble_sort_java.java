public class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            // 最后 i 个元素已经排好，不需要再比较
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // 交换元素
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    int temp2 = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] data = {64, 34, 25, 12, 22, 11, 90};
        System.out.print("原始数组: ");
        for (int num : data) {
            System.out.print(num + " ");
        }

        bubbleSort(data);

        System.out.print("\n排序后: ");
        for (int num : data) {
            System.out.print(num + " ");
        }
    }
}
