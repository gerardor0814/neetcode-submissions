class MinStack:

    def __init__(self):
        self.stack = []
        self.minum = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minum  == None or val < self.minum:
            self.minum = val

    def pop(self) -> None:
        self.stack.pop()

        if self.stack:
            localmin = self.stack[0]
            for num in self.stack:
                if num < localmin:
                    localmin = num
            self.minum = localmin
        else:
            self.minum = None

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minum
