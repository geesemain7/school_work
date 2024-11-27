import g2d

arena_w = 1000
arena_h = 1000
max_radius = 50
g2d.init_canvas((arena_w, arena_h))

x = 500
y = 500

n = int(g2d.prompt("Insert number of circles: "))

for i in reversed(range(n)):
    radius = (max_radius / 2) * i + (max_radius / n)
    color = (-255 / (n - 1)) * i + 255
    g2d.set_color((color, 0, 0))
    g2d.draw_circle((x, y), radius)

g2d.main_loop()