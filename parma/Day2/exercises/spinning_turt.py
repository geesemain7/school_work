import g2d, math, time, random

canH, canW = 240, 240

def rotate():
    g2d.clear_canvas()
    g2d.draw_circle((120, 120), 2)

    i, rad = 0, 100
    angle = i + time.time()
    x = rad * math.cos(angle * 0.8) + 110
    y = rad * math.sin(angle * 0.9) + 110

    g2d.draw_image_clip("sprites.png", (x, y), (0, 20), (20, 20))

    second_turt()
    third_turt()

def second_turt():
    i, rad = 0, 100

    angle = i + time.time() + 1
    x = rad * math.cos(angle * 1.2) + 110
    y = rad * math.sin(angle * 1.2) + 110

    g2d.draw_image_clip("sprites.png", (x, y), (0, 20), (20, 20))

def third_turt():
    i, rad = 0, 100

    angle = i + time.time() + 0.5
    x = rad * math.cos(angle * 0.3) + 110
    y = rad * math.sin(angle * 0.4) + 110

    g2d.draw_image_clip("sprites.png", (x, y), (0, 20), (20, 20))

def main():
    g2d.init_canvas((canH, canW))
    g2d.main_loop(rotate, 60)

main()