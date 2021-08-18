from __future__ import print_function, unicode_literals
import os
from bot.Validator import *
from PyInquirer import prompt
from examples import custom_style_3
from bot.prompt import  color_msg
from bot.Events import CustomPythonEvent
import json

event_question = [
    {
        "type": "list",
        "name": "name",
        "message": "Please select a event",
        "choices": [
            "fetch_channel",
            "fetch_guild",
            "fetch_guilds",
            "fetch_invite",
            "fetch_template",
            "fetch_user",
            "fetch_user_profile",
            "fetch_webhook",
            "fetch_widget",
            "get_all_channels",
            "get_all_members",
            "get_channel",
            "get_emoji",
            "get_guild",
            "get_user",
            "is_closed",
            "is_ready",
            "is_ws_ratelimited",
            "login",
            "logout",
            "on_error",
            "request_offline_members",
            "run",
            "start",
            "wait_for",
            "wait_until_ready",
            "Custom"
        ]
    }
]
custom_question = [
    {
        "type": "input",
        "name": "input",
        "message": "Enter the event name",
        "validate": CommandValidator
    }
]
def PythonEvent(here):
    try:
        with open(here + "/config.json", "r") as f:
            file = json.load(f)
        extensions = file['config']['language']
        if extensions == "py":
            event = prompt(event_question, style=custom_style_3)
            name = event['name']
            if name == "fetch_channel":
                pass
            elif name == "fetch_guild":
                pass
            elif name == "fetch_guilds":
                pass
            elif name == "fetch_invite":
                pass
            elif name == "fetch_template":
                pass
            elif name == "fetch_user":
                pass
            elif name == "fetch_user_profile":
                pass
            elif name == "fetch_webhook":
                pass
            elif name == "fetch_widget":
                pass
            elif name == "get_all_channels":
                pass
            elif name == "get_all_members":
                pass
            elif name == "get_channel":
                pass
            elif name == "get_emoji":
                pass
            elif name == "get_guild":
                pass
            elif name == "get_user":
                pass
            elif name == "is_closed":
                pass
            elif name == "is_ready":
                pass
            elif name == "is_ws_ratelimited":
                pass
            elif name == "login":
                pass
            elif name == "logout":
                pass
            elif name == "on_error":
                pass
            elif name == "request_offline_members":
                pass
            elif name == "run":
                pass
            elif name == "start":
                pass
            elif name == "wait_for":
                pass
            elif name == "wait_until_ready":
                pass
            elif name == "Custom":
                input = prompt(custom_question, style=custom_style_3)
                name = input['input']
                CustomPythonEvent(name, extensions)
    except FileNotFoundError:
        color_msg("#ff0000", "Make sure you are in CrateBot Project")