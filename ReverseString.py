def reverse_string1(s):
    return s[::-1]

s = "Ahmad Khan"
print(reverse_string1(s))
#2

def reverse_string3(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Test
s = "Ahmad Khan"
print(reverse_string3(s))
 
#3


def reverse_string2(s):
    return ''.join(reversed(s))

s = "Hello, World!"
print(reverse_string2(s))

