score = float(input("Inserisci lo score del tuo modello di ML (0.0 - 1.0): "))

if score > 1:
    print("0.0 - 1.0, dumbass")
elif 0.8 < score <= 1:
    print("Complimenti, ottimo modello!")
elif 0.6 < score <= 0.8:
    print("Buon modello!")
else:
    print("Ehm... non ci siamo")