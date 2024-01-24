# バブルソートのコード
def bubble_sort(numbers):
    """バブルソートのコード
    Args:
        numbers (list): ソートする数値が入ったリスト
    Returns:
        list: ソートされたリスト
    Examples:
        >>> bubble_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]
    """
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]: # 比較して交換
                numbers[j],numbers[j + 1] = numbers[j + 1],numbers[j] # 交換
    return numbers # ソート後のリストを返す

import heapq

def heap_sort(nums):
    """ヒープソートのコード
    Args:
        nums (list): ソートする数値が入ったリスト
    Returns:
        list: ソートされたリスト
    Examples:
        >>> heap_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]
    """
    # リストをヒープに変換
    heapq.heapify(nums)
    
    sorted_nums = []
    # ヒープから最小の要素を取り出し、ソートされたリストに追加
    while nums:
        sorted_nums.append(heapq.heappop(nums))
    
    return sorted_nums

# ヒープソートのコードをランダムな数字で実行
if __name__ == "__main__":
    import random
    nums = [random.randint(0,1000) for i in range(10)]
    print("ヒープソート")
    print(heap_sort(nums))

# 上記関数のテストコード
def test_bubble_sort():
    # テスト用のランダムな配列を生成する
    import random
    nums = [random.randint(0,1000) for i in range(10)]
    # バブルソートでnumsをソートする
    assert bubble_sort(nums) == sorted(nums)

# バブルソートのコードをランダムな数字で実行
if __name__ == "__main__":
    import random
    nums = [random.randint(0,1000) for i in range(10)]
    print("バブルソート")
    print(bubble_sort(nums))

def quick_sort(arr):
    """
    クイックソートのコード

    Args:
        arr (list): ソートする数値が入ったリスト

    Returns:
        list: ソートされたリスト

    Examples:
        >>> quick_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """マージソートのコード
    Args:
        arr (list): ソートする数値が入ったリスト
    Returns:
        list: ソートされたリスト
    Examples:
        >>> merge_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]
    """
    if len(arr) <= 1:
        return arr
    
    # リストを分割する
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # 再帰的に分割したリストをマージする
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    """マージソートのマージ処理
    Args:
        left (list): 左側のリスト
        right (list): 右側のリスト
    Returns:
        list: マージされたリスト
    """
    merged = []
    i = j = 0
    
    # 左右のリストを比較しながらマージする
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # 左側のリストが残っている場合、マージする
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # 右側のリストが残っている場合、マージする
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged
