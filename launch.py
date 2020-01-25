from memory import MemoryTypes
from pc import Pc

from configparser import ConfigParser

config = ConfigParser()
config.read("launch.ini")

if not config.sections():
    config["DEFAULT"] = {
        "debug": "False",
    }
    config["MEMORY"] = {
        "type": "MODIFIED_ACCESS",
    }
    config["INPUT"] = {
        "file": "./input.txt",
        "is_parsed": "True",
    }
    with open('launch.ini', 'w') as configfile:
        config.write(configfile)


memory_type = config.get("MEMORY", "type", fallback="BASIC")
memory = MemoryTypes[memory_type].instantiate()
input_file = config.get("INPUT", "file")
is_input_parsed = config.getboolean("INPUT", "is_parsed")
memory.read_file("./input.txt", is_parsed=is_input_parsed)

debug_mode = config.getboolean("DEFAULT", "debug", fallback=False)
pc = Pc(debug_mode=debug_mode)
pc.set_memory(memory)
pc.run()
