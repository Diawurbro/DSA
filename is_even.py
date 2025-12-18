def is_even(n):
    '''is_even'''
    if n & 1 == 0:
        return True
    if n & 1 == 1:
        return False

def main():
    """main"""
    n = int(input())
    print(is_even(n))
main()
