import threading
import multiprocessing


class Singleton:
    instance = None
    lock = threading.RLock()  # 锁

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        with cls.lock:  # 申请释放锁
            if cls.instance:
                return cls.instance
            cls.instance = object.__new__(cls)
            return cls.instance
