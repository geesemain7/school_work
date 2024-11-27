from actor import Arena, Actor
from random import randint

arenaW, arenaH, alienW, alienH = 1280, 720, 56, 32

class HolyLaser(Actor):
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._dy = -8

    def move(self, arena):
        self._y += self._dy

        if self._y < -self.size()[1]:
            arena.kill(self)

    def pos(self):
        return self._x, self._y

    def size(self):
        return 4, 28

    def sprite(self):
        return 441, 1895

class UnholyLaser(Actor):
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._dy = 6

    def move(self, arena):
        self._y += self._dy

        if self._y > arena.size()[1]:
            arena.kill(self)

    def pos(self):
        return self._x, self._y

    def size(self):
        return 4, 12

    def sprite(self):
        return 215, 1490

class Alien:
    def __init__(self, x0: int, y0: int):
        self._x, self._y = x0, y0
        self._vx = 1.5
        self._vy = 15
        self._xmax = 394 + x0  # first: arenaW - alienW - x0 of the first alien
        self._xmin = x0 - 92   # 1280 - 52 - 192
        self._shotcnt = randint(0, 200)
        self._shotint = randint(200, 400)

    def move(self, arena):
        kills, flag = 0, 0

        for other in arena.collisions():
            if isinstance(other, HolyLaser):
                arena.kill(self)
                arena.kill(other)
                kills += 1
            if isinstance(other, Ship):
                arena.kill(other)

        if not self._xmin <= self._x + self._vx <= self._xmax:
            self._vx = -self._vx
            self._y += self._vy
        else:
            self._x += self._vx

        self._shotcnt += 1
        if self._shotcnt >= self._shotint:
            m = UnholyLaser(self._x + 30, self._y + 25)
            arena.spawn(m)
            self._shotcnt = 0
            self._shotint = randint(200, 400)

    def pos(self) -> (int, int):
        return self._x, self._y

    def size(self):
        return alienW, alienH

    def sprite(self):
        return 208, 1948

class Ship(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._dx, self._dy = 0, 0
        self._w, self._h = 28, 32
        self._xspeed = 4
        self._yspeed = 4

    def move(self, arena: Arena):
        for other in arena.collisions():
            if isinstance(other, Alien):
                self.hit(arena)

        keys = arena.current_keys()
        prev_keys = arena.previous_keys()

        self._dx = self._dy = 0

        if "ArrowLeft" in keys:
            self._dx = -self._xspeed
        if "ArrowRight" in keys:
            self._dx = self._xspeed
        if "ArrowUp" in keys:
            self._dy = -self._yspeed
        if "ArrowDown" in keys:
            self._dy = self._yspeed

        xicbm = self._x + (self._w / 2) - 0.55
        yicbm = self._y - self._h

        if "Spacebar" in keys and "Spacebar" not in prev_keys:
            if not any(isinstance(obj, HolyLaser) for obj in arena.actors()):
                icbm = HolyLaser(xicbm, yicbm)
                arena.spawn(icbm)

        self._x += self._dx
        #self._y += self._dy

        aw, ah = arena.size()
        self._x = min(max(self._x, 0), aw - self._w)
        self._y = min(max(self._y, 0), ah - self._h)

        for other in arena.collisions():
            if isinstance(other, UnholyLaser):
                arena.kill(self)

    def hit(self, arena: Arena):
        arena.kill(self)

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 428, 1939

def game_won(arena) -> bool:
    for a in arena.actors():
        if isinstance(a, Alien):
            return False
    return True

def game_lost(arena) -> bool:
    for a in arena.actors():
        if isinstance(a, Ship):
            return False
    return True

def tick():
    g2d.clear_canvas()  # BG
    g2d.draw_image("si_background.png", (0, 0))

    if game_won(arena):
        g2d.alert("You win!")
        g2d.close_canvas()
        return

    if game_lost(arena):
        g2d.clear_canvas()
        g2d.draw_image("end_screen.png", (0, 0))

    for a in arena.actors():
        if a.sprite() is not None:
            g2d.draw_image_clip("si_sprites.png", a.pos(), a.sprite(), a.size())  # FG
        else:
            pass

    arena.tick(g2d.current_keys())

def spawner():
    keys = g2d.current_keys()
    if "Spacebar" in keys:
        for j in range(5):
            yspec = 30 + j * 50
            for i in range(1, 11):
                spc = 10 + i * 82
                arena.spawn(Alien(spc, yspec))
        arena.spawn(Ship((640, 660)))
        g2d.main_loop(tick, 60)

def main():
    global arena, g2d
    import g2d

    arena = Arena((arenaW, arenaH))
    g2d.init_canvas((arenaW, arenaH))
    g2d.draw_image("start_screen.png", (0, 0))

    g2d.main_loop(spawner, 60)

main()



