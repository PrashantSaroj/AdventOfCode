def exec_instructions(instructions):
    signalStrengthSum, strengthPtr = 0, 0
    currCycle, currX = 1, 1
    for instr in instructions:
        if instr == 'noop':
            currCycle += 1
        else:
            _, operand = instr.split()
            # strength event happens during the cycle
            if currCycle + 1 == cycles[strengthPtr]:
                signalStrengthSum += currX*cycles[strengthPtr]
                strengthPtr += 1
            currX += int(operand)
            currCycle += 2
        
        if strengthPtr == len(cycles):
            break

        if cycles[strengthPtr] == currCycle:
            signalStrengthSum += currX*cycles[strengthPtr]
            strengthPtr += 1
    print(signalStrengthSum)


cycles = [20 + i*40 for i in range(6)]
instructions = open('in.txt', 'r').read().split('\n')
exec_instructions(instructions)
