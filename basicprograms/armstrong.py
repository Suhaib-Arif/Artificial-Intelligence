def arm(n):
  
	temp=n
  
	sum=0
  
	while(temp>0):
    
		digit=temp%10
    
		sum+=digit**3
    
		temp//=10
  
	if(sum==temp):
    
		print(f"{n} is armstrong")
  
	else:
    
		print(f"{n} not an armstrong")


arm(153)
  