import g2d

g2d.init_canvas((600, 600))

r = int(g2d.prompt("Radius? [50-99]"))

while r < 50 or r > 99:
    g2d.alert("Out of range!")
    r = int(g2d.prompt("Radius? [50-99]"))

g2d.set_color((255, 255, 0))
g2d.draw_circle((200, 200), 25)

g2d.main_loop()

