"""serial communication library (win64), inclusing base class Port \n
    API: \n
        __init__(name, baudrate) \n
        sendData(arg) customizable interface \n
        readData(arg) customizable interface \n
        communicate(arg) \n"""

import serial
import serial.tools.list_ports
import csv
import os

print('Loading serial communication module ...')


class VirtualPort:
    '''
    Virtual machine, designed for common usage. Defines the following working procedure:
        __init__: open designated file (by prompting user input)
        communicate: return a line of data from the open csv file
    '''

    def __init__(self):
        fileName = input(
            '| Enter filename to open (should be under directory ./Data_Analysis_win64/virtual_data/): ')
        fileName = './Data_Analysis_win64/virtual_data/' + fileName
        self.m_port = []

        try:
            csv_file = open(fileName, encoding='utf-8')
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 1:
                    # the first line is used for formating or other info, not defined yet
                    tempList = []
                    for item in row:
                        tempList.append(item)
                    self.m_port.append(tempList)
                line_count += 1

        except FileNotFoundError:
            os.system('cls')
            print('File not found. ')
            self.m_port = False

    def sendData(self):
        pass

    def readData(self):
        if len(self.m_port) <= 0:
            return []
        returnList = self.m_port[0]
        self.m_port.pop(0)
        return returnList

    def communicate(self):
        """return a designated response from serial port"""
        # communicate
        result = self.readData()

        return result


class SerialPort:
    '''
    Abstraction of serial port, simplified to only search name and free.
    '''

    def __init__(self, name, br):
        port_list = list(serial.tools.list_ports.comports())
        self.m_name = ''
        self.m_br = br
        self.m_port = None
        self.m_error = ""
        # get input
        if len(port_list) <= 0:
            print('| There is no serial device connected.')
            self.m_error = "no-ser-device"
        else:
            for i in port_list:
                if name in i.description:
                    self.m_name = i.device  # find the first designated device
            if self.m_name == '':
                print('| The designated device is not connected. ')
                self.m_error = "target-not-found"
            # port open
            else:
                self.m_port = serial.Serial(self.m_name, self.m_br)

    def stop(self):
        """
        Free resource: serial port
        """
        if self.m_port and self.m_port.isOpen() == True:
            self.m_port.close()
    
    def __del__(self):
        self.stop()
