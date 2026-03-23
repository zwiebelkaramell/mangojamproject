

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

'''
    def zorder_workaround_1(trans, st, at, /):
        renpy.show("blue_orb", at_list=[ellipse_1], zorder=2)

    def zorder_workaround_2(trans, st, at, /):
        renpy.show("blue_orb", at_list=[ellipse_2], zorder=0)
'''

#------------ CHARACTER DEFINITIONS -----------------------------------
define fj = Character("Fishbo Jones", callback=gun_text_trick)
#----------------------------------------------------------------------

#------------------ IMAGE DEFINITIONS ---------------------------------
# backgrounds
image bg_space = Image("images/planet_scene/space.png")

# characters

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
            pause 15.0
            "images/planet_scene/moon.png"
            xalign 0.5 yalign 0.5 xoffset 440 yoffset 0

            linear 0.5 xoffset 437 yoffset 11
            linear 0.5 xoffset 430 yoffset 22
            linear 0.5 xoffset 418 yoffset 33
            linear 0.5 xoffset 401 yoffset 44
            linear 0.5 xoffset 381 yoffset 54
            linear 0.5 xoffset 355 yoffset 64
            linear 0.5 xoffset 326 yoffset 73
            linear 0.5 xoffset 294 yoffset 81
            linear 0.5 xoffset 258 yoffset 88
            linear 0.5 xoffset 219 yoffset 95
            linear 0.5 xoffset 178 yoffset 100
            linear 0.5 xoffset 135 yoffset 104
            linear 0.5 xoffset 91 yoffset 107
            linear 0.5 xoffset 45 yoffset 109
            linear 0.5 xoffset 0 yoffset 110
            linear 0.5 xoffset -45 yoffset 109
            linear 0.5 xoffset -91 yoffset 107
            linear 0.5 xoffset -135 yoffset 104
            linear 0.5 xoffset -178 yoffset 100
            linear 0.5 xoffset -219 yoffset 95
            linear 0.5 xoffset -258 yoffset 88
            linear 0.5 xoffset -294 yoffset 81
            linear 0.5 xoffset -326 yoffset 73
            linear 0.5 xoffset -355 yoffset 64
            linear 0.5 xoffset -381 yoffset 54
            linear 0.5 xoffset -401 yoffset 44
            linear 0.5 xoffset -418 yoffset 33
            linear 0.5 xoffset -430 yoffset 22
            linear 0.5 xoffset -437 yoffset 11
            linear 0.5 xoffset -440 yoffset 0
            Null()
            repeat
        contains: # planet
            "images/planet_scene/blue_orb.png"
            xalign 0.5 yalign 0.5
        contains: # moon infront
            "images/planet_scene/moon.png"
            xalign 0.5 yalign 0.5 xoffset -440 yoffset 0

            linear 0.5 xoffset -437 yoffset -11
            linear 0.5 xoffset -430 yoffset -22
            linear 0.5 xoffset -418 yoffset -33
            linear 0.5 xoffset -401 yoffset -44
            linear 0.5 xoffset -381 yoffset -55
            linear 0.5 xoffset -355 yoffset -64
            linear 0.5 xoffset -326 yoffset -73
            linear 0.5 xoffset -294 yoffset -81
            linear 0.5 xoffset -258 yoffset -88
            linear 0.5 xoffset -219 yoffset -95
            linear 0.5 xoffset -178 yoffset -100
            linear 0.5 xoffset -135 yoffset -104
            linear 0.5 xoffset -91 yoffset -107
            linear 0.5 xoffset -45 yoffset -109
            linear 0.5 xoffset 0 yoffset -110
            linear 0.5 xoffset 45 yoffset -109
            linear 0.5 xoffset 91 yoffset -107
            linear 0.5 xoffset 135 yoffset -104
            linear 0.5 xoffset 178 yoffset -100
            linear 0.5 xoffset 219 yoffset -95
            linear 0.5 xoffset 258 yoffset -88
            linear 0.5 xoffset 294 yoffset -81
            linear 0.5 xoffset 326 yoffset -73
            linear 0.5 xoffset 355 yoffset -64
            linear 0.5 xoffset 381 yoffset -55
            linear 0.5 xoffset 401 yoffset -44
            linear 0.5 xoffset 418 yoffset -33
            linear 0.5 xoffset 430 yoffset -22
            linear 0.5 xoffset 437 yoffset -11
            linear 0.5 xoffset 440 yoffset 0
            Null()
            pause 15.0
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
            pause 15.0
            "images/planet_scene/moon.png"
            xalign 0.5 yalign 0.5 xoffset 440 yoffset 0

            linear 0.5 xoffset 437 yoffset 11
            linear 0.5 xoffset 430 yoffset 22
            linear 0.5 xoffset 418 yoffset 33
            linear 0.5 xoffset 401 yoffset 44
            linear 0.5 xoffset 381 yoffset 54
            linear 0.5 xoffset 355 yoffset 64
            linear 0.5 xoffset 326 yoffset 73
            linear 0.5 xoffset 294 yoffset 81
            linear 0.5 xoffset 258 yoffset 88
            linear 0.5 xoffset 219 yoffset 95
            linear 0.5 xoffset 178 yoffset 100
            linear 0.5 xoffset 135 yoffset 104
            linear 0.5 xoffset 91 yoffset 107
            linear 0.5 xoffset 45 yoffset 109
            linear 0.5 xoffset 0 yoffset 110
            linear 0.5 xoffset -45 yoffset 109
            linear 0.5 xoffset -91 yoffset 107
            linear 0.5 xoffset -135 yoffset 104
            linear 0.5 xoffset -178 yoffset 100
            linear 0.5 xoffset -219 yoffset 95
            linear 0.5 xoffset -258 yoffset 88
            linear 0.5 xoffset -294 yoffset 81
            linear 0.5 xoffset -326 yoffset 73
            linear 0.5 xoffset -355 yoffset 64
            linear 0.5 xoffset -381 yoffset 54
            linear 0.5 xoffset -401 yoffset 44
            linear 0.5 xoffset -418 yoffset 33
            linear 0.5 xoffset -430 yoffset 22
            linear 0.5 xoffset -437 yoffset 11
            linear 0.5 xoffset -440 yoffset 0
            Null()
            repeat
        contains: # planet
            "images/planet_scene/blue_orb.png"
            xalign 0.5 yalign 0.5
        contains: # moon infront
            "images/planet_scene/moon.png"
            xalign 0.5 yalign 0.5 xoffset -440 yoffset 0

            linear 0.5 xoffset -437 yoffset -11
            linear 0.5 xoffset -430 yoffset -22
            linear 0.5 xoffset -418 yoffset -33
            linear 0.5 xoffset -401 yoffset -44
            linear 0.5 xoffset -381 yoffset -55
            linear 0.5 xoffset -355 yoffset -64
            linear 0.5 xoffset -326 yoffset -73
            linear 0.5 xoffset -294 yoffset -81
            linear 0.5 xoffset -258 yoffset -88
            linear 0.5 xoffset -219 yoffset -95
            linear 0.5 xoffset -178 yoffset -100
            linear 0.5 xoffset -135 yoffset -104
            linear 0.5 xoffset -91 yoffset -107
            linear 0.5 xoffset -45 yoffset -109
            linear 0.5 xoffset 0 yoffset -110
            linear 0.5 xoffset 45 yoffset -109
            linear 0.5 xoffset 91 yoffset -107
            linear 0.5 xoffset 135 yoffset -104
            linear 0.5 xoffset 178 yoffset -100
            linear 0.5 xoffset 219 yoffset -95
            linear 0.5 xoffset 258 yoffset -88
            linear 0.5 xoffset 294 yoffset -81
            linear 0.5 xoffset 326 yoffset -73
            linear 0.5 xoffset 355 yoffset -64
            linear 0.5 xoffset 381 yoffset -55
            linear 0.5 xoffset 401 yoffset -44
            linear 0.5 xoffset 418 yoffset -33
            linear 0.5 xoffset 430 yoffset -22
            linear 0.5 xoffset 437 yoffset -11
            linear 0.5 xoffset 440 yoffset 0
            Null()
            pause 15.0
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

transform ellipse_blue:
    linear 0.0 xalign 0.5 yalign 0.5 xoffset 400 yoffset 0
    block:
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
        repeat

transform ellipse_moon:
    linear 0.0 xalign 0.5 yalign 0.5 xoffset 440 yoffset 0
    block:
        linear 0.5 xoffset 437 yoffset 11
        linear 0.5 xoffset 430 yoffset 22
        linear 0.5 xoffset 418 yoffset 33
        linear 0.5 xoffset 401 yoffset 44
        linear 0.5 xoffset 381 yoffset 54
        linear 0.5 xoffset 355 yoffset 64
        linear 0.5 xoffset 326 yoffset 73
        linear 0.5 xoffset 294 yoffset 81
        linear 0.5 xoffset 258 yoffset 88
        linear 0.5 xoffset 219 yoffset 95
        linear 0.5 xoffset 178 yoffset 100
        linear 0.5 xoffset 135 yoffset 104
        linear 0.5 xoffset 91 yoffset 107
        linear 0.5 xoffset 45 yoffset 109
        linear 0.5 xoffset 0 yoffset 110
        linear 0.5 xoffset -45 yoffset 109
        linear 0.5 xoffset -91 yoffset 107
        linear 0.5 xoffset -135 yoffset 104
        linear 0.5 xoffset -178 yoffset 100
        linear 0.5 xoffset -219 yoffset 95
        linear 0.5 xoffset -258 yoffset 88
        linear 0.5 xoffset -294 yoffset 81
        linear 0.5 xoffset -326 yoffset 73
        linear 0.5 xoffset -355 yoffset 64
        linear 0.5 xoffset -381 yoffset 54
        linear 0.5 xoffset -401 yoffset 44
        linear 0.5 xoffset -418 yoffset 33
        linear 0.5 xoffset -430 yoffset 22
        linear 0.5 xoffset -437 yoffset 11
        linear 0.5 xoffset -440 yoffset 0
        linear 0.5 xoffset -437 yoffset -11
        linear 0.5 xoffset -430 yoffset -22
        linear 0.5 xoffset -418 yoffset -33
        linear 0.5 xoffset -401 yoffset -44
        linear 0.5 xoffset -381 yoffset -55
        linear 0.5 xoffset -355 yoffset -64
        linear 0.5 xoffset -326 yoffset -73
        linear 0.5 xoffset -294 yoffset -81
        linear 0.5 xoffset -258 yoffset -88
        linear 0.5 xoffset -219 yoffset -95
        linear 0.5 xoffset -178 yoffset -100
        linear 0.5 xoffset -135 yoffset -104
        linear 0.5 xoffset -91 yoffset -107
        linear 0.5 xoffset -45 yoffset -109
        linear 0.5 xoffset 0 yoffset -110
        linear 0.5 xoffset 45 yoffset -109
        linear 0.5 xoffset 91 yoffset -107
        linear 0.5 xoffset 135 yoffset -104
        linear 0.5 xoffset 178 yoffset -100
        linear 0.5 xoffset 219 yoffset -95
        linear 0.5 xoffset 258 yoffset -88
        linear 0.5 xoffset 294 yoffset -81
        linear 0.5 xoffset 326 yoffset -73
        linear 0.5 xoffset 355 yoffset -64
        linear 0.5 xoffset 381 yoffset -55
        linear 0.5 xoffset 401 yoffset -44
        linear 0.5 xoffset 418 yoffset -33
        linear 0.5 xoffset 430 yoffset -22
        linear 0.5 xoffset 437 yoffset -11
        linear 0.5 xoffset 440 yoffset 0
        repeat
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

    '''
    show sun_top at truecenter zorder 2
    show sun_bottom at truecenter zorder 0
    show blue_orb at ellipse_blue zorder 1
    show moon at ellipse_moon
    '''

    "Space..."
    return

label coffee_test:
    show mocapot
    "fuckin coffee man..."
    return