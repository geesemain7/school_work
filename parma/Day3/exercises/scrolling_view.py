import g2d

canW, canH = 344, 169
viewW, viewH = 86, 42

def tick():
    x, y = 0, 0

    g2d.clear_canvas()

    keys = g2d.current_keys()
    if "ArrowUp" in keys:
        y = max(y - 10, 0)
    elif "ArrowDown" in keys:
        y = min(y, + 10, canW - viewH)
    elif "LeftArrow" in keys:
        x = min(x - 10, canH - viewH)
    elif "RightArrow" in keys:
        x = max(x - 10, 0)

    g2d.draw_image_clip("scroll_bg.png", (0, 0), (x, y), (viewW, viewH))

def main():
    g2d.init_canvas((viewW, viewH))
    g2d.main_loop(tick)

main()
