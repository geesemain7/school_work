class BallArena:
    def __init__(self):
        self._balls = []
    def spawn(self, b: balls):
        self._balls.append(b)
    def tick(self):
        for b in self._balls:
                b.move()

arena = BallArena()
arena.spawn(Ball(40, 80))
arena.spawn(Ball(80, 40))  # ...
arena.tick()