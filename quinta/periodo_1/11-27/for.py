bookmarks = ["www.kaggle.com", "www.wikipedia.org", "www.numpy.org", "www.python.org"]
contatore = 0

for sito in bookmarks:
    contatore += 1

    print(f"sito n°{contatore}: {sito} su dominio: {sito[-4:]}")