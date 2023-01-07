allDivisors = [19, 2, 13, 5, 7, 11, 17, 3]


class Monkey:
    def __init__(self,  startItems, operation, divisor, trueId, falseId):
        """
        startItems: list of int starting items
        test: lambda returning true or false
        trueId, falseId: monkeys which will get the items in case of test pass/fail
        nextItems: items for next round
        operation: operation on id
        """
        self.items = [{d: item for d in allDivisors} for item in startItems]
        self.divisor = divisor
        self.trueId = trueId
        self.falseId = falseId
        self.operation = operation

    def catchItem(self, item):
        self.items.append(item)

    def inspectItem(self, item):
        newItem = {}
        for key, val in item.items():
            newItem[key] = self.operation(val) % key
        return newItem

    def throwItem(self, item):
        self.items.remove(item)
        newValue = self.inspectItem(item)
        catcher = self.trueId if newValue[self.divisor] == 0 else self.falseId
        return (catcher, newValue)


class Simulator:
    def __init__(self):
        self.idCount = 8
        self.monkeys = {
            0: Monkey([71, 86], lambda x: x*13, 19, 6, 7),
            1: Monkey([66, 50, 90, 53, 88, 85], lambda x: x + 3, 2, 5, 4),
            2: Monkey([97, 54, 89, 62, 84, 80, 63], lambda x: x + 6, 13, 4, 1),
            3: Monkey([82, 97, 56, 92], lambda x: x + 2, 5, 6, 0),
            4: Monkey([50, 99, 67, 61, 86], lambda x: x * x, 7, 5, 3),
            5: Monkey([61, 66, 72, 55, 64, 53, 72, 63], lambda x: x + 4, 11, 3, 0),
            6: Monkey([59, 79, 63], lambda x: x*7, 17, 2, 7),
            7: Monkey([55], lambda x: x + 7, 3, 2, 1)
        }
        self.inspectCount = dict([[i, 0] for i in range(self.idCount)])

    def simulate(self, rounds):
        for _ in range(rounds):
            for i in range(self.idCount):
                currMonkey = self.monkeys[i]
                self.inspectCount[i] += len(currMonkey.items)
                for _ in range(len(currMonkey.items)):
                    catcher, newVal = currMonkey.throwItem(currMonkey.items[0])
                    self.monkeys[catcher].catchItem(newVal)

        print(sorted(self.inspectCount.values()))


Simulator().simulate(10000)
