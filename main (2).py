# 1.1 implement e recursive function yo calculate the factorial of a given number.

def fact_rec(n):
   if n==0 or n==1:
      return 1
   else:
      return n*fact_rec(n-1)

number =4
res = fact_res(number)

print("the factorial of{} is {}.".format(number, res))