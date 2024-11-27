import g2d
red = 0
n = 3.8

g2d.init_canvas((255*n, 255*n))

for green in range(0, 256):

    for blue in range(0, 256):
        g2d.set_color((red, green, blue))
        g2d.draw_rect((blue*n, green*n), (n, n))

g2d.main_loop()