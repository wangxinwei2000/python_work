

def avg_grade(dict_grade):
    count=0
    sum=0
    for i in dict_grade.values():
        count+=1
        sum+=i
    return sum/count


def get_max_grade(dict_grade):
    max_person = max(dict_grade,key=dict_grade.get)
    max_grade = dict_grade[max_person]
    print('the highest score of ', max_grade, ' belongs to ', max_person)

def push_score(dict_grade,n):
    for i in range(n):
        name = input("please input name: ")
        while True:
            try:
                score = int(input("please input score: "))
                break
            except:
                print('the score is error!!')
        dict_grade[name] = score

def get_personGrade(dict_grade):
    peron_name = input('please input the name who you want to get his score ')
    try:
        print('the score is',dict_grade[peron_name])
    except:
        print('Don not have the score of ',peron_name)
if __name__ == '__main__':
    dict_grade={}
    push_score(dict_grade,3)
    print('the average grade is ',round(avg_grade(dict_grade),2))
    get_max_grade(dict_grade)
    get_personGrade(dict_grade)



