import sys

def brainfuck_interpreter(code, input_data=""):
    tape = [0] * 30000  # Memory tape
    ptr = 0  # Pointer to tape
    input_ptr = 0  # Pointer to input data
    output = []
    code_ptr = 0  # Pointer to Brainfuck code
    loop_stack = []
    
    while code_ptr < len(code):
        command = code[code_ptr]
        
        if command == '>':
            ptr += 1
        elif command == '<':
            ptr -= 1
        elif command == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif command == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif command == '.':
            output.append(chr(tape[ptr]))
        elif command == ',':
            if input_ptr < len(input_data):
                tape[ptr] = ord(input_data[input_ptr])
                input_ptr += 1
            else:
                tape[ptr] = 0  # Default to null byte if input is exhausted
        elif command == '[':
            if tape[ptr] == 0:
                open_brackets = 1
                while open_brackets > 0:
                    code_ptr += 1
                    if code[code_ptr] == '[':
                        open_brackets += 1
                    elif code[code_ptr] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(code_ptr)
        elif command == ']':
            if tape[ptr] != 0:
                code_ptr = loop_stack[-1] - 1
            else:
                loop_stack.pop()
        
        code_ptr += 1
    
    return "".join(output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python brainfuck.py <filename>")
        sys.exit(1)
    
    with open(sys.argv[1], "r") as file:
        brainfuck_code = file.read()
    
    result = brainfuck_interpreter(brainfuck_code)
    print(result)
