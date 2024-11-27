inglese_italiano = {"random": "casuale", "intelligence": "intelligenza"}
parola_inglese = "random"
print(f"In italiano {parola_inglese} significa {inglese_italiano[parola_inglese]}")

del inglese_italiano["random"]
print(inglese_italiano)