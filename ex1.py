def on_forever():
    if input.button_is_pressed(Button.B):
        basic.show_number(input.temperature())
    elif input.logo_is_pressed():
        # display the temperature
        basic.show_number(input.light_level())
    else:
        basic.clear_screen()
basic.forever(on_forever)
