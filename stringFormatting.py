'''
This is solution for the problem at
https://www.hackerrank.com/challenges/python-string-formatting/problem
'''
def print_formatted(number):
    '''
    print_formatted is function to print Decimal, hexadecimal, octal and binary
    equavalants of the input in each line
    args:
        number is argument for the number of lines needs to be printed
    '''
    padding_length = len(bin(number)[2:])+1
    for i in range(1, number+1):
        print(str(i).rjust(padding_length-1,' ')+str(oct(i)[2:]).rjust(padding_length,' ')+str(hex(i)[2:]).upper().rjust(padding_length,' ')+str(bin(i)[2:]).rjust(padding_length,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
