from memory import MemoryTypes
from pc import Pc

pc = Pc(debug_mode=False)
pc.read_data(data_file="./input.txt", memory_type=MemoryTypes.MODIFIED_ACCESS)
pc.run()
