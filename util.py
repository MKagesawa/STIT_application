import pymysql.cursors

# JSON Response formats
class ErrorResponse(object):
    def __init__(self):
        self.state = False
        self.error = {'errorCode': 0, 'errorMsg': 'blank'}

    def __str__(self):
        return str(self.__dict__)

class SuccessResponse(object):
    def __init__(self):
        self.state = True
        self.data = {'Welcome': 1}

    def __str__(self):
        return str(self.__dict__)

# DB functions
def query_mod(sql, config):
    connection = pymysql.connect(**config)
    result = 0
    try:
        with connection.cursor() as cursor:
            # Insert a new record
            cursor.execute(sql)
        connection.commit()
    except:
        result = 1
    finally:
        connection.close()
    return result

def query_fetch(sql, config):
    connection = pymysql.connect(**config)
    try:
        with connection.cursor() as cursor:
            # Read a single record
            cursor.execute(sql)
            result = cursor.fetchone()
        connection.commit()
    finally:
        connection.close()
    return result


def fetch_all(sql, config):
    connection = pymysql.connect(**config)
    try:
        with connection.cursor() as cursor:
            # Read all records
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.commit()
    finally:
        connection.close()
    return result
