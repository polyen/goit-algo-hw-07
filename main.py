from AVL import get_binary_tree
from get_max import get_max_number
from get_min import get_min_number
from get_sum import get_sum

if __name__ == '__main__':
    nums = [10, 12, 4, 5, 6, 9, 7, 24, 56, 10, 16, 2]
    root = get_binary_tree(nums)

    max_number = get_max_number(root)
    min_number = get_min_number(root)
    sum_of_values = get_sum(root)

    print('Max: ', max_number)
    print('Min: ', min_number)
    print('Sum: ', sum_of_values)
