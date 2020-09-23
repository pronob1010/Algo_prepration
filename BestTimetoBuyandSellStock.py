List = [7,1,5,3,6,4]
pro = 0
for i in range(1,len(List)):
    if List[i]>List[i-1]:
        buy = min((List[i], List[i-1]))
    if List[i]>List[i-1]:
        pro += List[i]-buy
print(pro)