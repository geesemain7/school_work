import g2d

x, y, vx, vy, g = 100, 100, 2, 3, 0.3
canW, canH, spriteW, spriteH = 1280, 720, 80, 44

class lefunny:
    def __init__(self):
        self._x = 100
        self._y = 100
        self._vx = 5
        self._vy = 3
        self._g = 0.7

    def pos(self):
        return self._x, self._y

    def move(self):
        if not 0 <= (self._x + self._vx) <= (canW - spriteW):
            self._vx = -self._vx
            g2d.play_audio("pipe.mp3")
        if not 0 <= (self._y + self._vy) <= (canH - spriteH):
            self._vy = -self._vy
            g2d.play_audio("pipe.mp3")
        else:
            self._vy = self._vy + g

        self._x += self._vx
        self._y += self._vy

p = lefunny()

def tick():
    g2d.clear_canvas()
    g2d.draw_image("pipe.png", p.pos())
    p.move()

def main():
    g2d.init_canvas((canW, canH))
    g2d.main_loop(tick, 60)

main()