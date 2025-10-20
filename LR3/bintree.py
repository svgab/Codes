# Root = 5; height = 6, left_leaf = root^2, right_leaf = root-2

def gen_bin_tree(height=6, root=5, left_leaf=lambda x: x**2,
                 right_leaf=lambda x: x-2):

    current = root
    if height == 0:
        return {str(current): []}

    left_value = left_leaf(root)
    right_value = right_leaf(root)

    left_subtree = gen_bin_tree(height - 1, left_value,
                                left_leaf, right_leaf)
    right_subtree = gen_bin_tree(height - 1, right_value,
                                 left_leaf, right_leaf)

    # Если поддерево пустое (из-за отрицательных значений и т.д.),
    # используем пустой список
    left_child = [left_subtree] if left_subtree else []
    right_child = [right_subtree] if right_subtree else []

    return {str(root): left_child + right_child}


print(gen_bin_tree())
