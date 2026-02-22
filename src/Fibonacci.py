def fibonacci(n):

	fi=1
	fi1=0

	for i in range(1,n+1):

		fn=fi+fi1 #F(n+1)=F(n)+F(n-1)
		fi1=fi #F(n-1) for next i value
		fi=fn #F(n) for next i value

	print(f"F(",n,")=",fi1)
n=33

fibonacci(n)
