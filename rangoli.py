from string import ascii_lowercase

def print_rangoli(size):
    n = size
    padding_length = 4*n - 3
    s = ascii_lowercase[0:n][::-1]
    a = 1
    while a < len(s):
        r = s[0:a][::-1]
        rd = r[::-1]+r[1:]
        print('-'.join(rd).center(padding_length, '-'))
        a = a + 1

    while a > 0:
        p = s[0:a][::-1]
        pd = p[::-1]+p[1:]
        print('-'.join(pd).center(padding_length, '-'))
        a = a - 1
		
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
