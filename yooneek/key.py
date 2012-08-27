import time


class IDGenerator(object):

    MAX_SEQ = 0b11111111111

    def __init__(self):
        self.host = 1
        self.sequence = 0
        self.timestamp = 0
    
    def _prime_timestamp(self):
        # not all versions of Python support getting milli-seconds, so we only rely on seconds
        timestamp = int(time.time())
        
        if timestamp < self.timestamp:
            raise Exception
        
        self.timestamp = timestamp

    def _prime_sequence(self):
        seq = self.sequence + 1
        if seq > IDGenerator.MAX_SEQ:
            self.sequence = 0
        else:
            self.sequence = seq

    def generate_key(self):
        self._prime_sequence()
        self._prime_timestamp()
    
        key = self.timestamp << (64 - 41)
        key |= self.host << (64 - 41 - 11)
        key |= self.sequence

        return key

generator = IDGenerator()
