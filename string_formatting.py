def to_binary(n):
    return str(bin(n))[2:]

def to_hex(n):
    return str(hex(n)).upper()[2:]

def to_oct(n):
    return str(oct(n))[2:]

def print_formatted(number):
    for n in range(1, number+1):
        print(n, to_oct(n), to_hex(n), to_binary(n))


n = int(input())
# n = 17
print_formatted(n)
