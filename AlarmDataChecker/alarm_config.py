ALARM_LOCAL_DB = {
    'host':     'localhost',
    'db':       'test',
    'user':     'test',
    'passwd':   'test123!@#',
    'charset':  'utf8'
}

ALARM_LEVEL_NORMAL = 0
ALARM_LEVEL_SEVERE = 1
ALARM_LEVEL_FATAL = 2

ALARM_TYPE_NONE = 0
ALARM_TYPE_INIT = 1
ALARM_TYPE_DB = 2
ALARM_TYPE_REST = 3
ALARM_TYPE_SFTP = 4
ALARM_TYPE_LOCALFILE = 5
ALARM_TYPE_HDFSFILE = 6
ALARM_TYPE_MD5 = 7