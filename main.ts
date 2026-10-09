input.onButtonPressed(Button.A, function () {
    music.play(music.createSoundExpression(
    WaveShape.Sine,
    5000,
    0,
    255,
    0,
    500,
    SoundExpressionEffect.None,
    InterpolationCurve.Linear
    ), music.PlaybackMode.InBackground)
    basic.showNumber(randint(1, 14))
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.showNumber(randint(1, 14))
})
input.onButtonPressed(Button.AB, function () {
    music.play(music.createSoundExpression(
    WaveShape.Sine,
    5000,
    0,
    255,
    0,
    500,
    SoundExpressionEffect.None,
    InterpolationCurve.Linear
    ), music.PlaybackMode.InBackground)
    basic.showNumber(randint(16, 30))
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.showNumber(randint(1, 14))
})
input.onButtonPressed(Button.B, function () {
    music.play(music.createSoundExpression(
    WaveShape.Sine,
    5000,
    0,
    255,
    0,
    500,
    SoundExpressionEffect.None,
    InterpolationCurve.Linear
    ), music.PlaybackMode.InBackground)
    basic.showNumber(randint(16, 30))
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.showNumber(randint(16, 30))
})
music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.InBackground)
music.setVolume(255)
for (let index = 0; index < 2; index++) {
    basic.showLeds(`
        # . # . #
        # . # . .
        # # # . #
        # . # . #
        # . # . #
        `)
    basic.pause(200)
    basic.showLeds(`
        # # # . #
        . # . # .
        . # . . .
        . # . . .
        # # # . .
        `)
    basic.showString("m")
    basic.pause(200)
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.pause(200)
    basic.showString("m")
    basic.showString("a")
    basic.showLeds(`
        . . # . .
        . # # # .
        . . # . .
        . . # . .
        . . # # .
        `)
    basic.showString("c")
    basic.showString("h")
    basic.showString("e")
    basic.showLeds(`
        . . . . .
        # . # # .
        # # . . .
        # . . . .
        # . . . .
        `)
    basic.pause(500)
    basic.showLeds(`
        . . . . .
        # . . . #
        # . . . #
        . # . # .
        . . # . .
        `)
    basic.showString("1.2")
}
