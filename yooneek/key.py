import time


class IDGenerator(object):
    """
    64-bits
    ---------
    41-bits  -> timestamp (in seconds)
    11-bits  -> worker_id index (up to 2047 unique workers/hosts)
    12-bits  -> sequence (up to 4095 unique keys/second)

    """

    MAX_SEQ = 4096

    def __init__(self):
        self.worker_id = 1
        self.sequence = 0
        self.timestamp = 0
        self._last_key = 0
    
    def _prime_timestamp(self):
        # not all versions of Python support getting milli-seconds, so we only rely on seconds
        timestamp = int(time.time())
        
        if timestamp < self.timestamp:
            raise Exception
        
        self.timestamp = timestamp

    def _prime_sequence(self):
        self.sequence = self.sequence % IDGenerator.MAX_SEQ
        self.sequence += 1

    def _generate_key(self):
        self._prime_sequence()
        self._prime_timestamp()
    
        key = self.timestamp << (64 - 41)
        key |= self.worker_id << (64 - 41 - 11)
        key |= self.sequence

        return key

    def key(self):
        key = self._generate_key()
        
        # if the requests for keys is faster than 4096 keys/second, we risk seeing collisions
        if key <= self._last_key:
            # wait for the second to change, then get the key
            time.sleep(1)
            key = self._generate_key()
        self._last_key = key

generator = IDGenerator()
