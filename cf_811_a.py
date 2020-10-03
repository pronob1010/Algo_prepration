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
	d+=1

if a>= d:
	print("Valera")
elif b>=d:
	print("Vladik")
elif a == 0:
	print("Valera")
elif b == 0:
	print("Vladik")