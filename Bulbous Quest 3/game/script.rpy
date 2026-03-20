

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
define fj = Character("Fishbo Jones", callback=gun_text_trick)
#----------------------------------------------------------------------

#------------------ IMAGE DEFINITIONS ---------------------------------
# backgrounds
image bg_space = Image("images/planet_scene/space.png")

# characters

# other sprites
image sun = Image("images/planet_scene/sun.png")
image blue_orb = Image("images/planet_scene/blue_orb.png")
image moon = Image("images/planet_scene/moon.png")
image mocapot = Image("images/Objects/Mocapot/mocapot.png")
#----------------------------------------------------------------------

#---------------- TRANSFORMS -------------------------------------------

transform ellipse_blue:
    linear 0.0 xalign 0.5 yalign 0.5 xoffset 100 yoffset 0
    block:
        linear 1.0 xoffset 95 yoffset 30
        linear 1.0 xoffset 80 yoffset 58
        linear 1.0 xoffset 58 yoffset 80
        linear 1.0 xoffset 30 yoffset 95
        linear 1.0 xoffset 0 yoffset 100
        linear 1.0 xoffset -30 yoffset 95
        linear 1.0 xoffset -58 yoffset 80
        linear 1.0 xoffset -80 yoffset 58
        linear 1.0 xoffset -95 yoffset 30
        linear 1.0 xoffset -100 yoffset 0
        linear 1.0 xoffset -95 yoffset -30
        linear 1.0 xoffset -80 yoffset -58
        linear 1.0 xoffset -58 yoffset -80
        linear 1.0 xoffset -30 yoffset -95
        linear 1.0 xoffset 0 yoffset -100
        linear 1.0 xoffset 30 yoffset -95
        linear 1.0 xoffset 58 yoffset -80
        linear 1.0 xoffset 80 yoffset -58
        linear 1.0 xoffset 95 yoffset -30
        linear 1.0 xoffset 100 yoffset 0
        repeat

transform ellipse_moon:
    linear 0.0 xalign 0.5 yalign 0.5 xoffset 100 yoffset 0
    block:
        linear 1.0 xoffset 95 yoffset 30
        linear 1.0 xoffset 80 yoffset 58
        linear 1.0 xoffset 58 yoffset 80
        linear 1.0 xoffset 30 yoffset 95
        linear 1.0 xoffset 0 yoffset 100
        linear 1.0 xoffset -30 yoffset 95
        linear 1.0 xoffset -58 yoffset 80
        linear 1.0 xoffset -80 yoffset 58
        linear 1.0 xoffset -95 yoffset 30
        linear 1.0 xoffset -100 yoffset 0
        linear 1.0 xoffset -95 yoffset -30
        linear 1.0 xoffset -80 yoffset -58
        linear 1.0 xoffset -58 yoffset -80
        linear 1.0 xoffset -30 yoffset -95
        linear 1.0 xoffset 0 yoffset -100
        linear 1.0 xoffset 30 yoffset -95
        linear 1.0 xoffset 58 yoffset -80
        linear 1.0 xoffset 80 yoffset -58
        linear 1.0 xoffset 95 yoffset -30
        linear 1.0 xoffset 100 yoffset 0
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
    show sun:
        xalign 0.5 yalign 0.5
    show blue_orb at ellipse_blue
    show moon at ellipse_moon
    "Space..."
    return

label coffee_test:
    show mocapot
    "fuckin coffee man..."
    return