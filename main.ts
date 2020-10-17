let 失敗次數 = 0
input.onButtonPressed(Button.A, function () {
    music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
    失敗次數 = 0
})
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P2) == 1) {
        music.playTone(262, music.beat(BeatFraction.Half))
        basic.showIcon(IconNames.No)
        失敗次數 += 1
        basic.showNumber(失敗次數)
    }
})
