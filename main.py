def on_button_pressed_a():
    music.play(music.create_sound_expression(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_number(randint(1, 14))
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.show_number(randint(1, 14))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(randint(16, 30))
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.show_number(randint(1, 14))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(randint(16, 30))
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.show_number(randint(16, 30))
input.on_button_pressed(Button.B, on_button_pressed_b)

music.play(music.builtin_playable_sound_effect(soundExpression.hello),
    music.PlaybackMode.IN_BACKGROUND)
music.set_volume(255)
for index in range(2):
    basic.show_leds("""
        # . # . #
        # . # . .
        # # # . #
        # . # . #
        # . # . #
        """)
    basic.pause(200)
    basic.show_leds("""
        # # # . #
        . # . # .
        . # . . .
        . # . . .
        # # # . .
        """)
    basic.show_string("m")
    basic.pause(200)
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.pause(200)
    basic.show_string("m")
    basic.show_string("a")
    basic.show_leds("""
        . . # . .
        . # # # .
        . . # . .
        . . # . .
        . . # # .
        """)
    basic.show_string("c")
    basic.show_string("h")
    basic.show_string("e")
    basic.show_leds("""
        . . . . .
        # . # # .
        # # . . .
        # . . . .
        # . . . .
        """)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
        # . . . #
        # . . . #
        . # . # .
        . . # . .
        """)
    basic.show_string("1.2")