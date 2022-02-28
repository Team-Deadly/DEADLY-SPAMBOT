
import sys
import logging
import importlib
from telethon import events
from pathlib import Path
import inspect
import re

def load_plugins(plugin_name):
    path = Path(f"Godfather/plugins/{plugin_name}.py")
    name = "Godfather.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Godfather.plugins." + plugin_name] = load
    print("Godfather Imported Successfully 🎉 " + plugin_name)

async def edit_or_reply(event, text):
    if event.sender_id in SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text)

