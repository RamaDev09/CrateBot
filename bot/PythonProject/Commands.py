import os
from bot.TextInput import TextInput
from bot.prompt import color_msg

def PythonCommands(file, name, category, description, slash):
    here = os.getcwd()
    # Writing a new import line
    cogs = file['config']['commands'] = []
    cogs.append(name)
    with open(here + "/main.py", "r") as f :
        lines = f.readlines()
    line = 0
    for i in lines :
        line += 1
        if lines[line - 1] == "\n" : break
    lines[line - 1] = f"from cogs.commands.{category}.{name} import {category}\n"

    with open(here + "/main.py", "w") as f :
        f.writelines(lines)
        f.close()
    if not slash['slash-command'] :
        try :
            dir = os.path.join(here + "/cogs/commands", category)
            os.mkdir(dir)
            try :
                with open(here + "/cogs/commands/" + category + "/" + name + ".py", "x") as f :
                    f.write(
                        TextInput.CommandPy(self=TextInput(), name=name, category=category, description=description))
                    color_msg("#00FF00", "Command Created")
            except FileExistsError :
                color_msg("#ff0000", "Command Already Exits")
        except FileNotFoundError :
            color_msg("#ff0000", "Make sure you are in CrateBot Project")
        except FileExistsError :
            try :
                with open(here + "/cogs/commands/" + category + "/" + name + ".py", "x") as f :
                    f.write(
                        TextInput.CommandPy(self=TextInput(), name=name, category=category, description=description))
                    color_msg("#00FF00", "Command Created")
            except FileExistsError :
                color_msg("#ff0000", "Command Already Exits")
    else :
        try :
            dir = os.path.join(here + "/cogs/commands", category)
            os.mkdir(dir)
            try :
                with open(here + "/cogs/commands/" + category + "/" + name + ".py", "x") as f :
                    f.write(
                        TextInput.CommandSlashPy(self=TextInput(), name=name, category=category,
                                                  description=description))
                    color_msg("#00FF00", "Command Created")
            except FileExistsError :
                color_msg("#ff0000", "Command Already Exits")
        except FileNotFoundError :
            color_msg("#ff0000", "Make sure you are in CrateBot Project")