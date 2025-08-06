def check_li(li,name):
    if name in li:
        return True
    else:
        return False
li=[1,2,3,4,5,6]
a1 = check_li(li,5)
# print(a1)

def str_freq(s:str):
    try:
        dic={}
        str_li = s.split(" ")
        for word in str_li:
            if word  not in dic.keys():
                dic[word] = 1
            else:
                dic[word] += 1
        return dic
    except AttributeError:
        return f"Wrong Input"

li1="Hello is am am or and and or or or"
s2 = str_freq(li1)
# print(s2)

def cap_word(li):
    lia = map(lambda x:x.capitalize(),li)
    return list(lia)

li2=["apple","banana","maggie","pizza"]
s3 = cap_word(li2)
# print(s3)

def sqr(li):
    li1 = map(lambda x:x**2, li)
    return list(li1)

li3 = [2,5,6,4]
s4= sqr(li3)
# print(s4)

def swap_value(dic:dict):
    keys = tuple(dic.keys())
    value = tuple(dic.values())
    temp_dic = {}
    for idx,key in enumerate(value):
        temp_dic[key] = keys[idx]
    return temp_dic

dic={
    'a':1,
    'b':2,
    'c':3
}
s5=swap_value(dic)
# print(s5)

def even_no(li):
    li1 = [x for x in li if x%2 == 0]
    return li1

li5 = range(1,20)
s6=even_no(li5)
# print(s6)
