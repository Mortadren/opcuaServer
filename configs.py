#  Подключение к redis
HOST_REDIS = ''
PORT_REDIS = 6379
PASSWORD = ''

# Подключение к ПЛК 1
HOST_PLC_AS = "" #  PLC 
PORT_PLC_AS = 502

# Подключение к ПЛК 2
HOST_PLC_ES = "" #  PLC 
PORT_PLC_ES = 502

# Регистры для чтения; [10, 2, True] где 10 - номер регистра, 2 - количество регистров, True - если тру, то значение флоат \100 
READ_REG_AS = {}

READ_REG_ES = {}

# регистры для записи
WRITE_REG_AS = {'defect': 500,
             'control_status': 505,
             'danger_red': 507,
            }


# Интервал опроса и записи в ПЛК
TIME_PLC = 0.2
