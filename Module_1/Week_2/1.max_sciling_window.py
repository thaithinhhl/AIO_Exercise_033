def max_sciling_window(num_list, k):
    n = len(num_list)

    if n == 0 or k == 0:
        return []

    def find_max(nums):
        return max(nums)

    max_list = []

    for i in range(n - k + 1):

        window = num_list[i:i+k]
        max_list.append(find_max(window))

    return max_list


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

print(max_sciling_window(num_list, k))
