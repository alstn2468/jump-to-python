# sub 매서드의 입력 인수로 함수 넣기
import re

def hexrepl(match) :
    "Return the hex string for ad decimal number"

    value = int(match.group())

    return hex(value)

p = re.compile(r'\d+')

print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))
# Call 0xffd2 for printing, 0xc000 for user code.
