import logging
import sys
from configparser import ConfigParser

from pypc.memory import MemoryTypes
from pypc.pc import Pc

config = ConfigParser()
config.read("launch.ini")

# --- LOGGING ---
log_format = "[%(levelname)s] %(name)s - %(message)s"
if config.getboolean("DEFAULT", "debug", fallback=False):
    log_level = logging.DEBUG
else:
    log_level = logging.INFO
logging.basicConfig(format=log_format,
                    stream=sys.stdout,
                    level=log_level)

if __name__ == "__main__":
    # --- MEMORY ---
    memory_type = config.get("MEMORY", "type", fallback="BASIC")
    memory = MemoryTypes[memory_type].instantiate()
    input_file = config.get("INPUT", "file")
    is_input_parsed = config.getboolean("INPUT", "is_parsed")
    memory.read_file("./input.txt", is_parsed=is_input_parsed)

    # --- PC ---
    pc = Pc()
    pc.set_memory(memory)
    pc.run()
