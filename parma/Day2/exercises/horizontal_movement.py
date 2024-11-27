import g2d

x, y, xspeed, flag = 200, 200, 5, 1
canW, canH = 600, 600


def move():
    global x, y, xspeed, flag

    if flag == 1:
        g2d.clear_canvas()
        g2d.draw_image_clip("../../frogger.png", (x, y), (192, 0), (33, 30))

    if flag == -1:
        g2d.clear_canvas()
        g2d.draw_image_clip("../../frogger.png", (x, y), (192, 32), (34, 33))

    if g2d.mouse_clicked():
        xspeed = -xspeed
        flag = -flag

    if x + xspeed > 710:
        x = -110

    if x + xspeed < -110:
        x = 710
    x = x + xspeed


def main():
    g2d.init_canvas((canW, canH))
    g2d.main_loop(move, 60)


main()
