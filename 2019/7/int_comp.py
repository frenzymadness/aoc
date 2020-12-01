class IntComputer:
    def __init__(self, source, input):
        with open(source + ".txt") as input_file:
            program = input_file.readlines()[0].split(",")
            self.program = [int(c) for c in program]
        self.input = input
        self.pointer = 0

    def process_opcode(self, opcode):
        zero_string = str(opcode).zfill(5)
        m3, m2, m1, *instruction = zero_string
        return int(m3), int(m2), int(m1), int("".join(instruction))

    def load_param(self, position, mode):
        if mode == 0:
            return self.program[self.program[position]]
        elif mode == 1:
            return self.program[position]
        return None

    def store_result(self, position, mode, result):
        if mode == 0:
            self.program[self.program[position]] = result
        elif mode == 1:
            self.program[position] = result

    def run(self):
        while True:
            opcode = self.program[self.pointer]
            m3, m2, m1, instruction = self.process_opcode(opcode)

            # print(instruction, pointer, self.program, self.input)

            if instruction == 99:
                #print(",".join([str(c) for c in program]))
                print("HALT")
                return None
            
            if instruction in (1, 2):
                # addition and multiplication
                a = self.load_param(self.pointer+1, m1)
                b = self.load_param(self.pointer+2, m2)
                if instruction == 1:
                    c = a + b
                elif instruction == 2:
                    c = a * b
                self.store_result(self.pointer+3, m3, c)

                self.pointer += 4
                continue
            
            if instruction == 3:
                # input
                try:
                    self.store_result(self.pointer+1, m1, self.input.pop())
                except IndexError:
                    print(self.pointer, self.program, self.input, self.output)
                    raise
                self.pointer += 2
                continue

            if instruction == 4:
                # output
                a = self.load_param(self.pointer+1, m1)
                self.pointer += 2
                return a
                continue

            if instruction == 5:
                # jump-if-true
                a = self.load_param(self.pointer+1, m1)
                if a != 0:
                    self.pointer = self.load_param(self.pointer+2, m2)
                else:
                    self.pointer += 3
                continue
            if instruction == 6:
                # jump-if-false
                a = self.load_param(self.pointer+1, m1)
                if a == 0:
                    self.pointer = self.load_param(self.pointer+2, m2)
                else:
                    self.pointer += 3
                continue
                
            if instruction == 7:
                # less than
                a = self.load_param(self.pointer+1, m1)
                b = self.load_param(self.pointer+2, m2)
                if a < b:
                    self.store_result(self.pointer+3, m3, 1)
                else:
                    self.store_result(self.pointer+3, m3, 0)
                
                self.pointer += 4
                continue
            if instruction == 8:
                # equals
                a = self.load_param(self.pointer+1, m1)
                b = self.load_param(self.pointer+2, m2)
                if a == b:
                    self.store_result(self.pointer+3, m3, 1)
                else:
                    self.store_result(self.pointer+3, m3, 0)
            
                self.pointer += 4
                continue

if __name__ == "__main__":
    computer = IntComputer("../5/input", 1)
    computer.run()
