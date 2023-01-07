def parse_line(l):
    return l.split(': ')


def parse_input():
    monkeyExpr = {}
    for line in open('in.txt', 'r').read().split('\n'):
        parsedLine = parse_line(line)
        monkeyExpr[parsedLine[0]] = parsedLine[1]
    return monkeyExpr


class Node:
    def __init__(self, value, lchild, rchild, operation=None) -> None:
        self.value = value
        self.lchild = lchild
        self.rchild = rchild
        self.operation = operation


class Graph:
    def __init__(self, monkeySet) -> None:
        self.monkeySet = monkeySet
        self.monkeySet['humn'] = None

        self.head = self.createGraph()

        # equate root childs
        self.head.lchild.value = self.head.rchild.value
        self.tracePath(self.head.lchild)

    def tracePath(self, node: Node):
        if node.lchild is None and node.rchild is None:
            print(node.value)
            return

        # print(node.value, node.lchild.value, node.rchild.value, node.operation)
        if node.lchild.value is None:
            node.lchild.value = self.reverseCalcL(node)
            self.tracePath(node.lchild)
        else:
            node.rchild.value = self.reverseCalcR(node)
            self.tracePath(node.rchild)

    def createGraph(self, nodeName: str = 'root') -> Node:
        expr = self.monkeySet[nodeName]
        # handle human
        if nodeName == "humn":
            return Node(None, None, None)

        if expr.isdigit():
            return Node(int(expr), None, None)
        else:
            parsedExpr = expr.split()
            lchild = self.createGraph(parsedExpr[0])
            rchild = self.createGraph(parsedExpr[2])
            value = self.calcValue(lchild, rchild, parsedExpr[1])
            return Node(value, lchild, rchild, parsedExpr[1])

    def calcValue(self, lchild: Node, rchild: Node, operation: str) -> int:
        if lchild.value is None or rchild.value is None:
            return None

        if operation == '+':
            return lchild.value + rchild.value
        if operation == '-':
            return lchild.value - rchild.value
        if operation == '*':
            return lchild.value * rchild.value
        if operation == '/':
            return lchild.value // rchild.value

    def reverseCalcL(self, node: Node):
        # left child is None and node has value
        if node.operation == '+':
            return node.value - node.rchild.value
        if node.operation == '-':
            return node.value + node.rchild.value
        if node.operation == '*':
            return node.value // node.rchild.value
        if node.operation == '/':
            return node.value * node.rchild.value

    def reverseCalcR(self, node: Node):
        # right child is None and node has value
        if node.operation == '+':
            return node.value - node.lchild.value
        if node.operation == '-':
            return node.lchild.value - node.value
        if node.operation == '*':
            return node.value // node.lchild.value
        if node.operation == '/':
            return node.lchild.value // node.value


def solveRiddle(monkeySet):
    Graph(monkeySet)


solveRiddle(parse_input())
