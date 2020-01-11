from pc import Pc

pc = Pc(debug_mode=False)
pc.read_data(data_file="./input.txt", memory_type=1)
pc.run()
