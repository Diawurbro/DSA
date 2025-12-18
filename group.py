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
        
def student_grouping():
    '''grouping'''
    m_groups = int(input())
    n_students = int(input())

    main_stack = ArrayStack()
    for _ in range(n_students):
        student_name = input()
        main_stack.push(student_name)

    group_stacks = []
    for _ in range(m_groups):
        group_stacks.append(ArrayStack())

    group_index = 0
    while not main_stack.is_empty():
        student = main_stack.pop()
        group_stacks[group_index].push(student)

        group_index += 1
        if group_index == m_groups:
            group_index = 0

    for i in range(m_groups):
        temp_stack = ArrayStack()
        target_stack = group_stacks[i]

        while not target_stack.is_empty():
            temp_stack.push(target_stack.pop())

        output_str = ""
        first_item = True

        while not temp_stack.is_empty():
            item = temp_stack.pop()

            if first_item:
                output_str += str(item)
                first_item = False
            else:
                output_str += ", " + str(item)
            
        print(f"Group {i + 1}: {output_str}")

student_grouping()

