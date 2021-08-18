from __future__ import print_function, unicode_literals
import os
import json
from bot.Events import *
from bot.Validator import *
from PyInquirer import prompt
from examples import custom_style_3
from bot.PythonProject.Commands import PythonCommands
from bot.PythonProject.Events import PythonEvent
from prompt_toolkit.shortcuts import print_tokens, style_from_dict, Token

generate_question = [
    {
        "type": "list",
        "name": "generate",
        "message": "What do you want to Generate?",
        "choices": [
            "Command",
            "Event"
        ]
    }
]
command_question = [
    {
        "type": "input",
        "name": "name",
        "message": "Enter Command Name",
        "validate": CommandValidator
    },
    {
        "type": "input",
        "name": "category",
        "message": "Enter Command Category",
        "validate": CommandValidator
    },
    {
        "type": "input",
        "name": "description",
        "message": "Enter Command Description"
    }
]

slash_command = [
    {
        "type": "confirm",
        "name": "slash-command",
        "message": "Do you want to use Discord Slash Command",
        "default": False
    }
]
def color_msg(col, msg):
    style = style_from_dict({
        Token.Color: col,
    })
    tokens = [
        (Token.Color, msg)
    ]
    print_tokens(tokens, style=style)

def GenerateCommand():
    # Generating Command
    here = os.getcwd()
    try:
        with open(here + "/config.json", "r") as f:
            file = json.load(f)
        command = prompt(command_question, style=custom_style_3)
        name = command['name']
        category = command['category']
        description = command['description']
        slash = prompt(slash_command, style=custom_style_3)

        if file['config']['language'] == "py":
            PythonCommands(file, name, category, description, slash)
        elif file['config']['language'] == 'js':
            pass
        with open(here + "/config.json", "w") as f:
            json.dump(file, f, indent=4)
    except FileNotFoundError:
            color_msg("#ff0000", "Make sure you are in CrateBot Project")


def GenerateEvent():
    here = os.getcwd()
    try:
        with open(here + "/config.json", "r") as f:
            file = json.load(f)

        if file['config']['language'] == "py":
            PythonEvent(here)
        elif file['config']['language'] == 'js':
            pass
        with open(here + "/config.json", "w") as f:
            json.dump(file, f, indent=4)
    except FileNotFoundError:
            color_msg("#ff0000", "Make sure you are in CrateBot Project")

def GenerateMain():
    generate = prompt(generate_question, style=custom_style_3)
    if generate['generate'] == "Command":
        GenerateCommand()
    elif generate['generate'] == "Event":
        GenerateEvent()