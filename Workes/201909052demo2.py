
def test1():
    for i in range(1000,1501):
        if i%8==0 and i%5!=0:
            print(i,end=";")

def test2(n,m):
    print()
    result_arr=[]
    for i in range(1,n+1):
        small_list = []
        for j in range(1,m+1):
            small_list.append(i*j+i)
        result_arr.append(small_list)
    print(result_arr)

def test3():
    str_list=['aysgdu','sbdsd','sadbs','dcsbsc']
    if 'abc' not in str_list:
        str_list.append('abc')
    for str in str_list:
        if 'a' not in str:
            str_list.remove(str)
    for i in range(len(str_list)):
        str_list[i] = str_list[i].replace('b','B')
    print(str_list)
    
def test4():
    strs = ["flower","flow","flight"]
    str_con=strs[0]
    for i in range(1,len(strs)):
        for j in range(0,len(strs[i])):
            if j>=len(str_con):
                break
            if str_con[j]!=strs[i][j]:
                str_con=str_con[0:j]
                break
    print("the result_str is--- ",str_con)




if __name__ == '__main__':
    test1()
    test2(2,3)
    test3()
    test4()

