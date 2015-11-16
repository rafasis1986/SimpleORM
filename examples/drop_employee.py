from simpleorm import BaseDao
from collections import OrderedDict

class DropEmployee(BaseDao):
    sql = 'DROP TABLE IF EXISTS EMPLOYEE'

if __name__ == '__main__':
    param = OrderedDict()
    result = DropEmployee(dbfile='test.db').execute(param)
    print('Rows affected:{}'.format(result))
