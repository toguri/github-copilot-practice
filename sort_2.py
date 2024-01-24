def bubble_sort (numbers):
    # バブルソートのコード
    # ここにコードを記述してください。
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j],numbers[j + 1] = numbers[j + 1],numbers[j]
    return numbers

before = [5, 1, 4, 2, 8]
print(before)
# => [1, 2, 4, 5, 8]
after = bubble_sort(before)
print(after)