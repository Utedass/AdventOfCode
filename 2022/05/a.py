import os, argparse, re

def solve_task(lines):
    # Extract the initial stacks and instructions from the input
    (stacks, raw_instructions) = load_stacks(lines)

    #print(f"Stacks: {stacks}\n")
    #print(f"Instructions: {raw_instructions}")
    #display_stacks(stacks)

    # Parse the instructions into a list of tuples
    packed_instructions = pack_instructions(raw_instructions)
    #print(f"Packed: {packed_instructions}")

    # Perform all instructions
    for instruction in packed_instructions:
        perform_instruction(stacks, instruction)
        #display_stacks(stacks)

    # Get the answer by getting the uppermost (last) element of
    # each stack. This way has side effects, but we won't need
    # to preserve the stacks past this line.
    print("Final answer: " + ''.join([s.pop() for s in stacks]))

def display_stacks(stacks):
    print("Current stacks:")
    for stack in stacks:
        print(''.join(stack))

def perform_instruction(stacks, instruction):
    quantity = int(instruction[0])
    source = int(instruction[1]) - 1
    destination = int(instruction[2]) - 1

    # Since lists are mutable, we can manipulate the supplied lists
    # instead of returning new ones
    for _ in range(quantity):
        stacks[destination].append(stacks[source].pop())

def pack_instructions(instr):
    # Return a list of instruction-tuples
    return [get_instruction_tuple(i) for i in instr]
    
def get_instruction_tuple(intr_line):
    # Returns a tuple with three values (quantity, source, destination)
    m = re.match("move (\d+) from (\d+) to (\d+)", intr_line)
    return (m.group(1), m.group(2), m.group(3))

def load_stacks(lines):
    number_of_piles = (len(lines[0])+1)//4
    piles = [[] for x in range(number_of_piles)]
    instructions_start_line = 0
    for linum in range(len(lines)):
        line = lines[linum]
        for col in range(len(line)):
            c = line[col]
            if col % 4 != 1 or c == ' ':
                continue
            if c == '1':
                instructions_start_line = linum+2
                break
            pile = col // 4
            piles[pile].insert(0, c)

        if instructions_start_line != 0:
            break
    return (piles, lines[instructions_start_line:])


def read_lines(filename):
    lines = []
    with open(filename) as infile:
        for raw_line in infile:
            line = raw_line.replace('\n', '')
            line = line.replace('\r', '')
            #line = raw_line.rstrip() # Usefull to keep space in this task
            lines.append(line)
    return lines

def parse_arguments():
    parser = argparse.ArgumentParser(description="Script that solves the case",epilog="Have a nice day!")
    parser.add_argument('filename', nargs='?', default="example.txt", help='Input file')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    lines = read_lines(args.filename)
    solve_task(lines)

if __name__ == "__main__":
    main()