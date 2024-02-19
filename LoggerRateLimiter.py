from collections import deque
from typing import Set, Deque


class Logger:
    def __init__(self):
        self.messageSet: Set[str] = set()
        self.messageQueue: Deque = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.messageQueue and self.messageQueue[0][0] <= (timestamp - 10):
            self.messageSet.remove(self.messageQueue[0][1])
            self.messageQueue.popleft()
        if message not in self.messageSet: # case when we should pop out message
            self.messageSet.add(message)
            self.messageQueue.append((timestamp, message))
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)