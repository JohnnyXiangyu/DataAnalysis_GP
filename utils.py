# some shared data structure

class OsError(Exception):
    pass

class OsMismatch(OsError):
    '''
    exception prepared to throw when OS-specific modules are loaded on wrong system
    e.g. loading Msvcrt_Input in linux
    '''
    pass
