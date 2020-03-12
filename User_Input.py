import DataAnalysis_GP.utils as utils

try: 
    import DataAnalysis_GP.Msvcrt_Input as in_funcs
except utils.OsMismatch:
    try:
        import DataAnalysis_GP.Stdin_Input as in_funcs
    except utils.OsMismatch:
        raise(utils.OsNotSupported)

class usrInput:
    '''
    User input object, windows version (Msvcrt)
    should maintain the following API on transplanted platforoms: 
        getInput(): return 1 for red button (EVENT button)
                    return 2 for black button (EXIT button)
    '''
    def __init__(self):
        in_funcs.inputInit()


    def getInput(self):
        '''action per frame, return 1 for red button and 2 for black button'''
        return in_funcs.getInput()

    def __del__(self):
        in_funcs.inputFinalize()

