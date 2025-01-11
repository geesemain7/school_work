import numpy as np

def main():
    v = np.array(
        [1, 5, 4, 3, 2]
    )
    a = np.array([
        [1, 2],
        [3, 4]
    ])
    b = np.array([
        [5, 6],
        [7, 8]
    ])

    print(f"size v = {v.size}\n")

    print(f"shape v = {v.shape}\n")

    print(f"max v = {np.max(v)}")
    print(f"min v = {np.min(v)}")
    print(f"mean v = {np.mean(v)}")
    print(f"standard deviation = {np.std(v)}\n")

    print(f"transpose a = {np.transpose(a)}")
    print(f"transpose b = {np.transpose(b)}\n")

    print(f"ordered v = {np.sort(v)}\n")

    print(f"sum a+b = {a+b}")
    print(f"difference a-b = {a-b}\n")

    print(f"product of a*b = {np.dot(a, b)}\n")

    vec_1 = np.arange(0, 10)
    print(f"vettore da 0-9:\n{vec_1}\n")

    vec_2 = np.arange(4, 37, 4)
    print(f"vettore da 4 a 36 con multipli di 4:\n{vec_2}\n")

    mat_0 = np.zeros((2, 2), dtype=np.int8)
    print(f"Matrice 2 x 2 di soli zero: {mat_0}\n")

    mat_1 = np.ones((2, 2), dtype=np.int8)
    print(f"Matrice 2 x 2 di soli uno: {mat_1}\n")

    mat_3 = np.full((10, 10), 3)
    print(f"Matrice 10 x 10 di soli 3: {mat_3}\n")

    mat_17 = np.ones((10, 10))
    np.fill_diagonal(mat_17, 7)
    print(f"Matrice 10 x 10 piena di 1 con 7 nelle diagonali: {mat_17}\n")

    mat_17[mat_17 == 7] = 9
    print(f"Matrice 10 x 10 piena di 1 e 9 nelle diagonali: {mat_17}")


if __name__ == '__main__':
    main()
