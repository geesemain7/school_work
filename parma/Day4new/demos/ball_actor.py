arenaW, arenaH, ballW, ballH = 480, 360, 20, 20

from actor import Arena, Actor

class Missile(Actor):
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._dy = -5

    def move(self, arena):
        self._y += self._dy

    def pos(self):
        return self._x, self._y

    def size(self):
        return 20, 20

    def sprite(self):
        return 0, 0

class Alien:
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._dx, self._dy = 5, 5

    def move(self, arena):
        for other in arena.collisions():
            if isinstance(other, Missile):
                arena.kill(self)
                arena.kill(other)

        if not 0 <= self._x + self._dx <= arenaW - ballW:
            self._dx = -self._dx
        if not 0 <= self._y + self._dy <= arenaH - ballH:
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def pos(self) -> (int, int):
        return self._x, self._y

    def size(self):
        return 20, 20

    def sprite(self):
        return 20, 0


def console_run():
    b1 = Ball(140, 180)
    b2 = Ball(180, 140)

    b1.move()
    b2.move()

    print("b1 @", b1.pos())
    print("b2 @", b2.pos())

class Turtle(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._dx, self._dy = 0, 0
        self._w, self._h = 20, 20
        self._speed = 10

    def move(self, arena: Arena):
        for other in arena.collisions():
            if isinstance(other, Alien):
                self.hit(arena)

        keys = arena.current_keys()
        self._dx = self._dy = 0
        if "ArrowLeft" in keys:
            self._dx = -self._speed
        elif "ArrowRight" in keys:
            self._dx = self._speed

        if "ArrowUp" in keys:
            icbm = Missile(self._x, self._y - 20)
            arena.spawn(icbm)
        self._x += self._dx
        self._y += self._dy

        aw, ah = arena.size()
        self._x = min(max(self._x, 0), aw - self._w)  # clamp
        self._y = min(max(self._y, 0), ah - self._h)  # clamp

    def hit(self, arena: Arena):
        arena.kill(self)
        g2d.prompt("you have skill issues")

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 20

def tick():
    g2d.clear_canvas()

    for a in arena.actors():
        g2d.draw_image_clip("sprites.png", a.pos(), a.sprite(), a.size())  # FG

    arena.tick(g2d.current_keys())

def main():
    global arena, g2d
    import g2d

    arena = Arena((480, 320))

    arena.spawn(Alien(140, 180))
    arena.spawn(Alien(180, 140))
    arena.spawn(Turtle((180, 300)))

    g2d.init_canvas((arenaW, arenaH))
    g2d.main_loop(tick, 60)

main()