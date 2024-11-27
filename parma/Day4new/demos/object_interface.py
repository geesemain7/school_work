class Actor:  # …
    def move(self, arena: Arena):
        raise NotImplementedError("Abstract method")

class Arena:  # …
    def __init__(self, size):
        self._w, self._h = size
        self._actors = []

    def spawn(self, a: Actor):
        self._actors.append(a)

    def tick(self):
        for a in self._actors:
            a.move(self)

    def size(self):
        return self._w, self._h