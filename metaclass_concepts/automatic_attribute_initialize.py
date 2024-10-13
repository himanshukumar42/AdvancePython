class InitDefaultMeta(type):
    def __new__(cls, name, bases, dct):
        dct["created_at"] = None
        dct["updated_at"] = None
        return super().__new__(cls, name, bases, dct)
