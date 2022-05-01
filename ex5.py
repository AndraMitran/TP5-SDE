left = 0
right = 0
while True:
    if input.is_gesture(Gesture.TILT_RIGHT):
        right = right + 1
        basic.show_number(right)
    elif input.is_gesture(Gesture.TILT_LEFT):
        left = left + 1
        basic.show_number(left)
    else:
        basic.clear_screen()
