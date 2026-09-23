class Logger:
    def __init__(self):
        self.message_time = {}    # message → last printed timestamp
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_time or \
           timestamp - self.message_time[message] >= 10:
            self.message_time[message] = timestamp    # update last printed time
            return True
        return False