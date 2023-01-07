visible_trees = set()


def row_traversal(tree_mat, r_i, start, dir):
    curr_max = -1
    for _ in range(len(tree_mat[r_i])):
        if tree_mat[r_i][start] > curr_max:
            visible_trees.add((r_i, start))
            curr_max = tree_mat[r_i][start]
        start += dir


def col_traversal(tree_mat, c_j, start, dir):
    curr_max = -1
    for _ in range(len(tree_mat)):
        if tree_mat[start][c_j] > curr_max:
            visible_trees.add((start, c_j))
            curr_max = tree_mat[start][c_j]
        start += dir


def visibility_counter(tree_mat):
    for i in range(len(tree_mat)):
        row_traversal(tree_mat, i, 0, 1)
        row_traversal(tree_mat, i, len(tree_mat[i])-1, -1)
 
    for j in range(len(tree_mat[0])):
        col_traversal(tree_mat, j, 0, 1)
        col_traversal(tree_mat, j, len(tree_mat)-1, -1)


def main():
    tree_mat = list(map(lambda l: list(map(int, list(l))),
                    open('in.txt', 'r').read().split('\n')))
    visibility_counter(tree_mat)
    print(len(visible_trees))


main()
