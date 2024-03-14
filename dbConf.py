class DBDesc:
    def __init__(self):
        self.__host="localhost"
        self.__user="dbtstaff692"
        self.__password="1234"
        self.__database="classicmodels"

    def getHost(self):
        return self.__host
    def getUser(self):
        return self.__user
    def getPassword(self):
        return self.__password
    def getDatabase(self):
        return self.__database