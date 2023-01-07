"""
nearest largest value no the left side:
A <- input
P[i] <- index of nlv(i) on left
for i in 1..n:
    j = i-1
    while j > 0 and A[j] < A[i]:
        j = P[j]
    P[i] = j
do similar thing for right, up and down directions
"""


def nlv_l(tree_mat, r_i, row_size):
    P = [-1 for _ in range(row_size)]
    for i in range(row_size):
        j = i-1
        while j >= 0 and tree_mat[r_i][j] < tree_mat[r_i][i]:
            j = P[j]
        P[i] = j
    return P


def nlv_u(tree_mat, c_j, col_size):
    P = [-1 for _ in range(col_size)]
    for i in range(col_size):
        j = i-1
        while j >= 0 and tree_mat[j][c_j] < tree_mat[i][c_j]:
            j = P[j]
        P[i] = j
    return P


def nlv_r(tree_mat, r_i, row_size):
    P = [row_size for _ in range(row_size)]
    for i in range(row_size-1, -1, -1):
        j = i+1
        while j < row_size and tree_mat[r_i][j] < tree_mat[r_i][i]:
            j = P[j]
        P[i] = j
    return P


def nlv_d(tree_mat, c_j, col_size):
    P = [col_size for _ in range(col_size)]
    for i in range(col_size-1, -1, -1):
        j = i+1
        while j < col_size and tree_mat[j][c_j] < tree_mat[i][c_j]:
            j = P[j]
        P[i] = j
    return P


L = []
R = []
U = []
D = []


def transpose_list(X):
    return [list(i) for i in zip(*X)]


def visibility_counter(tree_mat):
    global L, R, U, D
    row_count = len(tree_mat)
    col_count = len(tree_mat[0])

    for i in range(col_count):
        L.append(nlv_l(tree_mat, i, col_count))
        R.append(nlv_r(tree_mat, i, col_count))

    for j in range(len(tree_mat[0])):
        U.append(nlv_u(tree_mat, j, row_count))
        D.append(nlv_d(tree_mat, j, row_count))

    U = transpose_list(U)
    D = transpose_list(D)
    max_scenic_score = 0

    for i in range(row_count):
        for j in range(col_count):
            l_d = j if L[i][j] == -1 else j-L[i][j]
            u_d = i if U[i][j] == -1 else i-U[i][j]
            r_d = col_count-1-j if R[i][j] == col_count else R[i][j]-j
            d_d = row_count-1-i if D[i][j] == row_count else D[i][j]-i
            max_scenic_score = max(max_scenic_score, l_d*r_d*u_d*d_d)
    print(max_scenic_score)


def main():
    tree_mat = list(map(lambda l: list(map(int, list(l))),
                    open('in.txt', 'r').read().split('\n')))
    visibility_counter(tree_mat)


main()
