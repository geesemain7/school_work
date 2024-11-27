import g2d

g2d.init_canvas((500, 500))

for i in (range(4)):  # (0, 1, 2, 3)
    red = i * 85
    x = i * 100
    y = i * 100
    g2d.set_color((red, 0, 0))
    g2d.draw_rect((x, y), (200, 200))

g2d.main_loop()