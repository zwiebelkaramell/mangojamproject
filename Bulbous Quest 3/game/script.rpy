# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def text_trick(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show":
            renpy.music.set_volume(0.02, channel="sound")
            renpy.music.play('audio/typing.wav', channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

define fj = Character("Fishbo Jones", callback=text_trick)


# The game starts here.

label start:
    scene bg room

    show fishbo_jones trace

    fj "you think i'm funny?"

    fj "what am i, a clown to you?"

    # This ends the game.

    return
