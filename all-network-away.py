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
__module_version__ = "0.1-initial"
__module_description__ = "Marks you away on all networks you are connected to when you do it for one"

flag = False


def on_away(word, word_eol, userdata):
    global flag

    if not flag:
        try:
            away_msg = word_eol[1]
        except IndexError:
            away_msg = hexchat.get_prefs("away_reason")

        for channel in hexchat.get_list("channels"):
            if channel.type == 1:
                flag = True
                channel.context.command("away " + away_msg)

        return hexchat.EAT_HEXCHAT

hexchat.hook_command("AWAY", on_away)
