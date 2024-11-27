import g2d

x, y, xspeed, s = 200, 200, 6, 6
canW, canH = 600, 600

def move():
    global x, y, xspeed
    g2d.clear_canvas()
    g2d.draw_image_clip("sprites.png", (x, y), (20, 0), (20, 20))

    if x + xspeed > 580:
        y = y + 5
        xspeed = -s

    if x + xspeed < 0:
        y = y + 5
        xspeed = s

    x = x + xspeed

def main():
    g2d.init_canvas((canW, canH))
    g2d.main_loop(move)

main()