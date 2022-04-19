izbor=int(input("Unesite broj izmedu 1 -100 : "))

for x in range(1,izbor):
   if (x % 3 ==0 and x % 5 == 0):
        print("fizzBuzz")
   elif x % 3==0:
       print("fizz")
   elif x % 5==0:
       print("buzz")
   else:
       print(x)