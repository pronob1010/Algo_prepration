def isPelindrom(s):
    start = 0
    end = len(s)-1
    while(start<= end):
        # print(start,end)
        if s[start]==s[end]:

            start+=1
            end-=1
        else:
            return False
    else:
        return True

if __name__=="__main__":
    s = input()
    if isPelindrom(s):
        print("YES")
    else:
        print("NO")