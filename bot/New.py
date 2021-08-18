from __future__ import print_function, unicode_literals
from bot.prompt import color_msg
import json
import os
from bot.Validator import *
from PyInquirer import prompt
from bot.TextInput import TextInput
from examples import custom_style_3

question = [
        {
            "type": "list",
            "name": "language",
            "message": "Select the language",
            "choices": [
                {
                    "name": "Python",
                    'value': "py"
                },
                {
                    "name": "Java Script",
                    "disabled": "Soon",
                    "value": "js"
                },
                {
                    "name": "Type Script",
                    "disabled": "Soon",
                    "value": "ts"
                }
            ]
        },
        {
            "type": "input",
            "name": "name",
            "message": "Project Name",
            "validate": NameValidator
        },
        {
            "type": "password",
            "name": "token",
            "message": "Enter your bot token",
            "validate": TokenValidator
        },
        {
            "type": "input",
            "name": "prefix",
            "message": "Enter the bot prefix",
            "default": "!",
            "validate": PrefixValidator
        },
    ]
def New():
    here = os.path.dirname(os.path.abspath(__file__))
    cwd = os.getcwd()
    answers = prompt(question, style=custom_style_3)
    name = answers['name']
    token = answers['token']
    language = answers['language']
    prefix = answers['prefix']
    dir = os.path.join(cwd, name)
    cogs = os.path.join(cwd + "/" + name, "cogs")
    commands = os.path.join(cwd + "/" + name + "/cogs", "commands")
    event = os.path.join(cwd + "/" + name + "/cogs", "events")
    try:
        if language == "py":
            os.mkdir(dir)
            os.mkdir(cogs)
            os.mkdir(event)
            os.mkdir(commands)
            with open(cwd + "/" + name + "/main.py", 'x') as f:
                f.write(TextInput.MainPy(TextInput(), prefix, token))

            with open(cwd + "/" + name + "/config.json", 'x') as f:
                f.write('{}')
            with open(cwd + "/" + name + "/config.json", 'r') as f:
                file = json.load(f)

            file['config'] = {}
            file['config']['language'] = language

            with open(cwd + "/" + name + "/config.json", "w") as f:
                json.dump(file, f, indent=4)
        color_msg('#00ff00', 'Project Created')

    except FileExistsError:
        color_msg('#ff0000', 'Project Already Exits')
    except FileNotFoundError:
        color_msg('#ff0000', 'Directory Not Found')
