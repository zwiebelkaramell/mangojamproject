

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
define sf = Character("?????", callback=gun_text_trick, color="#ffffff")
define s = Character("Scorpion Barkeeper", callback=text_trick, color="#7d6671")
define i = Character("Inventor", callback=text_trick, color="#a3995a")

#----------------------------------------------------------------------

#------------- VARIABLES ----------------------------------------------
default has_inventor_name = False
default has_seen_cactus = False
default has_clowned = False
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
image bg_mountain = Image("images/Characters/inventor.png")
image bg_mountain_eyes = Image("images/Characters/inventor_home.png")

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
image barkeep = Image("images/Characters/Saloon_barkeep.png")
image barkeep_trace = Image("images/Characters/barkeep_trace.png")
image wyatt_shadow = Image("images/Characters/wyatt_shadow.png")
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

    jump menu

    return

label menu:
 menu:
        "What should I do?"


        "approach cactus" if has_seen_cactus == False: 
            jump cactus

        "approach a nearby town":
            jump clown

        "approach the saloon": if has_inventor_name == False:
            jump saloon


label cactus:

    scene bg_planet

    "So Finbo Jones decides to approaches the Cactus, not knowing what it is"

    show cactus_trace at center_left with dissolve

    show finbo_trace at center_right with dissolve

    fj  "Howdy there, ...mister? Are you by chance good with them words'n'stuff? I can't read, you see. My mama never tought me and ma dad was never arround."

    "The cactus does not react, but some drops of liquid begin to form on it's crown."

    fj  "Havin trouble hearin? I said I need some help with the readin mister!"

    c   "Lo siento, señor, no entiendo su idioma. Por favor, déjame en paz."

    fj  "I wasn't askin for no riddles mister, just need some help with this bulb you see,..."

    "Finbo shows the bulb to this strange creature"

    c   "¿Por qué me enseñas esta bombilla?"

    fj  "Maybe the sun has been messin with your mind, guess I'll have to try elsewhere..."

    c   "¡Por favor, déjame en paz, criatura loca!"

    show cactus_trace:
        xalign 0.0
        yalign 0.5
        linear 0.5 xoffset 3000

    "The cactus suddenly runs away and Finbo Jones now confused decides to continue his journey"

    $ has_seen_cactus = True

    jump menu

    return

label saloon:
    scene bg_planet

    "Finbo Jones wanders around aimlessly for a while until he comes across a lonesome saloon in the middle of nowhere in the dessert"
    
    "It looks quite small and kinda shabby from the outside, it reads: \"The Saloon\", Finbo Jones decides to step inside"
    
    scene bg_saloon

    "Once inside he realizes that this establishment isn't too shabby at all, it has a nice bar, some tables and seats, a piano in the corner next to the bar, but it seems pretty empty"

    show barkeep with dissolve

    pause 0.5

    show barkeep_trace at center_left with dissolve

    s   "Welcome to The Saloon mister, where the only thing that stings is our famous worm tequilla, sometimes even twice, what can I fetch ya?"

    show finbo_trace at center_right with dissolve

    fj  "jumpin' jehoshaphat!, quite the man you are, mister, who made you?"

    s   "The name is Pinch, can't say I've ever seen you around here, what gives?"

    fj  "I be lookin for someone"

    s   "Everbody be lookin for someone, gotta be more 'pacific, but also, can I intrest you in our famous dessert worm tequilla? First one's'on the house"

    fj  "Can't say no to that"

    "Finbo sits down and starts to relax, as Pinch begins preparing his drink."

    s   "So whom you lookin for, mister?"

    fj  "Been lookin for someone who can do the readin good."

    s   "Tough task indeed, not many of dem readin folks left around here, lucky for you I do"

    fj  "Heavens to betsy it must be my lucky day then, can you tell me whats written on that damn bulb of light right here good sir?"

    s   "Says Bulbus Dumblebulb, no idea who that is, son"

    fj  "Awe dang it all, where's a fish to find a whole pond for once"

    s   "Yeah, I feel ya. Listen, sumthin else. You see, haven't been havin lots of folks comin round these days, well for many days... would it be too much to ask you fo sumthin mister?"

    fj  "Spit it out barkeep"
    
    "Finbo takes a sip, spitting it out immediately"

    fj "Ain't used to worms beein in ma booze, sorry"

    s   "Could you recommend this place to folks you come across by chance, it would mean lots to a ol'barkeep who's tryin to make a livin out here, for each new customer one free tequilla"

    fj  "Got it barkeep, can keep dem worms tho. I be headin out then, so long"

    s   "Happy trails"

    $ has_inventor_name = True

    jump menu

label clown:

    if has_clowned:
        scene bg_planet

        "Finbo returns to the small town, where he met that very funny critter"

        show wyatt_trace at center_left with dissolve

        wm "Finbo Jones, brave of you to show your face around these parts"

        if has_inventor_name:

            show finbo_trace at center_right with dissolve

            fj "Mister \"Why Not\", I'm all out of ideas, do you know a \"Bulbus Dumblebulb\"?"

            wm "You're in luck"

            wm "I came across that man. Weird fella he is, makin no sense, with all dem stuffs he makes. He lives up there on that mountain in a dark cave, cause he hates company"

            fj "Thank you kindly, I'm gonna moosey along then, tryin findin that inventor, so long, mister why not mermaid"

            jump mountain

        else:

            wm "Git outta here!!!"

            jump menu




    else:
        scene bg_planet

        "Finbo Jones decides to walk into a small town, all the folks staring at him while he walks around trying to find somebody to talk to, but none of the residents seem interested in conversing with him"

        show finbo_trace at center_right with dissolve

        fj  "What a godforsaken town, and a unfriendly one at that."
        
        "Finbo notices a few faint squeeks and honks in the distance"

        "Noticing the noise, all the towns people hastily make their way into their houses and lock their doors, causing quite a ruckus, some daringly peekin out of the windows to see what might happen"

        "The honks become louder, approaching the town. suddenly a shadowy figure can be seen approaching over the horizon"

        show wyatt_shadow at center_left with dissolve

        fj "Who walks there?"

        sf  "What do we have here, someone walkin the streets like they own the place, right when the legendary Wyatt Murdock comes to town. Speak your name, boy?"

        fj  "Finbo Jones, mister, that's what ma mama named me, may she rest in peas"

        sf  "That's one awful name, makes me laugh" 

        hide wyatt_shadow
        show wyatt_trace at center_left with dissolve

        "The character lets out a silly, squeeky laugh, like a rubber chicken was stuck in his gullet"

        fj "Now that's a funny laugh, mister. And what's with dem clothes, lookin quite, how do folks say, fancy?"

        wm "What did ya just say, boy? I will show you what's funcy"

        "Murdock reaches for his pistol, producing a bouquet of flowers that squirt water in his face."

        wm "Urgh! oh fudge!"

        fj "Hahaha am loosin ma scales"

        wm "I will make ya loose all of em!" 

        "Face red in anger, clown make up now angry looking as well, Murdock aims a gun at Finbo and pulls the trigger"

        "Instead of a bullet going off, a flag comes out, reading \"Bang\""

        fj "What's that now mister? What does it even say?"

        wm "What do I know, I can't read this... Gol-dernit!, are ya makin fun of me, son?!"

        if has_inventor_name:

            fj "Well, that makes us two, can't read either mister, talked to a barkeep in a saloon he told me about Bulbus Dumblebulb, tryin to find him ever since."

            wm "Someone who can read all that mambo jambo? Lucky you I guess. Bulbus Dumblebulb you say?

            wm "I came across that man. Weird fella he is, makin no sense, with all dem stuffs he makes. He lives up there on that mountain in a dark cave, cause he hates company"

            fj "Thank you kindly, I'm gonna moosey along then, tryin findin that inventor, so long, mister why not mermaid"

            wm "Dadgummit! It's Wyatt Murdock! You come back here!"

            "Wyatt stomps angrily after Finbo, but trips on his own comically large shoes"

            mw "CURSE YOU FINBO JONES!!!!"

            jump mountain

        else:

            fj "Well, that makes us two, can't read either mister, was lookin for someone who can, actually"

            wm "Someone who can read all that mambo jambo? Can't help you, kid." 

            fj "Damnit, guess I gotta keep lookin then. Thank you kindly, I'm gonna moosey along then, tryin findin that inventor, so long, mister why not mermaid"

            wm "Dadgummit! It's Wyatt Murdock! You come back here!"

            "Wyatt stomps angrily after Finbo, but trips on his own comically large shoes"

            mw "CURSE YOU FINBO JONES!!!!"

            $ has_clowned = True

            jump menu


    return

label mountain:

    scene inventor

    "Finbo Jones makes it onto the mountain to find the entrance to a cave which seems to be an old mine"

    show finbo_trace at center_right with dissolve

    fj "Howdy, anyone in there?"

    scene inventor_home
    show finbo_trace at center_right

    i  "LEAVE!"

    fj "Im lookin for a fella called Bulbus Dumblebulb"

    i  "Go away! No bulbus here!"

    fj "God dangit, all that way for nothin. What am I gonna do with dat damn bulb now"

    i  "Bulb? Did you say bulb?"

    fj "Aye, that big ol bulb from the lighthouse"

    i  "Lighthouse?! Roll that bulb in here at once! Don't dare to come in here!"

    fj "Aight mister, rollin it in"

    "Finbo gingerly rolls the bulb into the cave."

    i  "Good heavens it is the lightbulb from the lighthouse. What happened to you? You were supposed to last 10 more years!"

    i "My calculations couldn't be incorrect could they. hmm hmm. Let me see... yes"

    fj "Mister, what's goin on in there? I don't have time for games..."

    i  "Silence lighthousekeeper, I need to think, this will take some time"

    fj "So, you must be Bulbus Dumblebulb after all?"

    i  "Yes indeed, the one and only. Inventor and mechanic, professor of science. Master of the mountain mine. Now let me work"

    fj "I guess, well I'll wait."

    i  "Let me just open this, yes, aha, maybe put this here and... yes yes, oh and tweak it here mmm, and now we try this, nono, wrong, but what if I...."

    fj "You sure that ya will be able to fix it?"

    i  "Silence! Let me work! Now back to you bulb, now, here, yes and that, looking good, HA! I AM A GENIUS! AHAHAHA! I did it"

    fj "You done it mister?"

    i  "I will roll it out, it is fixed, working and should work for at least the next 50 years"

    fj "Thank you kindly mister inventor"

    i  "Now leave, and never NEVER come back!"

    fj "Alright mister, geez, what a nut"

    "So finally Finbo Jones found someone who could repair the lightbulb, he makes his way home to the lighthouse."

    "Making it up and putting in the repaired lightbulb, turning it on. His life coming back to how it used to be.

    window hide
    show bg_fin with fade

    pause

    return

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

