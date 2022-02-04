
class DBClient(object):
    __data__ = list()

    def find(self):
        return self.__data__

    def find_one(self):
        return self.__data__[0]


def get_db_client():
    return DBClient()

