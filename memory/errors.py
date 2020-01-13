class MemoryAccessError(IndexError):
    pass


class MemoryReadError(MemoryAccessError):
    pass


class MemoryWriteError(MemoryAccessError):
    pass
