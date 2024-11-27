import g2d

canW, canH, ballW, ballH = 480, 360, 20, 20


class Ball:
    def __init__(self, x, y, vx, vy):
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy

    def pos(self):  # a method to pass location data
        return self._x, self._y

    def move(self):
        if not 0 <= self._x + self._vx <= canW - ballW:
            self._vx = -self._vx
        if not 0 <= self._y + self._vy < canH - ballH:
            self._vy = -self._vy

        self._x += self._vx
        self._y += self._vy


b1 = Ball(40, 50, 2, 3)
b2 = Ball(80, 20, 4, 1)
b3 = Ball(100, 120, 5, 7)
b4 = Ball(30, 20, 1, 2)
b5 = Ball(300, 300, 7, 3)
b6 = Ball(420, 10, 8, 7)

balls = [b1, b2, b3, b4, b5, b6]


def tick():
    g2d.clear_canvas()

    for b in balls:
        g2d.draw_image("ball.png", b.pos())
        b.move()


def main():
    g2d.init_canvas((canW, canH))
    g2d.main_loop(tick, 60)


main()
