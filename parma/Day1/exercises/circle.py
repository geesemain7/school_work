import g2d

g2d.init_canvas((600, 600))

r = int(g2d.prompt("Radius? [0-200]"))

while r < 0 or r > 200:
    g2d.alert("Out of range!")
    r = int(g2d.prompt("Radius? [0-200]"))

g2d.set_color((255, 255, 0))
g2d.draw_circle((300, 300), r)

g2d.main_loop()

