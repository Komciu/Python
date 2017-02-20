import datetime;

class Timer(object):

    resolution = 100; """ ms """
    
    def __init__(self):
        self.__time = 0;
        self.__run = false;

    def start(self):
        self.__run = true;
        self.__start = datetime.datetime.now();

    def stop(self):
        self.__run = false;
        self.__end = datetime.datetime.now();

    def setTimeout(self, timeout_ms):
        self.__timeout = timeout_ms;
        
    
