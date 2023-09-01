import random

def assign_rand(a,b,c):  
  lst=[a,b,c]
  rand_choice=random.choice(lst)
  return rand_choice

def compare(choice,n):
  str=check_combination(choice,n)
  if str=='user wins':
    return 'you won'
  elif str=='computer wins':
    return 'you lost'
  else:
      return 'tie'

def check_combination(choice,n):
  if choice==1 and n==1:
        return "tie"
  elif choice==2 and n==2:
        return "tie"
  elif choice==3 and n==3:
        return "tie"        
  elif choice==1 and n==2:
    return "computer wins"
  elif choice==1 and n==3:
    return "user wins"
  elif choice==2 and n==1:
    return "user wins"
  elif choice==2 and n==3:
    return 'computer wins'
  elif choice==3 and n==1:
    return 'computer wins'
  elif choice==3 and n==2:
    return 'user wins'

flag=1
while flag:
    print("1.Rock")
    print("2.Paper")
    print("3.Scisors")
    print("4.exit")
    choice=int(input("select your option:"))
    if choice==4:
        flag=0
    else:
        n=assign_rand(1,2,3)
        print('your choice:',choice)
        print("compute's choice:",n)
        status=compare(choice,n)
        print(status)
