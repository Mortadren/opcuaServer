from pymodbus.client import ModbusTcpClient
from redis import StrictRedis
import struct
import numpy as np
from time import sleep, time
import os
# import logging
from configs import *

class PLC:
    def __init__(self, plc_number):

        self.register_address_write = WRITE_REG_AS
        self.plc_data = {} # все данные полученные с плк
        self.plc_number = plc_number
        if self.plc_number == 1:
            self.register_address_read = READ_REG_AS
            self.client = ModbusTcpClient(host=HOST_PLC_AS, port=PORT_PLC_AS)
        elif self.plc_number == 2:
            self.register_address_read = READ_REG_ES
            self.client = ModbusTcpClient(host=HOST_PLC_ES, port=PORT_PLC_ES)
        self.client.connect()

        # # REDIS
        self.r = StrictRedis(host=HOST_REDIS, port=PORT_REDIS, decode_responses=True)
        
        
        
        # data
        self.response = None
        self.defect = None
        self.control_status = None
        self.marker_status = None
        
        
        # logging.getLogger("pymodbus").setLevel(logging.CRITICAL)
        # logging.basicConfig(filename='/log/plc_communication.log', level=logging.INFO, datefmt='%d-%m-%Y, %H:%M:%S', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.error_flag = False

    def read_register(self):
        for key, x in self.register_address_read.items():
            try:
                self.response = self.client.read_holding_registers(x[0], count=x[1])
                self.plc_data[key] = [self.response, x[1], x[2]]
                self.error_flag = False
            except Exception as e:
                print(e)
                if self.error_flag == False:
                    error_msg = f"Ошибка при чтении регистров: {e}"
                    # logging.error(msg=error_msg)
                    self.error_flag = True
               
    def encode_data(self):
        if self.error_flag == False:
            for key, x in self.plc_data.items():
                if x[1] > 1:
                    byte_string = struct.pack('<HH', *x[0].registers)
                    dt = np.dtype(np.float32)
                    dt = dt.newbyteorder('<')
                    self.plc_data[key] = str(round((np.frombuffer(bytearray(byte_string), dtype=dt)[0]), 2))
                elif x[2]:
                    self.plc_data[key] = float(x[0].registers[0])/100
                else:
                    self.plc_data[key] = str(x[0].registers[0])
            # logging.info(msg=self.plc_data)
        print(self.plc_data) 

    # def write2redis(self):
    #     try:
    #         self.r.hset('PLC', self.plc_data)
    #         self.error_flag = False
    #     except Exception as e:
    #         if self.error_flag == False:
    #             error_msg = f"Ошибка при записи в redis: {e}"
    #             # logging.error(msg=error_msg)
    #             self.error_flag = True

    # def get_control_status(self):
    # #     if int(self.r.get('SYS_MODE')) > 0:
    # #         self.control_status = 1
    # #     elif int(self.r.get('SYS_MODE')) == 0:
    # #         self.control_status = 0

    # # def get_defect_status(self):
    # #     if int(self.r.get('COLOR_STATUS')) == 1:
    # #         self.defect = 1
    # #     else:
    # #         self.defect = 0

    # # def get_marker_status(self):
    # #     if int(self.r.get('IS_TRIGGER_ACTIVE')) == 1:
    # #         self.marker_status = 1
    # #     else:
    # #         self.marker_status = 0

    # def get_data4plc(self):
    #     self.get_control_status()
    #     self.get_defect_status()
    #     self.get_marker_status()

    def write2plc(self):
        # self.client.write_register(address=self.register_address_write['MARKER_STATUS'], value=self.marker_status)
        # self.client.write_register(address=self.register_address_write['DEFECT'], value=self.defect)
        # test = int(self.r.get('control_status'))
        # print(test)
        if self.plc_number == 1:
            self.client.write_register(address=self.register_address_write['control_status'], value=int(self.r.get('control_status')))
            try:
                self.client.write_register(address=self.register_address_write['defect'], value=int(self.r.get('defect')))
                self.client.write_register(address=self.register_address_write['danger_red'], value=int(self.r.get('danger_red')))  
            except:
                pass
    def get_data_from_plc(self):
        self.read_register()
        self.encode_data()
        self.write2plc()
        return self.plc_data

    def start(self):
        # logging.info(msg='Запуск системы')
        print('start')
        while True:
            self.read_register()
            self.encode_data()
            # self.write2redis()
            # self.get_data4plc()
            self.write2plc()
            sleep(TIME_PLC)


if __name__ == '__main__':
    a = PLC(1)
    a.start()
    b = PLC(2)
    b.start()