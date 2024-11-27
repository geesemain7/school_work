import g2d
import time

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
        if g2d.mouse_clicked():
            for i in (0, 6):
                i += time.time() / 30

                if not 0 <= self._x + self._vx <= canW - ballW:
                    self._vx = -self._vx
                if not 0 <= self._y + self._vy < canH - ballH:
                    self._vy = -self._vy

                self._x += self._vx
                self._y += self._vy

b1 = Ball(40, 50, 5, 0)

def tick():
    g2d.clear_canvas()
    g2d.draw_image("ball.png", b1.pos())
    b1.move()

def main():
    g2d.init_canvas((canW, canH))
    g2d.main_loop(tick)

main()
