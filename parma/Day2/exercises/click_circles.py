import g2d
from random import randint

x, y, r, canH, canW = 0, 0, 10, 600, 600

def tick():
    global x, y, r

    if g2d.mouse_clicked():
        x, y = g2d.mouse_pos()
        g2d.set_color((randint(0, 255), randint(0, 255), randint(0, 255)))
        g2d.draw_circle((x, y), r)

def main():

    g2d.init_canvas((canH, canW))
    g2d.clear_canvas()
    g2d.main_loop(tick, 60)

main()