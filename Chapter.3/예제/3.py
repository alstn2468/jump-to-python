# while문 직접 만들기
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """
number = 0
while number != 4 :
    print(prompt)
    number = int(input())
