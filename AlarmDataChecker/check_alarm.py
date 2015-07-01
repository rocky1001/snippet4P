#!/usr/local/python2.7.5/bin/python
#encoding=utf-8
import sys
import MySQLdb
import alarm_config

NORMAL = 0
ERROR = 1
CRITICAL = 2


def check_alarm():
    """ Check the alarm data in MySQL database. """
    try:
        connection = MySQLdb.connect(**alarm_config.ALARM_LOCAL_DB)
        check_alarm_sql = "SELECT * FROM alarm WHERE is_notify=0"
        cursor = connection.cursor()
        cursor.execute(check_alarm_sql)
        rows_affected = cursor.rowcount
        if rows_affected > 0:
            rows = cursor.fetchall()
            ids = list()
            for row in rows:
                ids.append(str(row[0]))
                # print error msg
                print row[1], 'alarm_type=' + str(row[2]), 'alarm_level=' + str(row[3]), row[4] + ':', row[5]
            # update is_notify to 1
            update_is_notify_sql = "UPDATE alarm SET is_notify=1 WHERE id IN (%s) " % ",".join(ids)
            # print update_is_notify_sql
            cursor.execute(update_is_notify_sql)
            connection.commit()

            return ERROR
    except MySQLdb.MySQLError, e1:
        print "DB-ERROR: Failed when operating DB, due to [%s]" % e1
        return ERROR
    except Exception, e2:
        print "ERROR: Failed due to [%s]" % e2
        return ERROR
    finally:
        cursor.close()
        connection.close()
    print 'Congratulations:Everything is fine.'
    return NORMAL


if __name__ == '__main__':
    # print 'Mdm check alarm start.'
    sys.exit(check_alarm())