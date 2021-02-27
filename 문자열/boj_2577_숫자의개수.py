#새로 알게 된 것 : count()

mul = 1
for i in range(3):
      mul *= int(input())
          
string = str(mul)
for i in range(10):
    print(string.count(str(i)))
