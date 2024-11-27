import g2d
from random import randint

n = int(g2d.prompt("Insert number of squares"))

g2d.init_canvas((600, 600))

for i in range(n):
    g2d.set_color((randint(0, 255), randint(0, 255), randint(0, 255)))
    g2d.draw_rect((randint(0, 400), randint(0, 400)), (100, 100))

g2d.main_loop()