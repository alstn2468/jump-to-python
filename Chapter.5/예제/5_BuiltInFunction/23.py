# abs
print(abs(3)) # 3
print(abs(-3)) # 3
print(abs(-1.2)) # 1.2

# all
print(all([1, 2, 3])) # True
print(all([1, 2, 3, 0])) # False

# any
print(any([1, 2, 3, 0])) # True
print(any([0, ""])) # False

# chr
print(chr(97)) # 'a'
print(chr(48)) # '0'

# dir
print(dir([1, 2, 3]))
print(dir({'1', 'a'}))

# divmod
print(divmod(7, 3)) # (2, 1)
print(divmod(1.3, 0.2)) # (6.0, 0.09999...)

# enumerate
for i, name in enumerate(['body', 'foo', 'bar']) :
    print(i, name)
'''
0 body
1 foo
2 bar
'''

# eval
print(eval('1+2')) # 3
print(eval("'hi' + 'a'")) # 'hia'
print(eval('divmod(4, 3)')) # (1, 1)
