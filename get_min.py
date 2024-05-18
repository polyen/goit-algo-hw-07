from AVL import get_binary_tree


def get_min_number(root):
    if not root:
        return None

    min_number = root

    while min_number.left:
        min_number = min_number.left

    return min_number.key


def test_get_min_number():
    nums = [10, 12, 4, 5, 6, 9, 7, 24, 56, 8, 3, 2]
    root = get_binary_tree(nums)
    min_number = get_min_number(root)
    assert min_number == min(nums), f"Expected {min(nums)}, but got {min_number}"


if __name__ == "__main__":
    test_get_min_number()
