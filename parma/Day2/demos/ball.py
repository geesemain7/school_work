import g2d

x, y, vx, vy = 50, 50, 5, 2
canW, canH = 480, 360

def move():
    global x, y, vx, vy

    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x, y))  # Draw foreground

    if g2d.mouse_clicked() or (x + vx > (canW - 20)) or (x + vx < 0):
        vx = -vx

    if g2d.mouse_clicked() or (y + vy > (canH - 20)) or (y + vy < 0):
        vy = -vy

    x = x + vx  # Update ball's position
    y = y + vy

def main():
    g2d.init_canvas((canW, canH))
    g2d.main_loop(move)

main()