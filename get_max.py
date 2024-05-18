from AVL import get_binary_tree


def get_max_number(root):
    if not root:
        return None

    max_number = root

    while max_number.right:
        max_number = max_number.right

    return max_number.key


def test_get_max_number():
    nums = [10, 12, 4, 5, 6, 9, 7, 24, 56, 8, 3, 2]
    root = get_binary_tree(nums)
    max_number = get_max_number(root)
    assert max_number == max(nums), f"Expected {max(nums)}, but got {max_number}"


if __name__ == "__main__":
    test_get_max_number()
