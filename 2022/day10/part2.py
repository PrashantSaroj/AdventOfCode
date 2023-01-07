WIDTH, HEIGHT = 40, 6


def pixel_lit(spritePos, cycle):
    spriteL = spritePos - 1
    spriteR = spritePos + 1
    return spriteL <= cycle % 40 <= spriteR


def exec_instructions(instructions):
    crt = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    currCycle, currX = 0, 1

    def setPixel():
        if pixel_lit(currX, currCycle):
            crt[currCycle//40][currCycle % 40] = '█'

    for instr in instructions:
        if instr == 'noop':
            setPixel()
            currCycle += 1
        else:
            _, operand = instr.split()
            setPixel()
            currCycle += 1
            setPixel()
            currCycle += 1
            currX += int(operand)

    for row in crt:
        print(''.join(row))


instructions = open('in.txt', 'r').read().split('\n')
exec_instructions(instructions)
