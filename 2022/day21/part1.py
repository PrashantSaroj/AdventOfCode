def parse_line(l):
    return l.split(': ')


def parse_input():
    monkeyExpr = {}
    for line in open('in.txt', 'r').read().split('\n'):
        parsedLine = parse_line(line)
        monkeyExpr[parsedLine[0]] = parsedLine[1]
    return monkeyExpr


class Node:
    def __init__(self, value, lchild, rchild) -> None:
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class Graph:
    def __init__(self, monkeySet) -> None:
        self.monkeySet = monkeySet
        self.head = self.createGraph()
        print(self.head.value)

    def createGraph(self, nodeName: str = 'root') -> Node:
        expr = self.monkeySet[nodeName]
        if expr.isdigit():
            return Node(int(expr), None, None)
        else:
            parsedExpr = expr.split()
            lchild = self.createGraph(parsedExpr[0])
            rchild = self.createGraph(parsedExpr[2])
            value = self.calcValue(lchild, rchild, parsedExpr[1])
            return Node(value, lchild, rchild)

    def calcValue(self, lchild: Node, rchild: Node, operation: str) -> int:
        if operation == '+':
            return lchild.value + rchild.value
        if operation == '-':
            return lchild.value - rchild.value
        if operation == '*':
            return lchild.value * rchild.value
        if operation == '/':
            return lchild.value // rchild.value


def solveRiddle(monkeySet):
    Graph(monkeySet)


solveRiddle(parse_input())
