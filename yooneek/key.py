from functools import wraps


def sequence(fn):

    @wraps(fn)
    def wrapper(self):
        self.sequence += 1
        if self.sequence > IDGenerator.MAX_SEQ:
            self.sequence = 0
        return fn(self)
    return wrapper


class IDGenerator(object):

    MAX_SEQ = 0b11111111111

    def __init__(self):
        self.host = None
        self.sequence = 0
        
    @sequence
    def generate_key(self):
        return self.sequence

generator = IDGenerator()
