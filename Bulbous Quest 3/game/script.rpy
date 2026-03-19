

init python:
    #pre-game programming goes here
    def text_trick(event, interact=True, **kwargs):
        #does the phoenix write style text displaying noise
        if not interact:
            return
        
        if event == "show":
            renpy.music.set_volume(0.02, channel="sound")
            renpy.music.play('audio/typing.wav', channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")


#------------ CHARACTER DEFINITIONS -----------------------------------
define fj = Character("Fishbo Jones", callback=text_trick)
#----------------------------------------------------------------------

#------------------ IMAGE DEFINITIONS ---------------------------------
# backgrounds
image bg_space = Image("images/planet_scene/space.png")

# characters

# other sprites
image sun = Image("images/planet_scene/sun.png")
image blue_orb = Image("images/planet_scene/blue_orb.png")
image moon = Image("images/planet_scene/moon.png")
#----------------------------------------------------------------------

#---------------- TRANSFORMS -------------------------------------------

transform orbit_sun:
    

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

        "i dunno":
            pass

    # This ends the game.

    return

label menu_test:
    show bg_space
    show sun
    show blue_orb
    show moon
    "Space..."
    return