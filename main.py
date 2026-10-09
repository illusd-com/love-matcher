def on_button_pressed_a():
    for index in range(2):
        basic.show_number(randint(1, 14))
        basic.show_leds("""
            . # . # .
            # # # # #
            # # # # #
            . # # # .
            . . # . .
            """)
        basic.show_number(randint(1, 14))
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # . # .
        """)
    basic.show_string("estart")
    basic.pause(200)
    basic.show_leds("""
        . # # # .
        . # . # .
        . # # # .
        . # . . .
        . # . . .
        """)
    basic.show_string("ls")
    basic.pause(200)
    basic.show_leds("""
        . # # # .
        . # . # .
        . # # # .
        . # . . .
        . # . . .
        """)
    basic.show_string("ress")
    basic.pause(200)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # . # .
        """)
    basic.show_string("estart")
    basic.pause(200)
    basic.show_leds("""
        . # # # .
        . # . # .
        . # # . .
        . # . # .
        . # # # .
        """)
    basic.show_string("utton")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    for index2 in range(2):
        basic.show_number(randint(16, 30))
        basic.show_leds("""
            . # . # .
            # # # # #
            # # # # #
            . # # # .
            . . # . .
            """)
        basic.show_number(randint(1, 14))
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # . # .
        """)
    basic.show_string("estart")
    basic.pause(200)
    basic.show_leds("""
        . # # # .
        . # . # .
        . # # # .
        . # . . .
        . # . . .
        """)
    basic.show_string("ls")
    basic.pause(200)
    basic.show_leds("""
        . # # # .
        . # . # .
        . # # # .
        . # . . .
        . # . . .
        """)
    basic.show_string("ress")
    basic.pause(200)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # . # .
        """)
    basic.show_string("estart")
    basic.pause(200)
    basic.show_leds("""
        . # # # .
        . # . # .
        . # # . .
        . # . # .
        . # # # .
        """)
    basic.show_string("utton")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for index3 in range(2):
        basic.show_number(randint(16, 30))
        basic.show_leds("""
            . # . # .
            # # # # #
            # # # # #
            . # # # .
            . . # . .
            """)
        basic.show_number(randint(16, 30))
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # . # .
        """)
    basic.show_string("estart")
    basic.pause(200)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # # .
        . # . . .
        . # . . .
        """)
    basic.show_string("ls")
    basic.pause(200)
    basic.show_leds("""
        . # # # .
        . # . # .
        . # # # .
        . # . . .
        . # . . .
        """)
    basic.show_string("ress")
    basic.pause(200)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # . # .
        """)
    basic.show_string("estart")
    basic.pause(200)
    basic.show_leds("""
        . # # # .
        . # . # .
        . # # . .
        . # . # .
        . # # # .
        """)
    basic.show_string("utton")
input.on_button_pressed(Button.B, on_button_pressed_b)

music.set_volume(255)
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