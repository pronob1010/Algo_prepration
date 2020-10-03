a,b = list(map(int, input().split()))

d = 0
while True:
	if d%2==1:
		if a>0 and b>0:
			a -=d
		else:
			break
	else:
		if b>0 and a>0:
			b-=d
		else:
			break
	print(a,b)
	d+=1

if a>= d+1:
	print("Vladik")
elif b>= d+1:

	print("Valera")
elif a == 0:
	print("Valera")
elif b == 0:
	print("Vladik")