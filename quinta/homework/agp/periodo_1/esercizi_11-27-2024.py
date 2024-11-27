def esercizio_4():
    stringa = str("parola")

    print(
        f"lettera iniziale: {stringa[0]}\n"
        f"lettera finale: {stringa[-1]}\n"
    )


def esercizio_5():
    stringa = str("parola")

    print(stringa[1:-1])


def esercizio_6():
    stringa = str("parola con piu di otto lettere")
    stringa = str(stringa[:2] + "?" + stringa[3:])

    print(stringa)


def esercizio_10():
    lista_voti = list([8, 7.5, 10, 4.5, 7, 9])

    print(lista_voti[1:-1])

    lista_voti[3] = int(10)

    print(lista_voti[:3])


def esercizio_13():
    rubrica = {
        "Dave": 1234567890,
        "Alle": 2345678901,
    }

    print(list(rubrica.items())[0])

    rubrica["Alex"] = 3456789012

    print(rubrica)


def esercizio_14():
    nome = input("nome -> ")
    print(nome[::-1])


def main():
    print("\n<===== esercizio 4 =====>")
    esercizio_4()

    print("\n<===== esercizio 5 =====>")
    esercizio_5()

    print("\n<===== esercizio 6 =====>")
    esercizio_6()

    print("\n<===== esercizio 10 =====>")
    esercizio_10()

    print("\n<===== esercizio 13 =====>")
    esercizio_13()

    print("\n<===== esercizio_14 =====>")
    esercizio_14()


if __name__ == '__main__':
    main()
