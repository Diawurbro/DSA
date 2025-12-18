class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):    
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """Pop"""
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()
    
    def is_empty(self):
        """Is Empty"""
        return self.size == 0
    
    def get_stack_top(self):
        """Get Stack Top"""
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self.data[-1]


    def get_size(self):
        """Get Size"""
        return self.size
    
    def print_stack(self):
        """Print Stack"""
        print(self.data)
        

def is_parentheses_matching(expression):
    """parentheses"""
    stack = ArrayStack()
    is_matched = True
    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            pop = stack.pop()
            if pop is None:
                is_matched = False
    if not stack.is_empty():
        is_matched = False

    result = f"Parentheses in {expression} are {'matched' if is_matched else 'unmatched'}"
    print(result)
    print(is_matched)
    
    return is_matched

a = input()
is_parentheses_matching(a)