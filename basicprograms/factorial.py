def fact(n):
  
	f=1
  
	for i in range(1,n+1):
    
		f=f*i
  
	print(f"factorial of {n} is {f}")



n=int(input("enter the num:"))



fact(n)



