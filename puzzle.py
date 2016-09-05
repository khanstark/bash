import sys
def main():
	l=sys.argv[1:]
	h,f,b=int(l[0]),int(l[1]),int(l[2])
	i,j,dif,time=0,0,f-b,0
	if(dif!=0):
		while(i<=h):
			j=j+dif
			i=f+j
			time=time+1
	else:
		print("Bad Input. Infinite time to be taken :(")
	print(time)
	
if __name__=='__main__':
	main()
