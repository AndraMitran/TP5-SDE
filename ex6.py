def on_gesture_shake():
    if input.logo_is_pressed():
        music.play_melody("C5 C5 E F A C5 A B ", 120)
    elif input.button_is_pressed(Button.AB):
        music.stop_all_sounds()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
