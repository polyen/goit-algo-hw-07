from AVL import get_binary_tree


def get_sum(root):
    if not root:
        return 0

    return root.key + get_sum(root.left) + get_sum(root.right)


def test_get_sum():
    nums = [10, 12, 4, 5, 6, 9, 7, 24, 56, -65, -3, 2]
    root = get_binary_tree(nums)
    sum_of_values = get_sum(root)
    assert sum_of_values == sum(nums), f"Expected {sum(nums)}, but got {sum_of_values}"


if __name__ == '__main__':

    test_get_sum()
