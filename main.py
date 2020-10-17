失敗次數 = 0

def on_button_pressed_a():
    global 失敗次數
    music.start_melody(music.built_in_melody(Melodies.JUMP_UP), MelodyOptions.ONCE)
    失敗次數 = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global 失敗次數
    if pins.digital_read_pin(DigitalPin.P2) == 1:
        music.play_tone(262, music.beat(BeatFraction.HALF))
        basic.show_icon(IconNames.NO)
        失敗次數 += 1
        basic.show_number(失敗次數)
basic.forever(on_forever)
