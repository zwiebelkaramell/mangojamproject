

init python:
    #pre-game programming goes here

    import random as rand

    def text_trick(event, interact=True, **kwargs):
        #does the phoenix write style text displaying noise
        if not interact:
            return
        
        if event == "show":
            renpy.music.set_volume(0.02, channel="sound")
            renpy.music.play('audio/typing.wav', channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def gun_text_trick(event, interact=True, **kwargs):
        #does the phoenix write style text displaying noise
        if not interact:
            return
        
        if event == "show":
            renpy.music.set_volume(0.02, channel="sound")

            shot_list = ['audio/gunshots/shot1.wav', 'audio/gunshots/shot2.wav', 'audio/gunshots/shot3.wav','audio/gunshots/shot4.wav','audio/gunshots/shot5.wav','audio/gunshots/shot6.wav']
            rand.shuffle(shot_list)

            renpy.music.play(shot_list[0], channel="sound")
            for x in range(1,6):
                renpy.music.queue(shot_list[x], channel="sound")

        elif event == "slow_done" or event == "end":
            renpy.music.queue('audio/reload_fast.wav', channel="sound", clear_queue=True)

#------------ CHARACTER DEFINITIONS -----------------------------------
define fj = Character("Finbo Jones", callback=text_trick, color="#c7281d")
define h = Character("Spacehorse", callback=text_trick, color="#805227")
define c = Character("Cactus", callback=text_trick, color="#2e6021")
define ta = Character("Moonshiner Tally", callback=text_trick, color="#e4d96f")
define ti = Character("Moonshiner Tiny", callback=text_trick, color="1b2690")
define rtf = Character("Random Town Folk", callback=text_trick, color="#d3d3d3")
define wm = Character("Wyatt Murdock", callback=gun_text_trick, color="#e94257")
#----------------------------------------------------------------------

#------------------ IMAGE DEFINITIONS ---------------------------------
# backgrounds
image bg_space = Image("images/planet_scene/space.png")
image bg_lighthouse = Image("images/Lighthouse/Lighthouse_bg.png")
image bg_lamp_on = Image("images/Lighthouse/Lighthouse_lamp_on.png")
image bg_lamp_off = Image("images/Lighthouse/Lighthouse_lamp_off.png")
image bg_planet = Image("images/Planet.png")
image bg_saloon = Image("images/Saloon.png")

# characters
image finbo = Image("images/Characters/finbo_jones.png")
image finbo_trace = Image("images/Characters/finbo_jones_trace.png")
 = Image("images/Characters/.png")
  = Image("images/Characters/.png")
 = Image("images/Characters/.png")
  = Image("images/Characters/.png")
   = Image("images/Characters/.png")
    = Image("images/Characters/.png")
     = Image("images/Characters/.png")
# other sprites
image sun_top = Image("images/planet_scene/sun_top.png")
image sun_bottom = Image("images/planet_scene/sun_bottom.png")
image sun = Image("images/planet_scene/sun.png")
image blue_orb = Image("images/planet_scene/blue_orb.png")
image moon = Image("images/planet_scene/moon.png")
image mocapot = Image("images/Objects/Mocapot/mocapot.png")

# orbit animation thing
image orbit:
    contains: # behind planet-moon
        pause 15.0
        contains: # moon behind
            pause 7.5
            "images/planet_scene/moon.png"
            xalign 0.5 yalign 0.5 xoffset -100 yoffset 0

            linear 0.25 xoffset -99 yoffset -2
            linear 0.25 xoffset -97 yoffset -5
            linear 0.25 xoffset -95 yoffset -7
            linear 0.25 xoffset -91 yoffset -10
            linear 0.25 xoffset -86 yoffset -12
            linear 0.25 xoffset -80 yoffset -14
            linear 0.25 xoffset -74 yoffset -16
            linear 0.25 xoffset -66 yoffset -18
            linear 0.25 xoffset -58 yoffset -20
            linear 0.25 xoffset -49 yoffset -21
            linear 0.25 xoffset -40 yoffset -22
            linear 0.25 xoffset -30 yoffset -23
            linear 0.25 xoffset -20 yoffset -24
            linear 0.25 xoffset -10 yoffset -24
            linear 0.25 xoffset 0 yoffset -25
            linear 0.25 xoffset 10 yoffset -24
            linear 0.25 xoffset 20 yoffset -24
            linear 0.25 xoffset 30 yoffset -23
            linear 0.25 xoffset 40 yoffset -22
            linear 0.25 xoffset 49 yoffset -21
            linear 0.25 xoffset 58 yoffset -20
            linear 0.25 xoffset 66 yoffset -18
            linear 0.25 xoffset 74 yoffset -16
            linear 0.25 xoffset 80 yoffset -14
            linear 0.25 xoffset 86 yoffset -12
            linear 0.25 xoffset 91 yoffset -10
            linear 0.25 xoffset 95 yoffset -7
            linear 0.25 xoffset 97 yoffset -5
            linear 0.25 xoffset 99 yoffset -2
            linear 0.25 xoffset 100 yoffset 0

            Null()
            repeat
        contains: # planet
            "images/planet_scene/blue_orb.png"
            xalign 0.5 yalign 0.5
        contains: # moon infront
            "images/planet_scene/moon.png"
            xalign 0.5 yalign 0.5 xoffset 100 yoffset 0

            linear 0.25 xoffset 99 yoffset 2
            linear 0.25 xoffset 97 yoffset 5
            linear 0.25 xoffset 95 yoffset 7
            linear 0.25 xoffset 91 yoffset 10
            linear 0.25 xoffset 86 yoffset 12
            linear 0.25 xoffset 80 yoffset 14
            linear 0.25 xoffset 74 yoffset 16
            linear 0.25 xoffset 66 yoffset 18
            linear 0.25 xoffset 58 yoffset 20
            linear 0.25 xoffset 49 yoffset 21
            linear 0.25 xoffset 40 yoffset 22
            linear 0.25 xoffset 30 yoffset 23
            linear 0.25 xoffset 20 yoffset 24
            linear 0.25 xoffset 10 yoffset 24
            linear 0.25 xoffset 0 yoffset 25
            linear 0.25 xoffset -10 yoffset 24
            linear 0.25 xoffset -20 yoffset 24
            linear 0.25 xoffset -30 yoffset 23
            linear 0.25 xoffset -40 yoffset 22
            linear 0.25 xoffset -49 yoffset 21
            linear 0.25 xoffset -58 yoffset 20
            linear 0.25 xoffset -66 yoffset 18
            linear 0.25 xoffset -74 yoffset 16
            linear 0.25 xoffset -80 yoffset 14
            linear 0.25 xoffset -86 yoffset 12
            linear 0.25 xoffset -91 yoffset 10
            linear 0.25 xoffset -95 yoffset 7
            linear 0.25 xoffset -97 yoffset 5
            linear 0.25 xoffset -99 yoffset 2
            linear 0.25 xoffset -100 yoffset 0

            Null()
            pause 7.5
            repeat



        xalign 0.5 yalign 0.5 xoffset -400 yoffset 0

        linear 0.5 xoffset -397 yoffset -10
        linear 0.5 xoffset -391 yoffset -20
        linear 0.5 xoffset -380 yoffset -30
        linear 0.5 xoffset -365 yoffset -40
        linear 0.5 xoffset -346 yoffset -50
        linear 0.5 xoffset -323 yoffset -58
        linear 0.5 xoffset -297 yoffset -66
        linear 0.5 xoffset -267 yoffset -74
        linear 0.5 xoffset -235 yoffset -80
        linear 0.5 xoffset -199 yoffset -86
        linear 0.5 xoffset -162 yoffset -91
        linear 0.5 xoffset -123 yoffset -95
        linear 0.5 xoffset -83 yoffset -97
        linear 0.5 xoffset -41 yoffset -99
        linear 0.5 xoffset 0 yoffset -100
        linear 0.5 xoffset 41 yoffset -99
        linear 0.5 xoffset 83 yoffset -97
        linear 0.5 xoffset 123 yoffset -95
        linear 0.5 xoffset 162 yoffset -91
        linear 0.5 xoffset 199 yoffset -86
        linear 0.5 xoffset 235 yoffset -80
        linear 0.5 xoffset 267 yoffset -74
        linear 0.5 xoffset 297 yoffset -66
        linear 0.5 xoffset 323 yoffset -58
        linear 0.5 xoffset 346 yoffset -50
        linear 0.5 xoffset 365 yoffset -40
        linear 0.5 xoffset 380 yoffset -30
        linear 0.5 xoffset 391 yoffset -20
        linear 0.5 xoffset 397 yoffset -10
        linear 0.5 xoffset 400 yoffset 0
        Null()
        repeat
    contains: # sun
        "images/planet_scene/sun.png"
        xalign 0.5 yalign 0.5
    contains: # infront planet-moon
        contains: # moon behind
            pause 7.5
            "images/planet_scene/moon.png"
            xalign 0.5 yalign 0.5 xoffset -100 yoffset 0

            linear 0.25 xoffset -99 yoffset -2
            linear 0.25 xoffset -97 yoffset -5
            linear 0.25 xoffset -95 yoffset -7
            linear 0.25 xoffset -91 yoffset -10
            linear 0.25 xoffset -86 yoffset -12
            linear 0.25 xoffset -80 yoffset -14
            linear 0.25 xoffset -74 yoffset -16
            linear 0.25 xoffset -66 yoffset -18
            linear 0.25 xoffset -58 yoffset -20
            linear 0.25 xoffset -49 yoffset -21
            linear 0.25 xoffset -40 yoffset -22
            linear 0.25 xoffset -30 yoffset -23
            linear 0.25 xoffset -20 yoffset -24
            linear 0.25 xoffset -10 yoffset -24
            linear 0.25 xoffset 0 yoffset -25
            linear 0.25 xoffset 10 yoffset -24
            linear 0.25 xoffset 20 yoffset -24
            linear 0.25 xoffset 30 yoffset -23
            linear 0.25 xoffset 40 yoffset -22
            linear 0.25 xoffset 49 yoffset -21
            linear 0.25 xoffset 58 yoffset -20
            linear 0.25 xoffset 66 yoffset -18
            linear 0.25 xoffset 74 yoffset -16
            linear 0.25 xoffset 80 yoffset -14
            linear 0.25 xoffset 86 yoffset -12
            linear 0.25 xoffset 91 yoffset -10
            linear 0.25 xoffset 95 yoffset -7
            linear 0.25 xoffset 97 yoffset -5
            linear 0.25 xoffset 99 yoffset -2
            linear 0.25 xoffset 100 yoffset 0

            Null()
            repeat
        contains: # planet
            "images/planet_scene/blue_orb.png"
            xalign 0.5 yalign 0.5
        contains: # moon infront
            "images/planet_scene/moon.png"
            xalign 0.5 yalign 0.5 xoffset 100 yoffset 0

            linear 0.25 xoffset 99 yoffset 2
            linear 0.25 xoffset 97 yoffset 5
            linear 0.25 xoffset 95 yoffset 7
            linear 0.25 xoffset 91 yoffset 10
            linear 0.25 xoffset 86 yoffset 12
            linear 0.25 xoffset 80 yoffset 14
            linear 0.25 xoffset 74 yoffset 16
            linear 0.25 xoffset 66 yoffset 18
            linear 0.25 xoffset 58 yoffset 20
            linear 0.25 xoffset 49 yoffset 21
            linear 0.25 xoffset 40 yoffset 22
            linear 0.25 xoffset 30 yoffset 23
            linear 0.25 xoffset 20 yoffset 24
            linear 0.25 xoffset 10 yoffset 24
            linear 0.25 xoffset 0 yoffset 25
            linear 0.25 xoffset -10 yoffset 24
            linear 0.25 xoffset -20 yoffset 24
            linear 0.25 xoffset -30 yoffset 23
            linear 0.25 xoffset -40 yoffset 22
            linear 0.25 xoffset -49 yoffset 21
            linear 0.25 xoffset -58 yoffset 20
            linear 0.25 xoffset -66 yoffset 18
            linear 0.25 xoffset -74 yoffset 16
            linear 0.25 xoffset -80 yoffset 14
            linear 0.25 xoffset -86 yoffset 12
            linear 0.25 xoffset -91 yoffset 10
            linear 0.25 xoffset -95 yoffset 7
            linear 0.25 xoffset -97 yoffset 5
            linear 0.25 xoffset -99 yoffset 2
            linear 0.25 xoffset -100 yoffset 0

            Null()
            pause 7.5
            repeat

        xalign 0.5 yalign 0.5 xoffset 400 yoffset 0

        linear 0.5 xoffset 397 yoffset 10
        linear 0.5 xoffset 391 yoffset 20
        linear 0.5 xoffset 380 yoffset 30
        linear 0.5 xoffset 365 yoffset 40
        linear 0.5 xoffset 346 yoffset 49
        linear 0.5 xoffset 323 yoffset 58
        linear 0.5 xoffset 297 yoffset 66
        linear 0.5 xoffset 267 yoffset 74
        linear 0.5 xoffset 235 yoffset 80
        linear 0.5 xoffset 199 yoffset 86
        linear 0.5 xoffset 162 yoffset 91
        linear 0.5 xoffset 123 yoffset 95
        linear 0.5 xoffset 83 yoffset 97
        linear 0.5 xoffset 41 yoffset 99
        linear 0.5 xoffset 0 yoffset 100
        linear 0.5 xoffset -41 yoffset 99
        linear 0.5 xoffset -83 yoffset 97
        linear 0.5 xoffset -123 yoffset 95
        linear 0.5 xoffset -162 yoffset 91
        linear 0.5 xoffset -199 yoffset 86
        linear 0.5 xoffset -235 yoffset 80
        linear 0.5 xoffset -267 yoffset 74
        linear 0.5 xoffset -297 yoffset 66
        linear 0.5 xoffset -323 yoffset 58
        linear 0.5 xoffset -346 yoffset 49
        linear 0.5 xoffset -365 yoffset 40
        linear 0.5 xoffset -380 yoffset 30
        linear 0.5 xoffset -391 yoffset 20
        linear 0.5 xoffset -397 yoffset 10
        linear 0.5 xoffset -400 yoffset 0
        Null()
        pause 15.0
        repeat
#----------------------------------------------------------------------

#---------------- TRANSFORMS -------------------------------------------

#-----------------------------------------------------------------------

# The game starts here.

label start:
    scene bg room

    show fishbo_jones trace

    fj "you think i'm funny?"

    fj "what am i, a clown to you?"

    menu wip_test_menu:

        "show that funny planet thing":
            jump menu_test

        "make coffee":
            jump coffee_test

        "i dunno":
            pass

    # This ends the game.

    return

label menu_test:
    show bg_space
    show orbit at truecenter

    "Space..."
    return

label coffee_test:
    show mocapot
    "fuckin coffee man..."
    return