import os
import sys
print('Loading logger module ...')


class simpleLogger:
    # TODO: all open/close functions don't check failure yet
    '''
    logger object
    '''

    def __init__(self, msg, ind, dire=None):
        """
        initialize logger: open/create file
        dire: path to the file
        msg: any information besides test count
        index: numbering, type, anything related to defining an entry in a series of tests
        """
        if dire == None:
            dire = os.getcwd() + '/'
        self.m_file = open(dire + msg +
                           'test' + ind + '.csv', 'w')

    def printFile(self, data_list, separator=','):
        '''
        print a line of record as-is, not extra formatting
        data_list: a list (or any iteratable) object
        separator: default ',', deliminator in record
        '''
        for data in data_list:
            self.m_file.write(str(data))
            self.m_file.write(separator)
        self.m_file.write('\n')

    def switchFile(self, msg, ind, dire=None):
        """
        close previous log file, then open a new one
        dire: path to the file
        msg: any information besides test count
        index: numbering, type, anything related to defining an entry in a series of tests
        """
        self.m_file.close()
        if dire == None:
            dire = os.getcwd() + '/'
        self.m_file = open(dire + msg +
                           'test' + ind + '.csv', 'w')

    
    def close(self):
        self.m_file.close()
