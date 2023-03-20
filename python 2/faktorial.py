import os
os.system('cls')

def faktorial(a):
   if a == 0:
      return (1)
   else:
      return (a*faktorial(a-1))
  
print(f'{6}! = {faktorial(6)}')
print("")
# for i in range(12):
#     print(f'{i}! = {faktorial(i)}')