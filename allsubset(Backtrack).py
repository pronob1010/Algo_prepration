def subsetsUtil(list,subsets,index):
    print(subsets)
    for i in range(index,len(list)):
        subsets.append(list[i])

        subsetsUtil(list,subsets,i+1)

        subsets.pop(-1)
        # print("check")
        #print(subsets)
        # print("Done")

    # else:
    #     print(subsets)
    return


def subset(list):
    # global res
    subsets = []
    index = 0
    subsetsUtil(list,subsets,index)

s = input()
list = [s[i] for i in range(len(s))]
subset(list)
