import g2d
from random import randint

g2d.init_canvas((600, 600))

for r in (200, 175, 150):
    g2d.set_color((randint(0, 255), randint(0, 255), randint(0, 255)))
    g2d.draw_circle((200, 200), r)

g2d.main_loop()