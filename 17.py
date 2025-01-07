import re
import sys

data = sys.stdin.read()


def parse_input(data):
    A = int(re.findall(r"Register A: (\d+)\n", data).pop())
    B = int(re.findall(r"Register B: (\d+)\n", data).pop())
    C = int(re.findall(r"Register C: (\d+)\n", data).pop())

    program = [int(x) for x in re.findall(r"Program: (.+)", data).pop().split(",")]

    return A, B, C, program


def execute_program(A, B, C, program):
    out = []
    pointer = 0

    def evaluate_combo(v):
        if v <= 3:
            return v
        if v == 4:
            return A
        if v == 5:
            return B
        if v == 6:
            return C

        raise ValueError("Invalid combo")

    while pointer < len(program):
        instruction = program[pointer]
        operand = program[pointer + 1]

        match instruction:
            # Divide A by 2 ** combo
            case 0:
                A = A // (2 ** evaluate_combo(operand))
                pointer += 2

            # B XOR literal
            case 1:
                B = B ^ operand
                pointer += 2

            # Combo modulo 8
            case 2:
                B = evaluate_combo(operand) % 8
                pointer += 2

            # Jump to literal if A > 0
            case 3:
                pointer = operand if A > 0 else pointer + 2

            # B XOR C
            case 4:
                B = B ^ C
                pointer += 2

            # Print combo modulo 8
            case 5:
                out.append(evaluate_combo(operand) % 8)
                pointer += 2

            # Divide A by 2 ** combo, store in B
            case 6:
                B = A // (2 ** evaluate_combo(operand))
                pointer += 2

            # Divide A by 2 ** combo, store in C
            case 7:
                C = A // (2 ** evaluate_combo(operand))
                pointer += 2

    return out


A, B, C, program = parse_input(data)
print(",".join(map(str, execute_program(A, B, C, program))))

A_guess = 8**15 - 100000
while (out := execute_program(A_guess, B, C, program)) != program:
    A_guess += 1

    if A_guess % 100000 == 0:
        print(len(out))
        print(A_guess, out)


print(A_guess)
