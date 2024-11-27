import g2d
from random import randint

g2d.init_canvas(((600, 600)))

n = int(g2d.prompt("Insert number of squares: "))

for i in (range(n)):
    x = i * 15
    y = i * 15
    g2d.set_color((randint(0, 255), randint(0, 255), randint(0, 255)))
    g2d.draw_rect((x, y), (30, 30))

g2d.main_loop()