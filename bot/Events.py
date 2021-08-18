from __future__ import print_function, unicode_literals
import os
from bot.TextInput import TextInput
from bot.prompt import color_msg

# Python Event
def CustomPythonEvent(name, extensions):
    here = os.getcwd()
    try:
        with open(here + "/cogs/events/" + name + "." + extensions, "x") as f:
            f.write(TextInput.EventPy(self=TextInput(), name=name))
            color_msg("#00FF00", "Event Created")
    except FileExistsError:
        color_msg("#ff0000", "Event Already Exits")
    except FileNotFoundError:
        color_msg("#ff0000", "Make sure you are in Bot Project")