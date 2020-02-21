'''
user input module for unix-like systems
'''

import sys

class usrInput:
    '''
    User input object, windows version (Msvcrt)
    should maintain the following API on transplanted platforoms: 
        getInput(): return 1 for red button (EVENT button)
                    return 2 for black button (EXIT button)
    '''

    def getInput(self):
        '''action per frame, return 1 for red button and 2 for black button'''
        pass
