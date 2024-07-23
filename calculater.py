def cal():
    while True:
        print("1=Addition")
        print("2=Subtraction")
        print("3=multiplaction")
        print("4=division")
        n=int(input("enter your choice(1-4)"))
        if(n<4):
              if(n==1):
                  h=int(input("enter a number:"))
                  d=int(input("enter a number:"))
                  v=h+d
                  print("addition of h and d:",v)
              elif(n==2):
                  h=int(input("enter a number:"))
                  d=int(input("enter a number:"))
                  v=h-d
                  print("subtraction of h and d:",v)
              elif(n==3):
                  h=int(input("enter a number:"))
                  d=int(input("enter a number:"))
                  v=h*d
                  print("multiplaction of h and d:",v)
              elif(n==4):
                  h=int(input("enter a number:"))
                  d=int(input("enter a number:"))
                  v=h/d
                  print("division of h and d:",v)
        else:
            print("invalid")
            break
                  
cal()          
            
