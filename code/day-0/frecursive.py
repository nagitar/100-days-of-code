def factorial( n ):
   if n <1:   # base case
       return 1
   else:
       return n * factorial( n - 1 )  # recursive call
def fact(n):
       for i in range(1, n+1 ):
               print( i, factorial( i ) )

               /* output is not showing */
