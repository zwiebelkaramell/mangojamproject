

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
image bg_fin = Image("images/fin.png")

# characters
image finbo = Image("images/Characters/finbo_jones.png")
image finbo_trace = Image("images/Characters/finbo_jones_trace.png")
image horse = Image("images/Characters/horse.png")
image horse_trace = Image("images/Characters/horse_trace.png")
image cactus = Image("images/Characters/cactus.png")
image cactus_trace = Image("images/Characters/cactus_trace.png")
image wyatt = Image("images/Characters/wyatt.png")
image wyatt_trace = Image("images/Characters/wyatt_trace.png")
image finbo_horse = Image("images/Characters/finbo_horse.png")
# = Image("images/Characters/.png")
# = Image("images/Characters/.png")
# = Image("images/Characters/.png")

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

image orbit_busted:
    contains: # behind planet-moon
        pause 15.0
        contains: # moon behind
            pause 7.5
            "images/planet_scene/moon_busted.png"
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
            "images/planet_scene/moon_busted.png"
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
            "images/planet_scene/moon_busted.png"
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
            "images/planet_scene/moon_busted.png"
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
transform center_right:
    xalign 1.0
    yalign 0.5

transform center_left:
    xalign 0.0
    yalign 0.5
#-----------------------------------------------------------------------

# The game starts here.

label start:
    scene bg_space
    show orbit at truecenter with dissolve

    "On a vast, barren Planet, out in god knows where, something out of the ordinary was about to take place."

    "Just another mornin on the tiny planet of Bolb"

    scene bg_lighthouse with fade

    "Time for Finbo Jones to get up and going."

    show finbo_trace at center_right with dissolve

    "Every day, Finbo would be goin on bout his day, gettin up, makin some coffee, before makin his way up the planet's lighthouse, which reached all the way out to space."

    show finbo_trace at center_right with dissolve

    fj  "Another day, another coffee, gotta get steppin up those stairs soon, gotta check on that bulb"

    scene bg_lamp_off with fade

    pause 0.5

    show finbo_trace at center_right with dissolve

    fj  "All lookin good, lemme just turn on that switch"

    hide finbo_trace with dissolve

    "Click"

    scene bg_lamp_on

    pause 0.5

    "Another day comes and Finbo goes about his day as always."

    scene bg_lighthouse with fade

    show finbo_trace at center_right with dissolve

    fj  "Another day, another coffee, gotta get steppin up those stairs soon, gotta check on that bulb"

    scene bg_lamp_off with fade

    pause 0.5

    show finbo_trace at center_right with dissolve

    fj  "All lookin good like every day, lemme just turn on that switch"

    hide finbo_trace with dissolve

    "Click"

    pause 0.5

    show finbo_trace at center_right with dissolve

    fj  "What in tunation?! Something's'off with that bulb, gotta take a closer look"

    "But the bulb was busted"

    fj  "That never happened before. What to do now?"

    menu:
        "Finbo Jones decides to..."

        "Ignore the problem, and go to bed.":
            jump later
        "Check the bulb.":
            pass

    "Finbo checks the bulb, noticing something written on the base."

    fj  "What's that? Something scribbled there. Can't read it tho. Guess I'll be headin out to find me someone who can read me that mumbo jumbo I`sppose"

    hide finbo_trace with dissolve

    "Finbo begins the long trek down the 40,000 flights of stairs to the bottom of the lighthouse"

    scene bg_planet

    "Finally outside, Finbo notices a Space Horse™ in his path"

    show horse_trace at center_left with dissolve

    h   "Why the long face? Nyehehehe!"

    show finbo_trace at center_right with dissolve

    fj  "Darn tootin, a space horse, pretty big those fellas, aren't they, might come in handy"

    "Finbo mounts his newfound steed."

    scene bg_planet
    show finbo_horse:
        zoom 0.50
        xalign 0.5
        yalign 0.5
        xoffset -300

    fj  "Go now!"

    "..."

    fj  "Giddyup now!"

    "..."

    fj  "Walk, now!"

    "..."

    fj  "Alright then"

    hide finbo_horse
    show horse:
        zoom 0.50
        xalign 0.5
        yalign 0.5
        xoffset -300
    show finbo:
        xzoom -1
        xalign 0.5
        yalign 0.5
        xoffset 300

        linear 6.0 xoffset 2000

    "So Finbo Jones, for the first time in his life, stepped out of his lighthouse area and made it to the dessert, nothing but sand can be seen, except for one thing, one singular cactus in the distance."

    
    menu:
        "What should I do?"

        "approach cactus": 
            jump cactus

        "approach a nearby town":
            jump clown

        "approach the saloon":
            jump saloon

    return

label cactus:



label clown:

label saloon:


label later:
    scene bg_space
    show orbit
    "After a week of doing nothing a giant spaceship flies into the planet destroying it completely."
    hide orbit
    show orbit_busted with fade

    "WTF Finbo, why would you do that?"

    window hide
    show bg_fin with fade

    pause

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

