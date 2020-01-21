import os
print('Loading logger module ...')


class Logger:
    '''
    logger object
    '''

    def __init__(self, sensorType):
        """file open"""
        fileName = input('| Enter sequence of test: ')
        self.m_file = open('Data_Analysis_win64\\test_data\\' + sensorType +
                           'test' + fileName + '.csv', 'w')
        os.system('cls')
        print('Out file is open.')

    def printFile(self, data_list):
        '''print a list of data, includng flags, into the out file'''
        for data in data_list:
            self.m_file.write(str(data))
            self.m_file.write(', ')
        self.m_file.write('\n')
    
    def close(self):
        self.m_file.close()
        print('Out file is closed.')
