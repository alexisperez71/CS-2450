class VirtualMachine:
    def __init__(self) -> object:
        self._memory = []
        self._accumulator = "0000"
        with open("Test1.txt", "r") as file:
            for line in file:
                self._memory.append(line.strip("+").strip("\n"))

    def get_memory(self):
        return self._memory
    
    def get_accumulator(self):
        return self._accumulator

    def __str__(self):
        text = "------------------------\n"
        text += "Memory:\n"
        for i in self._memory:
            text += f"{i},\n"
        text += "\nAccumulator:\n"
        text += self.get_accumulator()
        text += "\n------------------------\n"
        return text
    
    def run(self):
        count = 0
        while(True)
            curr = self._memory[i][0:2]
            if curr == "43":
                break
            elif curr == "10":
                self.read(curr)
            elif curr == "11":
                self.write(curr)
            elif curr == "20":
                self.load(i)
            elif curr == "21":
                self.store(i)
            elif curr == "30":
                continue
            elif curr == "31":
                continue
            elif curr == "32":
                self.divide(self._memory[int(self._memory[count][2:4])])
            elif curr == "33":
                self.multiply(self._memory[int(self._memory[count][2:4])])
            elif curr == "40":
                count = int(self._memory[count][2:4]) - 1
            elif curr == "41":
                continue
            elif curr == "42":
                continue
            elif len(self._memory) == count:
                raise IndexError("No More Executable Instructions")
            count += 1

        print(self)

    def read(self, curr): #Fischer
        """Triggered by instruction '10'. Reads a word from the keyboard in to a specific location in memory"""
        mem_address = int(self._memory[curr][2:])                       #gets the last two characters from the word. This is the address we are printing the word from
        if mem_address >= len(self._memory) and mem_address < 100:      #if the command calls an address that is outside of the used memory, but less than total memory, print NULL
            print("NULL")
        elif mem_address < len(self._memory):                           #if the command calls an address that inside used memory, print the data at that address
            print(self._memory[mem_address])
        else:                                                           #otherwise, the command is calling an address that is > 100, which is outside the total memory. Raise an error;.
            raise IndexError("Segmentation fault. Memory address does not exist")

    def resize_memory(self, mem_address):  # Fischer
        """helper function to resize memory if needed"""
        new_list = [None] * mem_address
        for i in range(len(self._memory)):
            new_list[i] = self._memory[i]
        self._memory = new_list

    def write(self, curr):    #Fischer
        """Triggered by instruction '11'. Write a word from a specific location in memory to the screen"""
        mem_address = int(self._memory[curr][2:])
        plus = "+"
        user_word = input("Enter a 4-digit command (Digits 1-9 only): ")
        new_word = plus + user_word
        if mem_address < 100 and mem_address >= len(self._memory):          #if writing to an address that is outside of the current memory, but less than 100, resize memory and write word
           self.resize_memory(mem_address)
           self._memory[mem_address] = user_word
        elif mem_address < len(self._memory):
            self._memory[mem_address] = new_word
        else:
            raise IndexError("Segmentation fault. Cannot write to that memory address")

    def load(self, i):
        """Triggered by instruction '20'. Grabs number from a specific point in memory and puts it into accumulator"""
        self._accumulator = self._memory[int(self._memory[i][2:])]


    def store(self, i):
        """Triggered by instruction '21'. Grabs number from the accumulator and puts it into a specific point in memory."""
        self._memory[int(self._memory[i][2:])] = self._accumulator

    def add(self):
        pass

    def subtract(self):
        pass

    def divide(self, curr):
        self._accumulator = str(int(curr) // int(self._accumulator))
        while len(self.get_accumulator()) != 4:
            self._accumulator = "0" + self._accumulator

    def multiply(self, curr):
        self._accumulator = str(int(curr) * int(self._accumulator))
        while len(self.get_accumulator()) < 4:
            self._accumulator = "0" + self._accumulator
        if len(self.get_accumulator()) > 4:
            raise ValueError(f"Value Overflow; Accumlulator only supports up to 4 digits.")


def main():
    cole = VirtualMachine()
    cole.run()


if __name__ == "__main__":
    main()
