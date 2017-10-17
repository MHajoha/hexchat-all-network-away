# coding: utf8
"""
all-network-away.py - HexChat script to keep the user from having to mark themselves away from every network they are
connected to separately.

Copyright (c) 2017 Maximilian "MHajoha" Haye.
All rights reserved.

HexChat is copyright (c) 2009-2014 Berke Viktor.
https://hexchat.github.io/
"""

import hexchat

__module_name__ = "All Network Away"
__module_version__ = "1.0-final"
__module_description__ = "Marks you away on all networks you are connected to when you do it for one"

flag = False
""":var: Used to keep from handling away commands we generated ourselves, which would do bad things."""


def on_away(word, word_eol, userdata):
    """Hook function to be called upon usage of the away command"""
    global flag

    if not flag:
        try:
            away_msg = word_eol[1]
        except IndexError:
            away_msg = hexchat.get_prefs("away_reason")

        for channel in hexchat.get_list("channels"):
            if channel.type == 1 and channel.context.get_info("away") is None:
                flag = True
                channel.context.command("away " + away_msg)

        return hexchat.EAT_HEXCHAT
    else:
        flag = False


def on_back(word, word_eol, userdata):
    """Hook function to be called upon usage of the back command"""
    global flag

    if not flag:
        for channel in hexchat.get_list("channels"):
            if channel.type == 1 and channel.context.get_info("away") is not None:
                flag = True
                channel.context.command("back")

        return hexchat.EAT_HEXCHAT
    else:
        flag = False


hexchat.hook_command("AWAY", on_away)
hexchat.hook_command("BACK", on_back)

print("All Network Away loaded.")
