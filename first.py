# 1. identifier
# An identifier is a name given to entities like class, functions, variables, etc.
# It helps to differentiate one entity from another.
counter = 10
Counter = 100
this_is_a_sentence = "Yep!"

print("no problem")

# 2. Multi-line Statement
# In Python, the end of a statement is marked by a newline character.
# But we can make a statement extend over multiple lines with the line continuation character (\).
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

b = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8 + 9)

rgb = ['red',
       'blue',
       'green']

x = 1;
y = 2;
c = 3

"""This an example of 
    multi-line string 
    which is used as a comment"""

print(a, b)


# 3. Docstrings
# A docstring is short for documentation string.
# Python docstrings (documentation strings) are the string literals that
# appear right after the definition of a function, method, class, or module.
# Triple quotes are used while writing docstrings.

def double(num):
    """Function to double the value"""
    return 2 * num


print(double.__doc__)

# 4. Assigning multiple values to multiple variables

u, v, w = 5, 3.2, "Hello"

print(u, v, w)

u = v = w = "same"

print(u, v, w)

# 5. Numeric Literals
a = 0b1010  # Binary Literals
b = 100  # Decimal Literal
c = 0o310  # Octal Literal
d = 0x12c  # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

# 6. String Literals
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# 7. None
money = None

# 8. Literal Collections

fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}  # set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

print(a, "is complex number?", isinstance(1 + 2j, complex))

# 9. List
# are mutable
a = [5, 10, 15, 20, 25, 30, 35, 40, 5]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

# 10. Tuple
t = (5, 'program', 1 + 3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
# t[0] = 10

# 11. Set
# Set is an unordered collection of unique items.
a = {5, 2, 3, 1, 4}

# They eliminate duplicates.
a = {1, 2, 2, 3, 3, 3}
print(a)

# 12. Dictionary
d = {1: 'value', 'key': 2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
# print("d[2] = ", d[2])

# 13. Conversion between data types
print(float(5))

print(int(10.6))

conv1 = set([1,2,3])
conv2 = list('hello')