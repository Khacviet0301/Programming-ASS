

def product(M, N):
    a = M[0][0] * N[0][0] + M[0][1] * N[1][0]
    b = M[0][0] * N[0][1] + M[0][1] * N[1][1]
    c = M[1][0] * N[0][0] + M[1][1] * N[1][0]
    d = M[1][0] * N[0][1] + M[1][1] * N[1][1]
    return [[a, b], [c, d]]


def mat_add(M, N):
    return [[M[0][0]+N[0][0], M[0][1]+N[0][1]],
            [M[1][0]+N[1][0], M[1][1]+N[1][1]]]


def mat_scale(M, k):
    return [[M[0][0]*k, M[0][1]*k],
            [M[1][0]*k, M[1][1]*k]]


def compute_An_Bn(n):
    A = [[5, 3], [2, -1]]
    B = [[2, -3], [5, 4]]
    I = [[1, 0], [0, 1]]
    Z = [[0, 0], [0, 0]]

    res_P = [row[:] for row in I]
    res_Q = [row[:] for row in Z]

    base_P = [row[:] for row in A]
    base_Q = [[-B[i][j] for j in range(2)] for i in range(2)]

    power = n
    while power > 0:
        if power % 2 == 1:
            new_P = mat_add(product(res_P, base_P),
                            mat_scale(product(res_Q, base_Q), 11))
            new_Q = mat_add(product(res_P, base_Q),
                            product(res_Q, base_P))
            res_P, res_Q = new_P, new_Q
        new_P = mat_add(product(base_P, base_P),
                        mat_scale(product(base_Q, base_Q), 11))
        new_Q = mat_add(product(base_P, base_Q),
                        product(base_Q, base_P))
        base_P, base_Q = new_P, new_Q
        power //= 2

    return res_P, res_Q


def main():
    
    print("chuoi ma tran voi sqrt(11)")
    

    print("\n- 2.1 product(M, N) -")
    M = [[1, 2], [3, 4]]
    N = [[5, 6], [7, 8]]
    print(f"  product({M}, {N})")
    print(f"  = {product(M, N)}")

    print("\n- 2.2 compute_An_Bn(n) -")
    
    print(f"  A = [[5,3],[2,-1]],  B = [[2,-3],[5,4]]\n")
    for n in [1, 2, 3, 5, 10]:
        An, Bn = compute_An_Bn(n)
        print(f"  n={n}:")
        print(f"    A_n = {An}")
        print(f"    B_n = {Bn}")


if __name__ == "__main__":
    main()