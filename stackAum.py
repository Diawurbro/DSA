class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                self.input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                self.input_data = float(input_data)
            else:
                self.input_data = input_data
        except (TypeError, ValueError, ArithmeticError, AttributeError):
                    pass
        finally:
            self.data.append(self.input_data)
            self.size += 1

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if not self.size:
             print("Underflow: Cannot pop data from an empty list")
             return None
        self.size -= 1
        self.delete = self.data[-1]
        self.data= self.data[:-1]

        return self.delete
    
    def get_stack_top(self):
        if not self.size:
            print("Underflow: Cannot get stack top from an empty list")
            return None
    
    def get_size(self):
         return self.size
    
    def print_stack(self):
         print(self.data)

STACK_ = ArrayStack()

STACK_.push("100")
STACK_.push(100)
STACK_.push("3.14")
STACK_.push(3.14)
STACK_.push("66.4a")
STACK_.push("Ackerman")

STACK_.print_stack()

print(STACK_.get_size())
VAR1_ = STACK_.pop()
print(VAR1_)
STACK_.print_stack()
print(STACK_.get_size())

while not STACK_.is_empty():
    print(STACK_.pop())

print()
print(STACK_.pop())
print(STACK_.get_stack_top())
print(VAR1_)