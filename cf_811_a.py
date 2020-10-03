a,b = list(map(int, input().split()))

i = 0
while True:
	if i%2 == 1:
		if a!= 0:
			a-=i
		else:
			print("Valera")
			break
	else:
		if b!= 0:
			b-=i
		else:
			print("Vladik")
			break

	i+=1