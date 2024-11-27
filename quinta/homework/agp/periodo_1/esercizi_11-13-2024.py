def esercizio_1():
    print("----- Esercizio 1 -----")
 
    var_a = 17
    var_b = "hello world"
    var_c = 3.14
    var_d = True

    list = [var_a, var_b, var_c, var_d]

    for variable in list:
        print(
            f"valore: {variable}\n"
            f"tipo: {type(variable)}\n"
        )


def esercizio_2():
    print("----- Esercizio 2 -----")

    var_a, var_b, var_c, var_d = 17, "hello world", 3.14, True

    list = [var_a, var_b, var_c, var_d]

    for variable in list:
        print(
            f"valore: {variable}\n"
            f"tipo: {type(variable)}\n"
        )


def esercizio_3():
    print("----- Esercizio 3 -----")

    prima = 17
    seconda = 71

    temp = seconda
    seconda = prima
    prima = temp

    print(prima, seconda)


if __name__ == "__main__":
    esercizio_1()
    esercizio_2()
    esercizio_3()
