'''
user input (press key to blah blah) module used under Windows,
module msvcrt is Windows-specific
'''

import DataAnalysis_GP.utils as utils
try:
    print('Loading input module ...')
    import msvcrt
except ModuleNotFoundError:
    raise(utils.OsMismatch)

def inputInit():
    pass

def getInput():
    if msvcrt.kbhit():
        char = msvcrt.getwch()
        return str(char)
    else:
        return ''

def inputFinalize():
    pass
