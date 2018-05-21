# VERBOSE, X
import re

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
&[#]                # Start of a numeric entity reference
(
    0[0-7]+         # Octal form
    |[0-9]+         # Decimal form
    |x[0-9a-fA-F]+  # Hexadecimal form
)
;                   # Trailing semicolon
""", re.VERBOSE)

# 백슬래시 문제
p = re.compile('\\section')
p = re.compile('\\\\section')
p = re.compile(r'\\section')
