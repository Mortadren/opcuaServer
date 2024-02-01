#  Подключение к redis
HOST_REDIS = '192.168.55.4'
PORT_REDIS = 6379
PASSWORD = ''

# Подключение к ПЛК AS
HOST_PLC_AS = "192.168.55.235" #  PLC 
PORT_PLC_AS = 502

# Подключение к ПЛК ES
HOST_PLC_ES = "192.168.55.234" #  PLC 
PORT_PLC_ES = 502

# Регистры для чтения; [10, 2, True] где 10 - номер регистра, 2 - количество регистров, True - если тру, то значение флоат \100 
READ_REG_AS = {'defect': [500, 1, False], 'control_status': [505, 1, False], 'counter_storage': [506, 1, False], 'green_com': [501, 1, False],
               'yellow_com': [502, 1, False],'red_com': [503, 1, False], 'danger_red': [507, 1, False]
            }

READ_REG_ES = {'frq_read': [2103, 1, True], 'volt_read': [2109, 1, False], 'cur_read': [2104, 1, False], 'speed': [1005, 2, False], 'lenght': [1001, 2, False]
            }

# регистры для записи
WRITE_REG_AS = {'defect': 500,
             'control_status': 505,
             'danger_red': 507,
            }


# Интервал опроса и записи в ПЛК
TIME_PLC = 0.2
