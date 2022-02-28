
import sys
import logging
import importlib
from telethon import events
from pathlib import Path
import inspect
import re

def load_plugins(plugin_name):
    path = Path(f"Krishna/plugins/{plugin_name}.py")
    name = "Krishna.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Krishna.plugins." + plugin_name] = load
    print("Krishna Imported Successfully 🎉 " + plugin_name)

async def edit_or_reply(event, text):
    if event.sender_id in SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text)

