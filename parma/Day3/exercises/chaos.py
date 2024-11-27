from random import randint

import g2d

canW, canH, ballW, ballH = 1280, 720, 81, 46


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
            g2d.play_audio("pipe.mp3")
        if not 0 <= self._y + self._vy < canH - ballH:
            self._vy = -self._vy
            g2d.play_audio("pipe.mp3")

        self._x += self._vx
        self._y += self._vy


b1 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b2 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b3 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b4 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b5 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b6 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b7 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b8 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b9 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b10 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b11 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b12 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b13 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b14 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b15 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b16 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b17 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b18 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b19 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b20 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b21 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b22 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b23 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b24 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b25 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b26 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b27 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b28 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b29 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b30 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b31 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b32 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b33 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b34 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))
b35 = Ball(randint(0, 481), randint(0, 361), randint(0, 10), randint(0, 10))

balls = [b1, b2, b3, b4, b5, b6, b7, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22,
         b23, b24, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35]


def rep():
    g2d.clear_canvas()
    for b in balls:
        g2d.draw_image("../../Day2/exercises/pipe.png", b.pos())
        b.move()


def funny_thing():
    g2d.init_canvas((canW, canH))
    g2d.main_loop(rep, 60)


funny_thing()
