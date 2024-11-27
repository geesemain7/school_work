import g2d

canW, canH, spriteW, spriteH, inc = 1280, 720, 20, 20, 5

class Alien:
    def __init__(self, x, y, lorder):
        self._x = x
        self._y = y
        self._vx = 6
        self._vel = self._vx
        self._line_length = 3
        self._lorder = lorder

    def pos(self):
        return self._x, self._y

    def move(self):
        if self._x + self._vx > ((canW - (spriteW * self._line_length)) + (self._lorder * (spriteW + inc))):
            self._y += inc
            self._vx = -self._vel

        if self._x + self._vx < (0 + (self._lorder * (spriteW + 5))):
            self._y += inc
            self._vx = self._vel

        self._x += self._vx


g1 = Alien(20, 20, 0)
g2 = Alien(45, 20, 1)
g3 = Alien(70, 20, 2)
g4 = Alien(20, 45, 0)
g5 = Alien(45, 45, 1)
g6 = Alien(70, 45, 2)

ghosts = [g1, g2, g3, g4, g5, g6]

def tick():
    g2d.clear_canvas()

    for g in ghosts:
        g2d.draw_image_clip("sprites.png", g.pos(), (20, 0), (20, 20))
        g.move()


def main():
    g2d.init_canvas((canW, canH))
    g2d.main_loop(tick, 60)

main()
